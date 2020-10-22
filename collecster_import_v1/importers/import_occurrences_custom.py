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

def get_corresponding_release_attribute(release, note, lookup_dict):
    if note:
        return ReleaseAttribute.objects.get(release=release, note=note, attribute=Attribute.objects.get(Q(**lookup_dict)))
    else:
        return ReleaseAttribute.objects.get(release=release, attribute=Attribute.objects.get(Q(**lookup_dict)))

def get_corresponding_release_compo(lookup_dict):
    return ReleaseComposition.objects.get(Q(**lookup_dict))

# All pictures are attached to non-custom ReleaseAttribute instances.
ReleaseAttribute_contenttype = ContentType.objects.get_for_model(ReleaseAttribute)

# First free pk: 96

	#Alex Kidd
occurrence = Occurrence.objects.create(created_by=get_userextension("ad"), owner=get_person({'first_name': 'Adrien'}), release=Release.objects.get(pk=63), **{'blister': False, 'add_date': datetime.datetime(2016, 4, 22, 18, 30, 0, 536000, tzinfo=pytz.utc), 'lastmodif_date': datetime.datetime(2016, 4, 22, 18, 30, 0, 536000, tzinfo=pytz.utc), 'pk': 96})
occurrence.attributes.add( OccurrenceAnyAttribute(occurrence=occurrence, value=u'C', attribute_id=get_corresponding_release_attribute(release=63, note='', lookup_dict={'category__name': u'papers', 'name': u'manual'}).pk, attribute_type=ReleaseAttribute_contenttype), bulk=False )
specific = OccurrenceSpecific.OperationalOcc.objects.create(occurrence=occurrence, **{'working_condition': u'Y'})
tto = TagToOccurrence.objects.create(user_creator=get_userextension("ad"), user_occurrence_id=96, occurrence=occurrence)

	# Thy Flesh Consumed
occurrence = Occurrence.objects.create(created_by=get_userextension("ad"), owner=get_person({'first_name': 'Adrien'}), release=Release.objects.get(pk=99), **{'blister': False, 'add_date': datetime.datetime(2016, 4, 22, 18, 30, 0, 536000, tzinfo=pytz.utc), 'lastmodif_date': datetime.datetime(2016, 4, 22, 18, 30, 0, 536000, tzinfo=pytz.utc), 'pk': 97})
specific = OccurrenceSpecific.OperationalOcc.objects.create(occurrence=occurrence, **{'working_condition': u'Y'})
tto = TagToOccurrence.objects.create(user_creator=get_userextension("ad"), user_occurrence_id=97, occurrence=occurrence)

	# Beyond the dark portal
occurrence = Occurrence.objects.create(created_by=get_userextension("ad"), owner=get_person({'first_name': 'Adrien'}), release=Release.objects.get(pk=100), **{'origin': u'OR', 'blister': False, 'add_date': datetime.datetime(2016, 4, 22, 18, 30, 0, 536000, tzinfo=pytz.utc), 'lastmodif_date': datetime.datetime(2016, 4, 22, 18, 30, 0, 536000, tzinfo=pytz.utc), 'pk': 98, 'purchase_price': None})
occurrence.attributes.add( OccurrenceAnyAttribute(occurrence=occurrence, value=u'M', attribute_id=get_corresponding_release_attribute(release=100, note='', lookup_dict={'category__name': u'content', 'name': u'self'}).pk, attribute_type=ReleaseAttribute_contenttype), bulk=False )
occurrence.attributes.add( OccurrenceAnyAttribute(occurrence=occurrence, value=u'M', attribute_id=get_corresponding_release_attribute(release=100, note='', lookup_dict={'category__name': u'packaging', 'name': u'jewel box'}).pk, attribute_type=ReleaseAttribute_contenttype), bulk=False )
occurrence.attributes.add( OccurrenceAnyAttribute(occurrence=occurrence, value=u'M', attribute_id=get_corresponding_release_attribute(release=100, note='', lookup_dict={'category__name': u'papers', 'name': u'insert: jewel box'}).pk, attribute_type=ReleaseAttribute_contenttype), bulk=False )
specific = OccurrenceSpecific.OperationalOcc.objects.create(occurrence=occurrence, **{'working_condition': u'Y'})
tto = TagToOccurrence.objects.create(user_creator=get_userextension("ad"), user_occurrence_id=98, occurrence=occurrence)
occurrence.admin_post_save() # to generate and save the tag
