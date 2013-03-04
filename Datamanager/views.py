import StringIO

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.forms.models import modelformset_factory, inlineformset_factory
from django.core.files.base import ContentFile 
from django.forms import widgets

from django import conf
from Datamanager.models import *
from Datamanager import settings
from django import forms
from django.forms.formsets import all_valid

class InstanceForm(forms.ModelForm):
    release_id = 0

    class Meta:
        model = Instance
        #used to hide the tag 'image upload' widget, since the tag will be auto generated in the print view
        exclude = ('tag',)
        #fields = ('instanciated_release', )

    def __init__(self, *args, **kwargs):
        super(InstanceForm, self).__init__(*args, **kwargs)
        release_id = InstanceForm.release_id
        self.initial = {'instanciated_release' : release_id,}
        self.fields['instanciated_release'].queryset = Release.objects.filter(id=release_id)
        #This way the empty '-----' choice does not appear
        self.fields['instanciated_release'].empty_label = None
        
        #Set instanciated_release field in first position on the form
        # without using 'Class.fields' that forces to list all the fields...
        release = self.fields.pop('instanciated_release')
        self.fields.insert(0, 'instanciated_release', release)

class InstanceAttributeModelForm(forms.ModelForm):
    init = False
    form_id = 0
    initial_attributes = []

    def __init__(self, *args, **kwargs):
        super(InstanceAttributeModelForm, self).__init__(*args, **kwargs)
        attribute = InstanceAttributeModelForm.initial_attributes[InstanceAttributeModelForm.form_id]
        if InstanceAttributeModelForm.init:
            self.initial = attribute
        self.fields['attribute'].queryset = Attribute.objects.filter(id=attribute['attribute'].id)
        self.fields['attribute'].empty_label = None
        
        WidgetClass, options = AttributeType.get_class_and_options(attribute['attribute'].tipe)
        if options==None:
            options = {}
        self.fields['value'].widget = WidgetClass(**options)
        InstanceAttributeModelForm.form_id += 1


class InstanceCompositionModelForm(forms.ModelForm):
    form_id = 0
    composing_releases_ids = []
    
    def __init__(self, *args, **kwargs):
        super(InstanceCompositionModelForm, self).__init__(*args, **kwargs)
        release_index = InstanceCompositionModelForm.composing_releases_ids[InstanceCompositionModelForm.form_id]
        self.fields['element_instance'].queryset = Instance.objects.filter(instanciated_release=release_index)
        InstanceCompositionModelForm.form_id += 1

# \todo : why do those classes work without Meta:model ?
class SpecificsModelForm(forms.ModelForm):
    #hacky solution from SO : http://stackoverflow.com/questions/3657709/how-to-force-save-an-empty-unchanged-django-admin-inline
    def has_changed(self):
        """ Should returns True if data differs from initial. 
        By always returning true even unchanged inlines will get validated and saved."""
        return True

         
def save_all(instance, form, formsets):
    #Since we used 'commit=False' on form saving, we need to save the instance by hand, and also its many-2-many relationships
    instance.save()
    form.save_m2m()
    for formset in formsets:
        formset.save()



