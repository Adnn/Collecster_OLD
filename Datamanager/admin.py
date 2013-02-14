from Datamanager.models import Concept, Console, Game, Content, ContentCategory
from django.contrib import admin

class ConsoleAdmin(admin.ModelAdmin):
    raw_id_fields = ("realised_concept",)

admin.site.register(Console, ConsoleAdmin)
admin.site.register(Content)
admin.site.register(ContentCategory)
admin.site.register(Concept)
