from OOExample.models import *
from django.contrib import admin
from django.db import models
from django import forms
from django.forms.models import modelformset_factory, inlineformset_factory, BaseInlineFormSet

class AugmentedQuerySet(models.query.QuerySet):
    forwarded_id = 0

    def set_forwarded_id(self, aid):
        self.forwarded_id=aid

class CustomInlineFormset(BaseInlineFormSet):
    def __init__(self, data=None, files=None, instance=None,
        save_as_new=False, prefix=None, queryset=None, **kwargs):
        instance_id = queryset[1]
        print "__init__ received id : " + str(instance_id)
        super(CustomInlineFormset, self).__init__(data, files, instance, save_as_new, prefix, queryset[0], **kwargs)

    def _construct_form(self, i, **kwargs):
        form = super(CustomInlineFormset, self)._construct_form(i, **kwargs) 
        print "Custom::_construct_form"
        return form

class CustomInlineInstanceAttribute(admin.StackedInline):
    model = InstanceAttribute
    formset = CustomInlineFormset
    extra = 1 

    def queryset(self, request):
        print "Custom::_queryset for release : " + str(request.GET['release'])
        queryset_forward = [super(CustomInlineInstanceAttribute, self).queryset(request),
                            request.GET['release'],]
        print type(queryset_forward[0])
        return queryset_forward

class CustomAdmin(admin.ModelAdmin):
    inlines = [CustomInlineInstanceAttribute,]
