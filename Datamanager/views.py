from django.http import HttpResponse
from django.shortcuts import render, render_to_response
from django.forms.models import modelformset_factory

from Datamanager.models import *
from django import forms

class InstanceForm(forms.ModelForm):
    class Meta:
        model = Instance

class InstanceAttributeForm(forms.ModelForm):
    class Meta:
        model = InstanceAttribute

def add_instance(request, release_id):
    instanciedRelease = Release.objects.get(id=release_id)
    form = InstanceForm(initial={'instanciated_release' : instanciedRelease.id, 'price' : 10, 'price' : 10})

    #InstanceAttributeFormset = modelformset_factory(InstanceAttribute)
    #initialAttributes = []
    for attribute in instanciedRelease.attribute.all():
        instanceAttribute = InstanceAttribute()
        instanceAttribute.attribute = attribute

        form2 = InstanceAttributeForm(instance=instanceAttribute)
        #initialAttributes.append(instanceAttribute) 
        
        #formset = InstanceAttributeFormset(initial={'attribute':attribute})
        """form.fields[str(attribute)] = forms.ChoiceField(choices=(
            (u'A', u'A'),
            (u'B', u'B'),
        ))"""

    """for nestedRelease in ReleaseComposition.objects.filter(container_release=instanciedRelease.id):
        form.fields[str(nestedRelease.element_release)] = forms.ModelChoiceField(queryset=Instance.objects.filter(instanciated_release=nestedRelease.element_release.id))
    """
    return render(request, 'add_instance.html', {
        'form': form,
        'form2': form2,
    })
    
