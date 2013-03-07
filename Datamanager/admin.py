from Datamanager.models import * 
from django.contrib import admin
from django.db import models
from django import forms
from django.forms.formsets import formset_factory

from Datamanager import settings

class AttributeAdmin(admin.ModelAdmin):
    readonly_fields= ('implicit',)

    def queryset(self, request):
        qs = super(AttributeAdmin, self).queryset(request)
        return qs
#use the second return to filter out implicit attributes from the list view
        #return qs.filter(implicit=False)
    
#Define an InlineAdminModel on ReleaseCompostion in order to add compositions directly on 'add Release' pages
class ReleaseCompositionInline(admin.StackedInline):
    model = ReleaseComposition
    extra = 1
#Since a ReleaseComposition has 2 foreign keys on Release, we specify which Field name olds the key to the currently edited Release. So we set it to the container release.
    fk_name =  'container_release'

class SpecificityCompositionInline(admin.TabularInline):
    model = SpecificityComposition
    extra = 2

class ReleaseForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ReleaseForm, self).__init__(*args, **kwargs)
        #filter out the implicit attributes from the selectable list
        self.fields['attribute'].queryset = Attribute.objects.filter(implicit=False)

#Create a common admin ancestor for all derived Releases models to inherit.
class ReleaseAdmin(admin.ModelAdmin): 
    form = ReleaseForm

    list_display = ('id', str, 'instanciate_link')
    #since only games can be immaterial, the default is to hide the choice (default being False)
    exclude = ('immaterial',)
    #raw_id_fields = ("realised_concept",)
    inlines = [
        SpecificityCompositionInline,
        ReleaseCompositionInline,
    ] 
    filter_horizontal = [
        'attribute',
    ]

    def instanciate_link(self, obj):
        if obj.immaterial==False:
            url = '/' + settings.URL_DM + settings.URL_ADD_INSTANCE+str(obj.id) + '/'
            return '<a href="' + url + '">instanciate</a>' 
        else:
            return 'immaterial'

    instanciate_link.allow_tags = True
    instanciate_link.short_description = 'Add instance'

class ComboPackAdmin(ReleaseAdmin):
    pass

class ConsoleAdmin(ReleaseAdmin):
    pass

class GameAdmin(ReleaseAdmin):
    exclude = ()

class AccessoryAdmin(ReleaseAdmin):
    #filter_horizontal = ReleaseAdmin.filter_horizontal + [
    #    'colors',
    #] 
    pass

class InstanceAttributeInline(admin.StackedInline):
    model = InstanceAttribute      
    extra = 0 

class InstanceCompositionInline(admin.StackedInline):
    model = InstanceComposition
    fk_name = 'container_instance'
    extra = 0

class InstancePictureInline(admin.StackedInline):
    model = InstancePicture

class ConsoleSpecificsInline(admin.StackedInline):
    model = ConsoleSpecifics

class GameSpecificsInline(admin.StackedInline):
    model = GameSpecifics

class AccessorySpecificsInline(admin.StackedInline):
    model = AccessorySpecifics

class BundleCompositionInline(admin.StackedInline):
    model = BundleComposition
    extra = 4

class BuyingAdmin(admin.ModelAdmin):
    inlines = [BundleCompositionInline,]

#Solution to allow the duplication of 'empty' common_name values (unique otherwise)
#from SO : http://stackoverflow.com/questions/454436/unique-fields-that-allow-nulls-in-django
class ConceptForm(forms.ModelForm):
    class Meta:
        model = Concept
    def clean_complete_name(self):
        name = self.cleaned_data['complete_name']
        if name == '':
            name = None
        return name 

class ConceptAdmin(admin.ModelAdmin):
    form = ConceptForm

class PlatformForm(forms.ModelForm):
    class Meta:
        model = Platform
    def clean_abbreviated(self):
        abbreviated = self.cleaned_data['abbreviated']
        if abbreviated == '':
            abbreviated = None
        return abbreviated 

class PlatformAdmin(admin.ModelAdmin):
    form = PlatformForm

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
    DICT = {
        AccessorySpecifics : AccessorySpecificsInline,
        GameSpecifics : GameSpecificsInline,
        ConsoleSpecifics : ConsoleSpecificsInline,
    }

    def get_inline_instances(self, request):
        self.inlines = [InstanceAttributeInline, InstanceCompositionInline, InstancePictureInline]
        wordlist = request.path.rsplit('/', 3)
        if len(wordlist)==4 and (wordlist[1]=='instance') :
            try:
                instance_id = int(wordlist[2])
                instance = Instance.objects.get(id=instance_id)
                release = Release.objects.get_subclass(id=instance.instanciated_release.id)
                Specifics = type(release).Dna.specifics
                self.inlines.insert(0, self.DICT[Specifics])
            except:
                pass

        inline_instances = super(InstanceAdmin, self).get_inline_instances(request)
        return inline_instances

admin.site.register(Concept, ConceptAdmin)
admin.site.register(ComboPack, ComboPackAdmin)
admin.site.register(Console, ConsoleAdmin)
admin.site.register(Game, GameAdmin)
admin.site.register(Accessory, AccessoryAdmin)
admin.site.register(Platform, PlatformAdmin)
admin.site.register(Attribute, AttributeAdmin)
admin.site.register(AttributeCategory)
admin.site.register(Company)

#to del
admin.site.register(Instance, InstanceAdmin)
admin.site.register(Release, ReleaseAdmin)

admin.site.register(Buying, BuyingAdmin)
admin.site.register(BuyingContext)
admin.site.register(Location)
admin.site.register(Person)
admin.site.register(Specificity)
