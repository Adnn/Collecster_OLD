from concept_specifics_table import concept_specifics_table

from Datamanager.models import *

def fix_concept_name(concept):
    if concept.complete_name:
        concept_name = concept.complete_name
    else:
        concept_name = concept.common_name

    if concept_name in concept_translation:
        concept_name = concept_translation[concept_name]

    return concept_name


def get_company(release):
    return release.company.name


def get_manufacturer(release):
    if not isinstance(release, Accessory):
        return release.constructor.name if release.constructor else "#TODO" 
    else:
        try:
            return release.realised_concept.company.name
        except:
            return "#TODO"

def from_q(model_name, q_dict):
    return "{}.objects.get(Q(**{}))".format(model_name, q_dict)


def try_specifics(occurrence):
    specific_classes = [ConsoleSpecifics, GameSpecifics, DemoSpecifics, ApplicationSpecifics, AccessorySpecifics]
    for cls in specific_classes:
        if cls.objects.filter(instance=occurrence).exists():
            return repr(cls.objects.get(instance=occurrence).working)
    raise Exception("Specific not found in source.")


specifics_fields = {
    "ConceptSpecific.Remote": {"battery_type": None, },
    "ConceptSpecific.RemoteAccessory": {"wireless": False, },
    "ConceptSpecific.Shell": {"is_shell": False, },
    "ConceptSpecific.Controller": {
        "force_feedback": False,
        "rumble_feedback": False,
        "autofire": False,
        "slow": False,
    },
    "ConceptSpecific.DirectionalController": { "direction_input_type": (1,) },

    "ReleaseSpecific.Combo": {
        "brand": lambda release: from_q("Company", {"name": get_company(release)})
    },
    "ReleaseSpecific.Hardware": {
        "color": lambda release: from_q("Color", {"name": (release.color.name if hasattr(release, "color") else release.colors.all()[0].name)}),
        "manufacturer": lambda rel: from_q("Company", {"name": get_manufacturer(rel)}),
    },
    "ReleaseSpecific.Software": {
        "publisher": lambda release: from_q("Company", {"name": (release.publisher.name)}),
        "porter": None,
        "collection_label": "",
    },
    "ReleaseSpecific.Demo": {
        "issue_number": lambda release: (release.issue_number),
        "games_playable": lambda release: ( ", ".join([fix_concept_name(con) for con in release.playable_games.all()]) ),
        "games_video": lambda release: ( ", ".join([fix_concept_name(con) for con in release.video_games.all()]) )
    },
    "ReleaseSpecific.Media": {
        "media_types": "#TODO",
    },
    "ReleaseSpecific.Memory": {
        "capacity": "#TODO",
        "unit": "#TODO",
    },
    "ReleaseSpecific.Variant": {
        "system_variant": "#TODO",
    },

    "OccurrenceSpecific.OperationalOcc": {
        "working_condition": try_specifics
    },
    "OccurrenceSpecific.ConsoleOcc": {
        "region_modded": False,
        "copy_modded": False,
    },

}

concept_translation = {
    "Pad Saturn official": "Sega Saturn Control Pad",
    "3D Pad Saturn": "3D Control Pad (Saturn)",
    "Pad Dreamcast official": "Dreamcast Controller",
    "Pad Master System official": "Master System Control Pad",
    "Vibration Pack Dreamcast": "Dreamcast Vibration Pack",
    "Dreamon Collection": "Dream On Collection",
    "Sonic the Hedgehog 2": "Sonic the Hedgehog 2 (8-bit)",
    "Disney's Aladdin": "Disney's Aladdin (SIMS)",
    "Action Replay Saturn EMS": "Action Replay Plus 4M (Saturn EMS)",
    "Photo CD Operating System Saturn": "Photo CD Operating System (Saturn)",
    "Dragon Ball Z The Legend": "Dragon Ball Z: The Legend",
    "Sega Master System II": "Sega Master System",
    "_combopack_": "_COMBO",
}

specific_code_template = "specific = {specific_class}.objects.create({related_field}={related_instance}, {fields})"

def additional_fields(specific_classname, source_instance):
    data = specifics_fields[specific_classname]
    if isinstance(data, dict):
        #return "**{}".format(data)
        return "**{{{}}}".format(", ".join(["{}: {}".format(repr(key), value(source_instance) if callable(value) else repr(value))
                                            for key, value in data.iteritems()]))
    #else:
    #    return "{}, **{}".format(", ".join(data[0]), data[1])

def specific_code(specific_classname, related_field, related_instance, source_instance=None):
    return specific_code_template.format(specific_class=specific_classname, related_field=related_field,
                                         related_instance=related_instance,
                                         fields=additional_fields(specific_classname, source_instance))

def concept_specifics_code_for(nature):
    code = [] 
    for specific_classname in concept_specifics_table[nature]:
        code.append(specific_code(specific_classname, "concept", "concept"))
    return "\n".join(code)

def release_specifics_code_for(specific_list, release):
    code = [] 
    for specific_classname in specific_list:
            specific_classname = "ReleaseSpecific."+specific_classname
            code.append(specific_code(specific_classname, "release", "release", release))
    return "\n".join(code)

def occurrence_specifics_code_for(specific_list, occurrence):
    code = [] 
    for specific_classname in specific_list:
            specific_classname = "OccurrenceSpecific."+specific_classname
            code.append(specific_code(specific_classname, "occurrence", "occurrence", occurrence))
    return "\n".join(code)


def get_preamble():
    preamble = ("""#!/usr/bin/env python

import os, django
os.environ.setdefault(\"DJANGO_SETTINGS_MODULE\", \"Collecster.settings\")
django.setup()

from advideogame.models import *
from advideogame.configuration import *
from supervisor.models import *

import datetime
import pytz

def get_userextension(name):
    return UserExtension.objects.get(user__username=name)

def get_person(lookup):
    return Person.objects.get(Q(**lookup))

def get_concept(name):
    return Concept.objects.get(distinctive_name=name)

def get_occurrence(pk):
    return Occurrence.objects.get(pk=pk)

def get_corresponding_release_attribute(release, note, lookup_dict):
    if note:
        return ReleaseAttribute.objects.get(release=release, note=note, attribute=Attribute.objects.get(Q(**lookup_dict)))
    else:
        return ReleaseAttribute.objects.get(release=release, attribute=Attribute.objects.get(Q(**lookup_dict)))

def get_corresponding_release_compo(lookup_dict):
    return ReleaseComposition.objects.get(Q(**lookup_dict))
    
# All pictures are attached to non-custom ReleaseAttribute instances.
ReleaseAttribute_contentype = ContentType.objects.get_for_model(ReleaseAttribute)

""")
    return preamble

