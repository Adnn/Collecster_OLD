#!/usr/bin/env python

import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Collecster.settings")
django.setup()

from advideogame.models import *
from advideogame.configuration import *
from supervisor.models import *


current_path = os.path.dirname(os.path.abspath(__file__))

def naive_script(script):
    naive_system(os.path.join(current_path, script))

def naive_system(command):
    result = os.system(command)
    if result:
        raise Exception("Command '{}' did not complete successfully. Returned {}.".format(command, result))


Company.objects.all().delete()
naive_script("import_companies_edited.py")

Concept.objects.exclude(distinctive_name="_COMBO").delete()
naive_script("import_concepts_edited.py")

Distinction.objects.all().delete()
naive_script("import_distinctions.py")

SystemVariant.objects.all().delete()
naive_script("import_variants.py")

StorageUnit.objects.all().delete()
naive_script("import_storageunit.py")

naive_script("import_system_specs_manual.py")
BaseSystem.objects.all().delete()
SystemInterfaceDetail.objects.all().delete()
InterfacesSpecification.objects.all().delete()
naive_script("import_base_system.py")
#
LockoutRegion.objects.all().delete()
naive_script("import_lockoutregions.py")
#
naive_script("import_interface_spec.py")
naive_script("import_interface_spec_custom.py")

Release.objects.all().delete()
CollectionLabel.objects.all().delete()
SystemSpecification.objects.all().delete()
naive_script("import_releases_edited.py")

# Medias MUST BE DONE BEFORE OCCURRENCE, as occurences_custom generates some tags
if os.path.isdir("media"):
    naive_system("printf \"Replacing media content\\n\" && rm -r media")
naive_system("unzip -q {}".format(os.path.join(current_path, "exported_media.zip")))

Occurrence.objects.all().delete()
naive_script("import_occurrences_custom.py")
naive_script("import_occurrences_edited.py")

naive_script("delete_bundles.py")
naive_script("import_bundles_edited.py")

# Resets the next available primary key for all models in advideogame
# see: http://stackoverflow.com/q/9108833
naive_system("python manage.py sqlsequencereset advideogame | python manage.py dbshell -v 0")
