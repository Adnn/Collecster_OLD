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

	#DOOM
occurrence = Occurrence.objects.create(created_by=get_userextension("ad"), owner=get_person({'first_name': 'Adrien'}), release=Release.objects.get(pk=1), **{'origin': u'BC', 'blister': False, 'add_date': datetime.datetime(2013, 3, 6, 15, 9, 30, 536000, tzinfo=pytz.utc), 'lastmodif_date': datetime.datetime(2013, 3, 7, 7, 54, 29, 61219, tzinfo=pytz.utc), 'pk': 1, 'purchase_price': 10.0})
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'B', attribute_id=get_corresponding_release_attribute(release=1, note='', lookup_dict={'category__name': u'content', 'name': u'self'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'A', attribute_id=get_corresponding_release_attribute(release=1, note='', lookup_dict={'category__name': u'packaging', 'name': u'cardboard box'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'B', attribute_id=get_corresponding_release_attribute(release=1, note='', lookup_dict={'category__name': u'packaging', 'name': u'jewel box'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'A', attribute_id=get_corresponding_release_attribute(release=1, note='', lookup_dict={'category__name': u'papers', 'name': 'insert: jewel box'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'B', attribute_id=get_corresponding_release_attribute(release=1, note='', lookup_dict={'category__name': u'papers', 'name': u'manual'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'A', attribute_id=get_corresponding_release_attribute(release=1, note='', lookup_dict={'category__name': u'papers', 'name': u'registration card'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
OccurrenceComposition.objects.create(from_occurrence=occurrence, to_occurrence=Occurrence.objects.get(pk=97), release_composition=get_corresponding_release_compo({'to_release': 99, 'from_release': 1}))
specific = OccurrenceSpecific.OperationalOcc.objects.create(occurrence=occurrence, **{'working_condition': u'Y'})
tto = TagToOccurrence.objects.create(user_creator=get_userextension("ad"), user_occurrence_id=1, occurrence=occurrence)
# Tag and pictures
occurrence.tag_file = "advideogame/occurrences/1/tags/v1.png"
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=1, note='', lookup_dict={'category__name': u'packaging', 'name': u'cardboard box'}).pk, detail=u'FRT', image_file='advideogame/occurrences/1/pictures/DSC02984.jpg')
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=1, note='', lookup_dict={'category__name': u'packaging', 'name': u'cardboard box'}).pk, detail=u'SID', image_file='advideogame/occurrences/1/pictures/DSC02985.jpg')
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=1, note='', lookup_dict={'category__name': u'packaging', 'name': u'cardboard box'}).pk, detail=u'BCK', image_file='advideogame/occurrences/1/pictures/DSC02987.jpg')
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=1, note='', lookup_dict={'category__name': u'content', 'name': u'self'}).pk, detail=u'FRT', image_file='advideogame/occurrences/1/pictures/DSC02988.jpg')
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=1, note='', lookup_dict={'category__name': u'packaging', 'name': u'jewel box'}).pk, detail=u'FRT', image_file='advideogame/occurrences/1/pictures/DSC02993.jpg')
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=1, note='', lookup_dict={'category__name': u'packaging', 'name': u'jewel box'}).pk, detail=u'BCK', image_file='advideogame/occurrences/1/pictures/DSC02989.jpg')
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=1, note='', lookup_dict={'category__name': u'papers', 'name': u'manual'}).pk, detail=u'FRT', image_file='advideogame/occurrences/1/pictures/DSC02992.jpg')
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=1, note='', lookup_dict={'category__name': u'papers', 'name': u'manual'}).pk, detail=u'BCK', image_file='advideogame/occurrences/1/pictures/DSC02991.jpg')
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=1, note='', lookup_dict={'category__name': u'papers', 'name': u'manual'}).pk, detail=u'INS', image_file='advideogame/occurrences/1/pictures/DSC02990.jpg')
OccurrencePicture.objects.create(occurrence=occurrence, detail=u'GRP', image_file='advideogame/occurrences/1/pictures/DSC02994.jpg')
occurrence.save()

	#Nights into Dreams
occurrence = Occurrence.objects.create(created_by=get_userextension("ad"), owner=get_person({'first_name': 'Adrien'}), release=Release.objects.get(pk=2), **{'origin': u'OR', 'blister': False, 'add_date': datetime.datetime(2013, 3, 6, 15, 28, 29, 413000, tzinfo=pytz.utc), 'lastmodif_date': datetime.datetime(2013, 3, 7, 7, 54, 47, 121477, tzinfo=pytz.utc), 'pk': 2, 'purchase_price': None})
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'B', attribute_id=get_corresponding_release_attribute(release=2, note='', lookup_dict={'category__name': u'content', 'name': u'self'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'C', attribute_id=get_corresponding_release_attribute(release=2, note='', lookup_dict={'category__name': u'packaging', 'name': u'jewel box'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'B', attribute_id=get_corresponding_release_attribute(release=2, note='', lookup_dict={'category__name': u'papers', 'name': 'insert: jewel box'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value='0', attribute_id=get_corresponding_release_attribute(release=2, note='', lookup_dict={'category__name': u'papers', 'name': u'manual'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
specific = OccurrenceSpecific.OperationalOcc.objects.create(occurrence=occurrence, **{'working_condition': u'Y'})
tto = TagToOccurrence.objects.create(user_creator=get_userextension("ad"), user_occurrence_id=2, occurrence=occurrence)
# Tag and pictures
occurrence.tag_file = "advideogame/occurrences/2/tags/v1.png"
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=2, note='', lookup_dict={'category__name': u'packaging', 'name': u'jewel box'}).pk, detail=u'FRT', image_file='advideogame/occurrences/2/pictures/DSC02974.jpg')
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=2, note='', lookup_dict={'category__name': u'packaging', 'name': u'jewel box'}).pk, detail=u'BCK', image_file='advideogame/occurrences/2/pictures/DSC02975.jpg')
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=2, note='', lookup_dict={'category__name': u'packaging', 'name': u'jewel box'}).pk, detail=u'SLB', image_file='advideogame/occurrences/2/pictures/DSC02983.jpg')
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=2, note='', lookup_dict={'category__name': u'content', 'name': u'self'}).pk, detail=u'FRT', image_file='advideogame/occurrences/2/pictures/DSC02976.jpg')
occurrence.save()

	#Dragon Ball Z: Shin Butōden
occurrence = Occurrence.objects.create(created_by=get_userextension("ad"), owner=get_person({'first_name': 'Adrien'}), release=Release.objects.get(pk=3), **{'origin': u'BC', 'blister': False, 'add_date': datetime.datetime(2013, 3, 6, 15, 41, 16, 94000, tzinfo=pytz.utc), 'lastmodif_date': datetime.datetime(2013, 3, 7, 7, 54, 51, 421104, tzinfo=pytz.utc), 'pk': 3, 'purchase_price': None})
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'A', attribute_id=get_corresponding_release_attribute(release=3, note='', lookup_dict={'category__name': u'content', 'name': u'self'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'A', attribute_id=get_corresponding_release_attribute(release=3, note='', lookup_dict={'category__name': u'packaging', 'name': u'jewel box'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value='0', attribute_id=get_corresponding_release_attribute(release=3, note='', lookup_dict={'category__name': u'packaging', 'name': u'spine card'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'A', attribute_id=get_corresponding_release_attribute(release=3, note='', lookup_dict={'category__name': u'papers', 'name': 'insert: jewel box'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'B', attribute_id=get_corresponding_release_attribute(release=3, note='', lookup_dict={'category__name': u'papers', 'name': u'manual'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
specific = OccurrenceSpecific.OperationalOcc.objects.create(occurrence=occurrence, **{'working_condition': u'Y'})
tto = TagToOccurrence.objects.create(user_creator=get_userextension("ad"), user_occurrence_id=3, occurrence=occurrence)
# Tag and pictures
occurrence.tag_file = "advideogame/occurrences/3/tags/v1.png"
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=3, note='', lookup_dict={'category__name': u'packaging', 'name': u'jewel box'}).pk, detail=u'FRT', image_file='advideogame/occurrences/3/pictures/DSC02977.jpg')
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=3, note='', lookup_dict={'category__name': u'packaging', 'name': u'jewel box'}).pk, detail=u'FRT', image_file='advideogame/occurrences/3/pictures/DSC02978.jpg')
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=3, note='', lookup_dict={'category__name': u'packaging', 'name': u'jewel box'}).pk, detail=u'SLB', image_file='advideogame/occurrences/3/pictures/DSC02980.jpg')
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=3, note='', lookup_dict={'category__name': u'papers', 'name': u'manual'}).pk, detail=u'INS', image_file='advideogame/occurrences/3/pictures/DSC02981.jpg')
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=3, note='', lookup_dict={'category__name': u'content', 'name': u'self'}).pk, detail=u'FRT', image_file='advideogame/occurrences/3/pictures/DSC02979.jpg')
occurrence.save()

	#Virtua Fighter 2
occurrence = Occurrence.objects.create(created_by=get_userextension("ad"), owner=get_person({'first_name': 'Adrien'}), release=Release.objects.get(pk=4), **{'origin': u'OR', 'blister': False, 'add_date': datetime.datetime(2013, 3, 6, 15, 45, 35, 702000, tzinfo=pytz.utc), 'lastmodif_date': datetime.datetime(2013, 3, 7, 7, 55, 4, 501292, tzinfo=pytz.utc), 'pk': 4, 'purchase_price': None})
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'B', attribute_id=get_corresponding_release_attribute(release=4, note='', lookup_dict={'category__name': u'content', 'name': u'self'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'B', attribute_id=get_corresponding_release_attribute(release=4, note='', lookup_dict={'category__name': u'packaging', 'name': u'dvd box'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'A', attribute_id=get_corresponding_release_attribute(release=4, note='', lookup_dict={'category__name': u'papers', 'name': u'manual'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
specific = OccurrenceSpecific.OperationalOcc.objects.create(occurrence=occurrence, **{'working_condition': u'Y'})
tto = TagToOccurrence.objects.create(user_creator=get_userextension("ad"), user_occurrence_id=4, occurrence=occurrence)
# Tag and pictures
occurrence.tag_file = "advideogame/occurrences/4/tags/v1.png"
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=4, note='', lookup_dict={'category__name': u'packaging', 'name': u'dvd box'}).pk, detail=u'FRT', image_file='advideogame/occurrences/4/pictures/DSC03007.jpg')
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=4, note='', lookup_dict={'category__name': u'packaging', 'name': u'dvd box'}).pk, detail=u'BCK', image_file='advideogame/occurrences/4/pictures/DSC03008.jpg')
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=4, note='', lookup_dict={'category__name': u'packaging', 'name': u'dvd box'}).pk, detail=u'INS', image_file='advideogame/occurrences/4/pictures/DSC03009.jpg')
occurrence.save()

	#Bug!
occurrence = Occurrence.objects.create(created_by=get_userextension("ad"), owner=get_person({'first_name': 'Adrien'}), release=Release.objects.get(pk=5), **{'origin': u'BU', 'blister': False, 'add_date': datetime.datetime(2013, 3, 6, 15, 49, 40, 329000, tzinfo=pytz.utc), 'lastmodif_date': datetime.datetime(2013, 3, 7, 7, 57, 1, 87958, tzinfo=pytz.utc), 'pk': 5, 'purchase_price': 4.9})
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'C', attribute_id=get_corresponding_release_attribute(release=5, note='', lookup_dict={'category__name': u'content', 'name': u'self'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'C', attribute_id=get_corresponding_release_attribute(release=5, note='', lookup_dict={'category__name': u'packaging', 'name': u'dvd box'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value='0', attribute_id=get_corresponding_release_attribute(release=5, note='', lookup_dict={'category__name': u'papers', 'name': u'manual'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
specific = OccurrenceSpecific.OperationalOcc.objects.create(occurrence=occurrence, **{'working_condition': u'?'})
tto = TagToOccurrence.objects.create(user_creator=get_userextension("ad"), user_occurrence_id=5, occurrence=occurrence)
# Tag and pictures
occurrence.tag_file = "advideogame/occurrences/5/tags/v1.png"
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=5, note='', lookup_dict={'category__name': u'packaging', 'name': u'dvd box'}).pk, detail=u'FRT', image_file='advideogame/occurrences/5/pictures/DSC02999.jpg')
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=5, note='', lookup_dict={'category__name': u'packaging', 'name': u'dvd box'}).pk, detail=u'BCK', image_file='advideogame/occurrences/5/pictures/DSC03000.jpg')
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=5, note='', lookup_dict={'category__name': u'packaging', 'name': u'dvd box'}).pk, detail=u'SLB', image_file='advideogame/occurrences/5/pictures/DSC03005.jpg')
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=5, note='', lookup_dict={'category__name': u'content', 'name': u'self'}).pk, detail=u'FRT', image_file='advideogame/occurrences/5/pictures/DSC03001.jpg')
occurrence.save()

	#Bug Too!
occurrence = Occurrence.objects.create(created_by=get_userextension("ad"), owner=get_person({'first_name': 'Adrien'}), release=Release.objects.get(pk=6), **{'origin': u'BU', 'blister': False, 'add_date': datetime.datetime(2013, 3, 6, 15, 58, 3, 404000, tzinfo=pytz.utc), 'lastmodif_date': datetime.datetime(2013, 3, 7, 7, 57, 5, 203024, tzinfo=pytz.utc), 'pk': 6, 'purchase_price': 4.9})
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'D', attribute_id=get_corresponding_release_attribute(release=6, note='', lookup_dict={'category__name': u'content', 'name': u'self'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'C', attribute_id=get_corresponding_release_attribute(release=6, note='', lookup_dict={'category__name': u'packaging', 'name': u'dvd box'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value='0', attribute_id=get_corresponding_release_attribute(release=6, note='', lookup_dict={'category__name': u'papers', 'name': u'manual'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
specific = OccurrenceSpecific.OperationalOcc.objects.create(occurrence=occurrence, **{'working_condition': u'?'})
tto = TagToOccurrence.objects.create(user_creator=get_userextension("ad"), user_occurrence_id=6, occurrence=occurrence)
# Tag and pictures
occurrence.tag_file = "advideogame/occurrences/6/tags/v1.png"
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=6, note='', lookup_dict={'category__name': u'packaging', 'name': u'dvd box'}).pk, detail=u'FRT', image_file='advideogame/occurrences/6/pictures/DSC02995.jpg')
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=6, note='', lookup_dict={'category__name': u'packaging', 'name': u'dvd box'}).pk, detail=u'BCK', image_file='advideogame/occurrences/6/pictures/DSC02996.jpg')
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=6, note='', lookup_dict={'category__name': u'packaging', 'name': u'dvd box'}).pk, detail=u'SLB', image_file='advideogame/occurrences/6/pictures/DSC03006.jpg')
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=6, note='', lookup_dict={'category__name': u'content', 'name': u'self'}).pk, detail=u'FRT', image_file='advideogame/occurrences/6/pictures/DSC02997.jpg')
occurrence.save()

	#Mighty Hits
occurrence = Occurrence.objects.create(created_by=get_userextension("ad"), owner=get_person({'first_name': 'Adrien'}), release=Release.objects.get(pk=7), **{'origin': u'BU', 'blister': False, 'add_date': datetime.datetime(2013, 3, 6, 16, 22, 36, 951000, tzinfo=pytz.utc), 'lastmodif_date': datetime.datetime(2013, 3, 7, 7, 57, 8, 854524, tzinfo=pytz.utc), 'pk': 7, 'purchase_price': None})
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'B', attribute_id=get_corresponding_release_attribute(release=7, note='', lookup_dict={'category__name': u'content', 'name': u'self'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'B', attribute_id=get_corresponding_release_attribute(release=7, note='', lookup_dict={'category__name': u'packaging', 'name': u'dvd box'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'A', attribute_id=get_corresponding_release_attribute(release=7, note='', lookup_dict={'category__name': u'papers', 'name': u'manual'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
specific = OccurrenceSpecific.OperationalOcc.objects.create(occurrence=occurrence, **{'working_condition': u'Y'})
tto = TagToOccurrence.objects.create(user_creator=get_userextension("ad"), user_occurrence_id=7, occurrence=occurrence)
# Tag and pictures
occurrence.tag_file = "advideogame/occurrences/7/tags/v1.png"
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=7, note='', lookup_dict={'category__name': u'packaging', 'name': u'dvd box'}).pk, detail=u'FRT', image_file='advideogame/occurrences/7/pictures/DSC03010.jpg')
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=7, note='', lookup_dict={'category__name': u'packaging', 'name': u'dvd box'}).pk, detail=u'BCK', image_file='advideogame/occurrences/7/pictures/DSC03011.jpg')
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=7, note='', lookup_dict={'category__name': u'packaging', 'name': u'dvd box'}).pk, detail=u'INS', image_file='advideogame/occurrences/7/pictures/DSC03012.jpg')
OccurrencePicture.objects.create(occurrence=occurrence, detail=u'GRP', image_file='advideogame/occurrences/7/pictures/DSC03013.jpg')
occurrence.save()

	#NightStone
