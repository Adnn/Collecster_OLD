#!/usr/bin/env python

import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Collecster.settings")
django.setup()

import json

from advideogame.configuration import ConfigNature

nature_dict = {}
for nature in ConfigNature.DATA:
    print ("Nature: {}".format(nature))
    nature_dict[nature] = ["ConceptSpecific.{}".format(Specific.__name__) for Specific in ConfigNature.get_concept_specifics((nature,))]

with open("concept_specifics_table.py", "w") as f:
    f.write("concept_specifics_table = {}".format(json.dumps(nature_dict, sort_keys=True, indent=4)))
