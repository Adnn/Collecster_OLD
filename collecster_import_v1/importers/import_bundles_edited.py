#!/usr/bin/env python

import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Collecster.settings")
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


# Make the ADS contexts
context = PurchaseContext.objects.get_or_create(**{'category': u'ADS', 'url': 'https://www.leboncoin.fr/', 'name': u'Le bon coin', 'address_complement': u''})[0]
context = PurchaseContext.objects.get_or_create(**{'category': u'ADS', 'url': 'http://www.ebay.fr/', 'name': u'eBay', 'address_complement': u''})[0]


	#2013-01-07 Le bon coin (The Ultimate DOOM)
bundle = Purchase(created_by=get_userextension("ad"), **{'note': '', 'arrival_date': datetime.date(2013, 1, 7), 'address_complement': '', 'shipping_cost': 5.0, 'pk': 1, 'price': 15.0, 'retrieval': 'S'})
purchase_location = Location.objects.get_or_create(**{'country': u'FR', 'city': u'Vernouillet', 'post_code':'78540'})[0]
bundle.location = purchase_location
context = PurchaseContext.objects.get_or_create(**{'name': u'Le bon coin', 'address_complement': u''})[0]
bundle.context = context
bundle.save()
BundleComposition.objects.create(bundle=bundle, brand_new=False, occurrence=get_occurrence(1))
# Pictures

	#2013-01-11 Le bon coin (DoDonPachi, Resident Evil)
bundle = Purchase(created_by=get_userextension("ad"), **{'note': '', 'arrival_date': datetime.date(2013, 1, 11), 'address_complement': 'centre commercial Part Dieu', 'shipping_cost': None, 'pk': 2, 'price': 55.0, 'retrieval': 'P'})
purchase_location = Location.objects.get_or_create(**{'country': u'FR', 'city': u'Lyon', 'post_code':'69003'})[0]
bundle.location = purchase_location
context = PurchaseContext.objects.get_or_create(**{'name': u'Le bon coin', 'address_complement': u''})[0]
bundle.context = context
bundle.save()
BundleComposition.objects.create(bundle=bundle, brand_new=False, occurrence=get_occurrence(31))
BundleComposition.objects.create(bundle=bundle, brand_new=False, occurrence=get_occurrence(32))
# Pictures
BundlePicture.objects.create(bundle=bundle, image_file='advideogame/bundles/2/pictures/DSC03108.JPG')

	#2013-01-14 Le bon coin (Dragon Ball Z The Legend)
bundle = Purchase(created_by=get_userextension("ad"), **{'note': '', 'arrival_date': datetime.date(2013, 1, 14), 'address_complement': '', 'shipping_cost': None, 'pk': 3, 'price': 25.0, 'retrieval': 'P'})
purchase_location = Location.objects.get_or_create(**{'country': u'FR', 'city': u'Grenoble', 'post_code':'38000'})[0]
bundle.location = purchase_location
context = PurchaseContext.objects.get_or_create(**{'name': u'Le bon coin', 'address_complement': u''})[0]
bundle.context = context
bundle.save()
BundleComposition.objects.create(bundle=bundle, brand_new=False, occurrence=get_occurrence(17))
# Pictures

	#2013-01-07 eBay ("Virtua Gun & Virtua Cop")
bundle = Purchase(created_by=get_userextension("ad"), **{'note': '', 'arrival_date': datetime.date(2013, 1, 7), 'address_complement': '', 'shipping_cost': 7.77, 'pk': 4, 'price': 17.21, 'retrieval': 'S'})
purchase_location = Location.objects.get_or_create(**{'country': u'UK', 'city': ''})[0]
bundle.location = purchase_location
context = PurchaseContext.objects.get_or_create(**{'name': u'eBay', 'address_complement': u''})[0]
bundle.context = context
bundle.save()
BundleComposition.objects.create(bundle=bundle, brand_new=False, occurrence=get_occurrence(19))
# Pictures

	#2013-01-11 Le bon coin (Sega Touring Car, Formula Karts Special Edition, Virtua Gun)
guigui = Person.objects.get_or_create(first_name="Guillaume", last_name="Pascal", nickname="Pegazus")[0]
bundle = Purchase(created_by=get_userextension("ad"), **{'note': '', 'arrival_date': datetime.date(2013, 1, 11), 'address_complement': '', 'shipping_cost': None, 'pk': 5, 'price': 10.0, 'retrieval': 'F', 'pickup_person':guigui})
purchase_location = Location.objects.get_or_create(**{'country': u'FR', 'city': u'Paris'})[0]
bundle.location = purchase_location
context = PurchaseContext.objects.get_or_create(**{'name': u'Le bon coin', 'address_complement': u''})[0]
bundle.context = context
bundle.save()
BundleComposition.objects.create(bundle=bundle, brand_new=False, occurrence=get_occurrence(27))
BundleComposition.objects.create(bundle=bundle, brand_new=False, occurrence=get_occurrence(28))
BundleComposition.objects.create(bundle=bundle, brand_new=False, occurrence=get_occurrence(22))
# Pictures
BundlePicture.objects.create(bundle=bundle, image_file='advideogame/bundles/5/pictures/DSC03091.JPG')

	#2013-01-10 Le bon coin (Pad Saturn official, Pad Saturn official)
