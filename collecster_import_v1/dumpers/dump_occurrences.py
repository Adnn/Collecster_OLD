#!/usr/bin/env python

import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Collecster.settings")
django.setup()

from Datamanager.models import *

from helper_specifics import *

import collections, urllib, urllib2, json


def translate_attribute(attribute_dict):
    if attribute_dict["category__name"] == "stuffing" and attribute_dict["name"] == "printed inlay":
        attribute_dict.update({"category__name": "packaging", "name": "printed cardboard inlay"})
    if attribute_dict["category__name"] == "stuffing" and attribute_dict["name"] == "inlay":
        attribute_dict.update({"category__name": "packaging", "name": "cardboard inlay non-decorative"})
    if attribute_dict["category__name"] == "papers" and attribute_dict["name"] == "insert : jewel box":
        attribute_dict["name"] = "insert: jewel box"
    if attribute_dict["category__name"] == "stuffing" and attribute_dict["name"] == "baggies":
        attribute_dict["category__name"] = "packaging"
    if attribute_dict["category__name"] == "stuffing" and attribute_dict["name"] == "connector protection":
        attribute_dict.update({"category__name": "packaging", "name":  "disposable connector protection"})
    if attribute_dict["category__name"] == "content" and attribute_dict["name"] == "connector cap":
        attribute_dict["name"] =  "intrinsic connector cap"
    if attribute_dict["category__name"] == "stuffing" and attribute_dict["name"] == "inlay polystyrene":
        attribute_dict["category__name"] = "packaging"

## Actually useless: the migrated-from version does not instantiate immaterial releases.
#immaterial_releases = [63,] # Only Alex Kidd in the MSII is immaterial on this migration

occurrence_dict = {}

class DataObject(object):
    pass

