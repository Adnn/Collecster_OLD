#!/usr/bin/env python

import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Collecster.settings")
django.setup()

from advideogame.models import *
from advideogame.configuration import *
from supervisor.models import *

Purchase.objects.all().delete()
PurchaseContext.objects.all().delete()
Location.objects.all().delete()