def add_instance(request, release_id):
    #instanciated_release = Release.objects.get(id=release_id)
    instanciated_release = Release.objects.get_subclass(id=release_id)
    DerivedRelease = type(instanciated_release)

    initial_attributes = []
    attributes_count = 0
    for attribute in instanciated_release.attribute.all():
        initial_attributes.append({'attribute':attribute,})
        attributes_count += 1

    composing_releases_id = []
    composition_count = 0
    for nested_release in ReleaseComposition.objects.filter(container_release=instanciated_release):
        # .id is not necessary for functionnality, but does it change the value stored in the list ?
        # yes it does : it appends the element release itslef instead of its id
        composing_releases_id.append(nested_release.element_release.id)
        composition_count += 1
     
    formsets = []
    formset_factories = []

    #We are using Class attributes to pass parameters to forms __init__
    InstanceForm.release_id = release_id
    
    #Only necessary first time page is loaded (post data will later autopopulate the approriate number of forms)
    InstanceAttributeModelForm.init = request.method == 'GET'
    InstanceAttributeModelForm.form_id = 0
    InstanceAttributeModelForm.initial_attributes = initial_attributes
    #We get the factory for an inlineformset (derived from modelformset) that is modeling InstanceAttribute and links it to an Instance
    #with modelformset (and derived inlineformset), initial values only apply to extra forms : so we have to allow the exact number of extra forms matching the number of initials.
    InstanceAttributeFormset = inlineformset_factory(Instance, InstanceAttribute, form=InstanceAttributeModelForm, can_delete=False, extra=attributes_count)

    InstanceCompositionModelForm.form_id = 0
    InstanceCompositionModelForm.composing_releases_ids = composing_releases_id
    InstanceCompositionFormset = inlineformset_factory(Instance, InstanceComposition, form=InstanceCompositionModelForm, fk_name='container_instance',  can_delete=False, extra=composition_count)

    InstancePictureFormset = inlineformset_factory(Instance, InstancePicture, can_delete=False, extra=3)
    #The pythonic insane EAFP ... (http://stackoverflow.com/questions/610883/how-to-know-if-an-object-has-an-attribute-in-python)
    #We check if the DerivedRelease class has a specifics, and show an inline formset if it's the case
    try:
        InstanceSpecificsFormset = inlineformset_factory(Instance, DerivedRelease.Dna.specifics, form=SpecificsModelForm, can_delete=False, extra=1, max_num=1)
        formset_factories.append(InstanceSpecificsFormset)
    except AttributeError:
        pass

    formset_factories += [InstanceAttributeFormset, InstanceCompositionFormset, InstancePictureFormset]

    #if the form was submitted (false on first page load)
    if request.method == 'POST':
        #repopulate the form with posted data
        form = InstanceForm(request.POST, request.FILES)
        if form.is_valid():
            #We need the instance model to bind it to the inlineformset [which needs to know the foreign key], but we do not save it to the DB yet using 'commit=False'
            new_instance = form.save(commit=False)
            form_validated = True
        else:
            new_instance = Instance()
            form_validated = False

        for factory in formset_factories:
            formsets.append(factory(request.POST, request.FILES, instance=new_instance))

        if all_valid(formsets) and form_validated:
            save_all(new_instance, form, formsets)
            return HttpResponseRedirect('/dm/instance/print/'+str(new_instance.id)+'/')

    else:
        """Initial values now given in InstanceForm __init__()"""
        #form = InstanceForm(initial={'instanciated_release' : instanciated_release,})
        form = InstanceForm()
        """ Queryset restriction now done in form __init__()"""
        #form.fields['instanciated_release'].queryset = Release.objects.filter(id=release_id)


        """form.fields[str(attribute)] = forms.ChoiceField(choices=(
            (u'A', u'A'),
            (u'B', u'B'),
        ))"""

        #InstanceAttributeFormset.extra=attributes_count
        #formset_attributes = InstanceAttributeFormset()
        """Initial values now given in form __init__()"""
        #formset_attributes = InstanceAttributeFormset(initial=initial_attributes)
        """ Queryset restriction now done in form __init__()"""
        #for subform, attribute in zip(formset_attributes.forms, initial_attributes):
        #    subform.fields['attribute'].queryset = Attribute.objects.filter(id=attribute['attribute'].id)

    
        #InstanceCompositionFormset.extra=composition_count
        #formset_composition = InstanceCompositionFormset()
        """ Queryset restriction now done in form __init__()"""
        #for subform, release_index in zip(formset_composition.forms, composing_releases_id):
        #    subform.fields['element_instance'].queryset = Instance.objects.filter(instanciated_release=release_index)

        #formset_pictures = InstancePictureFormset()

        #formset_specifics = InstanceSpecificsFormset()
        for factory in formset_factories:
            formsets.append(factory())

    form_action = '/dm/instance/add/'+str(release_id)+'/'
    return render(request, 'add_instance.html', {
        'form_action' : form_action,
        'form': form,
        'formsets' : formsets,
        #'formset_attributes' : formset_attributes,
        #'formset_composition' : formset_composition,
        #'formset_pictures' : formset_pictures,
        #'formset_specifics' : formset_specifics,
    })

def print_instance(request, instance_id):
    instance = Instance.objects.get(id=instance_id) 

    tag_image = instance.generate_tag()
    tag_io = StringIO.StringIO()
    tag_image.save(tag_io, format='PNG')

    tag_file = ContentFile(tag_io.getvalue())
    #Django is automatically prepending the MEDIA_ROOT to the 'upload_to' value during the default file upload workflow, here we have to do it by hand.
    name = os.path.join(
        conf.settings.MEDIA_ROOT, 
        name_tag(instance),
    )

    #Delete the tag image if it already exists (django default behavior being to rename the file if there is a collision)
    try:
        os.remove(name)
    except:
        pass

    instance.tag.save(name, tag_file)
    #no clue if we have to close it by hand, better safe...
    tag_file.close()

    # replace() in an attempt to support Windows host and still return a valid url
    #\todo : test the tag_url under Windows host
    tag_url = os.path.join(conf.settings.MEDIA_URL, name_tag(instance)).replace('\\', '/')
    return render(request, 'view_tag.html', {
        'tag_url' : tag_url,
        'form_action' : '/' + settings.URL_TAG_REDIRECT
    })
