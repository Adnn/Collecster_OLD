#!/usr/bin/env python

import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Collecster.settings")
django.setup()

from Datamanager.models import *

from helper_specifics import *

# Maps old category name to new nature name, when there is no strict matching
categories_translation_map = {
    "ANALOG_PAD": ("PAD", ["# TODO analog", ]),
    "RUMBLE": ("RUMBLE_PACK", []),
    "GESTURE_RECO": ("MOTION_SENSING", ["# TODO is it motion sensing ?",]),
}

concept_dict = {}

for concept in Concept.objects.all():
    if concept.common_name=="_combopack_":
        continue

    if concept.complete_name:
        values = {
            "distinctive_name": concept.complete_name,
            "common_name": concept.common_name,
        }
    else:
        values = {
            "distinctive_name": concept.common_name,
        }

    extra = []
    primary_nature = concept.category
    if primary_nature not in concept_specifics_table:
        if primary_nature in categories_translation_map:
            primary_nature = categories_translation_map[concept.category][0]
            extra = categories_translation_map[concept.category][1]
        else:
            print ("Absent nature: {}".format(primary_nature))
            raise Exception

    values["primary_nature"] = primary_nature

    if not concept.company:
        developer = "get_company(#TODO)"
    else:
        developer = "get_company(\"{}\")".format(concept.company.name)

    concept_dict[concept.pk] = (values, developer, concept_specifics_code_for(primary_nature), extra)

with open("import_concepts.py", "w") as f :
    for key, concept in concept_dict.iteritems():
        line = "concept = Concept.objects.create(developer={}, **{})\n".format(concept[1], concept[0])
        if concept[2]: #specifics
            line += "{}\n".format(concept[2])
        if concept[3]: #extra
            line += "#{}\n".format(concept[3])
        line += "\n"
        f.write(line)
    #    if company["services"]:
    #        lines = ["company.services.add({})\n".format(service) for service in company["services"]]
    #        f.write("".join(lines))