bundle = Purchase(created_by=get_userextension("ad"), **{'note': 'I do not remember if it was shipping...', 'arrival_date': datetime.date(2013, 1, 10), 'address_complement': '', 'shipping_cost': None, 'pk': 6, 'price': 17.0, 'retrieval': 'S'})
purchase_location = Location.objects.get_or_create(**{'country': u'FR', 'city': ''})[0]
bundle.location = purchase_location
context = PurchaseContext.objects.get_or_create(**{'name': u'Le bon coin', 'address_complement': u''})[0]
bundle.context = context
bundle.save()
BundleComposition.objects.create(bundle=bundle, brand_new=False, occurrence=get_occurrence(35))
BundleComposition.objects.create(bundle=bundle, brand_new=False, occurrence=get_occurrence(34))
# Pictures
BundlePicture.objects.create(bundle=bundle, image_file='advideogame/bundles/6/pictures/DSC03137.JPG')

	#2013-01-08 Le bon coin (Bootleg Sampler)
bundle = Purchase(created_by=get_userextension("ad"), **{'note': '', 'arrival_date': datetime.date(2013, 1, 8), 'address_complement': '', 'shipping_cost': 2.4, 'pk': 7, 'price': 5.0, 'retrieval': 'S'})
purchase_location = Location.objects.get_or_create(**{'country': u'FR', 'city': ''})[0]
bundle.location = purchase_location
context = PurchaseContext.objects.get_or_create(**{'name': u'Le bon coin', 'address_complement': u''})[0]
bundle.context = context
bundle.save()
BundleComposition.objects.create(bundle=bundle, brand_new=False, occurrence=get_occurrence(39))
# Pictures

	#2013-01-12 Emmaüs, [FR] Lyon (FIFA 98)
bundle = Purchase(created_by=get_userextension("ad"), **{'note': '', 'arrival_date': datetime.date(2013, 1, 12), 'address_complement': '', 'shipping_cost': None, 'pk': 8, 'price': 3.0, 'retrieval': 'P'})
context_location = Location.objects.get_or_create(**{'country': u'FR', 'city': u'Lyon', 'post_code':'69007'})[0]
context = PurchaseContext.objects.get_or_create(location=context_location, **{'category': u'SHP', 'name': u'Emma\xfcs', 'address_complement': u'Emma\xfcs Créqui'})[0]
bundle.context = context
bundle.save()
BundleComposition.objects.create(bundle=bundle, brand_new=False, occurrence=get_occurrence(48))
# Pictures

	#2013-01-16 Affair's, [FR] St-Martin d'Hères (Pad Dreamcast official, VMU, The Lion King, Aladdin, Sonic 2, Sega Game Pack 4 in 1)
bundle = Purchase(created_by=get_userextension("ad"), **{'note': '', 'arrival_date': datetime.date(2013, 1, 16), 'address_complement': '', 'shipping_cost': None, 'pk': 9, 'price': 14.0, 'retrieval': 'P'})
context_location = Location.objects.get_or_create(**{'country': u'FR', 'city': u"St-Martin d'H\xe8res", "post_code":"38400"})[0]
context = PurchaseContext.objects.get_or_create(location=context_location, **{'category': u'SHP', 'name': u"Affair's", 'address_complement': u''})[0]
bundle.context = context
bundle.save()
BundleComposition.objects.create(bundle=bundle, brand_new=False, occurrence=get_occurrence(55))
BundleComposition.objects.create(bundle=bundle, brand_new=False, occurrence=get_occurrence(53))
BundleComposition.objects.create(bundle=bundle, brand_new=False, occurrence=get_occurrence(58))
BundleComposition.objects.create(bundle=bundle, brand_new=False, occurrence=get_occurrence(59))
BundleComposition.objects.create(bundle=bundle, brand_new=False, occurrence=get_occurrence(60))
BundleComposition.objects.create(bundle=bundle, brand_new=False, occurrence=get_occurrence(61))
# Pictures
BundlePicture.objects.create(bundle=bundle, image_file='advideogame/bundles/9/pictures/DSC03185.JPG')

	#2013-01-09 Le bon coin (Steering wheel Saturn Mad Catz)
bundle = Purchase(created_by=get_userextension("ad"), **{'note': '', 'arrival_date': datetime.date(2013, 1, 9), 'address_complement': '', 'shipping_cost': None, 'pk': 10, 'price': 22.0, 'retrieval': 'S'})
purchase_location = Location.objects.get_or_create(**{'country': u'FR', 'city': u'Saint-L\xf4', "post_code":"50000"})[0]
bundle.location = purchase_location
context = PurchaseContext.objects.get_or_create(**{'name': u'Le bon coin', 'address_complement': u''})[0]
bundle.context = context
bundle.save()
BundleComposition.objects.create(bundle=bundle, brand_new=False, occurrence=get_occurrence(69))
# Pictures

	#2013-01-01 Vide Grenier (The Curse of Monkey Island, Torin's Passage, Loom, Dr. Brain a perdu la tête !)
bundle = Purchase(created_by=get_userextension("ad"), **{'note': '', 'arrival_date': datetime.date(2013, 1, 1), 'address_complement': '', 'shipping_cost': None, 'pk': 11, 'price': 2.0, 'retrieval': 'P'})
context_location = Location.objects.get_or_create(**{'country': u'FR', 'city': u'Lyon', "post_code":"69003"})[0]
context = PurchaseContext.objects.get_or_create(**{'category': u'SEC', 'name': u'Vide Grenier', 'address_complement': u'avenue Maréchal de Saxe', 'location':context_location})[0]
bundle.context = context
bundle.save()
BundleComposition.objects.create(bundle=bundle, brand_new=False, occurrence=get_occurrence(87))
BundleComposition.objects.create(bundle=bundle, brand_new=False, occurrence=get_occurrence(84))
BundleComposition.objects.create(bundle=bundle, brand_new=False, occurrence=get_occurrence(85))
BundleComposition.objects.create(bundle=bundle, brand_new=False, occurrence=get_occurrence(86))
# Pictures
BundlePicture.objects.create(bundle=bundle, image_file='advideogame/bundles/11/pictures/DSC03485.JPG')

