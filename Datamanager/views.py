from django.http import HttpResponse
from django.shortcuts import render, render_to_response
from django.forms.models import modelformset_factory, inlineformset_factory

from Datamanager.models import *
from django import forms
from django.forms.formsets import all_valid

class InstanceForm(forms.ModelForm):
    class Meta:
        model = Instance

class InstanceAttributeForm(forms.ModelForm):
    class Meta:
        model = InstanceAttribute

def save_all(instance, form, formsets):
    #Since we used 'commit=False' on form saving, we need to save the instance by hand, and also its many-2-many relationships
    instance.save()
    form.save_m2m()
    for formset in formsets:
        formset.save()

def add_instance(request, release_id):
    formsets = []
    #if the form was submitted (false on first page load)
    if request.method == 'POST':
        #repopulate the form with posted data
        form = InstanceForm(request.POST)
        if form.is_valid():
            #We need the instance model to bind it to the inlineformset [which needs to know the foreign key], but we do not save it to the DB yet using 'commit=False'
            new_instance = form.save(commit=False)
            form_validated = True
        else:
            new_instance = Instance()
            form_validated = False

        #We get the factory for an inlineformset (derived from modelformset) that is modeling InstanceAttribute and links it to an Instance
        InstanceAttributeFormset = inlineformset_factory(Instance, InstanceAttribute, can_delete=False)
        formset = InstanceAttributeFormset(request.POST, instance=new_instance)

        formsets.append(formset)
        if all_valid(formsets) and form_validated:
            save_all(new_instance, form, formsets)
    else:
        instanciated_release = Release.objects.get(id=release_id)
        form = InstanceForm(initial={'instanciated_release' : instanciated_release,})

        initialAttributes = []
        attributesCount = 0
        for attribute in instanciated_release.attribute.all():
            initialAttributes.append({'attribute':attribute,})
            attributesCount += 1

            """form.fields[str(attribute)] = forms.ChoiceField(choices=(
                (u'A', u'A'),
                (u'B', u'B'),
            ))"""

        #with modelformset (and derived inlineformset), initial values only apply to extra forms : so we have to allow the exact number of extra forms matching the number of initials
        InstanceAttributeFormset = inlineformset_factory(Instance, InstanceAttribute, can_delete=False, extra=attributesCount)
        formset = InstanceAttributeFormset(initial=initialAttributes)

        composing_releases_id = []
        composition_count = 0
        for nested_release in ReleaseComposition.objects.filter(container_release=instanciated_release):
            # \todo : .id is not necessary for functionnality, but does it change the value stored in the list ?
            composing_releases_id.append(nested_release.element_release.id)
            composition_count += 1
            #form.fields[str(nested_release.element_release)] = forms.ModelChoiceField(queryset=Instance.objects.filter(instanciated_release=nested_release.element_release.id))
    
        InstanceCompositionFormset = inlineformset_factory(Instance, InstanceComposition, fk_name='container_instance',  can_delete=False, extra=composition_count)
    #InstanceCompositionFormset = modelformset_factory(Instance)
        formset_composition = InstanceCompositionFormset()
        for subform, release_id in zip(formset_composition.forms, composing_releases_id):
            subform.fields['element_instance'].queryset = Instance.objects.filter(instanciated_release=release_id)

    form_action = '/dm/instance/add/'+str(release_id)+'/'
    return render(request, 'add_instance.html', {
        'form_action' : form_action,
        'form': form,
        #'form2': form2,
        'formset_attributes' : formset,
        'formset_composition' : formset_composition
    })
    