for occurrence in Instance.objects.all():
    data = DataObject()
    occurrence_dict[occurrence.pk] = data
    extra = []
    data.extra = extra

    data.release_pk = occurrence.instanciated_release.pk

    data.dict = {
        "pk":       occurrence.pk,
        "purchase_price": occurrence.price,
        "origin":   occurrence.origin,

        "add_date": occurrence.add_date,
        "lastmodif_date": occurrence.lastmodif_date,
    }

    if occurrence.notes:
        extra.append("[NOTES] {}".format(occurrence.notes))

    try:
        gs = GameSpecifics.objects.get(instance=occurrence)
        data.dict["blister"] = gs.blister
    except GameSpecifics.DoesNotExist:
        data.dict["blister"] = False


    #
    # Attributes
    #
    data.attributes = []
    self_id = 0
    for instance_attribute in occurrence.instanceattribute_set.all():
        attribute_dict = {
            "category__name": instance_attribute.attribute.category.name,
            "name": instance_attribute.attribute.name,
        }
        translate_attribute(attribute_dict)

        # Adds notes to self
        note = ""
        if instance_attribute.attribute.name == "self":
            self_id += 1
            if occurrence.pk == 10: #singstar mic
                if self_id == 1:
                    note = "red"
                else:
                    note = "blue"
            elif occurrence.pk == 14: #buzzers
                 note = str(self_id)

        value = instance_attribute.value
        if value == "on":
            value = "1"
        if value == "":
            value = "0"
        data.attributes.append({"lookup": attribute_dict, "value": value, "note": note})

    # put self first
    insert_pos = 0
    for dump_attrib in data.attributes:
        lk = dump_attrib["lookup"]
        if lk["name"] == "self":
            data.attributes.remove(dump_attrib)
            data.attributes.insert(insert_pos, dump_attrib)
            insert_pos += 1

        if occurrence.pk in [21, 22] and lk["name"]=="manual": #loose VirtuaGun
            data.attributes.remove(dump_attrib)

        if occurrence.pk == 82 and lk["name"]=="manual": #delux WC2
            dump_attrib["note"] = "Tides of Darkness"

        if occurrence.pk in [84, 85, 86] and lk["name"]=="manual": #loose VirtuaGun
            lk["name"] = "manual: jewel box"

    # Manual attributes
    def reorder_attribute(attribute_name, destination_index):
        for attribute in data.attributes:
            if attribute["lookup"]["name"] == attribute_name:
                data.attributes.remove(attribute)
                data.attributes.insert(destination_index, attribute)
                return

    if occurrence.pk == 1: #Doom
        reorder_attribute("insert: jewel box", 3)
        
    if occurrence.pk == 10: #Singstar mic
        lookup = {
            "category__name": "content",
            "name": "receiver interface",
        }
        data.attributes.insert(2, {"lookup": lookup, "value": "M", "note":""})

    if occurrence.pk == 14: #Buzzers
        lookup = {
            "category__name": "content",
            "name": "receiver interface",
        }
        data.attributes.insert(4, {"lookup": lookup, "value": "M", "note":""})

    if occurrence.pk == 50: #VMU
        reorder_attribute("intrinsic connector cap", 1)
        data.attributes[1]["value"] = "A"

    if occurrence.pk == 53: #VMU
        data.attributes[1]["value"] = "0"

    if occurrence.pk == 62: #Operation wolf
        lookup = {
            "category__name": "packaging",
            "name": "hang on tab",
        }
        data.attributes.insert(2, {"lookup": lookup, "value": "1", "note":""})

    if occurrence.pk == 82: #Operation wolf
        lookup = {
            "category__name": "papers",
            "name": "manual",
        }
        data.attributes.insert(4, {"lookup": lookup, "value": "M", "note":"Edition Deluxe"})
        lookup = {
            "category__name": "papers",
            "name": "warranty",
        }
        data.attributes.insert(5, {"lookup": lookup, "value": "M", "note":""})


    #
    # composition
    #
    data.compositions = []
    for composition in occurrence.container_instance.all():
        data.compositions.append({
            "pk": composition.element_instance.pk,
            "release_pk": composition.element_instance.instanciated_release.pk,
        })

    if occurrence.pk == 19: # Virtua gun
        data.compositions.append({ #empty compo
            "release_pk": 19 #Virtua cop release
        })

    if occurrence.pk == 67: # SMS II
        data.compositions.insert(0, { 
            "pk": 96,
            "release_pk": 63,
        })

    if occurrence.pk == 1: # Doom
        data.compositions.insert(0, { 
            "pk": 97,
            "release_pk": 99,
        })

    if occurrence.pk == 82: # WC2
        data.compositions.append({ 
            "pk": 98,
            "release_pk": 100,
        })


    #
    # specifics
    #
    concept = occurrence.instanciated_release.realised_concept
    data.concept = fix_concept_name(concept)

    def get_specific_classnames():
        url = ("http://localhost:5000/advideogame/import_help/occurrence_specific_classes/concept/?{}"
                                    .format(urllib.urlencode({"distinctive_name": data.concept.encode("utf-8")})))
        resp = urllib2.urlopen(url)
        return json.loads(resp.read())

    data.specifics = occurrence_specifics_code_for(get_specific_classnames(), occurrence)

    #
    # pictures
    #
    data.pictures = []
    for picture in InstancePicture.objects.filter(instance=occurrence):
        pic_dict = {
            "file": os.path.basename(picture.image.name),
            "detail": picture.detail,
        }
        if picture.detail != "GRP":
            pic_dict["attribute_lookup"] = {
                "category__name": picture.attribute.category.name,
                "name": picture.attribute.name
            }
            translate_attribute(pic_dict["attribute_lookup"])
        data.pictures.append(pic_dict)

data = None

