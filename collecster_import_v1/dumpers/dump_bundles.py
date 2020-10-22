#!/usr/bin/env python

import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Collecster.settings")
django.setup()

from Datamanager.models import *

from helper_specifics import *

import collections, urllib, urllib2, json

bundle_dict = {}

class DataObject(object):
    pass

for bundle in Bundle.objects.select_subclasses():
    data = DataObject()
    bundle_dict[bundle.pk] = data
    extra = []
    data.extra = extra

    data.name = str(bundle)

    data.dict = {
        "arrival_date": bundle.acquisition_date,
        "note": "",
    }

    if not isinstance(bundle, Buying):
        raise Exception("Only bundle are handled by this dumper.")

    data.dict.update({
        "pk": bundle.pk,
        "price": bundle.price,
        "shipping_cost": bundle.shipping_cost,
        "address_complement": "",
        "retrieval": "TODO",
    })
    extra.append("Add retrieval")

    # Context
    context = bundle.context
    data.context = {
        "context": {
            "category": context.category,
            "name": context.name,
            "address_complement": context.complement,
        }
    }
    if context.category == "NET":
        extra.append("NET or ADS ?")
        data.context["context"]["url"] = "TODO"
        extra.append("Add url")

    ## Location
    def location_dict(loc, destination):
        if loc:
            location = {"country": loc.country}
            if loc.city:
                location["city"] = loc.city
                extra.append("Post code for loc {}".format(location))
            else:
                location["city"] = ""
            destination["location"] = location

    location_dict(context.location, data.context)
    data.location = {}

    # Purchase location
    location_dict(bundle.location, data.location)

    # Composition
    data.compositions = []
    for compo in bundle.bundlecomposition_set.all():
        data.compositions.append(compo.instance.pk)

    # Pictures
    data.pictures = []
    for picture in bundle.bundlepicture_set.all():
        data.pictures.append({"file": os.path.basename(picture.image.name)})

data = None

with open("import_bundles.py", "w") as f :
    f.write(get_preamble())
    for key, bundle_data in bundle_dict.iteritems():
        line = "\t#{}\n".format(bundle_data.name)
        # Nota: only purchases are present in the source data, otherwise an exception would be raised
        line += ("bundle = Purchase(created_by=get_userextension(\"ad\"), **{})\n"
                    .format(bundle_data.dict))


        # location
        location = bundle_data.location.get("location")
        if location:
            line += "purchase_location = Location.objects.get_or_create(**{})[0]\n".format(location)
            line += "bundle.location = purchase_location\n"

        # Context
        context = bundle_data.context
        location = context.get("location")
        location_argument = ""
        if location:
            line += "context_location = Location.objects.get_or_create(**{})[0]\n".format(location)
            location_argument = "location=context_location, "
        line += ("context = PurchaseContext.objects.get_or_create({location_arg}**{})[0]\n"
                    .format(context["context"], location_arg=location_argument))
        line += "bundle.context = context\n"

        line += "bundle.save()\n"
        
        # Composition
        if bundle_data.compositions:
            for compo in bundle_data.compositions:
                line += ("BundleComposition.objects.create(bundle=bundle, brand_new=False, occurrence=get_occurrence({occ_pk}))\n"
                            .format(occ_pk=compo))

        # Pictures
        line += ("# Pictures\n")

        for picture in bundle_data.pictures:
            pic_path = "media/advideogame/bundles/{pk}/pictures/{file}".format(pk=bundle_data.dict["pk"], file=picture["file"])
            if not os.path.isfile(os.path.join("export", pic_path)):
                raise Exception("Path '{}' not found on the filesystem".format(pic_path))

            line += ("BundlePicture.objects.create(bundle=bundle, image_file='/{path}')\n"
                .format(path=pic_path))


        if bundle_data.extra:
            extra_text = "".join(["#[EXTRA] {}\n".format(text) for text in bundle_data.extra])
            line += extra_text

        line += "\n"
        f.write(line)
