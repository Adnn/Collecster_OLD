#!/usr/bin/env python

import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Collecster.settings")
django.setup()

from advideogame.models import *
from advideogame.configuration import *
from supervisor.models import *


StorageUnit.objects.create(name="byte", byte_equivalence=1)
StorageUnit.objects.create(name="kilobyte", byte_equivalence=1024)
StorageUnit.objects.create(name="megabyte", byte_equivalence=1048576)

StorageUnit.objects.create(name="block (Dreamcast)", brand=Company.objects.get(name="Sega"), byte_equivalence=512)

StorageUnit.objects.create(name="block (GameCube)", brand=Company.objects.get(name="Nintendo"), byte_equivalence=65536)