with open("import_occurrences.py", "w") as f :
    f.write(get_preamble())
    for key, occurrence_data in occurrence_dict.iteritems():
        line = "\t#{}\n".format(occurrence_data.concept.encode("utf8"))
        line += ("occurrence = Occurrence.objects.create(created_by=get_userextension(\"ad\"), owner=get_person({{'first_name': 'Adrien'}}),"
                 #"                                  **{}\n"
                 " release=Release.objects.get(pk={}),"
                 " **{}"
                 ")\n").format(occurrence_data.release_pk, occurrence_data.dict,).replace("<UTC>", "pytz.utc")

        if occurrence_data.attributes:
            for attrib in occurrence_data.attributes:
                line += ("occurrence.attributes.add("
                             "OccurrenceAnyAttribute(occurrence=occurrence, value={attrib_value}, "
                             "attribute_id=get_corresponding_release_attribute(release={release}, note={note}, lookup_dict={corresp}).pk, "
                             "attribute_type=ReleaseAttribute_contentype), "
                         "bulk=False)\n"
                            .format(attrib_value=repr(attrib["value"]), release=occurrence_data.release_pk, note=repr(attrib["note"]), corresp=attrib["lookup"]))

        if occurrence_data.compositions:
            for compo in occurrence_data.compositions:
                lookup = {
                    "from_release": occurrence_data.release_pk,
                    "to_release": compo["release_pk"],
                }
                #line += ("occurrence.nested_occurrences.add( OccurrenceComposition(from_occurrence=occurrence, to_occurrence=Occurrence.objects.get(pk={}), "
                #         "release_composition=get_corresponding_release_compo({corresp})) )\n"
                #            .format(compo["pk"], corresp=lookup))
                to_occurrence = "to_occurrence=Occurrence.objects.get(pk={}), ".format(compo["pk"]) if "pk" in compo else "" 
                line += ("OccurrenceComposition.objects.create(from_occurrence=occurrence, {}"
                         "release_composition=get_corresponding_release_compo({corresp}))\n"
                            .format(to_occurrence, corresp=lookup))

        if occurrence_data.specifics:
            line += occurrence_data.specifics + "\n"

        # Tag to occurrence
        line += ("tto = TagToOccurrence.objects.create(user_creator=get_userextension(\"ad\"), user_occurrence_id={pk}, "
                  "occurrence=occurrence)\n"
                    .format(pk=occurrence_data.dict["pk"]))

        # Tag and pictures
        line += ("# Tag and pictures\n")
        # if occurrence_data.release_pk not in immaterial_releases: # The migrated-from version did not instantiate immaterial releases
        tag_path = "media/advideogame/occurrences/{pk}/tags/v1.png".format(pk=occurrence_data.dict["pk"])
        if not os.path.isfile(os.path.join("export", tag_path)):
            raise Exception("Path '{}' not found on the filesystem".format(tag_path))
        line += ("occurrence.tag_url = \"/{tag_path}\"\n".format(tag_path=tag_path))

        for picture in occurrence_data.pictures:
            pic_path = "media/advideogame/occurrences/{pk}/pictures/{file}".format(pk=occurrence_data.dict["pk"], file=picture["file"])
            if not os.path.isfile(os.path.join("export", pic_path)):
                raise Exception("Path '{}' not found on the filesystem".format(pic_path))
            if picture["detail"] != "GRP":
                attribute = (" attribute_type=ReleaseAttribute_contentype, "
                             "attribute_id = get_corresponding_release_attribute(release={release}, note={note}, lookup_dict={corresp}).pk,"
                                .format(release=occurrence_data.release_pk, note="''", corresp=picture["attribute_lookup"]))
            else:
                attribute = ""
            line += ("OccurrencePicture.objects.create(occurrence=occurrence,"
                                                     "{attribute} detail={detail}, image_file='/{path}')\n"
                        .format(attribute=attribute, detail=repr(picture["detail"]), path=pic_path))

        line += "occurrence.save()\n"
        

        if occurrence_data.extra:
            extra_text = "".join(["#[EXTRA] {}\n".format(text) for text in occurrence_data.extra])
            line += extra_text

        line += "\n"
        f.write(line)