occurrence = Occurrence.objects.create(created_by=get_userextension("ad"), owner=get_person({'first_name': 'Adrien'}), release=Release.objects.get(pk=8), **{'origin': u'BC', 'blister': True, 'add_date': datetime.datetime(2013, 3, 6, 16, 51, 12, 361000, tzinfo=pytz.utc), 'lastmodif_date': datetime.datetime(2013, 3, 7, 7, 57, 26, 399633, tzinfo=pytz.utc), 'pk': 8, 'purchase_price': 0.97})
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'M', attribute_id=get_corresponding_release_attribute(release=8, note='', lookup_dict={'category__name': u'content', 'name': u'self'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'B', attribute_id=get_corresponding_release_attribute(release=8, note='', lookup_dict={'category__name': u'packaging', 'name': u'cardboard box'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'M', attribute_id=get_corresponding_release_attribute(release=8, note='', lookup_dict={'category__name': u'packaging', 'name': u'jewel box'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'M', attribute_id=get_corresponding_release_attribute(release=8, note='', lookup_dict={'category__name': u'papers', 'name': 'insert: jewel box'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'M', attribute_id=get_corresponding_release_attribute(release=8, note='', lookup_dict={'category__name': u'papers', 'name': u'manual'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
specific = OccurrenceSpecific.OperationalOcc.objects.create(occurrence=occurrence, **{'working_condition': u'Y'})
tto = TagToOccurrence.objects.create(user_creator=get_userextension("ad"), user_occurrence_id=8, occurrence=occurrence)
# Tag and pictures
occurrence.tag_file = "advideogame/occurrences/8/tags/v1.png"
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=8, note='', lookup_dict={'category__name': u'packaging', 'name': u'cardboard box'}).pk, detail=u'FRT', image_file='advideogame/occurrences/8/pictures/DSC02967.jpg')
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=8, note='', lookup_dict={'category__name': u'packaging', 'name': u'cardboard box'}).pk, detail=u'BCK', image_file='advideogame/occurrences/8/pictures/DSC02968.jpg')
occurrence.save()

	#The Beatles: Rock Band
occurrence = Occurrence.objects.create(created_by=get_userextension("ad"), owner=get_person({'first_name': 'Adrien'}), release=Release.objects.get(pk=10), **{'origin': u'BU', 'blister': True, 'add_date': datetime.datetime(2013, 3, 7, 8, 36, 56, 128073, tzinfo=pytz.utc), 'lastmodif_date': datetime.datetime(2013, 3, 7, 8, 36, 56, 460114, tzinfo=pytz.utc), 'pk': 9, 'purchase_price': None})
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'M', attribute_id=get_corresponding_release_attribute(release=10, note='', lookup_dict={'category__name': u'content', 'name': u'self'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'M', attribute_id=get_corresponding_release_attribute(release=10, note='', lookup_dict={'category__name': u'packaging', 'name': u'dvd box'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'M', attribute_id=get_corresponding_release_attribute(release=10, note='', lookup_dict={'category__name': u'papers', 'name': u'manual'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
specific = OccurrenceSpecific.OperationalOcc.objects.create(occurrence=occurrence, **{'working_condition': u'Y'})
tto = TagToOccurrence.objects.create(user_creator=get_userextension("ad"), user_occurrence_id=9, occurrence=occurrence)
# Tag and pictures
occurrence.tag_file = "advideogame/occurrences/9/tags/v1.png"
occurrence.save()

	#Singstar Microphone
occurrence = Occurrence.objects.create(created_by=get_userextension("ad"), owner=get_person({'first_name': 'Adrien'}), release=Release.objects.get(pk=9), **{'origin': u'BU', 'blister': False, 'add_date': datetime.datetime(2013, 3, 7, 9, 7, 46, 922891, tzinfo=pytz.utc), 'lastmodif_date': datetime.datetime(2013, 3, 7, 9, 7, 47, 260522, tzinfo=pytz.utc), 'pk': 10, 'purchase_price': 5.99})
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'M', attribute_id=get_corresponding_release_attribute(release=9, note='red', lookup_dict={'category__name': u'content', 'name': u'self'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'M', attribute_id=get_corresponding_release_attribute(release=9, note='blue', lookup_dict={'category__name': u'content', 'name': u'self'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value='M', attribute_id=get_corresponding_release_attribute(release=9, note='', lookup_dict={'category__name': 'content', 'name': 'receiver interface'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'A', attribute_id=get_corresponding_release_attribute(release=9, note='', lookup_dict={'category__name': u'packaging', 'name': u'transparent thermoplastic'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'M', attribute_id=get_corresponding_release_attribute(release=9, note='', lookup_dict={'category__name': 'packaging', 'name': 'printed cardboard inlay'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'M', attribute_id=get_corresponding_release_attribute(release=9, note='', lookup_dict={'category__name': u'papers', 'name': u'manual'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
OccurrenceComposition.objects.create(from_occurrence=occurrence, to_occurrence=Occurrence.objects.get(pk=9), release_composition=get_corresponding_release_compo({'to_release': 10, 'from_release': 9}))
specific = OccurrenceSpecific.OperationalOcc.objects.create(occurrence=occurrence, **{'working_condition': u'Y'})
tto = TagToOccurrence.objects.create(user_creator=get_userextension("ad"), user_occurrence_id=10, occurrence=occurrence)
# Tag and pictures
occurrence.tag_file = "advideogame/occurrences/10/tags/v1.png"
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=9, note='', lookup_dict={'category__name': u'packaging', 'name': u'transparent thermoplastic'}).pk, detail=u'FRT', image_file='advideogame/occurrences/10/pictures/DSC02969.jpg')
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=9, note='', lookup_dict={'category__name': u'packaging', 'name': u'transparent thermoplastic'}).pk, detail=u'BCK', image_file='advideogame/occurrences/10/pictures/DSC02970.jpg')
occurrence.save()

	#Buzz!: Brain of...
occurrence = Occurrence.objects.create(created_by=get_userextension("ad"), owner=get_person({'first_name': 'Adrien'}), release=Release.objects.get(pk=11), **{'origin': u'BU', 'blister': True, 'add_date': datetime.datetime(2013, 3, 7, 9, 25, 17, 672080, tzinfo=pytz.utc), 'lastmodif_date': datetime.datetime(2013, 3, 7, 9, 25, 17, 986577, tzinfo=pytz.utc), 'pk': 11, 'purchase_price': None})
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'M', attribute_id=get_corresponding_release_attribute(release=11, note='', lookup_dict={'category__name': u'content', 'name': u'self'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'M', attribute_id=get_corresponding_release_attribute(release=11, note='', lookup_dict={'category__name': u'packaging', 'name': u'dvd box'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'M', attribute_id=get_corresponding_release_attribute(release=11, note='', lookup_dict={'category__name': u'papers', 'name': u'manual'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
specific = OccurrenceSpecific.OperationalOcc.objects.create(occurrence=occurrence, **{'working_condition': u'Y'})
tto = TagToOccurrence.objects.create(user_creator=get_userextension("ad"), user_occurrence_id=11, occurrence=occurrence)
# Tag and pictures
occurrence.tag_file = "advideogame/occurrences/11/tags/v1.png"
occurrence.save()

	#Buzz!: The Hollywood Quiz
occurrence = Occurrence.objects.create(created_by=get_userextension("ad"), owner=get_person({'first_name': 'Adrien'}), release=Release.objects.get(pk=12), **{'origin': u'BU', 'blister': True, 'add_date': datetime.datetime(2013, 3, 7, 12, 21, 14, 862088, tzinfo=pytz.utc), 'lastmodif_date': datetime.datetime(2013, 3, 7, 12, 21, 15, 178045, tzinfo=pytz.utc), 'pk': 12, 'purchase_price': None})
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'M', attribute_id=get_corresponding_release_attribute(release=12, note='', lookup_dict={'category__name': u'content', 'name': u'self'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'M', attribute_id=get_corresponding_release_attribute(release=12, note='', lookup_dict={'category__name': u'packaging', 'name': u'dvd box'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'M', attribute_id=get_corresponding_release_attribute(release=12, note='', lookup_dict={'category__name': u'papers', 'name': u'manual'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
specific = OccurrenceSpecific.OperationalOcc.objects.create(occurrence=occurrence, **{'working_condition': u'Y'})
tto = TagToOccurrence.objects.create(user_creator=get_userextension("ad"), user_occurrence_id=12, occurrence=occurrence)
# Tag and pictures
occurrence.tag_file = "advideogame/occurrences/12/tags/v1.png"
occurrence.save()

	#Buzz!: The Pop Quiz
occurrence = Occurrence.objects.create(created_by=get_userextension("ad"), owner=get_person({'first_name': 'Adrien'}), release=Release.objects.get(pk=13), **{'origin': u'BU', 'blister': True, 'add_date': datetime.datetime(2013, 3, 7, 12, 53, 14, 831577, tzinfo=pytz.utc), 'lastmodif_date': datetime.datetime(2013, 3, 7, 12, 53, 15, 139695, tzinfo=pytz.utc), 'pk': 13, 'purchase_price': None})
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'M', attribute_id=get_corresponding_release_attribute(release=13, note='', lookup_dict={'category__name': u'content', 'name': u'self'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'M', attribute_id=get_corresponding_release_attribute(release=13, note='', lookup_dict={'category__name': u'packaging', 'name': u'dvd box'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'M', attribute_id=get_corresponding_release_attribute(release=13, note='', lookup_dict={'category__name': u'papers', 'name': u'manual'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
specific = OccurrenceSpecific.OperationalOcc.objects.create(occurrence=occurrence, **{'working_condition': u'Y'})
tto = TagToOccurrence.objects.create(user_creator=get_userextension("ad"), user_occurrence_id=13, occurrence=occurrence)
# Tag and pictures
occurrence.tag_file = "advideogame/occurrences/13/tags/v1.png"
occurrence.save()

	#Buzz! Buzzer
occurrence = Occurrence.objects.create(created_by=get_userextension("ad"), owner=get_person({'first_name': 'Adrien'}), release=Release.objects.get(pk=14), **{'origin': u'BU', 'blister': False, 'add_date': datetime.datetime(2013, 3, 7, 12, 54, 38, 301887, tzinfo=pytz.utc), 'lastmodif_date': datetime.datetime(2013, 3, 7, 12, 54, 38, 645186, tzinfo=pytz.utc), 'pk': 14, 'purchase_price': 4.78})
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'M', attribute_id=get_corresponding_release_attribute(release=14, note='1', lookup_dict={'category__name': u'content', 'name': u'self'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'M', attribute_id=get_corresponding_release_attribute(release=14, note='2', lookup_dict={'category__name': u'content', 'name': u'self'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'M', attribute_id=get_corresponding_release_attribute(release=14, note='3', lookup_dict={'category__name': u'content', 'name': u'self'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'M', attribute_id=get_corresponding_release_attribute(release=14, note='4', lookup_dict={'category__name': u'content', 'name': u'self'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value='M', attribute_id=get_corresponding_release_attribute(release=14, note='', lookup_dict={'category__name': 'content', 'name': 'receiver interface'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'B', attribute_id=get_corresponding_release_attribute(release=14, note='', lookup_dict={'category__name': u'packaging', 'name': u'transparent thermoplastic'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'M', attribute_id=get_corresponding_release_attribute(release=14, note='', lookup_dict={'category__name': 'packaging', 'name': 'printed cardboard inlay'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'M', attribute_id=get_corresponding_release_attribute(release=14, note='', lookup_dict={'category__name': u'papers', 'name': u'manual'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
OccurrenceComposition.objects.create(from_occurrence=occurrence, to_occurrence=Occurrence.objects.get(pk=11), release_composition=get_corresponding_release_compo({'to_release': 11, 'from_release': 14}))
OccurrenceComposition.objects.create(from_occurrence=occurrence, to_occurrence=Occurrence.objects.get(pk=12), release_composition=get_corresponding_release_compo({'to_release': 12, 'from_release': 14}))
OccurrenceComposition.objects.create(from_occurrence=occurrence, to_occurrence=Occurrence.objects.get(pk=13), release_composition=get_corresponding_release_compo({'to_release': 13, 'from_release': 14}))
specific = OccurrenceSpecific.OperationalOcc.objects.create(occurrence=occurrence, **{'working_condition': u'Y'})
tto = TagToOccurrence.objects.create(user_creator=get_userextension("ad"), user_occurrence_id=14, occurrence=occurrence)
# Tag and pictures
occurrence.tag_file = "advideogame/occurrences/14/tags/v1.png"
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=14, note='', lookup_dict={'category__name': u'packaging', 'name': u'transparent thermoplastic'}).pk, detail=u'FRT', image_file='advideogame/occurrences/14/pictures/DSC02972.jpg')
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=14, note='', lookup_dict={'category__name': u'packaging', 'name': u'transparent thermoplastic'}).pk, detail=u'BCK', image_file='advideogame/occurrences/14/pictures/DSC02973.jpg')
occurrence.save()

	#Virtua Cop 2
occurrence = Occurrence.objects.create(created_by=get_userextension("ad"), owner=get_person({'first_name': 'Adrien'}), release=Release.objects.get(pk=15), **{'origin': u'OR', 'blister': False, 'add_date': datetime.datetime(2013, 3, 19, 19, 37, 52, 479663, tzinfo=pytz.utc), 'lastmodif_date': datetime.datetime(2013, 3, 19, 19, 48, 4, 154426, tzinfo=pytz.utc), 'pk': 15, 'purchase_price': None})
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'B', attribute_id=get_corresponding_release_attribute(release=15, note='', lookup_dict={'category__name': u'content', 'name': u'self'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'B', attribute_id=get_corresponding_release_attribute(release=15, note='', lookup_dict={'category__name': u'packaging', 'name': u'jewel box'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'A', attribute_id=get_corresponding_release_attribute(release=15, note='', lookup_dict={'category__name': u'papers', 'name': 'insert: jewel box'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value='0', attribute_id=get_corresponding_release_attribute(release=15, note='', lookup_dict={'category__name': u'papers', 'name': u'manual'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
specific = OccurrenceSpecific.OperationalOcc.objects.create(occurrence=occurrence, **{'working_condition': u'Y'})
tto = TagToOccurrence.objects.create(user_creator=get_userextension("ad"), user_occurrence_id=15, occurrence=occurrence)
# Tag and pictures
occurrence.tag_file = "advideogame/occurrences/15/tags/v1.png"
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=15, note='', lookup_dict={'category__name': u'packaging', 'name': u'jewel box'}).pk, detail=u'FRT', image_file='advideogame/occurrences/15/pictures/DSC03027.JPG')
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=15, note='', lookup_dict={'category__name': u'packaging', 'name': u'jewel box'}).pk, detail=u'BCK', image_file='advideogame/occurrences/15/pictures/DSC03028.JPG')
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=15, note='', lookup_dict={'category__name': u'packaging', 'name': u'jewel box'}).pk, detail=u'INS', image_file='advideogame/occurrences/15/pictures/DSC03029.JPG')
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=15, note='', lookup_dict={'category__name': u'packaging', 'name': u'jewel box'}).pk, detail=u'SLB', image_file='advideogame/occurrences/15/pictures/DSC03031.JPG')
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=15, note='', lookup_dict={'category__name': u'content', 'name': u'self'}).pk, detail=u'FRT', image_file='advideogame/occurrences/15/pictures/DSC03030.JPG')
occurrence.save()

	#The House of the Dead
occurrence = Occurrence.objects.create(created_by=get_userextension("ad"), owner=get_person({'first_name': 'Adrien'}), release=Release.objects.get(pk=16), **{'origin': u'BU', 'blister': False, 'add_date': datetime.datetime(2013, 3, 20, 1, 51, 41, 465495, tzinfo=pytz.utc), 'lastmodif_date': datetime.datetime(2013, 3, 20, 1, 51, 42, 186277, tzinfo=pytz.utc), 'pk': 16, 'purchase_price': None})
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'B', attribute_id=get_corresponding_release_attribute(release=16, note='', lookup_dict={'category__name': u'content', 'name': u'self'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'B', attribute_id=get_corresponding_release_attribute(release=16, note='', lookup_dict={'category__name': u'packaging', 'name': u'jewel box'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'A', attribute_id=get_corresponding_release_attribute(release=16, note='', lookup_dict={'category__name': u'papers', 'name': 'insert: jewel box'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value='0', attribute_id=get_corresponding_release_attribute(release=16, note='', lookup_dict={'category__name': u'papers', 'name': u'manual'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
specific = OccurrenceSpecific.OperationalOcc.objects.create(occurrence=occurrence, **{'working_condition': u'Y'})
tto = TagToOccurrence.objects.create(user_creator=get_userextension("ad"), user_occurrence_id=16, occurrence=occurrence)
# Tag and pictures
occurrence.tag_file = "advideogame/occurrences/16/tags/v1.png"
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=16, note='', lookup_dict={'category__name': u'packaging', 'name': u'jewel box'}).pk, detail=u'FRT', image_file='advideogame/occurrences/16/pictures/DSC03043.JPG')
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=16, note='', lookup_dict={'category__name': u'packaging', 'name': u'jewel box'}).pk, detail=u'BCK', image_file='advideogame/occurrences/16/pictures/DSC03044.JPG')
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=16, note='', lookup_dict={'category__name': u'packaging', 'name': u'jewel box'}).pk, detail=u'INS', image_file='advideogame/occurrences/16/pictures/DSC03045.JPG')
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=16, note='', lookup_dict={'category__name': u'content', 'name': u'self'}).pk, detail=u'FRT', image_file='advideogame/occurrences/16/pictures/DSC03046.JPG')
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=16, note='', lookup_dict={'category__name': u'packaging', 'name': u'jewel box'}).pk, detail=u'SLB', image_file='advideogame/occurrences/16/pictures/DSC03032.JPG')
occurrence.save()

	#Dragon Ball Z: The Legend
occurrence = Occurrence.objects.create(created_by=get_userextension("ad"), owner=get_person({'first_name': 'Adrien'}), release=Release.objects.get(pk=17), **{'origin': u'BA', 'blister': False, 'add_date': datetime.datetime(2013, 3, 20, 2, 3, 39, 812967, tzinfo=pytz.utc), 'lastmodif_date': datetime.datetime(2013, 3, 20, 2, 3, 40, 233457, tzinfo=pytz.utc), 'pk': 17, 'purchase_price': 25.0})
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'B', attribute_id=get_corresponding_release_attribute(release=17, note='', lookup_dict={'category__name': u'content', 'name': u'self'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'B', attribute_id=get_corresponding_release_attribute(release=17, note='', lookup_dict={'category__name': u'packaging', 'name': u'dvd box'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
manual = OccurrenceAnyAttribute(occurrence=occurrence, value=u'C', attribute_id=get_corresponding_release_attribute(release=17, note='', lookup_dict={'category__name': u'papers', 'name': u'manual'}).pk, attribute_type=ReleaseAttribute_contentype)
occurrence.attributes.add(manual, bulk=False)
specific = OccurrenceSpecific.OperationalOcc.objects.create(occurrence=occurrence, **{'working_condition': u'?'})
tto = TagToOccurrence.objects.create(user_creator=get_userextension("ad"), user_occurrence_id=17, occurrence=occurrence)
# Tag and pictures
occurrence.tag_file = "advideogame/occurrences/17/tags/v1.png"
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=17, note='', lookup_dict={'category__name': u'packaging', 'name': u'dvd box'}).pk, detail=u'FRT', image_file='advideogame/occurrences/17/pictures/DSC03038.JPG')
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=17, note='', lookup_dict={'category__name': u'packaging', 'name': u'dvd box'}).pk, detail=u'BCK', image_file='advideogame/occurrences/17/pictures/DSC03039.JPG')
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=17, note='', lookup_dict={'category__name': u'packaging', 'name': u'dvd box'}).pk, detail=u'INS', image_file='advideogame/occurrences/17/pictures/DSC03040.JPG')
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=17, note='', lookup_dict={'category__name': u'papers', 'name': u'manual'}).pk, detail=u'FRT', image_file='advideogame/occurrences/17/pictures/DSC03041.JPG')
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=17, note='', lookup_dict={'category__name': u'papers', 'name': u'manual'}).pk, detail=u'INS', image_file='advideogame/occurrences/17/pictures/DSC03042.JPG')
occurrence.save()
OccurrenceAnyAttributeDefect.objects.create(occurrence_any_attribute=manual, defect_description="pen on the cover")

	#Die Hard Arcade
occurrence = Occurrence.objects.create(created_by=get_userextension("ad"), owner=get_person({'first_name': 'Adrien'}), release=Release.objects.get(pk=18), **{'origin': u'BU', 'blister': False, 'add_date': datetime.datetime(2013, 3, 20, 4, 33, 41, 384452, tzinfo=pytz.utc), 'lastmodif_date': datetime.datetime(2013, 3, 20, 4, 33, 41, 980667, tzinfo=pytz.utc), 'pk': 18, 'purchase_price': None})
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'B', attribute_id=get_corresponding_release_attribute(release=18, note='', lookup_dict={'category__name': u'content', 'name': u'self'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'C', attribute_id=get_corresponding_release_attribute(release=18, note='', lookup_dict={'category__name': u'packaging', 'name': u'dvd box'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value='0', attribute_id=get_corresponding_release_attribute(release=18, note='', lookup_dict={'category__name': u'papers', 'name': u'manual'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
specific = OccurrenceSpecific.OperationalOcc.objects.create(occurrence=occurrence, **{'working_condition': u'Y'})
tto = TagToOccurrence.objects.create(user_creator=get_userextension("ad"), user_occurrence_id=18, occurrence=occurrence)
# Tag and pictures
occurrence.tag_file = "advideogame/occurrences/18/tags/v1.png"
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=18, note='', lookup_dict={'category__name': u'packaging', 'name': u'dvd box'}).pk, detail=u'FRT', image_file='advideogame/occurrences/18/pictures/DSC03035.JPG')
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=18, note='', lookup_dict={'category__name': u'packaging', 'name': u'dvd box'}).pk, detail=u'BCK', image_file='advideogame/occurrences/18/pictures/DSC03036.JPG')
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=18, note='', lookup_dict={'category__name': u'packaging', 'name': u'dvd box'}).pk, detail=u'SLB', image_file='advideogame/occurrences/18/pictures/DSC03034.JPG')
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=18, note='', lookup_dict={'category__name': u'content', 'name': u'self'}).pk, detail=u'FRT', image_file='advideogame/occurrences/18/pictures/DSC03037.JPG')
occurrence.save()

	#Virtua Gun
occurrence = Occurrence.objects.create(created_by=get_userextension("ad"), owner=get_person({'first_name': 'Adrien'}), release=Release.objects.get(pk=20), **{'origin': u'BC', 'blister': False, 'add_date': datetime.datetime(2013, 3, 20, 4, 49, 29, 619633, tzinfo=pytz.utc), 'lastmodif_date': datetime.datetime(2013, 3, 20, 4, 54, 34, 441227, tzinfo=pytz.utc), 'pk': 19, 'purchase_price': 9.44})
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'A', attribute_id=get_corresponding_release_attribute(release=20, note='', lookup_dict={'category__name': u'content', 'name': u'self'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'B', attribute_id=get_corresponding_release_attribute(release=20, note='', lookup_dict={'category__name': u'packaging', 'name': u'cardboard box'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'A', attribute_id=get_corresponding_release_attribute(release=20, note='', lookup_dict={'category__name': 'packaging', 'name': 'cardboard inlay non-decorative'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'B', attribute_id=get_corresponding_release_attribute(release=20, note='', lookup_dict={'category__name': u'papers', 'name': u'manual'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
OccurrenceComposition.objects.create(from_occurrence=occurrence, release_composition=get_corresponding_release_compo({'to_release': 19, 'from_release': 20}))
specific = OccurrenceSpecific.OperationalOcc.objects.create(occurrence=occurrence, **{'working_condition': u'?'})
tto = TagToOccurrence.objects.create(user_creator=get_userextension("ad"), user_occurrence_id=19, occurrence=occurrence)
# Tag and pictures
occurrence.tag_file = "advideogame/occurrences/19/tags/v1.png"
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=20, note='', lookup_dict={'category__name': u'packaging', 'name': u'cardboard box'}).pk, detail=u'FRT', image_file='advideogame/occurrences/19/pictures/DSC03047.JPG')
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=20, note='', lookup_dict={'category__name': u'packaging', 'name': u'cardboard box'}).pk, detail=u'BCK', image_file='advideogame/occurrences/19/pictures/DSC03048.JPG')
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=20, note='', lookup_dict={'category__name': u'packaging', 'name': u'cardboard box'}).pk, detail=u'SID', image_file='advideogame/occurrences/19/pictures/DSC03049.JPG')
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=20, note='', lookup_dict={'category__name': u'papers', 'name': u'manual'}).pk, detail=u'FRT', image_file='advideogame/occurrences/19/pictures/DSC03051.JPG')
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=20, note='', lookup_dict={'category__name': u'papers', 'name': u'manual'}).pk, detail=u'INS', image_file='advideogame/occurrences/19/pictures/DSC03052.JPG')
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=20, note='', lookup_dict={'category__name': 'packaging', 'name': 'cardboard inlay non-decorative'}).pk, detail=u'FRT', image_file='advideogame/occurrences/19/pictures/DSC03054.JPG')
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=20, note='', lookup_dict={'category__name': u'content', 'name': u'self'}).pk, detail=u'FRT', image_file='advideogame/occurrences/19/pictures/DSC03053.JPG')
OccurrencePicture.objects.create(occurrence=occurrence, detail=u'GRP', image_file='advideogame/occurrences/19/pictures/DSC03050.JPG')
occurrence.save()

	#Virtua Gun
occurrence = Occurrence.objects.create(created_by=get_userextension("ad"), owner=get_person({'first_name': 'Adrien'}), release=Release.objects.get(pk=21), **{'origin': u'OR', 'blister': False, 'add_date': datetime.datetime(2013, 3, 20, 5, 36, 33, 902037, tzinfo=pytz.utc), 'lastmodif_date': datetime.datetime(2013, 3, 20, 5, 36, 34, 244506, tzinfo=pytz.utc), 'pk': 20, 'purchase_price': None})
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'B', attribute_id=get_corresponding_release_attribute(release=21, note='', lookup_dict={'category__name': u'content', 'name': u'self'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value='0', attribute_id=get_corresponding_release_attribute(release=21, note='', lookup_dict={'category__name': u'packaging', 'name': u'cardboard box'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value='0', attribute_id=get_corresponding_release_attribute(release=21, note='', lookup_dict={'category__name': 'packaging', 'name': 'cardboard inlay non-decorative'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value='0', attribute_id=get_corresponding_release_attribute(release=21, note='', lookup_dict={'category__name': u'papers', 'name': u'manual'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
OccurrenceComposition.objects.create(from_occurrence=occurrence, to_occurrence=Occurrence.objects.get(pk=15), release_composition=get_corresponding_release_compo({'to_release': 15, 'from_release': 21}))
specific = OccurrenceSpecific.OperationalOcc.objects.create(occurrence=occurrence, **{'working_condition': u'Y'})
tto = TagToOccurrence.objects.create(user_creator=get_userextension("ad"), user_occurrence_id=20, occurrence=occurrence)
# Tag and pictures
occurrence.tag_file = "advideogame/occurrences/20/tags/v1.png"
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=21, note='', lookup_dict={'category__name': u'content', 'name': u'self'}).pk, detail=u'FRT', image_file='advideogame/occurrences/20/pictures/DSC03127.JPG')
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=21, note='', lookup_dict={'category__name': u'content', 'name': u'self'}).pk, detail=u'BCK', image_file='advideogame/occurrences/20/pictures/DSC03126.JPG')
OccurrencePicture.objects.create(occurrence=occurrence, detail=u'GRP', image_file='advideogame/occurrences/20/pictures/DSC03128.JPG')
occurrence.save()

	#Virtua Gun
occurrence = Occurrence.objects.create(created_by=get_userextension("ad"), owner=get_person({'first_name': 'Adrien'}), release=Release.objects.get(pk=22), **{'origin': u'BU', 'blister': False, 'add_date': datetime.datetime(2013, 3, 20, 5, 45, 14, 658702, tzinfo=pytz.utc), 'lastmodif_date': datetime.datetime(2013, 3, 20, 5, 45, 15, 14444, tzinfo=pytz.utc), 'pk': 21, 'purchase_price': None})
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'B', attribute_id=get_corresponding_release_attribute(release=22, note='', lookup_dict={'category__name': u'content', 'name': u'self'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
specific = OccurrenceSpecific.OperationalOcc.objects.create(occurrence=occurrence, **{'working_condition': u'Y'})
tto = TagToOccurrence.objects.create(user_creator=get_userextension("ad"), user_occurrence_id=21, occurrence=occurrence)
# Tag and pictures
occurrence.tag_file = "advideogame/occurrences/21/tags/v1.png"
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=22, note='', lookup_dict={'category__name': u'content', 'name': u'self'}).pk, detail=u'FRT', image_file='advideogame/occurrences/21/pictures/DSC03124.JPG')
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=22, note='', lookup_dict={'category__name': u'content', 'name': u'self'}).pk, detail=u'BCK', image_file='advideogame/occurrences/21/pictures/DSC03125.JPG')
occurrence.save()

	#Virtua Gun
occurrence = Occurrence.objects.create(created_by=get_userextension("ad"), owner=get_person({'first_name': 'Adrien'}), release=Release.objects.get(pk=23), **{'origin': u'BC', 'blister': False, 'add_date': datetime.datetime(2013, 3, 20, 5, 49, 52, 323513, tzinfo=pytz.utc), 'lastmodif_date': datetime.datetime(2013, 3, 20, 5, 49, 52, 636017, tzinfo=pytz.utc), 'pk': 22, 'purchase_price': None})
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'B', attribute_id=get_corresponding_release_attribute(release=23, note='', lookup_dict={'category__name': u'content', 'name': u'self'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
specific = OccurrenceSpecific.OperationalOcc.objects.create(occurrence=occurrence, **{'working_condition': u'?'})
tto = TagToOccurrence.objects.create(user_creator=get_userextension("ad"), user_occurrence_id=22, occurrence=occurrence)
# Tag and pictures
occurrence.tag_file = "advideogame/occurrences/22/tags/v1.png"
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=23, note='', lookup_dict={'category__name': u'content', 'name': u'self'}).pk, detail=u'FRT', image_file='advideogame/occurrences/22/pictures/DSC03090.JPG')
occurrence.save()

	#Worms
occurrence = Occurrence.objects.create(created_by=get_userextension("ad"), owner=get_person({'first_name': 'Adrien'}), release=Release.objects.get(pk=24), **{'origin': u'BU', 'blister': False, 'add_date': datetime.datetime(2013, 3, 27, 22, 16, 47, 46730, tzinfo=pytz.utc), 'lastmodif_date': datetime.datetime(2013, 3, 27, 22, 16, 49, 107700, tzinfo=pytz.utc), 'pk': 23, 'purchase_price': None})
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'B', attribute_id=get_corresponding_release_attribute(release=24, note='', lookup_dict={'category__name': u'content', 'name': u'self'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'B', attribute_id=get_corresponding_release_attribute(release=24, note='', lookup_dict={'category__name': u'packaging', 'name': u'dvd box'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value='0', attribute_id=get_corresponding_release_attribute(release=24, note='', lookup_dict={'category__name': u'papers', 'name': u'manual'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
specific = OccurrenceSpecific.OperationalOcc.objects.create(occurrence=occurrence, **{'working_condition': u'Y'})
tto = TagToOccurrence.objects.create(user_creator=get_userextension("ad"), user_occurrence_id=23, occurrence=occurrence)
# Tag and pictures
occurrence.tag_file = "advideogame/occurrences/23/tags/v1.png"
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=24, note='', lookup_dict={'category__name': u'packaging', 'name': u'dvd box'}).pk, detail=u'FRT', image_file='advideogame/occurrences/23/pictures/DSC03069.JPG')
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=24, note='', lookup_dict={'category__name': u'packaging', 'name': u'dvd box'}).pk, detail=u'BCK', image_file='advideogame/occurrences/23/pictures/DSC03070.JPG')
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=24, note='', lookup_dict={'category__name': u'packaging', 'name': u'dvd box'}).pk, detail=u'SLB', image_file='advideogame/occurrences/23/pictures/DSC03068.JPG')
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=24, note='', lookup_dict={'category__name': u'content', 'name': u'self'}).pk, detail=u'FRT', image_file='advideogame/occurrences/23/pictures/DSC03071.JPG')
occurrence.save()

	#Sega Rally Championship
occurrence = Occurrence.objects.create(created_by=get_userextension("ad"), owner=get_person({'first_name': 'Adrien'}), release=Release.objects.get(pk=25), **{'origin': u'OR', 'blister': False, 'add_date': datetime.datetime(2013, 3, 27, 22, 27, 0, 555750, tzinfo=pytz.utc), 'lastmodif_date': datetime.datetime(2013, 3, 27, 22, 27, 1, 194771, tzinfo=pytz.utc), 'pk': 24, 'purchase_price': None})
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'A', attribute_id=get_corresponding_release_attribute(release=25, note='', lookup_dict={'category__name': u'content', 'name': u'self'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'B', attribute_id=get_corresponding_release_attribute(release=25, note='', lookup_dict={'category__name': u'packaging', 'name': u'dvd box'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'B', attribute_id=get_corresponding_release_attribute(release=25, note='', lookup_dict={'category__name': u'papers', 'name': u'manual'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
specific = OccurrenceSpecific.OperationalOcc.objects.create(occurrence=occurrence, **{'working_condition': u'Y'})
tto = TagToOccurrence.objects.create(user_creator=get_userextension("ad"), user_occurrence_id=24, occurrence=occurrence)
# Tag and pictures
occurrence.tag_file = "advideogame/occurrences/24/tags/v1.png"
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=25, note='', lookup_dict={'category__name': u'packaging', 'name': u'dvd box'}).pk, detail=u'FRT', image_file='advideogame/occurrences/24/pictures/DSC03065.JPG')
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=25, note='', lookup_dict={'category__name': u'packaging', 'name': u'dvd box'}).pk, detail=u'BCK', image_file='advideogame/occurrences/24/pictures/DSC03066.JPG')
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=25, note='', lookup_dict={'category__name': u'packaging', 'name': u'dvd box'}).pk, detail=u'SLB', image_file='advideogame/occurrences/24/pictures/DSC03064.JPG')
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=25, note='', lookup_dict={'category__name': u'packaging', 'name': u'dvd box'}).pk, detail=u'INS', image_file='advideogame/occurrences/24/pictures/DSC03067.JPG')
occurrence.save()

	#Daytona USA
occurrence = Occurrence.objects.create(created_by=get_userextension("ad"), owner=get_person({'first_name': 'Adrien'}), release=Release.objects.get(pk=26), **{'origin': u'BU', 'blister': False, 'add_date': datetime.datetime(2013, 3, 27, 22, 29, 24, 440369, tzinfo=pytz.utc), 'lastmodif_date': datetime.datetime(2013, 3, 27, 22, 29, 25, 95779, tzinfo=pytz.utc), 'pk': 25, 'purchase_price': None})
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'B', attribute_id=get_corresponding_release_attribute(release=26, note='', lookup_dict={'category__name': u'content', 'name': u'self'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'B', attribute_id=get_corresponding_release_attribute(release=26, note='', lookup_dict={'category__name': u'packaging', 'name': u'dvd box'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'A', attribute_id=get_corresponding_release_attribute(release=26, note='', lookup_dict={'category__name': u'papers', 'name': u'manual'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
specific = OccurrenceSpecific.OperationalOcc.objects.create(occurrence=occurrence, **{'working_condition': u'Y'})
tto = TagToOccurrence.objects.create(user_creator=get_userextension("ad"), user_occurrence_id=25, occurrence=occurrence)
# Tag and pictures
occurrence.tag_file = "advideogame/occurrences/25/tags/v1.png"
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=26, note='', lookup_dict={'category__name': u'packaging', 'name': u'dvd box'}).pk, detail=u'FRT', image_file='advideogame/occurrences/25/pictures/DSC03061.JPG')
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=26, note='', lookup_dict={'category__name': u'packaging', 'name': u'dvd box'}).pk, detail=u'BCK', image_file='advideogame/occurrences/25/pictures/DSC03062.JPG')
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=26, note='', lookup_dict={'category__name': u'packaging', 'name': u'dvd box'}).pk, detail=u'SLB', image_file='advideogame/occurrences/25/pictures/DSC03060.JPG')
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=26, note='', lookup_dict={'category__name': u'packaging', 'name': u'dvd box'}).pk, detail=u'INS', image_file='advideogame/occurrences/25/pictures/DSC03063.JPG')
occurrence.save()

	#Marvel Super Heroes
occurrence = Occurrence.objects.create(created_by=get_userextension("ad"), owner=get_person({'first_name': 'Adrien'}), release=Release.objects.get(pk=27), **{'origin': u'BU', 'blister': False, 'add_date': datetime.datetime(2013, 3, 27, 22, 31, 27, 949353, tzinfo=pytz.utc), 'lastmodif_date': datetime.datetime(2013, 3, 27, 22, 31, 28, 436161, tzinfo=pytz.utc), 'pk': 26, 'purchase_price': None})
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'B', attribute_id=get_corresponding_release_attribute(release=27, note='', lookup_dict={'category__name': u'content', 'name': u'self'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'A', attribute_id=get_corresponding_release_attribute(release=27, note='', lookup_dict={'category__name': u'packaging', 'name': u'dvd box'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value='0', attribute_id=get_corresponding_release_attribute(release=27, note='', lookup_dict={'category__name': u'papers', 'name': u'manual'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
specific = OccurrenceSpecific.OperationalOcc.objects.create(occurrence=occurrence, **{'working_condition': u'Y'})
tto = TagToOccurrence.objects.create(user_creator=get_userextension("ad"), user_occurrence_id=26, occurrence=occurrence)
# Tag and pictures
occurrence.tag_file = "advideogame/occurrences/26/tags/v1.png"
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=27, note='', lookup_dict={'category__name': u'packaging', 'name': u'dvd box'}).pk, detail=u'FRT', image_file='advideogame/occurrences/26/pictures/DSC03056.JPG')
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=27, note='', lookup_dict={'category__name': u'packaging', 'name': u'dvd box'}).pk, detail=u'BCK', image_file='advideogame/occurrences/26/pictures/DSC03057.JPG')
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=27, note='', lookup_dict={'category__name': u'packaging', 'name': u'dvd box'}).pk, detail=u'SLB', image_file='advideogame/occurrences/26/pictures/DSC03058.JPG')
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=27, note='', lookup_dict={'category__name': u'content', 'name': u'self'}).pk, detail=u'FRT', image_file='advideogame/occurrences/26/pictures/DSC03059.JPG')
occurrence.save()

	#Sega Touring Car Championship
occurrence = Occurrence.objects.create(created_by=get_userextension("ad"), owner=get_person({'first_name': 'Adrien'}), release=Release.objects.get(pk=28), **{'origin': u'BC', 'blister': False, 'add_date': datetime.datetime(2013, 3, 27, 22, 54, 18, 161793, tzinfo=pytz.utc), 'lastmodif_date': datetime.datetime(2013, 3, 27, 22, 54, 18, 596435, tzinfo=pytz.utc), 'pk': 27, 'purchase_price': None})
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'B', attribute_id=get_corresponding_release_attribute(release=28, note='', lookup_dict={'category__name': u'content', 'name': u'self'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'B', attribute_id=get_corresponding_release_attribute(release=28, note='', lookup_dict={'category__name': u'packaging', 'name': u'dvd box'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'A', attribute_id=get_corresponding_release_attribute(release=28, note='', lookup_dict={'category__name': u'papers', 'name': u'leaflet'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
manual = OccurrenceAnyAttribute(occurrence=occurrence, value=u'B', attribute_id=get_corresponding_release_attribute(release=28, note='', lookup_dict={'category__name': u'papers', 'name': u'manual'}).pk, attribute_type=ReleaseAttribute_contentype)
occurrence.attributes.add(manual, bulk=False)
specific = OccurrenceSpecific.OperationalOcc.objects.create(occurrence=occurrence, **{'working_condition': u'?'})
tto = TagToOccurrence.objects.create(user_creator=get_userextension("ad"), user_occurrence_id=27, occurrence=occurrence)
# Tag and pictures
occurrence.tag_file = "advideogame/occurrences/27/tags/v1.png"
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=28, note='', lookup_dict={'category__name': u'packaging', 'name': u'dvd box'}).pk, detail=u'FRT', image_file='advideogame/occurrences/27/pictures/DSC03085.JPG')
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=28, note='', lookup_dict={'category__name': u'packaging', 'name': u'dvd box'}).pk, detail=u'BCK', image_file='advideogame/occurrences/27/pictures/DSC03086.JPG')
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=28, note='', lookup_dict={'category__name': u'packaging', 'name': u'dvd box'}).pk, detail=u'SLB', image_file='advideogame/occurrences/27/pictures/DSC03084.JPG')
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=28, note='', lookup_dict={'category__name': u'packaging', 'name': u'dvd box'}).pk, detail=u'INS', image_file='advideogame/occurrences/27/pictures/DSC03089.JPG')
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=28, note='', lookup_dict={'category__name': u'papers', 'name': u'leaflet'}).pk, detail=u'FRT', image_file='advideogame/occurrences/27/pictures/DSC03087.JPG')
OccurrencePicture.objects.create(occurrence=occurrence, detail=u'GRP', image_file='advideogame/occurrences/27/pictures/DSC03088.JPG')
occurrence.save()
OccurrenceAnyAttributeDefect.objects.create(occurrence_any_attribute=manual, defect_description="pen on the last page")

	#Formula Karts Special Edition
occurrence = Occurrence.objects.create(created_by=get_userextension("ad"), owner=get_person({'first_name': 'Adrien'}), release=Release.objects.get(pk=30), **{'origin': u'BC', 'blister': False, 'add_date': datetime.datetime(2013, 3, 27, 22, 57, 37, 969093, tzinfo=pytz.utc), 'lastmodif_date': datetime.datetime(2013, 3, 27, 22, 57, 38, 326303, tzinfo=pytz.utc), 'pk': 28, 'purchase_price': None})
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'B', attribute_id=get_corresponding_release_attribute(release=30, note='', lookup_dict={'category__name': u'content', 'name': u'self'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'B', attribute_id=get_corresponding_release_attribute(release=30, note='', lookup_dict={'category__name': u'packaging', 'name': u'dvd box'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'B', attribute_id=get_corresponding_release_attribute(release=30, note='', lookup_dict={'category__name': u'papers', 'name': u'manual'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
specific = OccurrenceSpecific.OperationalOcc.objects.create(occurrence=occurrence, **{'working_condition': u'?'})
tto = TagToOccurrence.objects.create(user_creator=get_userextension("ad"), user_occurrence_id=28, occurrence=occurrence)
# Tag and pictures
occurrence.tag_file = "advideogame/occurrences/28/tags/v1.png"
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=30, note='', lookup_dict={'category__name': u'packaging', 'name': u'dvd box'}).pk, detail=u'FRT', image_file='advideogame/occurrences/28/pictures/DSC03073.JPG')
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=30, note='', lookup_dict={'category__name': u'packaging', 'name': u'dvd box'}).pk, detail=u'BCK', image_file='advideogame/occurrences/28/pictures/DSC03074.JPG')
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=30, note='', lookup_dict={'category__name': u'packaging', 'name': u'dvd box'}).pk, detail=u'SLB', image_file='advideogame/occurrences/28/pictures/DSC03072.JPG')
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=30, note='', lookup_dict={'category__name': u'packaging', 'name': u'dvd box'}).pk, detail=u'INS', image_file='advideogame/occurrences/28/pictures/DSC03075.JPG')
occurrence.save()

	#Sonic Jam
occurrence = Occurrence.objects.create(created_by=get_userextension("ad"), owner=get_person({'first_name': 'Adrien'}), release=Release.objects.get(pk=31), **{'origin': u'OR', 'blister': False, 'add_date': datetime.datetime(2013, 3, 27, 23, 4, 51, 126899, tzinfo=pytz.utc), 'lastmodif_date': datetime.datetime(2013, 3, 27, 23, 4, 51, 543179, tzinfo=pytz.utc), 'pk': 29, 'purchase_price': None})
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'B', attribute_id=get_corresponding_release_attribute(release=31, note='', lookup_dict={'category__name': u'content', 'name': u'self'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'B', attribute_id=get_corresponding_release_attribute(release=31, note='', lookup_dict={'category__name': u'packaging', 'name': u'dvd box'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'A', attribute_id=get_corresponding_release_attribute(release=31, note='', lookup_dict={'category__name': u'papers', 'name': u'manual'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
specific = OccurrenceSpecific.OperationalOcc.objects.create(occurrence=occurrence, **{'working_condition': u'Y'})
tto = TagToOccurrence.objects.create(user_creator=get_userextension("ad"), user_occurrence_id=29, occurrence=occurrence)
# Tag and pictures
occurrence.tag_file = "advideogame/occurrences/29/tags/v1.png"
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=31, note='', lookup_dict={'category__name': u'packaging', 'name': u'dvd box'}).pk, detail=u'FRT', image_file='advideogame/occurrences/29/pictures/DSC03081.JPG')
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=31, note='', lookup_dict={'category__name': u'packaging', 'name': u'dvd box'}).pk, detail=u'BCK', image_file='advideogame/occurrences/29/pictures/DSC03082.JPG')
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=31, note='', lookup_dict={'category__name': u'packaging', 'name': u'dvd box'}).pk, detail=u'SLB', image_file='advideogame/occurrences/29/pictures/DSC03080.JPG')
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=31, note='', lookup_dict={'category__name': u'packaging', 'name': u'dvd box'}).pk, detail=u'INS', image_file='advideogame/occurrences/29/pictures/DSC03083.JPG')
occurrence.save()

	#Duke Nukem 3D
occurrence = Occurrence.objects.create(created_by=get_userextension("ad"), owner=get_person({'first_name': 'Adrien'}), release=Release.objects.get(pk=32), **{'origin': u'GF', 'blister': False, 'add_date': datetime.datetime(2013, 3, 27, 23, 6, 55, 722616, tzinfo=pytz.utc), 'lastmodif_date': datetime.datetime(2013, 3, 27, 23, 6, 56, 56055, tzinfo=pytz.utc), 'pk': 30, 'purchase_price': None})
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'C', attribute_id=get_corresponding_release_attribute(release=32, note='', lookup_dict={'category__name': u'content', 'name': u'self'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'B', attribute_id=get_corresponding_release_attribute(release=32, note='', lookup_dict={'category__name': u'packaging', 'name': u'dvd box'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'A', attribute_id=get_corresponding_release_attribute(release=32, note='', lookup_dict={'category__name': u'papers', 'name': u'manual'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
specific = OccurrenceSpecific.OperationalOcc.objects.create(occurrence=occurrence, **{'working_condition': u'?'})
tto = TagToOccurrence.objects.create(user_creator=get_userextension("ad"), user_occurrence_id=30, occurrence=occurrence)
# Tag and pictures
occurrence.tag_file = "advideogame/occurrences/30/tags/v1.png"
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=32, note='', lookup_dict={'category__name': u'packaging', 'name': u'dvd box'}).pk, detail=u'FRT', image_file='advideogame/occurrences/30/pictures/DSC03077.JPG')
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=32, note='', lookup_dict={'category__name': u'packaging', 'name': u'dvd box'}).pk, detail=u'BCK', image_file='advideogame/occurrences/30/pictures/DSC03078.JPG')
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=32, note='', lookup_dict={'category__name': u'packaging', 'name': u'dvd box'}).pk, detail=u'SLB', image_file='advideogame/occurrences/30/pictures/DSC03076.JPG')
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=32, note='', lookup_dict={'category__name': u'packaging', 'name': u'dvd box'}).pk, detail=u'INS', image_file='advideogame/occurrences/30/pictures/DSC03079.JPG')
occurrence.save()

	#DoDonPachi
occurrence = Occurrence.objects.create(created_by=get_userextension("ad"), owner=get_person({'first_name': 'Adrien'}), release=Release.objects.get(pk=33), **{'origin': u'BC', 'blister': False, 'add_date': datetime.datetime(2013, 3, 27, 23, 19, 30, 588265, tzinfo=pytz.utc), 'lastmodif_date': datetime.datetime(2013, 3, 27, 23, 20, 45, 840659, tzinfo=pytz.utc), 'pk': 31, 'purchase_price': None})
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'A', attribute_id=get_corresponding_release_attribute(release=33, note='', lookup_dict={'category__name': u'content', 'name': u'self'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'B', attribute_id=get_corresponding_release_attribute(release=33, note='', lookup_dict={'category__name': u'packaging', 'name': u'jewel box'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value='0', attribute_id=get_corresponding_release_attribute(release=33, note='', lookup_dict={'category__name': u'packaging', 'name': u'spine card'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'A', attribute_id=get_corresponding_release_attribute(release=33, note='', lookup_dict={'category__name': u'papers', 'name': u'leaflet'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'B', attribute_id=get_corresponding_release_attribute(release=33, note='', lookup_dict={'category__name': u'papers', 'name': u'manual'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'A', attribute_id=get_corresponding_release_attribute(release=33, note='', lookup_dict={'category__name': u'papers', 'name': u'registration card'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
specific = OccurrenceSpecific.OperationalOcc.objects.create(occurrence=occurrence, **{'working_condition': u'?'})
tto = TagToOccurrence.objects.create(user_creator=get_userextension("ad"), user_occurrence_id=31, occurrence=occurrence)
# Tag and pictures
occurrence.tag_file = "advideogame/occurrences/31/tags/v1.png"
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=33, note='', lookup_dict={'category__name': u'packaging', 'name': u'jewel box'}).pk, detail=u'FRT', image_file='advideogame/occurrences/31/pictures/DSC03115.JPG')
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=33, note='', lookup_dict={'category__name': u'packaging', 'name': u'jewel box'}).pk, detail=u'BCK', image_file='advideogame/occurrences/31/pictures/DSC03116.JPG')
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=33, note='', lookup_dict={'category__name': u'packaging', 'name': u'jewel box'}).pk, detail=u'SLB', image_file='advideogame/occurrences/31/pictures/DSC03113.JPG')
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=33, note='', lookup_dict={'category__name': u'packaging', 'name': u'jewel box'}).pk, detail=u'SLB', image_file='advideogame/occurrences/31/pictures/DSC03114.JPG')
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=33, note='', lookup_dict={'category__name': u'packaging', 'name': u'jewel box'}).pk, detail=u'INS', image_file='advideogame/occurrences/31/pictures/DSC03117.JPG')
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=33, note='', lookup_dict={'category__name': u'papers', 'name': u'manual'}).pk, detail=u'INS', image_file='advideogame/occurrences/31/pictures/DSC03118.JPG')
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=33, note='', lookup_dict={'category__name': u'papers', 'name': u'leaflet'}).pk, detail=u'FRT', image_file='advideogame/occurrences/31/pictures/DSC03120.JPG')
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=33, note='', lookup_dict={'category__name': u'papers', 'name': u'leaflet'}).pk, detail=u'BCK', image_file='advideogame/occurrences/31/pictures/DSC03121.JPG')
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=33, note='', lookup_dict={'category__name': u'papers', 'name': u'registration card'}).pk, detail=u'FRT', image_file='advideogame/occurrences/31/pictures/DSC03122.JPG')
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=33, note='', lookup_dict={'category__name': u'papers', 'name': u'registration card'}).pk, detail=u'BCK', image_file='advideogame/occurrences/31/pictures/DSC03123.JPG')
OccurrencePicture.objects.create(occurrence=occurrence, detail=u'GRP', image_file='advideogame/occurrences/31/pictures/DSC03119.JPG')
occurrence.save()

	#Resident Evil
occurrence = Occurrence.objects.create(created_by=get_userextension("ad"), owner=get_person({'first_name': 'Adrien'}), release=Release.objects.get(pk=34), **{'origin': u'BC', 'blister': False, 'add_date': datetime.datetime(2013, 3, 27, 23, 22, 26, 180120, tzinfo=pytz.utc), 'lastmodif_date': datetime.datetime(2013, 3, 27, 23, 22, 26, 571814, tzinfo=pytz.utc), 'pk': 32, 'purchase_price': None})
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'B', attribute_id=get_corresponding_release_attribute(release=34, note='', lookup_dict={'category__name': u'content', 'name': u'self'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'B', attribute_id=get_corresponding_release_attribute(release=34, note='', lookup_dict={'category__name': u'packaging', 'name': u'dvd box'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'B', attribute_id=get_corresponding_release_attribute(release=34, note='', lookup_dict={'category__name': u'papers', 'name': u'manual'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
specific = OccurrenceSpecific.OperationalOcc.objects.create(occurrence=occurrence, **{'working_condition': u'?'})
tto = TagToOccurrence.objects.create(user_creator=get_userextension("ad"), user_occurrence_id=32, occurrence=occurrence)
# Tag and pictures
occurrence.tag_file = "advideogame/occurrences/32/tags/v1.png"
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=34, note='', lookup_dict={'category__name': u'packaging', 'name': u'dvd box'}).pk, detail=u'FRT', image_file='advideogame/occurrences/32/pictures/DSC03109.JPG')
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=34, note='', lookup_dict={'category__name': u'packaging', 'name': u'dvd box'}).pk, detail=u'BCK', image_file='advideogame/occurrences/32/pictures/DSC03110.JPG')
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=34, note='', lookup_dict={'category__name': u'packaging', 'name': u'dvd box'}).pk, detail=u'SLB', image_file='advideogame/occurrences/32/pictures/DSC03112.JPG')
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=34, note='', lookup_dict={'category__name': u'packaging', 'name': u'dvd box'}).pk, detail=u'INS', image_file='advideogame/occurrences/32/pictures/DSC03111.JPG')
occurrence.save()

	#Virtua Cop
occurrence = Occurrence.objects.create(created_by=get_userextension("ad"), owner=get_person({'first_name': 'Adrien'}), release=Release.objects.get(pk=35), **{'origin': u'BC', 'blister': False, 'add_date': datetime.datetime(2013, 3, 27, 23, 27, 28, 795651, tzinfo=pytz.utc), 'lastmodif_date': datetime.datetime(2013, 3, 27, 23, 27, 29, 192785, tzinfo=pytz.utc), 'pk': 33, 'purchase_price': 11.77})
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'B', attribute_id=get_corresponding_release_attribute(release=35, note='', lookup_dict={'category__name': u'content', 'name': u'self'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'B', attribute_id=get_corresponding_release_attribute(release=35, note='', lookup_dict={'category__name': u'packaging', 'name': u'dvd box'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'A', attribute_id=get_corresponding_release_attribute(release=35, note='', lookup_dict={'category__name': u'papers', 'name': u'manual'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
specific = OccurrenceSpecific.OperationalOcc.objects.create(occurrence=occurrence, **{'working_condition': u'?'})
tto = TagToOccurrence.objects.create(user_creator=get_userextension("ad"), user_occurrence_id=33, occurrence=occurrence)
# Tag and pictures
occurrence.tag_file = "advideogame/occurrences/33/tags/v1.png"
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=35, note='', lookup_dict={'category__name': u'packaging', 'name': u'dvd box'}).pk, detail=u'FRT', image_file='advideogame/occurrences/33/pictures/DSC03101.JPG')
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=35, note='', lookup_dict={'category__name': u'packaging', 'name': u'dvd box'}).pk, detail=u'BCK', image_file='advideogame/occurrences/33/pictures/DSC03102.JPG')
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=35, note='', lookup_dict={'category__name': u'packaging', 'name': u'dvd box'}).pk, detail=u'SLB', image_file='advideogame/occurrences/33/pictures/DSC03100.JPG')
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=35, note='', lookup_dict={'category__name': u'packaging', 'name': u'dvd box'}).pk, detail=u'INS', image_file='advideogame/occurrences/33/pictures/DSC03103.JPG')
occurrence.save()

	#Sega Saturn Control Pad
occurrence = Occurrence.objects.create(created_by=get_userextension("ad"), owner=get_person({'first_name': 'Adrien'}), release=Release.objects.get(pk=37), **{'origin': u'BC', 'blister': False, 'add_date': datetime.datetime(2013, 3, 28, 1, 33, 14, 296900, tzinfo=pytz.utc), 'lastmodif_date': datetime.datetime(2013, 3, 28, 1, 43, 25, 985522, tzinfo=pytz.utc), 'pk': 34, 'purchase_price': None})
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'B', attribute_id=get_corresponding_release_attribute(release=37, note='', lookup_dict={'category__name': u'content', 'name': u'self'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
specific = OccurrenceSpecific.OperationalOcc.objects.create(occurrence=occurrence, **{'working_condition': u'Y'})
tto = TagToOccurrence.objects.create(user_creator=get_userextension("ad"), user_occurrence_id=34, occurrence=occurrence)
# Tag and pictures
occurrence.tag_file = "advideogame/occurrences/34/tags/v1.png"
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=37, note='', lookup_dict={'category__name': u'content', 'name': u'self'}).pk, detail=u'FRT', image_file='advideogame/occurrences/34/pictures/DSC03138.JPG')
occurrence.save()

	#Sega Saturn Control Pad
occurrence = Occurrence.objects.create(created_by=get_userextension("ad"), owner=get_person({'first_name': 'Adrien'}), release=Release.objects.get(pk=36), **{'origin': u'BC', 'blister': False, 'add_date': datetime.datetime(2013, 3, 28, 1, 45, 45, 107872, tzinfo=pytz.utc), 'lastmodif_date': datetime.datetime(2013, 3, 28, 1, 45, 45, 432093, tzinfo=pytz.utc), 'pk': 35, 'purchase_price': None})
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'C', attribute_id=get_corresponding_release_attribute(release=36, note='', lookup_dict={'category__name': u'content', 'name': u'self'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
specific = OccurrenceSpecific.OperationalOcc.objects.create(occurrence=occurrence, **{'working_condition': u'Y'})
tto = TagToOccurrence.objects.create(user_creator=get_userextension("ad"), user_occurrence_id=35, occurrence=occurrence)
# Tag and pictures
occurrence.tag_file = "advideogame/occurrences/35/tags/v1.png"
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=36, note='', lookup_dict={'category__name': u'content', 'name': u'self'}).pk, detail=u'FRT', image_file='advideogame/occurrences/35/pictures/DSC03139.JPG')
occurrence.save()

	#Pad Saturn ST.2
occurrence = Occurrence.objects.create(created_by=get_userextension("ad"), owner=get_person({'first_name': 'Adrien'}), release=Release.objects.get(pk=38), **{'origin': u'OR', 'blister': False, 'add_date': datetime.datetime(2013, 3, 28, 1, 47, 23, 123518, tzinfo=pytz.utc), 'lastmodif_date': datetime.datetime(2013, 3, 28, 1, 47, 23, 433699, tzinfo=pytz.utc), 'pk': 36, 'purchase_price': None})
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'B', attribute_id=get_corresponding_release_attribute(release=38, note='', lookup_dict={'category__name': u'content', 'name': u'self'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value='0', attribute_id=get_corresponding_release_attribute(release=38, note='', lookup_dict={'category__name': u'packaging', 'name': u'cardboard box'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value='0', attribute_id=get_corresponding_release_attribute(release=38, note='', lookup_dict={'category__name': u'papers', 'name': u'manual'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
specific = OccurrenceSpecific.OperationalOcc.objects.create(occurrence=occurrence, **{'working_condition': u'Y'})
tto = TagToOccurrence.objects.create(user_creator=get_userextension("ad"), user_occurrence_id=36, occurrence=occurrence)
# Tag and pictures
occurrence.tag_file = "advideogame/occurrences/36/tags/v1.png"
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=38, note='', lookup_dict={'category__name': u'content', 'name': u'self'}).pk, detail=u'FRT', image_file='advideogame/occurrences/36/pictures/DSC03135.JPG')
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=38, note='', lookup_dict={'category__name': u'content', 'name': u'self'}).pk, detail=u'FRT', image_file='advideogame/occurrences/36/pictures/DSC03136.JPG')
occurrence.save()

	#3D Control Pad (Saturn)
occurrence = Occurrence.objects.create(created_by=get_userextension("ad"), owner=get_person({'first_name': 'Adrien'}), release=Release.objects.get(pk=41), **{'origin': u'OR', 'blister': False, 'add_date': datetime.datetime(2013, 3, 28, 1, 52, 42, 596576, tzinfo=pytz.utc), 'lastmodif_date': datetime.datetime(2013, 3, 28, 1, 52, 42, 937688, tzinfo=pytz.utc), 'pk': 37, 'purchase_price': None})
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'B', attribute_id=get_corresponding_release_attribute(release=41, note='', lookup_dict={'category__name': u'content', 'name': u'self'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value='0', attribute_id=get_corresponding_release_attribute(release=41, note='', lookup_dict={'category__name': u'packaging', 'name': u'cardboard box'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value='0', attribute_id=get_corresponding_release_attribute(release=41, note='', lookup_dict={'category__name': 'packaging', 'name': u'baggies'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value='0', attribute_id=get_corresponding_release_attribute(release=41, note='', lookup_dict={'category__name': 'packaging', 'name': 'disposable connector protection'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value='0', attribute_id=get_corresponding_release_attribute(release=41, note='', lookup_dict={'category__name': 'packaging', 'name': 'cardboard inlay non-decorative'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
OccurrenceComposition.objects.create(from_occurrence=occurrence, to_occurrence=Occurrence.objects.get(pk=2), release_composition=get_corresponding_release_compo({'to_release': 2, 'from_release': 41}))
specific = OccurrenceSpecific.OperationalOcc.objects.create(occurrence=occurrence, **{'working_condition': u'Y'})
tto = TagToOccurrence.objects.create(user_creator=get_userextension("ad"), user_occurrence_id=37, occurrence=occurrence)
# Tag and pictures
occurrence.tag_file = "advideogame/occurrences/37/tags/v1.png"
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=41, note='', lookup_dict={'category__name': u'content', 'name': u'self'}).pk, detail=u'FRT', image_file='advideogame/occurrences/37/pictures/DSC03105.JPG')
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=41, note='', lookup_dict={'category__name': u'content', 'name': u'self'}).pk, detail=u'FRT', image_file='advideogame/occurrences/37/pictures/DSC03104.JPG')
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=41, note='', lookup_dict={'category__name': u'content', 'name': u'self'}).pk, detail=u'BCK', image_file='advideogame/occurrences/37/pictures/DSC03106.JPG')
OccurrencePicture.objects.create(occurrence=occurrence, detail=u'GRP', image_file='advideogame/occurrences/37/pictures/DSC03107.JPG')
occurrence.save()

	#Sega Saturn Control Pad
occurrence = Occurrence.objects.create(created_by=get_userextension("ad"), owner=get_person({'first_name': 'Adrien'}), release=Release.objects.get(pk=37), **{'origin': u'OR', 'blister': False, 'add_date': datetime.datetime(2013, 3, 28, 2, 7, 6, 471200, tzinfo=pytz.utc), 'lastmodif_date': datetime.datetime(2013, 3, 28, 2, 7, 6, 810197, tzinfo=pytz.utc), 'pk': 38, 'purchase_price': None})
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'B', attribute_id=get_corresponding_release_attribute(release=37, note='', lookup_dict={'category__name': u'content', 'name': u'self'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
specific = OccurrenceSpecific.OperationalOcc.objects.create(occurrence=occurrence, **{'working_condition': u'Y'})
tto = TagToOccurrence.objects.create(user_creator=get_userextension("ad"), user_occurrence_id=38, occurrence=occurrence)
# Tag and pictures
occurrence.tag_file = "advideogame/occurrences/38/tags/v1.png"
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=37, note='', lookup_dict={'category__name': u'content', 'name': u'self'}).pk, detail=u'FRT', image_file='advideogame/occurrences/38/pictures/DSC03134.JPG')
occurrence.save()

	#Sega Saturn Bootleg Sampler
occurrence = Occurrence.objects.create(created_by=get_userextension("ad"), owner=get_person({'first_name': 'Adrien'}), release=Release.objects.get(pk=43), **{'origin': u'BA', 'blister': False, 'add_date': datetime.datetime(2013, 3, 29, 14, 50, 57, 371487, tzinfo=pytz.utc), 'lastmodif_date': datetime.datetime(2013, 3, 29, 14, 55, 58, 520302, tzinfo=pytz.utc), 'pk': 39, 'purchase_price': 2.6})
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'A', attribute_id=get_corresponding_release_attribute(release=43, note='', lookup_dict={'category__name': u'content', 'name': u'self'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'B', attribute_id=get_corresponding_release_attribute(release=43, note='', lookup_dict={'category__name': u'packaging', 'name': u'jewel box'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'A', attribute_id=get_corresponding_release_attribute(release=43, note='', lookup_dict={'category__name': u'papers', 'name': u'leaflet'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
specific = OccurrenceSpecific.OperationalOcc.objects.create(occurrence=occurrence, **{'working_condition': u'?'})
tto = TagToOccurrence.objects.create(user_creator=get_userextension("ad"), user_occurrence_id=39, occurrence=occurrence)
# Tag and pictures
occurrence.tag_file = "advideogame/occurrences/39/tags/v1.png"
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=43, note='', lookup_dict={'category__name': u'packaging', 'name': u'jewel box'}).pk, detail=u'FRT', image_file='advideogame/occurrences/39/pictures/DSC03095.JPG')
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=43, note='', lookup_dict={'category__name': u'packaging', 'name': u'jewel box'}).pk, detail=u'INS', image_file='advideogame/occurrences/39/pictures/DSC03096.JPG')
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=43, note='', lookup_dict={'category__name': u'papers', 'name': u'leaflet'}).pk, detail=u'FRT', image_file='advideogame/occurrences/39/pictures/DSC03098.JPG')
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=43, note='', lookup_dict={'category__name': u'papers', 'name': u'leaflet'}).pk, detail=u'BCK', image_file='advideogame/occurrences/39/pictures/DSC03097.JPG')
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=43, note='', lookup_dict={'category__name': u'content', 'name': u'self'}).pk, detail=u'FRT', image_file='advideogame/occurrences/39/pictures/DSC03099.JPG')
occurrence.save()

	#Sega Saturn
occurrence = Occurrence.objects.create(created_by=get_userextension("ad"), owner=get_person({'first_name': 'Adrien'}), release=Release.objects.get(pk=42), **{'origin': u'OR', 'blister': False, 'add_date': datetime.datetime(2013, 3, 29, 14, 58, 20, 254776, tzinfo=pytz.utc), 'lastmodif_date': datetime.datetime(2013, 3, 29, 14, 58, 21, 26728, tzinfo=pytz.utc), 'pk': 40, 'purchase_price': None})
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'B', attribute_id=get_corresponding_release_attribute(release=42, note='', lookup_dict={'category__name': u'content', 'name': u'self'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value='0', attribute_id=get_corresponding_release_attribute(release=42, note='', lookup_dict={'category__name': u'packaging', 'name': u'cardboard box'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value='0', attribute_id=get_corresponding_release_attribute(release=42, note='', lookup_dict={'category__name': 'packaging', 'name': u'baggies'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value='0', attribute_id=get_corresponding_release_attribute(release=42, note='', lookup_dict={'category__name': 'packaging', 'name': 'disposable connector protection'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value='0', attribute_id=get_corresponding_release_attribute(release=42, note='', lookup_dict={'category__name': 'packaging', 'name': 'cardboard inlay non-decorative'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value='0', attribute_id=get_corresponding_release_attribute(release=42, note='', lookup_dict={'category__name': u'papers', 'name': u'manual'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value='0', attribute_id=get_corresponding_release_attribute(release=42, note='', lookup_dict={'category__name': u'papers', 'name': u'warranty'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value='1', attribute_id=get_corresponding_release_attribute(release=42, note='', lookup_dict={'category__name': u'content', 'name': u'cord-220v'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value='1', attribute_id=get_corresponding_release_attribute(release=42, note='', lookup_dict={'category__name': u'content', 'name': u'scart'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
OccurrenceComposition.objects.create(from_occurrence=occurrence, to_occurrence=Occurrence.objects.get(pk=38), release_composition=get_corresponding_release_compo({'to_release': 37, 'from_release': 42}))
OccurrenceComposition.objects.create(from_occurrence=occurrence, to_occurrence=Occurrence.objects.get(pk=39), release_composition=get_corresponding_release_compo({'to_release': 43, 'from_release': 42}))
specific = OccurrenceSpecific.OperationalOcc.objects.create(occurrence=occurrence, **{'working_condition': u'Y'})
specific = OccurrenceSpecific.ConsoleOcc.objects.create(occurrence=occurrence, **{'copy_modded': False, 'region_modded': False})
tto = TagToOccurrence.objects.create(user_creator=get_userextension("ad"), user_occurrence_id=40, occurrence=occurrence)
# Tag and pictures
occurrence.tag_file = "advideogame/occurrences/40/tags/v1.png"
OccurrencePicture.objects.create(occurrence=occurrence, detail=u'GRP', image_file='advideogame/occurrences/40/pictures/DSC03129.JPG')
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=42, note='', lookup_dict={'category__name': u'content', 'name': u'self'}).pk, detail=u'FRT', image_file='advideogame/occurrences/40/pictures/DSC03130.JPG')
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=42, note='', lookup_dict={'category__name': u'content', 'name': u'self'}).pk, detail=u'FRT', image_file='advideogame/occurrences/40/pictures/DSC03131.JPG')
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=42, note='', lookup_dict={'category__name': u'content', 'name': u'self'}).pk, detail=u'SID', image_file='advideogame/occurrences/40/pictures/DSC03132.JPG')
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=42, note='', lookup_dict={'category__name': u'content', 'name': u'self'}).pk, detail=u'SID', image_file='advideogame/occurrences/40/pictures/DSC03133.JPG')
occurrence.save()

	#Jet Set Radio
occurrence = Occurrence.objects.create(created_by=get_userextension("ad"), owner=get_person({'first_name': 'Adrien'}), release=Release.objects.get(pk=44), **{'origin': u'BC', 'blister': True, 'add_date': datetime.datetime(2013, 3, 29, 17, 45, 46, 152841, tzinfo=pytz.utc), 'lastmodif_date': datetime.datetime(2013, 3, 29, 17, 45, 47, 395381, tzinfo=pytz.utc), 'pk': 41, 'purchase_price': None})
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'M', attribute_id=get_corresponding_release_attribute(release=44, note='', lookup_dict={'category__name': u'content', 'name': u'self'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'M', attribute_id=get_corresponding_release_attribute(release=44, note='', lookup_dict={'category__name': u'packaging', 'name': u'big-jewel box'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'M', attribute_id=get_corresponding_release_attribute(release=44, note='', lookup_dict={'category__name': u'papers', 'name': 'insert: jewel box'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'M', attribute_id=get_corresponding_release_attribute(release=44, note='', lookup_dict={'category__name': u'papers', 'name': u'manual'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
specific = OccurrenceSpecific.OperationalOcc.objects.create(occurrence=occurrence, **{'working_condition': u'Y'})
tto = TagToOccurrence.objects.create(user_creator=get_userextension("ad"), user_occurrence_id=41, occurrence=occurrence)
# Tag and pictures
occurrence.tag_file = "advideogame/occurrences/41/tags/v1.png"
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=44, note='', lookup_dict={'category__name': u'packaging', 'name': u'big-jewel box'}).pk, detail=u'SLB', image_file='advideogame/occurrences/41/pictures/DSC03150.JPG')
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=44, note='', lookup_dict={'category__name': u'packaging', 'name': u'big-jewel box'}).pk, detail=u'FRT', image_file='advideogame/occurrences/41/pictures/DSC03151.JPG')
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=44, note='', lookup_dict={'category__name': u'packaging', 'name': u'big-jewel box'}).pk, detail=u'BCK', image_file='advideogame/occurrences/41/pictures/DSC03152.JPG')
occurrence.save()

	#Jet Set Radio
occurrence = Occurrence.objects.create(created_by=get_userextension("ad"), owner=get_person({'first_name': 'Adrien'}), release=Release.objects.get(pk=44), **{'origin': u'GF', 'blister': False, 'add_date': datetime.datetime(2013, 3, 29, 17, 47, 50, 841518, tzinfo=pytz.utc), 'lastmodif_date': datetime.datetime(2013, 3, 29, 17, 48, 3, 693294, tzinfo=pytz.utc), 'pk': 42, 'purchase_price': None})
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'C', attribute_id=get_corresponding_release_attribute(release=44, note='', lookup_dict={'category__name': u'content', 'name': u'self'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'D', attribute_id=get_corresponding_release_attribute(release=44, note='', lookup_dict={'category__name': u'packaging', 'name': u'big-jewel box'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'B', attribute_id=get_corresponding_release_attribute(release=44, note='', lookup_dict={'category__name': u'papers', 'name': 'insert: jewel box'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value='0', attribute_id=get_corresponding_release_attribute(release=44, note='', lookup_dict={'category__name': u'papers', 'name': u'manual'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
specific = OccurrenceSpecific.OperationalOcc.objects.create(occurrence=occurrence, **{'working_condition': u'Y'})
tto = TagToOccurrence.objects.create(user_creator=get_userextension("ad"), user_occurrence_id=42, occurrence=occurrence)
# Tag and pictures
occurrence.tag_file = "advideogame/occurrences/42/tags/v1.png"
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=44, note='', lookup_dict={'category__name': u'packaging', 'name': u'big-jewel box'}).pk, detail=u'FRT', image_file='advideogame/occurrences/42/pictures/DSC03141.JPG')
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=44, note='', lookup_dict={'category__name': u'packaging', 'name': u'big-jewel box'}).pk, detail=u'BCK', image_file='advideogame/occurrences/42/pictures/DSC03142.JPG')
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=44, note='', lookup_dict={'category__name': u'packaging', 'name': u'big-jewel box'}).pk, detail=u'SLB', image_file='advideogame/occurrences/42/pictures/DSC03140.JPG')
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=44, note='', lookup_dict={'category__name': u'content', 'name': u'self'}).pk, detail=u'FRT', image_file='advideogame/occurrences/42/pictures/DSC03143.JPG')
occurrence.save()

	#Sega Bass Fishing
occurrence = Occurrence.objects.create(created_by=get_userextension("ad"), owner=get_person({'first_name': 'Adrien'}), release=Release.objects.get(pk=45), **{'origin': u'BC', 'blister': True, 'add_date': datetime.datetime(2013, 3, 29, 17, 49, 37, 185063, tzinfo=pytz.utc), 'lastmodif_date': datetime.datetime(2013, 3, 29, 17, 49, 38, 753264, tzinfo=pytz.utc), 'pk': 43, 'purchase_price': None})
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'M', attribute_id=get_corresponding_release_attribute(release=45, note='', lookup_dict={'category__name': u'content', 'name': u'self'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'M', attribute_id=get_corresponding_release_attribute(release=45, note='', lookup_dict={'category__name': u'packaging', 'name': u'big-jewel box'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'M', attribute_id=get_corresponding_release_attribute(release=45, note='', lookup_dict={'category__name': u'papers', 'name': 'insert: jewel box'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'M', attribute_id=get_corresponding_release_attribute(release=45, note='', lookup_dict={'category__name': u'papers', 'name': u'manual'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
specific = OccurrenceSpecific.OperationalOcc.objects.create(occurrence=occurrence, **{'working_condition': u'Y'})
tto = TagToOccurrence.objects.create(user_creator=get_userextension("ad"), user_occurrence_id=43, occurrence=occurrence)
# Tag and pictures
occurrence.tag_file = "advideogame/occurrences/43/tags/v1.png"
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=45, note='', lookup_dict={'category__name': u'packaging', 'name': u'big-jewel box'}).pk, detail=u'FRT', image_file='advideogame/occurrences/43/pictures/DSC03145.JPG')
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=45, note='', lookup_dict={'category__name': u'packaging', 'name': u'big-jewel box'}).pk, detail=u'BCK', image_file='advideogame/occurrences/43/pictures/DSC03146.JPG')
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=45, note='', lookup_dict={'category__name': u'packaging', 'name': u'big-jewel box'}).pk, detail=u'SLB', image_file='advideogame/occurrences/43/pictures/DSC03144.JPG')
occurrence.save()

	#Crazy Taxi
occurrence = Occurrence.objects.create(created_by=get_userextension("ad"), owner=get_person({'first_name': 'Adrien'}), release=Release.objects.get(pk=46), **{'origin': u'BC', 'blister': True, 'add_date': datetime.datetime(2013, 3, 29, 17, 50, 38, 161600, tzinfo=pytz.utc), 'lastmodif_date': datetime.datetime(2013, 3, 29, 17, 50, 45, 35898, tzinfo=pytz.utc), 'pk': 44, 'purchase_price': None})
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'M', attribute_id=get_corresponding_release_attribute(release=46, note='', lookup_dict={'category__name': u'content', 'name': u'self'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'M', attribute_id=get_corresponding_release_attribute(release=46, note='', lookup_dict={'category__name': u'packaging', 'name': u'big-jewel box'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'M', attribute_id=get_corresponding_release_attribute(release=46, note='', lookup_dict={'category__name': u'papers', 'name': 'insert: jewel box'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'M', attribute_id=get_corresponding_release_attribute(release=46, note='', lookup_dict={'category__name': u'papers', 'name': u'manual'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
specific = OccurrenceSpecific.OperationalOcc.objects.create(occurrence=occurrence, **{'working_condition': u'Y'})
tto = TagToOccurrence.objects.create(user_creator=get_userextension("ad"), user_occurrence_id=44, occurrence=occurrence)
# Tag and pictures
occurrence.tag_file = "advideogame/occurrences/44/tags/v1.png"
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=46, note='', lookup_dict={'category__name': u'packaging', 'name': u'big-jewel box'}).pk, detail=u'FRT', image_file='advideogame/occurrences/44/pictures/DSC03148.JPG')
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=46, note='', lookup_dict={'category__name': u'packaging', 'name': u'big-jewel box'}).pk, detail=u'BCK', image_file='advideogame/occurrences/44/pictures/DSC03149.JPG')
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=46, note='', lookup_dict={'category__name': u'packaging', 'name': u'big-jewel box'}).pk, detail=u'SLB', image_file='advideogame/occurrences/44/pictures/DSC03147.JPG')
occurrence.save()

	#Confidential Mission
occurrence = Occurrence.objects.create(created_by=get_userextension("ad"), owner=get_person({'first_name': 'Adrien'}), release=Release.objects.get(pk=47), **{'origin': u'BC', 'blister': True, 'add_date': datetime.datetime(2013, 3, 29, 17, 51, 30, 124301, tzinfo=pytz.utc), 'lastmodif_date': datetime.datetime(2013, 3, 29, 17, 51, 31, 262611, tzinfo=pytz.utc), 'pk': 45, 'purchase_price': None})
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'M', attribute_id=get_corresponding_release_attribute(release=47, note='', lookup_dict={'category__name': u'content', 'name': u'self'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'M', attribute_id=get_corresponding_release_attribute(release=47, note='', lookup_dict={'category__name': u'packaging', 'name': u'big-jewel box'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'M', attribute_id=get_corresponding_release_attribute(release=47, note='', lookup_dict={'category__name': u'papers', 'name': 'insert: jewel box'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'M', attribute_id=get_corresponding_release_attribute(release=47, note='', lookup_dict={'category__name': u'papers', 'name': u'manual'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
specific = OccurrenceSpecific.OperationalOcc.objects.create(occurrence=occurrence, **{'working_condition': u'Y'})
tto = TagToOccurrence.objects.create(user_creator=get_userextension("ad"), user_occurrence_id=45, occurrence=occurrence)
# Tag and pictures
occurrence.tag_file = "advideogame/occurrences/45/tags/v1.png"
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=47, note='', lookup_dict={'category__name': u'packaging', 'name': u'big-jewel box'}).pk, detail=u'FRT', image_file='advideogame/occurrences/45/pictures/DSC03154.JPG')
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=47, note='', lookup_dict={'category__name': u'packaging', 'name': u'big-jewel box'}).pk, detail=u'BCK', image_file='advideogame/occurrences/45/pictures/DSC03155.JPG')
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=47, note='', lookup_dict={'category__name': u'packaging', 'name': u'big-jewel box'}).pk, detail=u'SLB', image_file='advideogame/occurrences/45/pictures/DSC03153.JPG')
occurrence.save()

	#Skies of Arcadia
occurrence = Occurrence.objects.create(created_by=get_userextension("ad"), owner=get_person({'first_name': 'Adrien'}), release=Release.objects.get(pk=48), **{'origin': u'GF', 'blister': False, 'add_date': datetime.datetime(2013, 3, 29, 17, 53, 10, 293797, tzinfo=pytz.utc), 'lastmodif_date': datetime.datetime(2013, 3, 29, 17, 53, 24, 220748, tzinfo=pytz.utc), 'pk': 46, 'purchase_price': None})
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'A', attribute_id=get_corresponding_release_attribute(release=48, note='', lookup_dict={'category__name': u'content', 'name': u'self'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'B', attribute_id=get_corresponding_release_attribute(release=48, note='', lookup_dict={'category__name': u'packaging', 'name': u'big-jewel box'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'A', attribute_id=get_corresponding_release_attribute(release=48, note='', lookup_dict={'category__name': u'papers', 'name': 'insert: jewel box'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'A', attribute_id=get_corresponding_release_attribute(release=48, note='', lookup_dict={'category__name': u'papers', 'name': u'manual'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
specific = OccurrenceSpecific.OperationalOcc.objects.create(occurrence=occurrence, **{'working_condition': u'Y'})
tto = TagToOccurrence.objects.create(user_creator=get_userextension("ad"), user_occurrence_id=46, occurrence=occurrence)
# Tag and pictures
occurrence.tag_file = "advideogame/occurrences/46/tags/v1.png"
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=48, note='', lookup_dict={'category__name': u'packaging', 'name': u'big-jewel box'}).pk, detail=u'FRT', image_file='advideogame/occurrences/46/pictures/DSC03157.JPG')
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=48, note='', lookup_dict={'category__name': u'packaging', 'name': u'big-jewel box'}).pk, detail=u'BCK', image_file='advideogame/occurrences/46/pictures/DSC03158.JPG')
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=48, note='', lookup_dict={'category__name': u'packaging', 'name': u'big-jewel box'}).pk, detail=u'SLB', image_file='advideogame/occurrences/46/pictures/DSC03156.JPG')
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=48, note='', lookup_dict={'category__name': u'packaging', 'name': u'big-jewel box'}).pk, detail=u'INS', image_file='advideogame/occurrences/46/pictures/DSC03161.JPG')
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=48, note='', lookup_dict={'category__name': u'packaging', 'name': u'big-jewel box'}).pk, detail=u'INS', image_file='advideogame/occurrences/46/pictures/DSC03160.JPG')
occurrence.save()

	#Capcom vs. SNK: Millennium Fight 2000
occurrence = Occurrence.objects.create(created_by=get_userextension("ad"), owner=get_person({'first_name': 'Adrien'}), release=Release.objects.get(pk=49), **{'origin': u'BU', 'blister': False, 'add_date': datetime.datetime(2013, 3, 29, 17, 55, 7, 241539, tzinfo=pytz.utc), 'lastmodif_date': datetime.datetime(2013, 3, 29, 17, 56, 48, 840528, tzinfo=pytz.utc), 'pk': 47, 'purchase_price': 15.0})
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'A', attribute_id=get_corresponding_release_attribute(release=49, note='', lookup_dict={'category__name': u'content', 'name': u'self'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'B', attribute_id=get_corresponding_release_attribute(release=49, note='', lookup_dict={'category__name': u'packaging', 'name': u'jewel box'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'A', attribute_id=get_corresponding_release_attribute(release=49, note='', lookup_dict={'category__name': u'papers', 'name': 'insert: jewel box'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'A', attribute_id=get_corresponding_release_attribute(release=49, note='', lookup_dict={'category__name': u'papers', 'name': u'leaflet'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'A', attribute_id=get_corresponding_release_attribute(release=49, note='', lookup_dict={'category__name': u'papers', 'name': u'manual'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'A', attribute_id=get_corresponding_release_attribute(release=49, note='', lookup_dict={'category__name': u'papers', 'name': u'registration card'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
specific = OccurrenceSpecific.OperationalOcc.objects.create(occurrence=occurrence, **{'working_condition': u'Y'})
tto = TagToOccurrence.objects.create(user_creator=get_userextension("ad"), user_occurrence_id=47, occurrence=occurrence)
# Tag and pictures
occurrence.tag_file = "advideogame/occurrences/47/tags/v1.png"
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=49, note='', lookup_dict={'category__name': u'packaging', 'name': u'jewel box'}).pk, detail=u'FRT', image_file='advideogame/occurrences/47/pictures/DSC03168.JPG')
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=49, note='', lookup_dict={'category__name': u'packaging', 'name': u'jewel box'}).pk, detail=u'BCK', image_file='advideogame/occurrences/47/pictures/DSC03169.JPG')
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=49, note='', lookup_dict={'category__name': u'packaging', 'name': u'jewel box'}).pk, detail=u'SLB', image_file='advideogame/occurrences/47/pictures/DSC03167.JPG')
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=49, note='', lookup_dict={'category__name': u'packaging', 'name': u'jewel box'}).pk, detail=u'SLB', image_file='advideogame/occurrences/47/pictures/DSC03166.JPG')
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=49, note='', lookup_dict={'category__name': u'packaging', 'name': u'jewel box'}).pk, detail=u'INS', image_file='advideogame/occurrences/47/pictures/DSC03170.JPG')
OccurrencePicture.objects.create(occurrence=occurrence, detail=u'GRP', image_file='advideogame/occurrences/47/pictures/DSC03171.JPG')
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=49, note='', lookup_dict={'category__name': u'papers', 'name': u'manual'}).pk, detail=u'INS', image_file='advideogame/occurrences/47/pictures/DSC03172.JPG')
occurrence.save()

	#FIFA 98
occurrence = Occurrence.objects.create(created_by=get_userextension("ad"), owner=get_person({'first_name': 'Adrien'}), release=Release.objects.get(pk=50), **{'origin': u'BC', 'blister': True, 'add_date': datetime.datetime(2013, 3, 29, 17, 58, 1, 757802, tzinfo=pytz.utc), 'lastmodif_date': datetime.datetime(2013, 3, 29, 17, 58, 3, 516836, tzinfo=pytz.utc), 'pk': 48, 'purchase_price': 3.0})
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'M', attribute_id=get_corresponding_release_attribute(release=50, note='', lookup_dict={'category__name': u'content', 'name': u'self'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'A', attribute_id=get_corresponding_release_attribute(release=50, note='', lookup_dict={'category__name': u'packaging', 'name': u'cardboard box'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'M', attribute_id=get_corresponding_release_attribute(release=50, note='', lookup_dict={'category__name': u'papers', 'name': u'manual'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
specific = OccurrenceSpecific.OperationalOcc.objects.create(occurrence=occurrence, **{'working_condition': u'Y'})
tto = TagToOccurrence.objects.create(user_creator=get_userextension("ad"), user_occurrence_id=48, occurrence=occurrence)
# Tag and pictures
occurrence.tag_file = "advideogame/occurrences/48/tags/v1.png"
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=50, note='', lookup_dict={'category__name': u'packaging', 'name': u'cardboard box'}).pk, detail=u'FRT', image_file='advideogame/occurrences/48/pictures/DSC03174.JPG')
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=50, note='', lookup_dict={'category__name': u'packaging', 'name': u'cardboard box'}).pk, detail=u'BCK', image_file='advideogame/occurrences/48/pictures/DSC03175.JPG')
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=50, note='', lookup_dict={'category__name': u'packaging', 'name': u'cardboard box'}).pk, detail=u'SLB', image_file='advideogame/occurrences/48/pictures/DSC03173.JPG')
occurrence.save()

	#Dreamcast Vibration Pack
occurrence = Occurrence.objects.create(created_by=get_userextension("ad"), owner=get_person({'first_name': 'Adrien'}), release=Release.objects.get(pk=51), **{'origin': u'OR', 'blister': False, 'add_date': datetime.datetime(2013, 3, 29, 18, 9, 28, 216670, tzinfo=pytz.utc), 'lastmodif_date': datetime.datetime(2013, 3, 29, 18, 9, 28, 572280, tzinfo=pytz.utc), 'pk': 49, 'purchase_price': None})
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'A', attribute_id=get_corresponding_release_attribute(release=51, note='', lookup_dict={'category__name': u'content', 'name': u'self'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
specific = OccurrenceSpecific.OperationalOcc.objects.create(occurrence=occurrence, **{'working_condition': u'Y'})
tto = TagToOccurrence.objects.create(user_creator=get_userextension("ad"), user_occurrence_id=49, occurrence=occurrence)
# Tag and pictures
occurrence.tag_file = "advideogame/occurrences/49/tags/v1.png"
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=51, note='', lookup_dict={'category__name': u'content', 'name': u'self'}).pk, detail=u'FRT', image_file='advideogame/occurrences/49/pictures/DSC03176.JPG')
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=51, note='', lookup_dict={'category__name': u'content', 'name': u'self'}).pk, detail=u'BCK', image_file='advideogame/occurrences/49/pictures/DSC03177.JPG')
occurrence.save()

	#Visual Memory Unit
occurrence = Occurrence.objects.create(created_by=get_userextension("ad"), owner=get_person({'first_name': 'Adrien'}), release=Release.objects.get(pk=52), **{'origin': u'OR', 'blister': False, 'add_date': datetime.datetime(2013, 3, 29, 18, 10, 39, 443996, tzinfo=pytz.utc), 'lastmodif_date': datetime.datetime(2013, 3, 29, 18, 30, 8, 50198, tzinfo=pytz.utc), 'pk': 50, 'purchase_price': None})
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'A', attribute_id=get_corresponding_release_attribute(release=52, note='', lookup_dict={'category__name': u'content', 'name': u'self'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value='A', attribute_id=get_corresponding_release_attribute(release=52, note='', lookup_dict={'category__name': u'content', 'name': 'intrinsic connector cap'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'B', attribute_id=get_corresponding_release_attribute(release=52, note='', lookup_dict={'category__name': u'packaging', 'name': u'cardboard box'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'A', attribute_id=get_corresponding_release_attribute(release=52, note='', lookup_dict={'category__name': 'packaging', 'name': 'cardboard inlay non-decorative'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'A', attribute_id=get_corresponding_release_attribute(release=52, note='', lookup_dict={'category__name': u'papers', 'name': u'manual'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
specific = OccurrenceSpecific.OperationalOcc.objects.create(occurrence=occurrence, **{'working_condition': u'Y'})
specific = OccurrenceSpecific.ConsoleOcc.objects.create(occurrence=occurrence, **{'copy_modded': False, 'region_modded': False})
tto = TagToOccurrence.objects.create(user_creator=get_userextension("ad"), user_occurrence_id=50, occurrence=occurrence)
# Tag and pictures
occurrence.tag_file = "advideogame/occurrences/50/tags/v1.png"
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=52, note='', lookup_dict={'category__name': u'packaging', 'name': u'cardboard box'}).pk, detail=u'FRT', image_file='advideogame/occurrences/50/pictures/DSC03184.JPG')
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=52, note='', lookup_dict={'category__name': u'packaging', 'name': u'cardboard box'}).pk, detail=u'BCK', image_file='advideogame/occurrences/50/pictures/DSC03182.JPG')
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=52, note='', lookup_dict={'category__name': u'packaging', 'name': u'cardboard box'}).pk, detail=u'SLB', image_file='advideogame/occurrences/50/pictures/DSC03180.JPG')
OccurrencePicture.objects.create(occurrence=occurrence, detail=u'GRP', image_file='advideogame/occurrences/50/pictures/DSC03183.JPG')
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=52, note='', lookup_dict={'category__name': u'packaging', 'name': u'cardboard box'}).pk, detail=u'FRT', image_file='advideogame/occurrences/50/pictures/DSC03181.JPG')
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=52, note='', lookup_dict={'category__name': u'content', 'name': u'self'}).pk, detail=u'FRT', image_file='advideogame/occurrences/50/pictures/DSC03178.JPG')
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=52, note='', lookup_dict={'category__name': u'content', 'name': u'self'}).pk, detail=u'BCK', image_file='advideogame/occurrences/50/pictures/DSC03179.JPG')
occurrence.save()

	#Dreamkey
occurrence = Occurrence.objects.create(created_by=get_userextension("ad"), owner=get_person({'first_name': 'Adrien'}), release=Release.objects.get(pk=54), **{'origin': u'OR', 'blister': False, 'add_date': datetime.datetime(2013, 3, 29, 18, 12, 18, 489514, tzinfo=pytz.utc), 'lastmodif_date': datetime.datetime(2013, 3, 29, 18, 12, 18, 850152, tzinfo=pytz.utc), 'pk': 51, 'purchase_price': None})
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'A', attribute_id=get_corresponding_release_attribute(release=54, note='', lookup_dict={'category__name': u'content', 'name': u'self'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'B', attribute_id=get_corresponding_release_attribute(release=54, note='', lookup_dict={'category__name': u'packaging', 'name': u'jewel box'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'A', attribute_id=get_corresponding_release_attribute(release=54, note='', lookup_dict={'category__name': u'papers', 'name': 'insert: jewel box'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'A', attribute_id=get_corresponding_release_attribute(release=54, note='', lookup_dict={'category__name': u'papers', 'name': u'manual'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
specific = OccurrenceSpecific.OperationalOcc.objects.create(occurrence=occurrence, **{'working_condition': u'?'})
tto = TagToOccurrence.objects.create(user_creator=get_userextension("ad"), user_occurrence_id=51, occurrence=occurrence)
# Tag and pictures
occurrence.tag_file = "advideogame/occurrences/51/tags/v1.png"
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=54, note='', lookup_dict={'category__name': u'packaging', 'name': u'jewel box'}).pk, detail=u'FRT', image_file='advideogame/occurrences/51/pictures/DSC03162.JPG')
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=54, note='', lookup_dict={'category__name': u'packaging', 'name': u'jewel box'}).pk, detail=u'BCK', image_file='advideogame/occurrences/51/pictures/DSC03163.JPG')
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=54, note='', lookup_dict={'category__name': u'packaging', 'name': u'jewel box'}).pk, detail=u'INS', image_file='advideogame/occurrences/51/pictures/DSC03164.JPG')
occurrence.save()

	#Dream On Collection
occurrence = Occurrence.objects.create(created_by=get_userextension("ad"), owner=get_person({'first_name': 'Adrien'}), release=Release.objects.get(pk=57), **{'origin': u'OR', 'blister': False, 'add_date': datetime.datetime(2013, 3, 29, 18, 19, 47, 859719, tzinfo=pytz.utc), 'lastmodif_date': datetime.datetime(2013, 3, 29, 18, 19, 48, 182788, tzinfo=pytz.utc), 'pk': 52, 'purchase_price': None})
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'A', attribute_id=get_corresponding_release_attribute(release=57, note='', lookup_dict={'category__name': u'content', 'name': u'self'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'B', attribute_id=get_corresponding_release_attribute(release=57, note='', lookup_dict={'category__name': u'packaging', 'name': u'jewel box'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
specific = OccurrenceSpecific.OperationalOcc.objects.create(occurrence=occurrence, **{'working_condition': u'Y'})
tto = TagToOccurrence.objects.create(user_creator=get_userextension("ad"), user_occurrence_id=52, occurrence=occurrence)
# Tag and pictures
occurrence.tag_file = "advideogame/occurrences/52/tags/v1.png"
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=57, note='', lookup_dict={'category__name': u'packaging', 'name': u'jewel box'}).pk, detail=u'FRT', image_file='advideogame/occurrences/52/pictures/DSC03165.JPG')
occurrence.save()

	#Visual Memory Unit
occurrence = Occurrence.objects.create(created_by=get_userextension("ad"), owner=get_person({'first_name': 'Adrien'}), release=Release.objects.get(pk=58), **{'origin': u'BC', 'blister': False, 'add_date': datetime.datetime(2013, 3, 29, 18, 28, 59, 82995, tzinfo=pytz.utc), 'lastmodif_date': datetime.datetime(2013, 3, 29, 18, 28, 59, 436256, tzinfo=pytz.utc), 'pk': 53, 'purchase_price': None})
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'B', attribute_id=get_corresponding_release_attribute(release=58, note='', lookup_dict={'category__name': u'content', 'name': u'self'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value='0', attribute_id=get_corresponding_release_attribute(release=58, note='', lookup_dict={'category__name': u'content', 'name': 'intrinsic connector cap'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
specific = OccurrenceSpecific.OperationalOcc.objects.create(occurrence=occurrence, **{'working_condition': u'?'})
specific = OccurrenceSpecific.ConsoleOcc.objects.create(occurrence=occurrence, **{'copy_modded': False, 'region_modded': False})
tto = TagToOccurrence.objects.create(user_creator=get_userextension("ad"), user_occurrence_id=53, occurrence=occurrence)
# Tag and pictures
occurrence.tag_file = "advideogame/occurrences/53/tags/v1.png"
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=58, note='', lookup_dict={'category__name': u'content', 'name': u'self'}).pk, detail=u'FRT', image_file='advideogame/occurrences/53/pictures/DSC03190.JPG')
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=58, note='', lookup_dict={'category__name': u'content', 'name': u'self'}).pk, detail=u'BCK', image_file='advideogame/occurrences/53/pictures/DSC03179.JPG')
occurrence.save()

	#Dreamcast Controller
occurrence = Occurrence.objects.create(created_by=get_userextension("ad"), owner=get_person({'first_name': 'Adrien'}), release=Release.objects.get(pk=55), **{'origin': u'OR', 'blister': False, 'add_date': datetime.datetime(2013, 3, 29, 18, 31, 2, 154860, tzinfo=pytz.utc), 'lastmodif_date': datetime.datetime(2013, 3, 29, 18, 31, 3, 908680, tzinfo=pytz.utc), 'pk': 54, 'purchase_price': None})
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'B', attribute_id=get_corresponding_release_attribute(release=55, note='', lookup_dict={'category__name': u'content', 'name': u'self'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
specific = OccurrenceSpecific.OperationalOcc.objects.create(occurrence=occurrence, **{'working_condition': u'Y'})
tto = TagToOccurrence.objects.create(user_creator=get_userextension("ad"), user_occurrence_id=54, occurrence=occurrence)
# Tag and pictures
occurrence.tag_file = "advideogame/occurrences/54/tags/v1.png"
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=55, note='', lookup_dict={'category__name': u'content', 'name': u'self'}).pk, detail=u'FRT', image_file='advideogame/occurrences/54/pictures/DSC03196.JPG')
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=55, note='', lookup_dict={'category__name': u'content', 'name': u'self'}).pk, detail=u'BCK', image_file='advideogame/occurrences/54/pictures/DSC03197.JPG')
occurrence.save()

	#Dreamcast Controller
occurrence = Occurrence.objects.create(created_by=get_userextension("ad"), owner=get_person({'first_name': 'Adrien'}), release=Release.objects.get(pk=55), **{'origin': u'BC', 'blister': False, 'add_date': datetime.datetime(2013, 3, 29, 18, 31, 56, 651851, tzinfo=pytz.utc), 'lastmodif_date': datetime.datetime(2013, 3, 30, 3, 12, 9, 459153, tzinfo=pytz.utc), 'pk': 55, 'purchase_price': None})
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'B', attribute_id=get_corresponding_release_attribute(release=55, note='', lookup_dict={'category__name': u'content', 'name': u'self'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
specific = OccurrenceSpecific.OperationalOcc.objects.create(occurrence=occurrence, **{'working_condition': u'?'})
tto = TagToOccurrence.objects.create(user_creator=get_userextension("ad"), user_occurrence_id=55, occurrence=occurrence)
# Tag and pictures
occurrence.tag_file = "advideogame/occurrences/55/tags/v1.png"
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=55, note='', lookup_dict={'category__name': u'content', 'name': u'self'}).pk, detail=u'FRT', image_file='advideogame/occurrences/55/pictures/DSC03192_1.JPG')
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=55, note='', lookup_dict={'category__name': u'content', 'name': u'self'}).pk, detail=u'BCK', image_file='advideogame/occurrences/55/pictures/DSC03193.JPG')
occurrence.save()

	#Quantum Fighterpad
occurrence = Occurrence.objects.create(created_by=get_userextension("ad"), owner=get_person({'first_name': 'Adrien'}), release=Release.objects.get(pk=56), **{'origin': u'OR', 'blister': False, 'add_date': datetime.datetime(2013, 3, 29, 18, 32, 47, 31695, tzinfo=pytz.utc), 'lastmodif_date': datetime.datetime(2013, 3, 29, 18, 32, 47, 377819, tzinfo=pytz.utc), 'pk': 56, 'purchase_price': None})
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'B', attribute_id=get_corresponding_release_attribute(release=56, note='', lookup_dict={'category__name': u'content', 'name': u'self'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
specific = OccurrenceSpecific.OperationalOcc.objects.create(occurrence=occurrence, **{'working_condition': u'Y'})
tto = TagToOccurrence.objects.create(user_creator=get_userextension("ad"), user_occurrence_id=56, occurrence=occurrence)
# Tag and pictures
occurrence.tag_file = "advideogame/occurrences/56/tags/v1.png"
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=56, note='', lookup_dict={'category__name': u'content', 'name': u'self'}).pk, detail=u'FRT', image_file='advideogame/occurrences/56/pictures/DSC03194.JPG')
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=56, note='', lookup_dict={'category__name': u'content', 'name': u'self'}).pk, detail=u'BCK', image_file='advideogame/occurrences/56/pictures/DSC03195.JPG')
occurrence.save()

	#Sega Dreamcast
occurrence = Occurrence.objects.create(created_by=get_userextension("ad"), owner=get_person({'first_name': 'Adrien'}), release=Release.objects.get(pk=53), **{'origin': u'OR', 'blister': False, 'add_date': datetime.datetime(2013, 3, 29, 18, 36, 28, 945847, tzinfo=pytz.utc), 'lastmodif_date': datetime.datetime(2013, 3, 29, 18, 37, 24, 505325, tzinfo=pytz.utc), 'pk': 57, 'purchase_price': None})
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'A', attribute_id=get_corresponding_release_attribute(release=53, note='', lookup_dict={'category__name': u'content', 'name': u'self'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'A', attribute_id=get_corresponding_release_attribute(release=53, note='', lookup_dict={'category__name': u'packaging', 'name': u'cardboard box'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value='0', attribute_id=get_corresponding_release_attribute(release=53, note='', lookup_dict={'category__name': 'packaging', 'name': u'baggies'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
inlay = OccurrenceAnyAttribute(occurrence=occurrence, value=u'C', attribute_id=get_corresponding_release_attribute(release=53, note='', lookup_dict={'category__name': 'packaging', 'name': 'cardboard inlay non-decorative'}).pk, attribute_type=ReleaseAttribute_contentype)
occurrence.attributes.add(inlay, bulk=False)
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value='0', attribute_id=get_corresponding_release_attribute(release=53, note='', lookup_dict={'category__name': u'papers', 'name': u'manual'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value='0', attribute_id=get_corresponding_release_attribute(release=53, note='', lookup_dict={'category__name': u'papers', 'name': u'warranty'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value='1', attribute_id=get_corresponding_release_attribute(release=53, note='', lookup_dict={'category__name': u'content', 'name': u'cord-220v'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value='1', attribute_id=get_corresponding_release_attribute(release=53, note='', lookup_dict={'category__name': u'content', 'name': u'scart'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
OccurrenceComposition.objects.create(from_occurrence=occurrence, to_occurrence=Occurrence.objects.get(pk=54), release_composition=get_corresponding_release_compo({'to_release': 55, 'from_release': 53}))
OccurrenceComposition.objects.create(from_occurrence=occurrence, to_occurrence=Occurrence.objects.get(pk=51), release_composition=get_corresponding_release_compo({'to_release': 54, 'from_release': 53}))
OccurrenceComposition.objects.create(from_occurrence=occurrence, to_occurrence=Occurrence.objects.get(pk=52), release_composition=get_corresponding_release_compo({'to_release': 57, 'from_release': 53}))
specific = OccurrenceSpecific.OperationalOcc.objects.create(occurrence=occurrence, **{'working_condition': u'Y'})
specific = OccurrenceSpecific.ConsoleOcc.objects.create(occurrence=occurrence, **{'copy_modded': False, 'region_modded': False})
tto = TagToOccurrence.objects.create(user_creator=get_userextension("ad"), user_occurrence_id=57, occurrence=occurrence)
# Tag and pictures
occurrence.tag_file = "advideogame/occurrences/57/tags/v1.png"
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=53, note='', lookup_dict={'category__name': u'packaging', 'name': u'cardboard box'}).pk, detail=u'FRT', image_file='advideogame/occurrences/57/pictures/DSC03198.JPG')
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=53, note='', lookup_dict={'category__name': u'packaging', 'name': u'cardboard box'}).pk, detail=u'BCK', image_file='advideogame/occurrences/57/pictures/DSC03200.JPG')
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=53, note='', lookup_dict={'category__name': u'packaging', 'name': u'cardboard box'}).pk, detail=u'SID', image_file='advideogame/occurrences/57/pictures/DSC03199.JPG')
OccurrencePicture.objects.create(occurrence=occurrence, detail=u'GRP', image_file='advideogame/occurrences/57/pictures/DSC03202.JPG')
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=53, note='', lookup_dict={'category__name': u'content', 'name': u'self'}).pk, detail=u'FRT', image_file='advideogame/occurrences/57/pictures/DSC03203.JPG')
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=53, note='', lookup_dict={'category__name': u'content', 'name': u'self'}).pk, detail=u'SID', image_file='advideogame/occurrences/57/pictures/DSC03204.JPG')
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=53, note='', lookup_dict={'category__name': u'content', 'name': u'self'}).pk, detail=u'BCK', image_file='advideogame/occurrences/57/pictures/DSC03205.JPG')
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=53, note='', lookup_dict={'category__name': u'content', 'name': u'self'}).pk, detail=u'SID', image_file='advideogame/occurrences/57/pictures/DSC03206.JPG')
occurrence.save()
OccurrenceAnyAttributeDefect.objects.create(occurrence_any_attribute=inlay, defect_description="missing one inlay")

	#The Lion King
occurrence = Occurrence.objects.create(created_by=get_userextension("ad"), owner=get_person({'first_name': 'Adrien'}), release=Release.objects.get(pk=59), **{'origin': u'BC', 'blister': False, 'add_date': datetime.datetime(2013, 3, 30, 2, 56, 53, 286534, tzinfo=pytz.utc), 'lastmodif_date': datetime.datetime(2013, 3, 30, 2, 56, 53, 644417, tzinfo=pytz.utc), 'pk': 58, 'purchase_price': 1.0})
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'A', attribute_id=get_corresponding_release_attribute(release=59, note='', lookup_dict={'category__name': u'content', 'name': u'self'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
specific = OccurrenceSpecific.OperationalOcc.objects.create(occurrence=occurrence, **{'working_condition': u'?'})
tto = TagToOccurrence.objects.create(user_creator=get_userextension("ad"), user_occurrence_id=58, occurrence=occurrence)
# Tag and pictures
occurrence.tag_file = "advideogame/occurrences/58/tags/v1.png"
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=59, note='', lookup_dict={'category__name': u'content', 'name': u'self'}).pk, detail=u'FRT', image_file='advideogame/occurrences/58/pictures/DSC03186.JPG')
occurrence.save()

	#Disney's Aladdin (SIMS)
occurrence = Occurrence.objects.create(created_by=get_userextension("ad"), owner=get_person({'first_name': 'Adrien'}), release=Release.objects.get(pk=60), **{'origin': u'BC', 'blister': False, 'add_date': datetime.datetime(2013, 3, 30, 2, 57, 24, 335161, tzinfo=pytz.utc), 'lastmodif_date': datetime.datetime(2013, 3, 30, 2, 57, 25, 529886, tzinfo=pytz.utc), 'pk': 59, 'purchase_price': 1.0})
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'A', attribute_id=get_corresponding_release_attribute(release=60, note='', lookup_dict={'category__name': u'content', 'name': u'self'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
specific = OccurrenceSpecific.OperationalOcc.objects.create(occurrence=occurrence, **{'working_condition': u'?'})
tto = TagToOccurrence.objects.create(user_creator=get_userextension("ad"), user_occurrence_id=59, occurrence=occurrence)
# Tag and pictures
occurrence.tag_file = "advideogame/occurrences/59/tags/v1.png"
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=60, note='', lookup_dict={'category__name': u'content', 'name': u'self'}).pk, detail=u'FRT', image_file='advideogame/occurrences/59/pictures/DSC03187.JPG')
occurrence.save()

	#Sonic the Hedgehog 2 (8-bit)
occurrence = Occurrence.objects.create(created_by=get_userextension("ad"), owner=get_person({'first_name': 'Adrien'}), release=Release.objects.get(pk=61), **{'origin': u'BC', 'blister': False, 'add_date': datetime.datetime(2013, 3, 30, 2, 58, 8, 183240, tzinfo=pytz.utc), 'lastmodif_date': datetime.datetime(2013, 3, 30, 2, 58, 8, 612387, tzinfo=pytz.utc), 'pk': 60, 'purchase_price': 1.0})
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'A', attribute_id=get_corresponding_release_attribute(release=61, note='', lookup_dict={'category__name': u'content', 'name': u'self'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
specific = OccurrenceSpecific.OperationalOcc.objects.create(occurrence=occurrence, **{'working_condition': u'?'})
tto = TagToOccurrence.objects.create(user_creator=get_userextension("ad"), user_occurrence_id=60, occurrence=occurrence)
# Tag and pictures
occurrence.tag_file = "advideogame/occurrences/60/tags/v1.png"
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=61, note='', lookup_dict={'category__name': u'content', 'name': u'self'}).pk, detail=u'FRT', image_file='advideogame/occurrences/60/pictures/DSC03189.JPG')
occurrence.save()

	#Sega Game Pack 4 in 1
occurrence = Occurrence.objects.create(created_by=get_userextension("ad"), owner=get_person({'first_name': 'Adrien'}), release=Release.objects.get(pk=62), **{'origin': u'BC', 'blister': False, 'add_date': datetime.datetime(2013, 3, 30, 2, 59, 10, 580525, tzinfo=pytz.utc), 'lastmodif_date': datetime.datetime(2013, 3, 30, 2, 59, 10, 983892, tzinfo=pytz.utc), 'pk': 61, 'purchase_price': 1.0})
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'A', attribute_id=get_corresponding_release_attribute(release=62, note='', lookup_dict={'category__name': u'content', 'name': u'self'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
specific = OccurrenceSpecific.OperationalOcc.objects.create(occurrence=occurrence, **{'working_condition': u'?'})
tto = TagToOccurrence.objects.create(user_creator=get_userextension("ad"), user_occurrence_id=61, occurrence=occurrence)
# Tag and pictures
occurrence.tag_file = "advideogame/occurrences/61/tags/v1.png"
OccurrencePicture.objects.create(occurrence=occurrence, detail=u'GRP', image_file='advideogame/occurrences/61/pictures/DSC03188.JPG')
occurrence.save()

	#Operation Wolf
occurrence = Occurrence.objects.create(created_by=get_userextension("ad"), owner=get_person({'first_name': 'Adrien'}), release=Release.objects.get(pk=64), **{'origin': u'OR', 'blister': False, 'add_date': datetime.datetime(2013, 3, 30, 3, 3, 43, 340436, tzinfo=pytz.utc), 'lastmodif_date': datetime.datetime(2013, 3, 30, 3, 3, 44, 308193, tzinfo=pytz.utc), 'pk': 62, 'purchase_price': None})
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'A', attribute_id=get_corresponding_release_attribute(release=64, note='', lookup_dict={'category__name': u'content', 'name': u'self'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'A', attribute_id=get_corresponding_release_attribute(release=64, note='', lookup_dict={'category__name': u'packaging', 'name': u'cartridge box'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value='1', attribute_id=get_corresponding_release_attribute(release=64, note='', lookup_dict={'category__name': 'packaging', 'name': 'hang on tab'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'B', attribute_id=get_corresponding_release_attribute(release=64, note='', lookup_dict={'category__name': u'papers', 'name': u'manual'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
specific = OccurrenceSpecific.OperationalOcc.objects.create(occurrence=occurrence, **{'working_condition': u'Y'})
tto = TagToOccurrence.objects.create(user_creator=get_userextension("ad"), user_occurrence_id=62, occurrence=occurrence)
# Tag and pictures
occurrence.tag_file = "advideogame/occurrences/62/tags/v1.png"
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=64, note='', lookup_dict={'category__name': u'packaging', 'name': u'cartridge box'}).pk, detail=u'FRT', image_file='advideogame/occurrences/62/pictures/DSC03209.JPG')
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=64, note='', lookup_dict={'category__name': u'packaging', 'name': u'cartridge box'}).pk, detail=u'BCK', image_file='advideogame/occurrences/62/pictures/DSC03210.JPG')
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=64, note='', lookup_dict={'category__name': u'packaging', 'name': u'cartridge box'}).pk, detail=u'SLB', image_file='advideogame/occurrences/62/pictures/DSC03212.JPG')
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=64, note='', lookup_dict={'category__name': u'packaging', 'name': u'cartridge box'}).pk, detail=u'INS', image_file='advideogame/occurrences/62/pictures/DSC03211.JPG')
occurrence.save()

	#Wheel Wii Sonic
occurrence = Occurrence.objects.create(created_by=get_userextension("ad"), owner=get_person({'first_name': 'Adrien'}), release=Release.objects.get(pk=65), **{'origin': u'BC', 'blister': False, 'add_date': datetime.datetime(2013, 3, 30, 3, 4, 59, 6328, tzinfo=pytz.utc), 'lastmodif_date': datetime.datetime(2013, 3, 30, 3, 4, 59, 375056, tzinfo=pytz.utc), 'pk': 63, 'purchase_price': 1.9})
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'B', attribute_id=get_corresponding_release_attribute(release=65, note='', lookup_dict={'category__name': u'content', 'name': u'self'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
specific = OccurrenceSpecific.OperationalOcc.objects.create(occurrence=occurrence, **{'working_condition': u'Y'})
tto = TagToOccurrence.objects.create(user_creator=get_userextension("ad"), user_occurrence_id=63, occurrence=occurrence)
# Tag and pictures
occurrence.tag_file = "advideogame/occurrences/63/tags/v1.png"
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=65, note='', lookup_dict={'category__name': u'content', 'name': u'self'}).pk, detail=u'FRT', image_file='advideogame/occurrences/63/pictures/DSC03207.JPG')
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=65, note='', lookup_dict={'category__name': u'content', 'name': u'self'}).pk, detail=u'BCK', image_file='advideogame/occurrences/63/pictures/DSC03208.JPG')
occurrence.save()

	#The Sega Light Phaser
occurrence = Occurrence.objects.create(created_by=get_userextension("ad"), owner=get_person({'first_name': 'Adrien'}), release=Release.objects.get(pk=66), **{'origin': u'OR', 'blister': False, 'add_date': datetime.datetime(2013, 3, 30, 3, 7, 19, 209256, tzinfo=pytz.utc), 'lastmodif_date': datetime.datetime(2013, 3, 30, 3, 35, 35, 758641, tzinfo=pytz.utc), 'pk': 64, 'purchase_price': None})
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'B', attribute_id=get_corresponding_release_attribute(release=66, note='', lookup_dict={'category__name': u'content', 'name': u'self'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'A', attribute_id=get_corresponding_release_attribute(release=66, note='', lookup_dict={'category__name': u'packaging', 'name': u'cardboard box'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'A', attribute_id=get_corresponding_release_attribute(release=66, note='', lookup_dict={'category__name': 'packaging', 'name': u'inlay polystyrene'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'A', attribute_id=get_corresponding_release_attribute(release=66, note='', lookup_dict={'category__name': u'papers', 'name': u'manual'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
specific = OccurrenceSpecific.OperationalOcc.objects.create(occurrence=occurrence, **{'working_condition': u'Y'})
tto = TagToOccurrence.objects.create(user_creator=get_userextension("ad"), user_occurrence_id=64, occurrence=occurrence)
# Tag and pictures
occurrence.tag_file = "advideogame/occurrences/64/tags/v1.png"
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=66, note='', lookup_dict={'category__name': u'packaging', 'name': u'cardboard box'}).pk, detail=u'FRT', image_file='advideogame/occurrences/64/pictures/DSC03220.JPG')
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=66, note='', lookup_dict={'category__name': u'packaging', 'name': u'cardboard box'}).pk, detail=u'BCK', image_file='advideogame/occurrences/64/pictures/DSC03221.JPG')
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=66, note='', lookup_dict={'category__name': u'packaging', 'name': u'cardboard box'}).pk, detail=u'SID', image_file='advideogame/occurrences/64/pictures/DSC03222.JPG')
OccurrencePicture.objects.create(occurrence=occurrence, detail=u'GRP', image_file='advideogame/occurrences/64/pictures/DSC03219.JPG')
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=66, note='', lookup_dict={'category__name': u'content', 'name': u'self'}).pk, detail=u'FRT', image_file='advideogame/occurrences/64/pictures/DSC03213.JPG')
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=66, note='', lookup_dict={'category__name': u'content', 'name': u'self'}).pk, detail=u'FRT', image_file='advideogame/occurrences/64/pictures/DSC03217.JPG')
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=66, note='', lookup_dict={'category__name': u'papers', 'name': u'manual'}).pk, detail=u'FRT', image_file='advideogame/occurrences/64/pictures/DSC03233.JPG')
OccurrencePicture.objects.create(occurrence=occurrence, detail=u'GRP', image_file='advideogame/occurrences/64/pictures/DSC03239.JPG')
occurrence.save()

	#Master System Control Pad
occurrence = Occurrence.objects.create(created_by=get_userextension("ad"), owner=get_person({'first_name': 'Adrien'}), release=Release.objects.get(pk=68), **{'origin': u'OR', 'blister': False, 'add_date': datetime.datetime(2013, 3, 30, 3, 22, 0, 889148, tzinfo=pytz.utc), 'lastmodif_date': datetime.datetime(2013, 3, 30, 3, 22, 1, 233333, tzinfo=pytz.utc), 'pk': 65, 'purchase_price': None})
self = OccurrenceAnyAttribute(occurrence=occurrence, value=u'D', attribute_id=get_corresponding_release_attribute(release=68, note='', lookup_dict={'category__name': u'content', 'name': u'self'}).pk, attribute_type=ReleaseAttribute_contentype)
occurrence.attributes.add(self, bulk=False)
specific = OccurrenceSpecific.OperationalOcc.objects.create(occurrence=occurrence, **{'working_condition': u'Y'})
tto = TagToOccurrence.objects.create(user_creator=get_userextension("ad"), user_occurrence_id=65, occurrence=occurrence)
# Tag and pictures
occurrence.tag_file = "advideogame/occurrences/65/tags/v1.png"
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=68, note='', lookup_dict={'category__name': u'content', 'name': u'self'}).pk, detail=u'FRT', image_file='advideogame/occurrences/65/pictures/DSC03225.JPG')
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=68, note='', lookup_dict={'category__name': u'content', 'name': u'self'}).pk, detail=u'DEF', image_file='advideogame/occurrences/65/pictures/DSC03226.JPG')
occurrence.save()
OccurrenceAnyAttributeDefect.objects.create(occurrence_any_attribute=self, defect_description="detached d-pad")

	#Master System Control Pad
occurrence = Occurrence.objects.create(created_by=get_userextension("ad"), owner=get_person({'first_name': 'Adrien'}), release=Release.objects.get(pk=68), **{'origin': u'BU', 'blister': False, 'add_date': datetime.datetime(2013, 3, 30, 3, 22, 52, 914636, tzinfo=pytz.utc), 'lastmodif_date': datetime.datetime(2013, 3, 30, 3, 22, 53, 285005, tzinfo=pytz.utc), 'pk': 66, 'purchase_price': None})
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'B', attribute_id=get_corresponding_release_attribute(release=68, note='', lookup_dict={'category__name': u'content', 'name': u'self'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
specific = OccurrenceSpecific.OperationalOcc.objects.create(occurrence=occurrence, **{'working_condition': u'Y'})
tto = TagToOccurrence.objects.create(user_creator=get_userextension("ad"), user_occurrence_id=66, occurrence=occurrence)
# Tag and pictures
occurrence.tag_file = "advideogame/occurrences/66/tags/v1.png"
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=68, note='', lookup_dict={'category__name': u'content', 'name': u'self'}).pk, detail=u'FRT', image_file='advideogame/occurrences/66/pictures/DSC03246.JPG')
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=68, note='', lookup_dict={'category__name': u'content', 'name': u'self'}).pk, detail=u'BCK', image_file='advideogame/occurrences/66/pictures/DSC03247.JPG')
occurrence.save()

	#Sega Master System
occurrence = Occurrence.objects.create(created_by=get_userextension("ad"), owner=get_person({'first_name': 'Adrien'}), release=Release.objects.get(pk=67), **{'origin': u'OR', 'blister': False, 'add_date': datetime.datetime(2013, 3, 30, 3, 26, 34, 901426, tzinfo=pytz.utc), 'lastmodif_date': datetime.datetime(2013, 3, 30, 3, 28, 3, 421845, tzinfo=pytz.utc), 'pk': 67, 'purchase_price': None})
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'B', attribute_id=get_corresponding_release_attribute(release=67, note='', lookup_dict={'category__name': u'content', 'name': u'self'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value='0', attribute_id=get_corresponding_release_attribute(release=67, note='', lookup_dict={'category__name': u'packaging', 'name': u'cardboard box'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value='0', attribute_id=get_corresponding_release_attribute(release=67, note='', lookup_dict={'category__name': 'packaging', 'name': u'inlay polystyrene'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'B', attribute_id=get_corresponding_release_attribute(release=67, note='', lookup_dict={'category__name': u'papers', 'name': u'leaflet'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'A', attribute_id=get_corresponding_release_attribute(release=67, note='', lookup_dict={'category__name': u'papers', 'name': u'manual'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'A', attribute_id=get_corresponding_release_attribute(release=67, note='', lookup_dict={'category__name': u'papers', 'name': u'warranty'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value='1', attribute_id=get_corresponding_release_attribute(release=67, note='', lookup_dict={'category__name': u'content', 'name': u'cord-220v'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value='1', attribute_id=get_corresponding_release_attribute(release=67, note='', lookup_dict={'category__name': u'content', 'name': u'scart'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
OccurrenceComposition.objects.create(from_occurrence=occurrence, to_occurrence=Occurrence.objects.get(pk=96), release_composition=get_corresponding_release_compo({'to_release': 63, 'from_release': 67}))
OccurrenceComposition.objects.create(from_occurrence=occurrence, to_occurrence=Occurrence.objects.get(pk=65), release_composition=get_corresponding_release_compo({'to_release': 68, 'from_release': 67}))
specific = OccurrenceSpecific.OperationalOcc.objects.create(occurrence=occurrence, **{'working_condition': u'Y'})
specific = OccurrenceSpecific.ConsoleOcc.objects.create(occurrence=occurrence, **{'copy_modded': False, 'region_modded': False})
tto = TagToOccurrence.objects.create(user_creator=get_userextension("ad"), user_occurrence_id=67, occurrence=occurrence)
# Tag and pictures
occurrence.tag_file = "advideogame/occurrences/67/tags/v1.png"
OccurrencePicture.objects.create(occurrence=occurrence, detail=u'GRP', image_file='advideogame/occurrences/67/pictures/DSC03223.JPG')
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=67, note='', lookup_dict={'category__name': u'content', 'name': u'self'}).pk, detail=u'FRT', image_file='advideogame/occurrences/67/pictures/DSC03237.JPG')
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=67, note='', lookup_dict={'category__name': u'content', 'name': u'self'}).pk, detail=u'SID', image_file='advideogame/occurrences/67/pictures/DSC03238.JPG')
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=67, note='', lookup_dict={'category__name': u'papers', 'name': u'leaflet'}).pk, detail=u'FRT', image_file='advideogame/occurrences/67/pictures/DSC03228.JPG')
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=67, note='', lookup_dict={'category__name': u'papers', 'name': u'leaflet'}).pk, detail=u'FRT', image_file='advideogame/occurrences/67/pictures/DSC03229.JPG')
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=67, note='', lookup_dict={'category__name': u'papers', 'name': u'warranty'}).pk, detail=u'FRT', image_file='advideogame/occurrences/67/pictures/DSC03230.JPG')
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=67, note='', lookup_dict={'category__name': u'papers', 'name': u'warranty'}).pk, detail=u'BCK', image_file='advideogame/occurrences/67/pictures/DSC03231.JPG')
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=67, note='', lookup_dict={'category__name': u'papers', 'name': u'manual'}).pk, detail=u'FRT', image_file='advideogame/occurrences/67/pictures/DSC03234.JPG')
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=67, note='', lookup_dict={'category__name': u'papers', 'name': u'manual'}).pk, detail=u'FRT', image_file='advideogame/occurrences/67/pictures/DSC03235.JPG')
occurrence.save()

	#_COMBO
occurrence = Occurrence.objects.create(created_by=get_userextension("ad"), owner=get_person({'first_name': 'Adrien'}), release=Release.objects.get(pk=69), **{'origin': u'OR', 'blister': False, 'add_date': datetime.datetime(2013, 3, 30, 3, 33, 54, 292830, tzinfo=pytz.utc), 'lastmodif_date': datetime.datetime(2013, 3, 30, 3, 34, 37, 941355, tzinfo=pytz.utc), 'pk': 68, 'purchase_price': None})
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'B', attribute_id=get_corresponding_release_attribute(release=69, note='', lookup_dict={'category__name': u'packaging', 'name': u'cardboard box'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
OccurrenceComposition.objects.create(from_occurrence=occurrence, to_occurrence=Occurrence.objects.get(pk=67), release_composition=get_corresponding_release_compo({'to_release': 67, 'from_release': 69}))
OccurrenceComposition.objects.create(from_occurrence=occurrence, to_occurrence=Occurrence.objects.get(pk=64), release_composition=get_corresponding_release_compo({'to_release': 66, 'from_release': 69}))
OccurrenceComposition.objects.create(from_occurrence=occurrence, to_occurrence=Occurrence.objects.get(pk=62), release_composition=get_corresponding_release_compo({'to_release': 64, 'from_release': 69}))
tto = TagToOccurrence.objects.create(user_creator=get_userextension("ad"), user_occurrence_id=68, occurrence=occurrence)
# Tag and pictures
occurrence.tag_file = "advideogame/occurrences/68/tags/v1.png"
OccurrencePicture.objects.create(occurrence=occurrence, detail=u'GRP', image_file='advideogame/occurrences/68/pictures/DSC03227.JPG')
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=69, note='', lookup_dict={'category__name': u'packaging', 'name': u'cardboard box'}).pk, detail=u'FRT', image_file='advideogame/occurrences/68/pictures/DSC03241.JPG')
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=69, note='', lookup_dict={'category__name': u'packaging', 'name': u'cardboard box'}).pk, detail=u'BCK', image_file='advideogame/occurrences/68/pictures/DSC03243.JPG')
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=69, note='', lookup_dict={'category__name': u'packaging', 'name': u'cardboard box'}).pk, detail=u'SID', image_file='advideogame/occurrences/68/pictures/DSC03244.JPG')
occurrence.save()

	#Steering wheel Saturn Mad Catz
occurrence = Occurrence.objects.create(created_by=get_userextension("ad"), owner=get_person({'first_name': 'Adrien'}), release=Release.objects.get(pk=70), **{'origin': u'BA', 'blister': False, 'add_date': datetime.datetime(2013, 5, 10, 16, 48, 52, 543475, tzinfo=pytz.utc), 'lastmodif_date': datetime.datetime(2013, 5, 10, 16, 48, 52, 908978, tzinfo=pytz.utc), 'pk': 69, 'purchase_price': 22.0})
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'B', attribute_id=get_corresponding_release_attribute(release=70, note='', lookup_dict={'category__name': u'content', 'name': u'self'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'C', attribute_id=get_corresponding_release_attribute(release=70, note='', lookup_dict={'category__name': u'packaging', 'name': u'cardboard box'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'B', attribute_id=get_corresponding_release_attribute(release=70, note='', lookup_dict={'category__name': 'packaging', 'name': u'baggies'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'A', attribute_id=get_corresponding_release_attribute(release=70, note='', lookup_dict={'category__name': u'papers', 'name': u'manual'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
specific = OccurrenceSpecific.OperationalOcc.objects.create(occurrence=occurrence, **{'working_condition': u'?'})
tto = TagToOccurrence.objects.create(user_creator=get_userextension("ad"), user_occurrence_id=69, occurrence=occurrence)
# Tag and pictures
occurrence.tag_file = "advideogame/occurrences/69/tags/v1.png"
occurrence.save()

	#Half-Life
occurrence = Occurrence.objects.create(created_by=get_userextension("ad"), owner=get_person({'first_name': 'Adrien'}), release=Release.objects.get(pk=72), **{'origin': u'OR', 'blister': False, 'add_date': datetime.datetime(2014, 8, 7, 21, 37, 29, 148067, tzinfo=pytz.utc), 'lastmodif_date': datetime.datetime(2014, 8, 7, 21, 41, 6, 631244, tzinfo=pytz.utc), 'pk': 70, 'purchase_price': None})
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'B', attribute_id=get_corresponding_release_attribute(release=72, note='', lookup_dict={'category__name': u'content', 'name': u'self'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'A', attribute_id=get_corresponding_release_attribute(release=72, note='', lookup_dict={'category__name': u'packaging', 'name': u'cardboard box'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'C', attribute_id=get_corresponding_release_attribute(release=72, note='', lookup_dict={'category__name': u'packaging', 'name': u'jewel box'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'A', attribute_id=get_corresponding_release_attribute(release=72, note='', lookup_dict={'category__name': 'packaging', 'name': 'cardboard inlay non-decorative'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'M', attribute_id=get_corresponding_release_attribute(release=72, note='', lookup_dict={'category__name': u'papers', 'name': u'catalog'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'B', attribute_id=get_corresponding_release_attribute(release=72, note='', lookup_dict={'category__name': u'papers', 'name': 'insert: jewel box'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'M', attribute_id=get_corresponding_release_attribute(release=72, note='', lookup_dict={'category__name': u'papers', 'name': u'leaflet'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'M', attribute_id=get_corresponding_release_attribute(release=72, note='', lookup_dict={'category__name': u'papers', 'name': u'manual'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'M', attribute_id=get_corresponding_release_attribute(release=72, note='', lookup_dict={'category__name': u'papers', 'name': u'registration card'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
specific = OccurrenceSpecific.OperationalOcc.objects.create(occurrence=occurrence, **{'working_condition': u'Y'})
tto = TagToOccurrence.objects.create(user_creator=get_userextension("ad"), user_occurrence_id=70, occurrence=occurrence)
# Tag and pictures
occurrence.tag_file = "advideogame/occurrences/70/tags/v1.png"
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=72, note='', lookup_dict={'category__name': u'packaging', 'name': u'cardboard box'}).pk, detail=u'FRT', image_file='advideogame/occurrences/70/pictures/DSC03506.JPG')
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=72, note='', lookup_dict={'category__name': u'packaging', 'name': u'cardboard box'}).pk, detail=u'BCK', image_file='advideogame/occurrences/70/pictures/DSC03507.JPG')
OccurrencePicture.objects.create(occurrence=occurrence, detail=u'GRP', image_file='advideogame/occurrences/70/pictures/DSC03526.JPG')
occurrence.save()

	#Half-Life: Opposing Force
occurrence = Occurrence.objects.create(created_by=get_userextension("ad"), owner=get_person({'first_name': 'Adrien'}), release=Release.objects.get(pk=73), **{'origin': u'OR', 'blister': False, 'add_date': datetime.datetime(2014, 8, 7, 21, 50, 23, 55749, tzinfo=pytz.utc), 'lastmodif_date': datetime.datetime(2014, 8, 7, 21, 50, 23, 487783, tzinfo=pytz.utc), 'pk': 71, 'purchase_price': None})
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'A', attribute_id=get_corresponding_release_attribute(release=73, note='', lookup_dict={'category__name': u'content', 'name': u'self'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'B', attribute_id=get_corresponding_release_attribute(release=73, note='', lookup_dict={'category__name': u'packaging', 'name': u'cardboard box'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'A', attribute_id=get_corresponding_release_attribute(release=73, note='', lookup_dict={'category__name': u'packaging', 'name': u'jewel box'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'M', attribute_id=get_corresponding_release_attribute(release=73, note='', lookup_dict={'category__name': 'packaging', 'name': 'cardboard inlay non-decorative'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'M', attribute_id=get_corresponding_release_attribute(release=73, note='', lookup_dict={'category__name': u'papers', 'name': u'catalog'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'M', attribute_id=get_corresponding_release_attribute(release=73, note='', lookup_dict={'category__name': u'papers', 'name': 'insert: jewel box'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'M', attribute_id=get_corresponding_release_attribute(release=73, note='', lookup_dict={'category__name': u'papers', 'name': u'manual'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'M', attribute_id=get_corresponding_release_attribute(release=73, note='', lookup_dict={'category__name': u'papers', 'name': u'registration card'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
specific = OccurrenceSpecific.OperationalOcc.objects.create(occurrence=occurrence, **{'working_condition': u'Y'})
tto = TagToOccurrence.objects.create(user_creator=get_userextension("ad"), user_occurrence_id=71, occurrence=occurrence)
# Tag and pictures
occurrence.tag_file = "advideogame/occurrences/71/tags/v1.png"
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=73, note='', lookup_dict={'category__name': u'packaging', 'name': u'cardboard box'}).pk, detail=u'FRT', image_file='advideogame/occurrences/71/pictures/DSC03508.JPG')
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=73, note='', lookup_dict={'category__name': u'packaging', 'name': u'cardboard box'}).pk, detail=u'BCK', image_file='advideogame/occurrences/71/pictures/DSC03509.JPG')
OccurrencePicture.objects.create(occurrence=occurrence, detail=u'GRP', image_file='advideogame/occurrences/71/pictures/DSC03527.JPG')
occurrence.save()

	#_COMBO
occurrence = Occurrence.objects.create(created_by=get_userextension("ad"), owner=get_person({'first_name': 'Adrien'}), release=Release.objects.get(pk=74), **{'origin': u'OR', 'blister': False, 'add_date': datetime.datetime(2014, 8, 7, 21, 58, 30, 353167, tzinfo=pytz.utc), 'lastmodif_date': datetime.datetime(2014, 8, 7, 21, 58, 30, 753633, tzinfo=pytz.utc), 'pk': 72, 'purchase_price': None})
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'B', attribute_id=get_corresponding_release_attribute(release=74, note='', lookup_dict={'category__name': u'packaging', 'name': u'sheath'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
OccurrenceComposition.objects.create(from_occurrence=occurrence, to_occurrence=Occurrence.objects.get(pk=70), release_composition=get_corresponding_release_compo({'to_release': 72, 'from_release': 74}))
OccurrenceComposition.objects.create(from_occurrence=occurrence, to_occurrence=Occurrence.objects.get(pk=71), release_composition=get_corresponding_release_compo({'to_release': 73, 'from_release': 74}))
tto = TagToOccurrence.objects.create(user_creator=get_userextension("ad"), user_occurrence_id=72, occurrence=occurrence)
# Tag and pictures
occurrence.tag_file = "advideogame/occurrences/72/tags/v1.png"
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=74, note='', lookup_dict={'category__name': u'packaging', 'name': u'sheath'}).pk, detail=u'FRT', image_file='advideogame/occurrences/72/pictures/DSC03503.JPG')
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=74, note='', lookup_dict={'category__name': u'packaging', 'name': u'sheath'}).pk, detail=u'BCK', image_file='advideogame/occurrences/72/pictures/DSC03505.JPG')
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=74, note='', lookup_dict={'category__name': u'packaging', 'name': u'sheath'}).pk, detail=u'SID', image_file='advideogame/occurrences/72/pictures/DSC03504.JPG')
occurrence.save()

	#Pole Position
occurrence = Occurrence.objects.create(created_by=get_userextension("ad"), owner=get_person({'first_name': 'Adrien'}), release=Release.objects.get(pk=75), **{'origin': u'BC', 'blister': False, 'add_date': datetime.datetime(2014, 8, 7, 22, 42, 35, 614023, tzinfo=pytz.utc), 'lastmodif_date': datetime.datetime(2014, 8, 7, 22, 42, 36, 82045, tzinfo=pytz.utc), 'pk': 73, 'purchase_price': 3.0})
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'B', attribute_id=get_corresponding_release_attribute(release=75, note='', lookup_dict={'category__name': u'content', 'name': u'self'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
specific = OccurrenceSpecific.OperationalOcc.objects.create(occurrence=occurrence, **{'working_condition': u'?'})
tto = TagToOccurrence.objects.create(user_creator=get_userextension("ad"), user_occurrence_id=73, occurrence=occurrence)
# Tag and pictures
occurrence.tag_file = "advideogame/occurrences/73/tags/v1.png"
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=75, note='', lookup_dict={'category__name': u'content', 'name': u'self'}).pk, detail=u'FRT', image_file='advideogame/occurrences/73/pictures/DSC03468.JPG')
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=75, note='', lookup_dict={'category__name': u'content', 'name': u'self'}).pk, detail=u'SLB', image_file='advideogame/occurrences/73/pictures/DSC03469.JPG')
occurrence.save()

	#Centipede
occurrence = Occurrence.objects.create(created_by=get_userextension("ad"), owner=get_person({'first_name': 'Adrien'}), release=Release.objects.get(pk=76), **{'origin': u'BC', 'blister': False, 'add_date': datetime.datetime(2014, 8, 7, 22, 46, 20, 285727, tzinfo=pytz.utc), 'lastmodif_date': datetime.datetime(2014, 8, 7, 22, 46, 20, 720351, tzinfo=pytz.utc), 'pk': 74, 'purchase_price': 3.0})
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'B', attribute_id=get_corresponding_release_attribute(release=76, note='', lookup_dict={'category__name': u'content', 'name': u'self'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
specific = OccurrenceSpecific.OperationalOcc.objects.create(occurrence=occurrence, **{'working_condition': u'?'})
tto = TagToOccurrence.objects.create(user_creator=get_userextension("ad"), user_occurrence_id=74, occurrence=occurrence)
# Tag and pictures
occurrence.tag_file = "advideogame/occurrences/74/tags/v1.png"
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=76, note='', lookup_dict={'category__name': u'content', 'name': u'self'}).pk, detail=u'FRT', image_file='advideogame/occurrences/74/pictures/DSC03466.JPG')
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=76, note='', lookup_dict={'category__name': u'content', 'name': u'self'}).pk, detail=u'SLB', image_file='advideogame/occurrences/74/pictures/DSC03467.JPG')
occurrence.save()

	#Millennium Soldier: Expendable
occurrence = Occurrence.objects.create(created_by=get_userextension("ad"), owner=get_person({'first_name': 'Adrien'}), release=Release.objects.get(pk=77), **{'origin': u'OR', 'blister': False, 'add_date': datetime.datetime(2014, 8, 7, 22, 56, 21, 399844, tzinfo=pytz.utc), 'lastmodif_date': datetime.datetime(2014, 8, 7, 23, 14, 33, 431613, tzinfo=pytz.utc), 'pk': 75, 'purchase_price': None})
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'A', attribute_id=get_corresponding_release_attribute(release=77, note='', lookup_dict={'category__name': u'content', 'name': u'self'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'B', attribute_id=get_corresponding_release_attribute(release=77, note='', lookup_dict={'category__name': u'packaging', 'name': u'cardboard box'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'B', attribute_id=get_corresponding_release_attribute(release=77, note='', lookup_dict={'category__name': u'packaging', 'name': u'jewel box'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'A', attribute_id=get_corresponding_release_attribute(release=77, note='', lookup_dict={'category__name': 'packaging', 'name': 'cardboard inlay non-decorative'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'A', attribute_id=get_corresponding_release_attribute(release=77, note='', lookup_dict={'category__name': u'papers', 'name': 'insert: jewel box'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
specific = OccurrenceSpecific.OperationalOcc.objects.create(occurrence=occurrence, **{'working_condition': u'Y'})
tto = TagToOccurrence.objects.create(user_creator=get_userextension("ad"), user_occurrence_id=75, occurrence=occurrence)
# Tag and pictures
occurrence.tag_file = "advideogame/occurrences/75/tags/v1.png"
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=77, note='', lookup_dict={'category__name': u'packaging', 'name': u'cardboard box'}).pk, detail=u'FRT', image_file='advideogame/occurrences/75/pictures/DSC03514.JPG')
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=77, note='', lookup_dict={'category__name': u'packaging', 'name': u'cardboard box'}).pk, detail=u'BCK', image_file='advideogame/occurrences/75/pictures/DSC03515.JPG')
occurrence.save()

	#Action Replay Plus 4M (Saturn EMS)
occurrence = Occurrence.objects.create(created_by=get_userextension("ad"), owner=get_person({'first_name': 'Adrien'}), release=Release.objects.get(pk=78), **{'origin': u'BU', 'blister': False, 'add_date': datetime.datetime(2014, 8, 7, 23, 29, 37, 958650, tzinfo=pytz.utc), 'lastmodif_date': datetime.datetime(2014, 8, 7, 23, 29, 38, 398665, tzinfo=pytz.utc), 'pk': 76, 'purchase_price': None})
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'M', attribute_id=get_corresponding_release_attribute(release=78, note='', lookup_dict={'category__name': u'content', 'name': u'self'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'A', attribute_id=get_corresponding_release_attribute(release=78, note='', lookup_dict={'category__name': u'packaging', 'name': u'cardboard box'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'M', attribute_id=get_corresponding_release_attribute(release=78, note='', lookup_dict={'category__name': 'packaging', 'name': 'cardboard inlay non-decorative'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'M', attribute_id=get_corresponding_release_attribute(release=78, note='', lookup_dict={'category__name': u'papers', 'name': u'leaflet'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
specific = OccurrenceSpecific.OperationalOcc.objects.create(occurrence=occurrence, **{'working_condition': u'?'})
tto = TagToOccurrence.objects.create(user_creator=get_userextension("ad"), user_occurrence_id=76, occurrence=occurrence)
# Tag and pictures
occurrence.tag_file = "advideogame/occurrences/76/tags/v1.png"
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=78, note='', lookup_dict={'category__name': u'packaging', 'name': u'cardboard box'}).pk, detail=u'FRT', image_file='advideogame/occurrences/76/pictures/DSC03474.JPG')
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=78, note='', lookup_dict={'category__name': u'packaging', 'name': u'cardboard box'}).pk, detail=u'BCK', image_file='advideogame/occurrences/76/pictures/DSC03475.JPG')
OccurrencePicture.objects.create(occurrence=occurrence, detail=u'GRP', image_file='advideogame/occurrences/76/pictures/DSC03479.JPG')
occurrence.save()

	#Titan Quest
occurrence = Occurrence.objects.create(created_by=get_userextension("ad"), owner=get_person({'first_name': 'Adrien'}), release=Release.objects.get(pk=79), **{'origin': u'OR', 'blister': False, 'add_date': datetime.datetime(2014, 8, 7, 23, 33, 57, 169582, tzinfo=pytz.utc), 'lastmodif_date': datetime.datetime(2014, 8, 7, 23, 33, 57, 529519, tzinfo=pytz.utc), 'pk': 77, 'purchase_price': None})
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'M', attribute_id=get_corresponding_release_attribute(release=79, note='', lookup_dict={'category__name': u'content', 'name': u'self'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'A', attribute_id=get_corresponding_release_attribute(release=79, note='', lookup_dict={'category__name': u'packaging', 'name': u'dvd box'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'B', attribute_id=get_corresponding_release_attribute(release=79, note='', lookup_dict={'category__name': u'papers', 'name': u'leaflet'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'A', attribute_id=get_corresponding_release_attribute(release=79, note='', lookup_dict={'category__name': u'papers', 'name': u'manual'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
specific = OccurrenceSpecific.OperationalOcc.objects.create(occurrence=occurrence, **{'working_condition': u'Y'})
tto = TagToOccurrence.objects.create(user_creator=get_userextension("ad"), user_occurrence_id=77, occurrence=occurrence)
# Tag and pictures
occurrence.tag_file = "advideogame/occurrences/77/tags/v1.png"
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=79, note='', lookup_dict={'category__name': u'packaging', 'name': u'dvd box'}).pk, detail=u'FRT', image_file='advideogame/occurrences/77/pictures/DSC03520.JPG')
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=79, note='', lookup_dict={'category__name': u'packaging', 'name': u'dvd box'}).pk, detail=u'BCK', image_file='advideogame/occurrences/77/pictures/DSC03521.JPG')
OccurrencePicture.objects.create(occurrence=occurrence, detail=u'GRP', image_file='advideogame/occurrences/77/pictures/DSC03522.JPG')
occurrence.save()

	#Diablo II
occurrence = Occurrence.objects.create(created_by=get_userextension("ad"), owner=get_person({'first_name': 'Adrien'}), release=Release.objects.get(pk=80), **{'origin': u'OR', 'blister': False, 'add_date': datetime.datetime(2014, 8, 7, 23, 38, 35, 993906, tzinfo=pytz.utc), 'lastmodif_date': datetime.datetime(2014, 8, 7, 23, 38, 36, 416715, tzinfo=pytz.utc), 'pk': 78, 'purchase_price': 10.0})
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'B', attribute_id=get_corresponding_release_attribute(release=80, note='', lookup_dict={'category__name': u'content', 'name': u'self'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'C', attribute_id=get_corresponding_release_attribute(release=80, note='', lookup_dict={'category__name': u'packaging', 'name': u'dvd box'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'B', attribute_id=get_corresponding_release_attribute(release=80, note='', lookup_dict={'category__name': u'papers', 'name': u'catalog'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'B', attribute_id=get_corresponding_release_attribute(release=80, note='', lookup_dict={'category__name': u'papers', 'name': u'manual'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
specific = OccurrenceSpecific.OperationalOcc.objects.create(occurrence=occurrence, **{'working_condition': u'Y'})
tto = TagToOccurrence.objects.create(user_creator=get_userextension("ad"), user_occurrence_id=78, occurrence=occurrence)
# Tag and pictures
occurrence.tag_file = "advideogame/occurrences/78/tags/v1.png"
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=80, note='', lookup_dict={'category__name': u'packaging', 'name': u'dvd box'}).pk, detail=u'FRT', image_file='advideogame/occurrences/78/pictures/DSC03523.JPG')
occurrence.save()

	#Diablo II
occurrence = Occurrence.objects.create(created_by=get_userextension("ad"), owner=get_person({'first_name': 'Adrien'}), release=Release.objects.get(pk=81), **{'origin': u'GF', 'blister': True, 'add_date': datetime.datetime(2014, 8, 7, 23, 41, 47, 122658, tzinfo=pytz.utc), 'lastmodif_date': datetime.datetime(2014, 8, 7, 23, 41, 47, 509073, tzinfo=pytz.utc), 'pk': 79, 'purchase_price': None})
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'M', attribute_id=get_corresponding_release_attribute(release=81, note='', lookup_dict={'category__name': u'content', 'name': u'self'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'M', attribute_id=get_corresponding_release_attribute(release=81, note='', lookup_dict={'category__name': u'packaging', 'name': u'cardboard box'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'M', attribute_id=get_corresponding_release_attribute(release=81, note='', lookup_dict={'category__name': u'packaging', 'name': u'jewel box'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'M', attribute_id=get_corresponding_release_attribute(release=81, note='', lookup_dict={'category__name': u'papers', 'name': u'manual'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
specific = OccurrenceSpecific.OperationalOcc.objects.create(occurrence=occurrence, **{'working_condition': u'Y'})
tto = TagToOccurrence.objects.create(user_creator=get_userextension("ad"), user_occurrence_id=79, occurrence=occurrence)
# Tag and pictures
occurrence.tag_file = "advideogame/occurrences/79/tags/v1.png"
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=81, note='', lookup_dict={'category__name': u'packaging', 'name': u'cardboard box'}).pk, detail=u'FRT', image_file='advideogame/occurrences/79/pictures/DSC03510.JPG')
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=81, note='', lookup_dict={'category__name': u'packaging', 'name': u'cardboard box'}).pk, detail=u'BCK', image_file='advideogame/occurrences/79/pictures/DSC03511.JPG')
occurrence.save()

	#Wolfenstein 3D
occurrence = Occurrence.objects.create(created_by=get_userextension("ad"), owner=get_person({'first_name': 'Adrien'}), release=Release.objects.get(pk=82), **{'origin': u'GF', 'blister': True, 'add_date': datetime.datetime(2014, 8, 7, 23, 45, 25, 410175, tzinfo=pytz.utc), 'lastmodif_date': datetime.datetime(2014, 8, 7, 23, 45, 25, 774427, tzinfo=pytz.utc), 'pk': 80, 'purchase_price': None})
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'M', attribute_id=get_corresponding_release_attribute(release=82, note='', lookup_dict={'category__name': u'content', 'name': u'self'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'M', attribute_id=get_corresponding_release_attribute(release=82, note='', lookup_dict={'category__name': u'packaging', 'name': u'dvd box'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
specific = OccurrenceSpecific.OperationalOcc.objects.create(occurrence=occurrence, **{'working_condition': u'Y'})
tto = TagToOccurrence.objects.create(user_creator=get_userextension("ad"), user_occurrence_id=80, occurrence=occurrence)
# Tag and pictures
occurrence.tag_file = "advideogame/occurrences/80/tags/v1.png"
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=82, note='', lookup_dict={'category__name': u'packaging', 'name': u'dvd box'}).pk, detail=u'FRT', image_file='advideogame/occurrences/80/pictures/DSC03524.JPG')
occurrence.save()

	#Final Doom
occurrence = Occurrence.objects.create(created_by=get_userextension("ad"), owner=get_person({'first_name': 'Adrien'}), release=Release.objects.get(pk=83), **{'origin': u'GF', 'blister': True, 'add_date': datetime.datetime(2014, 8, 7, 23, 50, 7, 62355, tzinfo=pytz.utc), 'lastmodif_date': datetime.datetime(2014, 8, 7, 23, 50, 7, 505858, tzinfo=pytz.utc), 'pk': 81, 'purchase_price': None})
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'M', attribute_id=get_corresponding_release_attribute(release=83, note='', lookup_dict={'category__name': u'content', 'name': u'self'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'B', attribute_id=get_corresponding_release_attribute(release=83, note='', lookup_dict={'category__name': u'packaging', 'name': u'cardboard box'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'M', attribute_id=get_corresponding_release_attribute(release=83, note='', lookup_dict={'category__name': u'packaging', 'name': u'jewel box'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'M', attribute_id=get_corresponding_release_attribute(release=83, note='', lookup_dict={'category__name': u'papers', 'name': u'manual'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
specific = OccurrenceSpecific.OperationalOcc.objects.create(occurrence=occurrence, **{'working_condition': u'Y'})
tto = TagToOccurrence.objects.create(user_creator=get_userextension("ad"), user_occurrence_id=81, occurrence=occurrence)
# Tag and pictures
occurrence.tag_file = "advideogame/occurrences/81/tags/v1.png"
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=83, note='', lookup_dict={'category__name': u'packaging', 'name': u'cardboard box'}).pk, detail=u'FRT', image_file='advideogame/occurrences/81/pictures/DSC03518.JPG')
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=83, note='', lookup_dict={'category__name': u'packaging', 'name': u'cardboard box'}).pk, detail=u'BCK', image_file='advideogame/occurrences/81/pictures/DSC03519.JPG')
occurrence.save()

	#Warcraft II: Tides of Darkness
occurrence = Occurrence.objects.create(created_by=get_userextension("ad"), owner=get_person({'first_name': 'Adrien'}), release=Release.objects.get(pk=84), **{'origin': u'GF', 'blister': True, 'add_date': datetime.datetime(2014, 8, 7, 23, 55, 34, 553528, tzinfo=pytz.utc), 'lastmodif_date': datetime.datetime(2014, 8, 7, 23, 55, 34, 919756, tzinfo=pytz.utc), 'pk': 82, 'purchase_price': None})
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'M', attribute_id=get_corresponding_release_attribute(release=84, note='', lookup_dict={'category__name': u'content', 'name': u'self'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'B', attribute_id=get_corresponding_release_attribute(release=84, note='', lookup_dict={'category__name': u'packaging', 'name': u'cardboard box'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'M', attribute_id=get_corresponding_release_attribute(release=84, note='', lookup_dict={'category__name': u'packaging', 'name': u'jewel box'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'M', attribute_id=get_corresponding_release_attribute(release=84, note='Tides of Darkness', lookup_dict={'category__name': u'papers', 'name': u'manual'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value='M', attribute_id=get_corresponding_release_attribute(release=84, note='Edition Deluxe', lookup_dict={'category__name': 'papers', 'name': 'manual'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value='M', attribute_id=get_corresponding_release_attribute(release=84, note='', lookup_dict={'category__name': 'papers', 'name': 'warranty'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
OccurrenceComposition.objects.create(from_occurrence=occurrence, to_occurrence=Occurrence.objects.get(pk=98), release_composition=get_corresponding_release_compo({'to_release': 100, 'from_release': 84}))
specific = OccurrenceSpecific.OperationalOcc.objects.create(occurrence=occurrence, **{'working_condition': u'Y'})
tto = TagToOccurrence.objects.create(user_creator=get_userextension("ad"), user_occurrence_id=82, occurrence=occurrence)
# Tag and pictures
occurrence.tag_file = "advideogame/occurrences/82/tags/v1.png"
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=84, note='', lookup_dict={'category__name': u'packaging', 'name': u'cardboard box'}).pk, detail=u'FRT', image_file='advideogame/occurrences/82/pictures/DSC03513.JPG')
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=84, note='', lookup_dict={'category__name': u'packaging', 'name': u'cardboard box'}).pk, detail=u'BCK', image_file='advideogame/occurrences/82/pictures/DSC03512.JPG')
occurrence.save()

	#Carmageddon II: Carpocalypse Now
occurrence = Occurrence.objects.create(created_by=get_userextension("ad"), owner=get_person({'first_name': 'Adrien'}), release=Release.objects.get(pk=85), **{'origin': u'OR', 'blister': False, 'add_date': datetime.datetime(2014, 8, 8, 0, 4, 20, 722103, tzinfo=pytz.utc), 'lastmodif_date': datetime.datetime(2014, 8, 8, 0, 4, 21, 181912, tzinfo=pytz.utc), 'pk': 83, 'purchase_price': None})
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'B', attribute_id=get_corresponding_release_attribute(release=85, note='', lookup_dict={'category__name': u'content', 'name': u'self'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'B', attribute_id=get_corresponding_release_attribute(release=85, note='', lookup_dict={'category__name': u'packaging', 'name': u'cardboard box'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'C', attribute_id=get_corresponding_release_attribute(release=85, note='', lookup_dict={'category__name': u'packaging', 'name': u'jewel box'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'B', attribute_id=get_corresponding_release_attribute(release=85, note='', lookup_dict={'category__name': u'packaging', 'name': u'sheath'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'B', attribute_id=get_corresponding_release_attribute(release=85, note='', lookup_dict={'category__name': 'packaging', 'name': 'cardboard inlay non-decorative'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'A', attribute_id=get_corresponding_release_attribute(release=85, note='', lookup_dict={'category__name': u'papers', 'name': u'leaflet'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'A', attribute_id=get_corresponding_release_attribute(release=85, note='', lookup_dict={'category__name': u'papers', 'name': u'manual'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'A', attribute_id=get_corresponding_release_attribute(release=85, note='', lookup_dict={'category__name': u'papers', 'name': u'registration card'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
specific = OccurrenceSpecific.OperationalOcc.objects.create(occurrence=occurrence, **{'working_condition': u'Y'})
tto = TagToOccurrence.objects.create(user_creator=get_userextension("ad"), user_occurrence_id=83, occurrence=occurrence)
# Tag and pictures
occurrence.tag_file = "advideogame/occurrences/83/tags/v1.png"
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=85, note='', lookup_dict={'category__name': u'packaging', 'name': u'cardboard box'}).pk, detail=u'FRT', image_file='advideogame/occurrences/83/pictures/DSC03499.JPG')
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=85, note='', lookup_dict={'category__name': u'packaging', 'name': u'cardboard box'}).pk, detail=u'BCK', image_file='advideogame/occurrences/83/pictures/DSC03501.JPG')
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=85, note='', lookup_dict={'category__name': u'content', 'name': u'self'}).pk, detail=u'FRT', image_file='advideogame/occurrences/83/pictures/DSC03498.JPG')
OccurrencePicture.objects.create(occurrence=occurrence, detail=u'GRP', image_file='advideogame/occurrences/83/pictures/DSC03497.JPG')
occurrence.save()

	#Torin's Passage
occurrence = Occurrence.objects.create(created_by=get_userextension("ad"), owner=get_person({'first_name': 'Adrien'}), release=Release.objects.get(pk=86), **{'origin': u'BC', 'blister': False, 'add_date': datetime.datetime(2014, 8, 8, 0, 13, 34, 139278, tzinfo=pytz.utc), 'lastmodif_date': datetime.datetime(2014, 8, 8, 0, 13, 34, 519619, tzinfo=pytz.utc), 'pk': 84, 'purchase_price': 0.0})
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'B', attribute_id=get_corresponding_release_attribute(release=86, note='', lookup_dict={'category__name': u'content', 'name': u'self'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'B', attribute_id=get_corresponding_release_attribute(release=86, note='', lookup_dict={'category__name': u'packaging', 'name': u'jewel box'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'B', attribute_id=get_corresponding_release_attribute(release=86, note='', lookup_dict={'category__name': u'papers', 'name': 'manual: jewel box'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
specific = OccurrenceSpecific.OperationalOcc.objects.create(occurrence=occurrence, **{'working_condition': u'?'})
tto = TagToOccurrence.objects.create(user_creator=get_userextension("ad"), user_occurrence_id=84, occurrence=occurrence)
# Tag and pictures
occurrence.tag_file = "advideogame/occurrences/84/tags/v1.png"
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=86, note='', lookup_dict={'category__name': u'packaging', 'name': u'jewel box'}).pk, detail=u'FRT', image_file='advideogame/occurrences/84/pictures/DSC03486.JPG')
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=86, note='', lookup_dict={'category__name': u'packaging', 'name': u'jewel box'}).pk, detail=u'BCK', image_file='advideogame/occurrences/84/pictures/DSC03487.JPG')
occurrence.save()

	#Loom
occurrence = Occurrence.objects.create(created_by=get_userextension("ad"), owner=get_person({'first_name': 'Adrien'}), release=Release.objects.get(pk=87), **{'origin': u'BC', 'blister': False, 'add_date': datetime.datetime(2014, 8, 8, 0, 14, 44, 345945, tzinfo=pytz.utc), 'lastmodif_date': datetime.datetime(2014, 8, 8, 0, 14, 44, 733861, tzinfo=pytz.utc), 'pk': 85, 'purchase_price': 0.0})
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'B', attribute_id=get_corresponding_release_attribute(release=87, note='', lookup_dict={'category__name': u'content', 'name': u'self'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'B', attribute_id=get_corresponding_release_attribute(release=87, note='', lookup_dict={'category__name': u'packaging', 'name': u'jewel box'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'B', attribute_id=get_corresponding_release_attribute(release=87, note='', lookup_dict={'category__name': u'papers', 'name': 'manual: jewel box'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
specific = OccurrenceSpecific.OperationalOcc.objects.create(occurrence=occurrence, **{'working_condition': u'?'})
tto = TagToOccurrence.objects.create(user_creator=get_userextension("ad"), user_occurrence_id=85, occurrence=occurrence)
# Tag and pictures
occurrence.tag_file = "advideogame/occurrences/85/tags/v1.png"
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=87, note='', lookup_dict={'category__name': u'packaging', 'name': u'jewel box'}).pk, detail=u'FRT', image_file='advideogame/occurrences/85/pictures/DSC03489.JPG')
occurrence.save()

	#The Lost Mind of Dr. Brain
occurrence = Occurrence.objects.create(created_by=get_userextension("ad"), owner=get_person({'first_name': 'Adrien'}), release=Release.objects.get(pk=88), **{'origin': u'BC', 'blister': False, 'add_date': datetime.datetime(2014, 8, 8, 0, 15, 45, 609116, tzinfo=pytz.utc), 'lastmodif_date': datetime.datetime(2014, 8, 8, 0, 15, 45, 956383, tzinfo=pytz.utc), 'pk': 86, 'purchase_price': 0.0})
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'B', attribute_id=get_corresponding_release_attribute(release=88, note='', lookup_dict={'category__name': u'content', 'name': u'self'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'B', attribute_id=get_corresponding_release_attribute(release=88, note='', lookup_dict={'category__name': u'packaging', 'name': u'jewel box'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'C', attribute_id=get_corresponding_release_attribute(release=88, note='', lookup_dict={'category__name': u'papers', 'name': 'manual: jewel box'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
specific = OccurrenceSpecific.OperationalOcc.objects.create(occurrence=occurrence, **{'working_condition': u'?'})
tto = TagToOccurrence.objects.create(user_creator=get_userextension("ad"), user_occurrence_id=86, occurrence=occurrence)
# Tag and pictures
occurrence.tag_file = "advideogame/occurrences/86/tags/v1.png"
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=88, note='', lookup_dict={'category__name': u'packaging', 'name': u'jewel box'}).pk, detail=u'FRT', image_file='advideogame/occurrences/86/pictures/DSC03488.JPG')
occurrence.save()

	#The Curse of Monkey Island
occurrence = Occurrence.objects.create(created_by=get_userextension("ad"), owner=get_person({'first_name': 'Adrien'}), release=Release.objects.get(pk=89), **{'origin': u'BC', 'blister': False, 'add_date': datetime.datetime(2014, 8, 8, 0, 27, 41, 649330, tzinfo=pytz.utc), 'lastmodif_date': datetime.datetime(2014, 8, 8, 0, 27, 42, 111235, tzinfo=pytz.utc), 'pk': 87, 'purchase_price': 2.0})
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'B', attribute_id=get_corresponding_release_attribute(release=89, note='', lookup_dict={'category__name': u'content', 'name': u'self'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'C', attribute_id=get_corresponding_release_attribute(release=89, note='', lookup_dict={'category__name': u'packaging', 'name': u'cardboard box'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'C', attribute_id=get_corresponding_release_attribute(release=89, note='', lookup_dict={'category__name': u'packaging', 'name': u'jewel box'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'B', attribute_id=get_corresponding_release_attribute(release=89, note='', lookup_dict={'category__name': u'papers', 'name': u'manual'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
specific = OccurrenceSpecific.OperationalOcc.objects.create(occurrence=occurrence, **{'working_condition': u'?'})
tto = TagToOccurrence.objects.create(user_creator=get_userextension("ad"), user_occurrence_id=87, occurrence=occurrence)
# Tag and pictures
occurrence.tag_file = "advideogame/occurrences/87/tags/v1.png"
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=89, note='', lookup_dict={'category__name': u'packaging', 'name': u'cardboard box'}).pk, detail=u'FRT', image_file='advideogame/occurrences/87/pictures/DSC03481.JPG')
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=89, note='', lookup_dict={'category__name': u'packaging', 'name': u'cardboard box'}).pk, detail=u'BCK', image_file='advideogame/occurrences/87/pictures/DSC03482.JPG')
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=89, note='', lookup_dict={'category__name': u'packaging', 'name': u'cardboard box'}).pk, detail=u'SID', image_file='advideogame/occurrences/87/pictures/DSC03483.JPG')
OccurrencePicture.objects.create(occurrence=occurrence, detail=u'GRP', image_file='advideogame/occurrences/87/pictures/DSC03484.JPG')
occurrence.save()

	#Nymphéas Photo CD
occurrence = Occurrence.objects.create(created_by=get_userextension("ad"), owner=get_person({'first_name': 'Adrien'}), release=Release.objects.get(pk=92), **{'origin': u'BC', 'blister': False, 'add_date': datetime.datetime(2014, 8, 8, 0, 49, 46, 574005, tzinfo=pytz.utc), 'lastmodif_date': datetime.datetime(2014, 8, 8, 0, 49, 46, 950084, tzinfo=pytz.utc), 'pk': 88, 'purchase_price': None})
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'M', attribute_id=get_corresponding_release_attribute(release=92, note='', lookup_dict={'category__name': u'content', 'name': u'self'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'M', attribute_id=get_corresponding_release_attribute(release=92, note='', lookup_dict={'category__name': u'papers', 'name': u'manual'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
specific = OccurrenceSpecific.OperationalOcc.objects.create(occurrence=occurrence, **{'working_condition': u'Y'})
tto = TagToOccurrence.objects.create(user_creator=get_userextension("ad"), user_occurrence_id=88, occurrence=occurrence)
# Tag and pictures
occurrence.tag_file = "advideogame/occurrences/88/tags/v1.png"
occurrence.save()

	#Photo CD Operating System (Saturn)
occurrence = Occurrence.objects.create(created_by=get_userextension("ad"), owner=get_person({'first_name': 'Adrien'}), release=Release.objects.get(pk=91), **{'origin': u'BC', 'blister': False, 'add_date': datetime.datetime(2014, 8, 8, 0, 52, 28, 78947, tzinfo=pytz.utc), 'lastmodif_date': datetime.datetime(2014, 8, 8, 0, 52, 28, 471357, tzinfo=pytz.utc), 'pk': 89, 'purchase_price': None})
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'M', attribute_id=get_corresponding_release_attribute(release=91, note='', lookup_dict={'category__name': u'content', 'name': u'self'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'M', attribute_id=get_corresponding_release_attribute(release=91, note='', lookup_dict={'category__name': u'packaging', 'name': u'dvd box'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'M', attribute_id=get_corresponding_release_attribute(release=91, note='', lookup_dict={'category__name': u'papers', 'name': u'manual'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
OccurrenceComposition.objects.create(from_occurrence=occurrence, to_occurrence=Occurrence.objects.get(pk=88), release_composition=get_corresponding_release_compo({'to_release': 92, 'from_release': 91}))
specific = OccurrenceSpecific.OperationalOcc.objects.create(occurrence=occurrence, **{'working_condition': u'Y'})
tto = TagToOccurrence.objects.create(user_creator=get_userextension("ad"), user_occurrence_id=89, occurrence=occurrence)
# Tag and pictures
occurrence.tag_file = "advideogame/occurrences/89/tags/v1.png"
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=91, note='', lookup_dict={'category__name': u'packaging', 'name': u'dvd box'}).pk, detail=u'FRT', image_file='advideogame/occurrences/89/pictures/DSC03470.JPG')
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=91, note='', lookup_dict={'category__name': u'packaging', 'name': u'dvd box'}).pk, detail=u'BCK', image_file='advideogame/occurrences/89/pictures/DSC03471.JPG')
occurrence.save()

	#Wii Remote
occurrence = Occurrence.objects.create(created_by=get_userextension("ad"), owner=get_person({'first_name': 'Adrien'}), release=Release.objects.get(pk=93), **{'origin': u'OR', 'blister': False, 'add_date': datetime.datetime(2014, 8, 8, 1, 6, 21, 40739, tzinfo=pytz.utc), 'lastmodif_date': datetime.datetime(2014, 8, 8, 1, 8, 56, 571464, tzinfo=pytz.utc), 'pk': 90, 'purchase_price': None})
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'M', attribute_id=get_corresponding_release_attribute(release=93, note='', lookup_dict={'category__name': u'content', 'name': u'self'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
specific = OccurrenceSpecific.OperationalOcc.objects.create(occurrence=occurrence, **{'working_condition': u'?'})
tto = TagToOccurrence.objects.create(user_creator=get_userextension("ad"), user_occurrence_id=90, occurrence=occurrence)
# Tag and pictures
occurrence.tag_file = "advideogame/occurrences/90/tags/v1.png"
occurrence.save()

	#Nunchuk
occurrence = Occurrence.objects.create(created_by=get_userextension("ad"), owner=get_person({'first_name': 'Adrien'}), release=Release.objects.get(pk=94), **{'origin': u'OR', 'blister': False, 'add_date': datetime.datetime(2014, 8, 8, 1, 7, 3, 188582, tzinfo=pytz.utc), 'lastmodif_date': datetime.datetime(2014, 8, 8, 1, 8, 24, 107417, tzinfo=pytz.utc), 'pk': 91, 'purchase_price': None})
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'M', attribute_id=get_corresponding_release_attribute(release=94, note='', lookup_dict={'category__name': u'content', 'name': u'self'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
specific = OccurrenceSpecific.OperationalOcc.objects.create(occurrence=occurrence, **{'working_condition': u'?'})
tto = TagToOccurrence.objects.create(user_creator=get_userextension("ad"), user_occurrence_id=91, occurrence=occurrence)
# Tag and pictures
occurrence.tag_file = "advideogame/occurrences/91/tags/v1.png"
occurrence.save()

	#Wii MotionPlus
occurrence = Occurrence.objects.create(created_by=get_userextension("ad"), owner=get_person({'first_name': 'Adrien'}), release=Release.objects.get(pk=95), **{'origin': u'OR', 'blister': False, 'add_date': datetime.datetime(2014, 8, 8, 1, 9, 20, 607115, tzinfo=pytz.utc), 'lastmodif_date': datetime.datetime(2014, 8, 8, 1, 9, 20, 954621, tzinfo=pytz.utc), 'pk': 92, 'purchase_price': None})
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'M', attribute_id=get_corresponding_release_attribute(release=95, note='', lookup_dict={'category__name': u'content', 'name': u'self'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
specific = OccurrenceSpecific.OperationalOcc.objects.create(occurrence=occurrence, **{'working_condition': u'?'})
tto = TagToOccurrence.objects.create(user_creator=get_userextension("ad"), user_occurrence_id=92, occurrence=occurrence)
# Tag and pictures
occurrence.tag_file = "advideogame/occurrences/92/tags/v1.png"
occurrence.save()

	#Wii Sports
occurrence = Occurrence.objects.create(created_by=get_userextension("ad"), owner=get_person({'first_name': 'Adrien'}), release=Release.objects.get(pk=96), **{'origin': u'OR', 'blister': False, 'add_date': datetime.datetime(2014, 8, 8, 1, 15, 17, 805387, tzinfo=pytz.utc), 'lastmodif_date': datetime.datetime(2014, 8, 8, 1, 15, 18, 205708, tzinfo=pytz.utc), 'pk': 93, 'purchase_price': None})
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'M', attribute_id=get_corresponding_release_attribute(release=96, note='', lookup_dict={'category__name': u'content', 'name': u'self'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'M', attribute_id=get_corresponding_release_attribute(release=96, note='', lookup_dict={'category__name': u'packaging', 'name': u'cardboard cd sleeve'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
specific = OccurrenceSpecific.OperationalOcc.objects.create(occurrence=occurrence, **{'working_condition': u'?'})
tto = TagToOccurrence.objects.create(user_creator=get_userextension("ad"), user_occurrence_id=93, occurrence=occurrence)
# Tag and pictures
occurrence.tag_file = "advideogame/occurrences/93/tags/v1.png"
occurrence.save()

	#Wii Sports Resort
occurrence = Occurrence.objects.create(created_by=get_userextension("ad"), owner=get_person({'first_name': 'Adrien'}), release=Release.objects.get(pk=97), **{'origin': u'OR', 'blister': False, 'add_date': datetime.datetime(2014, 8, 8, 1, 15, 33, 974875, tzinfo=pytz.utc), 'lastmodif_date': datetime.datetime(2014, 8, 8, 1, 15, 34, 338204, tzinfo=pytz.utc), 'pk': 94, 'purchase_price': None})
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'M', attribute_id=get_corresponding_release_attribute(release=97, note='', lookup_dict={'category__name': u'content', 'name': u'self'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'M', attribute_id=get_corresponding_release_attribute(release=97, note='', lookup_dict={'category__name': u'packaging', 'name': u'cardboard cd sleeve'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
specific = OccurrenceSpecific.OperationalOcc.objects.create(occurrence=occurrence, **{'working_condition': u'?'})
tto = TagToOccurrence.objects.create(user_creator=get_userextension("ad"), user_occurrence_id=94, occurrence=occurrence)
# Tag and pictures
occurrence.tag_file = "advideogame/occurrences/94/tags/v1.png"
occurrence.save()

	#Wii
occurrence = Occurrence.objects.create(created_by=get_userextension("ad"), owner=get_person({'first_name': 'Adrien'}), release=Release.objects.get(pk=98), **{'origin': u'OR', 'blister': False, 'add_date': datetime.datetime(2014, 8, 8, 1, 20, 35, 106702, tzinfo=pytz.utc), 'lastmodif_date': datetime.datetime(2014, 8, 8, 1, 20, 35, 502498, tzinfo=pytz.utc), 'pk': 95, 'purchase_price': None})
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'M', attribute_id=get_corresponding_release_attribute(release=98, note='', lookup_dict={'category__name': u'content', 'name': u'self'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'C', attribute_id=get_corresponding_release_attribute(release=98, note='', lookup_dict={'category__name': u'packaging', 'name': u'cardboard box'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'M', attribute_id=get_corresponding_release_attribute(release=98, note='', lookup_dict={'category__name': 'packaging', 'name': u'baggies'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'M', attribute_id=get_corresponding_release_attribute(release=98, note='', lookup_dict={'category__name': 'packaging', 'name': 'cardboard inlay non-decorative'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'M', attribute_id=get_corresponding_release_attribute(release=98, note='', lookup_dict={'category__name': u'papers', 'name': u'manual'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value=u'M', attribute_id=get_corresponding_release_attribute(release=98, note='', lookup_dict={'category__name': u'papers', 'name': u'warranty'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value='1', attribute_id=get_corresponding_release_attribute(release=98, note='', lookup_dict={'category__name': u'content', 'name': u'cord-220v'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
occurrence.attributes.add(OccurrenceAnyAttribute(occurrence=occurrence, value='1', attribute_id=get_corresponding_release_attribute(release=98, note='', lookup_dict={'category__name': u'content', 'name': u'scart'}).pk, attribute_type=ReleaseAttribute_contentype), bulk=False)
OccurrenceComposition.objects.create(from_occurrence=occurrence, to_occurrence=Occurrence.objects.get(pk=93), release_composition=get_corresponding_release_compo({'to_release': 96, 'from_release': 98}))
OccurrenceComposition.objects.create(from_occurrence=occurrence, to_occurrence=Occurrence.objects.get(pk=94), release_composition=get_corresponding_release_compo({'to_release': 97, 'from_release': 98}))
OccurrenceComposition.objects.create(from_occurrence=occurrence, to_occurrence=Occurrence.objects.get(pk=90), release_composition=get_corresponding_release_compo({'to_release': 93, 'from_release': 98}))
OccurrenceComposition.objects.create(from_occurrence=occurrence, to_occurrence=Occurrence.objects.get(pk=91), release_composition=get_corresponding_release_compo({'to_release': 94, 'from_release': 98}))
OccurrenceComposition.objects.create(from_occurrence=occurrence, to_occurrence=Occurrence.objects.get(pk=92), release_composition=get_corresponding_release_compo({'to_release': 95, 'from_release': 98}))
specific = OccurrenceSpecific.OperationalOcc.objects.create(occurrence=occurrence, **{'working_condition': u'?'})
specific = OccurrenceSpecific.ConsoleOcc.objects.create(occurrence=occurrence, **{'copy_modded': False, 'region_modded': False})
tto = TagToOccurrence.objects.create(user_creator=get_userextension("ad"), user_occurrence_id=95, occurrence=occurrence)
# Tag and pictures
occurrence.tag_file = "advideogame/occurrences/95/tags/v1.png"
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=98, note='', lookup_dict={'category__name': u'packaging', 'name': u'cardboard box'}).pk, detail=u'FRT', image_file='advideogame/occurrences/95/pictures/DSC03493.JPG')
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=98, note='', lookup_dict={'category__name': u'packaging', 'name': u'cardboard box'}).pk, detail=u'BCK', image_file='advideogame/occurrences/95/pictures/DSC03496.JPG')
OccurrencePicture.objects.create(occurrence=occurrence, attribute_type=ReleaseAttribute_contentype, attribute_id = get_corresponding_release_attribute(release=98, note='', lookup_dict={'category__name': u'packaging', 'name': u'cardboard box'}).pk, detail=u'SLB', image_file='advideogame/occurrences/95/pictures/DSC03494.JPG')
occurrence.save()

