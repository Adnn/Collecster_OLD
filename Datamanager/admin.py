from Datamanager.models import * 
from django.contrib import admin
from django.db import models

#Define an InlineAdminModel on ReleaseCompostion in order to add compositions directly on 'add Release' pages
class CompositionInline(admin.StackedInline):
    model = ReleaseComposition
    extra = 1
#Since a ReleaseComposition has 2 foreign keys on Release, we specify which Field name olds the key to the currently edited Release. So we set it to the container release.
    fk_name =  "container_release"

#Create a common admin ancestor for all derived Releases models to inherit.
class ReleaseAdmin(admin.ModelAdmin): 
    inlines = [
        CompositionInline,
    ] 

class ConsoleAdmin(ReleaseAdmin):
    raw_id_fields = ("realised_concept",)
    list_display = ("__unicode__", "id",)


class InstanceAttributeInline(admin.StackedInline):
    model = InstanceAttribute      

class InstanceCompositionInline(admin.StackedInline):
    model = InstanceComposition
    fk_name = 'container_instance'

class InstancePictureInline(admin.StackedInline):
    model = InstancePicture

class ConsoleSpecificsInline(admin.StackedInline):
    model = ConsoleSpecifics

from django import forms
from django.forms.formsets import formset_factory
class TestForm(forms.Form):
    title = forms.CharField()

class InstanceAdmin(admin.ModelAdmin):
    """def get_form(self, request, obj=None, **kwargs):
        self.inlines += [ InstanceAttributeInline,]
        return super(InstanceAdmin, self).get_form(request, obj, **kwargs)
        """
    """def get_formsets(self, request, obj=None):
        #yield InstanceAttributeInline
        for inline in self.get_inline_instances(request):
            print "B\n"
            #yield inline.get_formset(request, obj)
            yield InstanceAttributeInline(Instance, admin.site).get_formset(request, obj)
            """ 
    def get_inline_instances(self, request):
        InstanceAttributeInline.extra = 1 
        self.inlines = [InstanceAttributeInline, InstanceCompositionInline, InstancePictureInline, ConsoleSpecificsInline]
        inline_instances = super(InstanceAdmin, self).get_inline_instances(request)
        
        for inline in inline_instances:
            #inline.fields['value'].default = 5
            pass
        return inline_instances

admin.site.register(Concept)
admin.site.register(Console, ConsoleAdmin)
admin.site.register(Attribute)
admin.site.register(AttributeCategory)

#to del
admin.site.register(Instance, InstanceAdmin)
