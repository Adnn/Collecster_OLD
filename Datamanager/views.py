from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.forms.models import modelformset_factory, inlineformset_factory

from Datamanager.models import *
from django import forms
from django.forms.formsets import all_valid

class InstanceForm(forms.ModelForm):
    release_id = 0

    class Meta:
        model = Instance

    def __init__(self, *args, **kwargs):
        super(InstanceForm, self).__init__(*args, **kwargs)
        release_id = InstanceForm.release_id
        self.initial = {'instanciated_release' : release_id,}
        self.fields['instanciated_release'].queryset = Release.objects.filter(id=release_id)

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
        InstanceAttributeModelForm.form_id += 1


class InstanceCompositionModelForm(forms.ModelForm):
    form_id = 0
    composing_releases_ids = []
    
    def __init__(self, *args, **kwargs):
        super(InstanceCompositionModelForm, self).__init__(*args, **kwargs)
        release_index = InstanceCompositionModelForm.composing_releases_ids[InstanceCompositionModelForm.form_id]
        self.fields['element_instance'].queryset = Instance.objects.filter(instanciated_release=release_index)
        InstanceCompositionModelForm.form_id += 1
         
def save_all(instance, form, formsets):
    #Since we used 'commit=False' on form saving, we need to save the instance by hand, and also its many-2-many relationships
    instance.save()
    form.save_m2m()
    for formset in formsets:
        formset.save()



def add_instance(request, release_id):
    #instanciated_release = Release.objects.get(id=release_id)
    instanciated_release = Release.objects.get_subclass(id=release_id)
    DerivedInstance = type(instanciated_release)
    print DerivedInstance

    initial_attributes = []
    attributes_count = 0
    for attribute in instanciated_release.attribute.all():
        initial_attributes.append({'attribute':attribute,})
        attributes_count += 1

    composing_releases_id = []
    composition_count = 0
    for nested_release in ReleaseComposition.objects.filter(container_release=instanciated_release):
        # \todo : .id is not necessary for functionnality, but does it change the value stored in the list ?
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
        InstanceSpecificsFormset = inlineformset_factory(Instance, DerivedInstance.Dna.specifics, can_delete=False, extra=1, max_num=1)
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

        formset_specifics = InstanceSpecificsFormset()
        for factory in formset_factories:
            formsets.append(factory())

    print formsets[0].as_p()
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
    release_id = Instance.objects.get(id=instance_id).instanciated_release.id 
    derived_release = Release.objects.get_subclass(id=release_id)

    import qrcode
    from PIL import Image, ImageDraw 

    qr = qrcode.QRCode(
        box_size=2,
    )
    qr.add_data(str(instance_id))
    qr_image = qr.make_image()._img
    
    width = 180
    height = 60
    border_size = 1
    final_image = Image.new('RGB', (width, height), (255, 255, 255))
    draw = ImageDraw.Draw(final_image)
    #the image border
    draw.rectangle([(0,0), (width-1, height-1)], outline=(0,0,0))

    text_color = (255, 0, 0)
    draw.text((2, 1), derived_release.realised_concept.usual_name, fill=text_color)

    spot_color = (0, 255, 0)
    draw.ellipse([5,45,15,55], fill=spot_color)

    work_string = 'work'
    work_len = draw.textsize(work_string)[0]
    draw.text([25, 45], work_string, fill='black')
    draw.rectangle([25+work_len+2, 45, 35+work_len+2, 55], outline='black')

    final_image.paste(qr_image, (width-border_size-qr_image.size[0], border_size))
    
    final_image.show() 

    return HttpResponse(str(derived_release)) 
