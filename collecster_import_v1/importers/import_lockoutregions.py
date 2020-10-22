#!/usr/bin/env python

import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Collecster.settings")
django.setup()

from advideogame.models import *

lockouts = [
    ("NTSC-J", "Japan and Asia", None), 
    ("NTSC-U", "North America and South America", None),
    ("PAL", "Europe, New Zealand and Australia", None),
    ("NTSC-C", "China", None),

    ("\"Famicom\"", "Japan", ("NES",)),
    ("NTSC", "North America", ("NES",)),
    ("PAL-A", "United Kingdom and Italy", ("NES",)),
    ("PAL-B", "Europe excluding both UK and Italy", ("NES",)),
]

for lockout in lockouts:
    lk = LockoutRegion.objects.create(region_name=lockout[0], note=lockout[1])
    if lockout[2]:
        for scope in lockout[2]:
            lk.limit_scope.add(BaseSystem.objects.get(abbreviated_name=scope))
