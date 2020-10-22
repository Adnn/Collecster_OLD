#!/usr/bin/env python

import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Collecster.settings")
django.setup()

from advideogame.models import *
from advideogame.configuration import *
from supervisor.models import *

SystemVariant.objects.create(system_concept=Concept.objects.get(distinctive_name="Sega Master System"), variant_name="Sega Master System I")
SystemVariant.objects.create(system_concept=Concept.objects.get(distinctive_name="Sega Master System"), variant_name="Sega Master System II")

#SystemVariant.objects.create(system_concept=Concept.objects.get(distinctive_name="Sega Mega Drive"), variant_name="Sega Mega Drive II")
#SystemVariant.objects.create(system_concept=Concept.objects.get(distinctive_name="Sega Mega Drive"), variant_name="Sega Mega Drive II")

SystemVariant.objects.create(system_concept=Concept.objects.get(distinctive_name="Sega Saturn"), variant_name="Sega Saturn")
SystemVariant.objects.create(system_concept=Concept.objects.get(distinctive_name="Sega Saturn"), variant_name="Hitachi HiSaturn")

SystemVariant.objects.create(system_concept=Concept.objects.get(distinctive_name="Sega Dreamcast"), no_variant=True)

SystemVariant.objects.create(system_concept=Concept.objects.get(distinctive_name="Wii"), variant_name="Wii")
SystemVariant.objects.create(system_concept=Concept.objects.get(distinctive_name="Wii"), variant_name="Wii mini")
