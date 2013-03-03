from OOExample.models import *
from django.contrib import admin
from django.db import models
from django import forms
from django.forms.models import modelformset_factory, inlineformset_factory

import traceback
import sys


class InstanceForm(forms.ModelForm):
    class Meta:
        model = Instance

    #static id of the instanciated release, that should be set before constructor call.
    release_id = 0
    
    def __init__(self, *args, **kwargs):
        super(InstanceForm, self).__init__(*args, **kwargs)
        self.initial = {'release' : InstanceForm.release_id,}
        self.fields['release'].queryset = Release.objects.filter(id=InstanceForm.release_id)

class InstanceAttributeForm(forms.ModelForm):
    #form_id count the initializations (to know which form is currently constructed by the formset)
    form_id = 0
    total = 0
    #the list of attributes in the instanciated release
    #it should be populated before the formset start the constructor calls
    attributes = []

    def __init__(self, *args, **kwargs):
        super(InstanceAttributeForm, self).__init__(*args, **kwargs)
        #Some 'deferred template rendering' is trying to construct 3 additional forms each time
        #bonus point if you can comment on the reason for this behavior  ; )
        if InstanceAttributeForm.form_id==InstanceAttributeForm.total:
            return

        attribute = InstanceAttributeForm.attributes[InstanceAttributeForm.form_id]
        self.initial = {'attribute' : attribute}
        self.fields['attribute'].queryset = Attribute.objects.filter(id=attribute.id)
        InstanceAttributeForm.form_id += 1


def initialize_globalstate(request):
    instanciated_release = Release.objects.get(id=request.GET['release'])
    InstanceForm.release_id = instanciated_release.id

    InstanceAttributeForm.form_id = 0
    InstanceAttributeForm.attributes = instanciated_release.attributes.all()
    InstanceAttributeForm.total = len(InstanceAttributeForm.attributes)
    
    
    
class InstanceAttributeInline(admin.StackedInline):
    model = InstanceAttribute

class InstanceAdmin(admin.ModelAdmin):
    form = InstanceForm
    inlines = [InstanceAttributeInline,]

    #Responsible for re-initializing the global state each time before calling the super add_view
    def add_view(self, request, form_url='', extra_context=None):
        initialize_globalstate(request)
        return super(InstanceAdmin, self).add_view(request, form_url, extra_context)

    #Return a formset factory specifying the exact number of required, and hooking our specialised ModelForm class
    def get_formsets(self, request, obj=None):
        for inline in self.get_inline_instances(request):
            if type(inline) == InstanceAttributeInline:
                yield inlineformset_factory(Instance, InstanceAttribute, form=InstanceAttributeForm, can_delete=False, extra=InstanceAttributeForm.total)
            else:
                yield inline.get_formset(request, obj)

admin.site.register(Attribute)
admin.site.register(Release)
admin.site.register(Instance, InstanceAdmin)
