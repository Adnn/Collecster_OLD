#!/usr/bin/env python

import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Collecster.settings")
django.setup()

from Datamanager.models import *

from helper_specifics import *

from bridge_destination import *

import collections, urllib, urllib2, json

release_dict = {}
#DataTuple = collections.namedtuple("DataTuple", ["concept", "dict", "extra"])
class DataTuple(object):
    pass


#for release in Release.objects.all():
for release in Release.objects.select_subclasses():
    data = DataTuple()
    extra = []


    if release.pk == 19: # the problematic VirtuaCop
        release.loose = False
        release.region = "EU"
        #release.platform = "EU"
        release.publisher = Company.objects.get(name="Sega")

    if release.pk == 92:  # nympheas photo cd
        release.publisher = Company.objects.get(name="Sega")

    #
    # Concept name
    #
    concept = release.realised_concept
    data.concept = fix_concept_name(concept)


    print(u"pk: {} || {} || {}".format(release.pk, repr(release.name), data.concept))

    data.dict = {
        "name": release.name,
        "pk": release.pk
    }

    #
    # Partial date
    #
    if release.date:
        if release.date.day == 1:
            if release.date.month == 1:
                partial_precision = "YYYY"
            else:
                partial_precision = "MM"
        else:
            partial_precision = "DD"
        data.dict["partial_date"] = release.date
        data.dict["partial_date_precision"] = partial_precision

    #
    # Specificity
    #
    if release.specificity_text:
        extra.append("[SPECIFICITY] {}".format(release.specificity_text))


    #
    # Attributes
    #
    data.attributes = []
    #for attribute in release.attribute.all():
    for attribute in release.get_attributes():
        attribute_dict = {
            "category__name": attribute.category.name,
            "name": attribute.name,
        }
        #attribute_translation = {
        #    {"category__name": "stuffing", "name": "printed inlay"}: {"category__name": "packaging", "name": "printed cardboard inlay"}
        #}
        if attribute_dict["category__name"] == "stuffing" and attribute_dict["name"] == "printed inlay":
            attribute_dict = {"category__name": "packaging", "name": "printed cardboard inlay"}
        data.attributes.append(attribute_dict)

    # alert on duplicates
    unique_attribs = set()
    for dump_attrib in data.attributes:
        if str(dump_attrib) not in unique_attribs:
            unique_attribs.add(str(dump_attrib))
        else:
            extra.append("[DUPLICATE ATTIBUTE] {}".format(dump_attrib))

    # put self first
    for dump_attrib in data.attributes:
        if dump_attrib["name"] == "self":
            data.attributes.remove(dump_attrib)
            data.attributes.insert(0, dump_attrib)


    #
    # release composition
    #
    data.compositions = []
    for composition in ReleaseComposition.objects.filter(container_release=release):
        data.compositions.append({
            "pk": composition.element_release.pk
        })

    #
    # immaterial & loose
    #
    if release.pk not in (69, 74):
        data.dict["immaterial"] = release.immaterial
        #data.dict["loose"] = release.loose
        if release.loose:
            extra.append("[LOOSE]")
    else:
        data.dict["immaterial"] = False
        data.dict["loose"] = False

    data.extra = extra
    release_dict[release.pk] = data

    #
    # specificity
    #
    for specificity_comp in SpecificityComposition.objects.filter(release=release):
        extra.append("[SPECIFICITY] {}: {}".format(specificity_comp.specificity.name, specificity_comp.value))

    #
    # Region
    #
    data.m2m = []
    region_map = {
            "EU": "EU",
            "JP": "JP",
    }

    if release.region:
        data.m2m.append(("ReleaseRegion", "release_regions", {"name": region_map[release.region]},))
    else:
        extra.append("[REGION] no region")
    data.dict["unsure_region"] = True

    #
    # specifics
    #
    def get_specific_classnames(release):
        resp = urllib2.urlopen("http://localhost:5000/advideogame/import_help/release_specific_classes/concept/?{}"
                                    .format(urllib.urlencode({"distinctive_name": data.concept.encode("utf-8")})))
        return json.loads(resp.read())

    data.specifics = release_specifics_code_for(get_specific_classnames(release), release)

    #
    # Derived Release
    #
    if isinstance(release, Accessory) and release.quantity != 1:
        data.extra.append("[QTY] {} with colors: {}".format(release.quantity, ", ".join(["{}".format(color) for color in release.colors.all()])))
    ## COMBO
    #release.company -> ReleaseSpecific.Combo.brand

    #
    # version
    #
    if hasattr(release, "version"):
        data.dict["version"] = release.version if release.version is not None else ""

    if isinstance(release, Accessory):
        if release.wireless:
            data.extra.append("Wireless")
        if release.force_feedback:
            data.extra.append("Force feedback")
        if release.rumble_feedback:
            data.extra.append("Rumble")

data = None
release

preamble = ("""#!/usr/bin/env python

import os, django
os.environ.setdefault(\"DJANGO_SETTINGS_MODULE\", \"Collecster.settings\")
django.setup()

from advideogame.models import *
from advideogame.configuration import *
from supervisor.models import *

import datetime

def get_userextension(name):
    return UserExtension.objects.get(user__username=name)

def get_concept(name):
    return Concept.objects.get(distinctive_name=name)

""")

with open("import_releases.py", "w") as f :
    f.write(preamble)
    for key, release_data in release_dict.iteritems():
        line = "\t#{}\n".format(release_data.concept.encode("utf8"))
        line += ("release = Release.objects.create(created_by=get_userextension(\"ad\"), concept=get_concept({}),\n"
                 "                                  **{}\n"
                 #"                                 , system_specification=#TODO")
                 ")\n").format(repr(release_data.concept), release_data.dict,)
        if release_data.attributes:
            for attrib in release_data.attributes:
                #line += "release.releaseattribute_set.add( Attribute.objects.get(Q(**{})) )\n".format(attrib)
                line += "release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{}))), bulk=False )\n".format(attrib)
        if release_data.compositions:
            for compo in release_data.compositions:
                line += "release.nested_releases.add( ReleaseComposition(from_release=release, to_release=Release.objects.get(Q(**{}))), bulk=False )\n".format(compo)
        if release_data.m2m:
            for m2m in release_data.m2m:
                line += "release.{field}.add( {model_class}.objects.get(Q(**{lookup})) )\n".format(model_class=m2m[0], field=m2m[1], lookup=m2m[2])
        if release_data.extra:
            extra_text = "".join(["#{}\n".format(text) for text in release_data.extra])
            line += extra_text
        if release_data.specifics:
            line += release_data.specifics + "\n"
        line += "\n"
        f.write(line)
