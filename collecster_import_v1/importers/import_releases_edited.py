#!/usr/bin/env python

import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Collecster.settings")
django.setup()

from advideogame.models import *
from advideogame.configuration import *
from supervisor.models import *

import datetime

def get_userextension(name):
    return UserExtension.objects.get(user__username=name)

def get_concept(name):
    return Concept.objects.get(distinctive_name=name)

def get_or_create_sysspec(interface_spec_name, lockout_regions=()):
    # IMPORTANT: this method is not exact, as a SysSpec with additional lockout regions would be accepted too.
    ispec = InterfacesSpecification.objects.get(internal_name=interface_spec_name)
    qs = SystemSpecification.objects.filter(interfaces_specification=ispec)
    for region in lockout_regions:
        if region:
            qs = qs.filter(regional_lockout=LockoutRegion.objects.get(region_name=region))
    
    if qs.count() == 0:
        sys_spec = SystemSpecification.objects.create(interfaces_specification=ispec)
        for region in lockout_regions:
            if region:
                sys_spec.regional_lockout.add(LockoutRegion.objects.get(region_name=region))
        return get_or_create_sysspec(interface_spec_name, lockout_regions)
    elif qs.count() == 1:
        if qs[0].regional_lockout.all().count() > len(lockout_regions):
            raise Exception("Found a superset with {} elements instead of {}.".format(", ".join([str(lk) for lk in qs[0].regional_lockout.all()]), len(lockout_regions)))
            #raise Exception("Found a superset with {} elements instead of {}.")
        return qs[0]
    else:
        raise Exception

    # Manual split Thy Flesh Consumed
release = Release.objects.create(created_by=get_userextension("ad"), concept=get_concept(u'Thy Flesh Consumed'),
                                  **{'immaterial': True, 'pk': 99})
specific = ReleaseSpecific.Software.objects.create(release=release, **{'publisher': None, 'collection_label': None, 'porter': None})

	#DOOM
release = Release.objects.create(created_by=get_userextension("ad"), concept=get_concept(u'DOOM'),
                                  **{'name': u'The Ultimate DOOM', 'immaterial': False, 'partial_date_precision': 'YYYY', 'unsure_region': True, 'partial_date': datetime.date(1995, 1, 1), 'pk': 1}
)
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'content', 'name': u'self'}))), bulk=False )
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'packaging', 'name': u'cardboard box'}))), bulk=False )
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'packaging', 'name': u'jewel box'}))), bulk=False )
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'papers', 'name': u'insert: jewel box'}))), bulk=False )
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'papers', 'name': u'manual'}))), bulk=False )
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'papers', 'name': u'registration card'}))), bulk=False )
release.release_regions.add( ReleaseRegion.objects.get(Q(**{'name': 'EU'})) )
specific = ReleaseSpecific.Software.objects.create(release=release, **{'publisher': Company.objects.get(Q(**{'name': u'GT Interactive'})), 'collection_label': None, 'porter': None})
release.system_specification = get_or_create_sysspec("PC-CD", ())
release.save()
ReleaseComposition.objects.create(from_release=release, to_release=Release.objects.get(Q(**{'pk': 99})))

	#Nights into Dreams
release = Release.objects.create(created_by=get_userextension("ad"), concept=get_concept(u'Nights into Dreams'),
                                  **{'name': u'', 'immaterial': False, 'partial_date_precision': 'YYYY', 'unsure_region': True, 'partial_date': datetime.date(1996, 1, 1), 'pk': 2}
)
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'content', 'name': u'self'}))), bulk=False )
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'packaging', 'name': u'jewel box'}))), bulk=False )
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'papers', 'name': u'insert: jewel box'}))), bulk=False )
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'papers', 'name': u'manual'}))), bulk=False )
release.release_regions.add( ReleaseRegion.objects.get(Q(**{'name': 'EU'})) )
specific = ReleaseSpecific.Software.objects.create(release=release, **{'publisher': Company.objects.get(Q(**{'name': u'Sega'})), 'collection_label': None, 'porter': None})
release.system_specification = get_or_create_sysspec("Saturn game", ("PAL",))
release.save()

	#Dragon Ball Z: Shin Butōden
release = Release.objects.create(created_by=get_userextension("ad"), concept=get_concept(u'Dragon Ball Z: Shin But\u014dden'),
                                  **{'name': u'', 'immaterial': False, 'partial_date_precision': 'DD', 'unsure_region': False, 'partial_date': datetime.date(1995, 11, 17), 'pk': 3}
)
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'content', 'name': u'self'}))), bulk=False )
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'packaging', 'name': u'jewel box'}))), bulk=False )
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'packaging', 'name': u'spine card'}))), bulk=False )
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'papers', 'name': u'insert: jewel box'}))), bulk=False )
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'papers', 'name': u'manual'}))), bulk=False )
release.release_regions.add( ReleaseRegion.objects.get(Q(**{'name': 'JP'})) )
specific = ReleaseSpecific.Software.objects.create(release=release, **{'publisher': Company.objects.get(Q(**{'name': u'Bandai'})), 'collection_label': None, 'porter': None})
release.system_specification = get_or_create_sysspec("Saturn game", ("NTSC-J",))
release.save()

	#Virtua Fighter 2
release = Release.objects.create(created_by=get_userextension("ad"), concept=get_concept(u'Virtua Fighter 2'),
                                  **{'name': u'', 'immaterial': False, 'partial_date_precision': 'YYYY', 'unsure_region': True, 'partial_date': datetime.date(1995, 1, 1), 'pk': 4}
)
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'content', 'name': u'self'}))), bulk=False )
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'packaging', 'name': u'dvd box'}))), bulk=False )
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'papers', 'name': u'manual'}))), bulk=False )
release.release_regions.add( ReleaseRegion.objects.get(Q(**{'name': 'EU'})) )
specific = ReleaseSpecific.Software.objects.create(release=release, **{'publisher': Company.objects.get(Q(**{'name': u'Sega'})), 'collection_label': None, 'porter': None})
release.system_specification = get_or_create_sysspec("Saturn game", ("PAL",))
release.save()

	#Bug!
release = Release.objects.create(created_by=get_userextension("ad"), concept=get_concept(u'Bug!'),
                                  **{'name': u'', 'immaterial': False, 'partial_date_precision': 'DD', 'unsure_region': True, 'partial_date': datetime.date(1995, 9, 15), 'pk': 5}
)
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'content', 'name': u'self'}))), bulk=False )
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'packaging', 'name': u'dvd box'}))), bulk=False )
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'papers', 'name': u'manual'}))), bulk=False )
release.release_regions.add( ReleaseRegion.objects.get(Q(**{'name': 'EU'})) )
specific = ReleaseSpecific.Software.objects.create(release=release, **{'publisher': Company.objects.get(Q(**{'name': u'Sega'})), 'collection_label': None, 'porter': None})
release.system_specification = get_or_create_sysspec("Saturn game", ("PAL",))
release.save()

	#Bug Too!
release = Release.objects.create(created_by=get_userextension("ad"), concept=get_concept(u'Bug Too!'),
                                  **{'name': u'', 'immaterial': False, 'partial_date_precision': 'YYYY', 'unsure_region': True, 'partial_date': datetime.date(1997, 1, 1), 'pk': 6}
)
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'content', 'name': u'self'}))), bulk=False )
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'packaging', 'name': u'dvd box'}))), bulk=False )
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'papers', 'name': u'manual'}))), bulk=False )
release.release_regions.add( ReleaseRegion.objects.get(Q(**{'name': 'EU'})) )
specific = ReleaseSpecific.Software.objects.create(release=release, **{'publisher': Company.objects.get(Q(**{'name': u'Sega'})), 'collection_label': None, 'porter': None})
release.system_specification = get_or_create_sysspec("Saturn game", ("PAL",))
release.save()

	#Mighty Hits
release = Release.objects.create(created_by=get_userextension("ad"), concept=get_concept(u'Mighty Hits'),
                                  **{'name': u'', 'immaterial': False, 'partial_date_precision': 'YYYY', 'unsure_region': True, 'partial_date': datetime.date(1996, 1, 1), 'pk': 7}
)
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'content', 'name': u'self'}))), bulk=False )
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'packaging', 'name': u'dvd box'}))), bulk=False )
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'papers', 'name': u'manual'}))), bulk=False )
release.release_regions.add( ReleaseRegion.objects.get(Q(**{'name': 'EU'})) )
specific = ReleaseSpecific.Software.objects.create(release=release, **{'publisher': Company.objects.get(Q(**{'name': u'Sega'})), 'collection_label': None, 'porter': None})
release.system_specification = get_or_create_sysspec("Saturn game", ("PAL",))
release.save()

	#NightStone
release = Release.objects.create(created_by=get_userextension("ad"), concept=get_concept(u'NightStone'),
        **{'name': u'', 'immaterial': False, 'partial_date_precision': 'DD', 'unsure_region': True, 'partial_date': datetime.date(2002, 4, 16), 'pk': 8, "unsure_content": True,}
)
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'content', 'name': u'self'}))), bulk=False )
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'packaging', 'name': u'cardboard box'}))), bulk=False )
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'packaging', 'name': u'jewel box'}))), bulk=False )
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'papers', 'name': u'insert: jewel box'}))), bulk=False )
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'papers', 'name': u'manual'}))), bulk=False )
release.release_regions.add( ReleaseRegion.objects.get(Q(**{'name': 'EU'})) )
specific = ReleaseSpecific.Software.objects.create(release=release, **{'publisher': Company.objects.get(Q(**{'name': u'Virgin Interactive'})), 'collection_label': None, 'porter': None})
release.system_specification = get_or_create_sysspec("PC-CD", ("",))
release.save()

	#The Beatles: Rock Band
release = Release.objects.create(created_by=get_userextension("ad"), concept=get_concept(u'The Beatles: Rock Band'),
        **{'name': u'', 'immaterial': False, 'partial_date_precision': 'DD', 'unsure_region': True, 'partial_date': datetime.date(2009, 9, 9), 'pk': 10, "unsure_content": True,}
)
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'content', 'name': u'self'}))), bulk=False )
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'packaging', 'name': u'dvd box'}))), bulk=False )
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'papers', 'name': u'manual'}))), bulk=False )
release.release_regions.add( ReleaseRegion.objects.get(Q(**{'name': 'EU'})) )
specific = ReleaseSpecific.Software.objects.create(release=release, **{'publisher': Company.objects.get(Q(**{'name': u'MTV Games'})), 'collection_label': None, 'porter': None})
release.system_specification = get_or_create_sysspec("PlayStation 3 game", ("",))
release.save()

    #Singstar Microphone
release = Release.objects.create(created_by=get_userextension("ad"), concept=get_concept(u'Singstar Microphone'),
                                  **{'name': u'Singstar-The Beatles Rock Band', 'immaterial': False, 'partial_date_precision': 'DD', 'unsure_region': True, 'partial_date': datetime.date(2009, 11, 19), 'version': '', 'pk': 9}
)
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'content', 'name': u'self'})), note="red"), bulk=False )
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'content', 'name': u'self'})), note="blue"), bulk=False )
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'content', 'name': u'receiver interface'}))), bulk=False )
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'packaging', 'name': u'transparent thermoplastic'}))), bulk=False )
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': 'packaging', 'name': 'printed cardboard inlay'}))), bulk=False )
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'papers', 'name': u'manual'}))), bulk=False )
ReleaseComposition.objects.create(from_release=release, to_release=Release.objects.get(Q(**{'pk': 10})))
release.release_regions.add( ReleaseRegion.objects.get(Q(**{'name': 'EU'})) )
specific = ReleaseSpecific.Hardware.objects.create(release=release, **{'manufacturer': None})
specific.colors.add(Color.objects.get(Q(**{'name': u'Red'})))
specific.colors.add(Color.objects.get(Q(**{'name': u'Blue'})))
release.system_specification = get_or_create_sysspec("PlayStation 3 USB accessory", ("",))
release.save()

	#Buzz!: Brain of...
release = Release.objects.create(created_by=get_userextension("ad"), concept=get_concept(u'Buzz!: Brain of...'),
        **{'name': u'Buzz!: Le Plus Malin Des Fran\xe7ais', 'immaterial': False, 'partial_date_precision': 'DD', 'unsure_region': False, 'partial_date': datetime.date(2009, 3, 27), 'pk': 11, "unsure_content": True}
)
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'content', 'name': u'self'}))), bulk=False )
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'packaging', 'name': u'dvd box'}))), bulk=False )
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'papers', 'name': u'manual'}))), bulk=False )
release.release_regions.add( ReleaseRegion.objects.get(Q(**{'name': 'FR'})) )
specific = ReleaseSpecific.Software.objects.create(release=release, **{'publisher': Company.objects.get(Q(**{'name': u'Sony Computer Entertainment Europe'})), 'collection_label': None, 'porter': None})
release.system_specification = get_or_create_sysspec("PlayStation 2 game", ("PAL",))
release.save()

	#Buzz!: The Hollywood Quiz
release = Release.objects.create(created_by=get_userextension("ad"), concept=get_concept(u'Buzz!: The Hollywood Quiz'),
        **{'name': u'Buzz!: Hollywood Quiz', 'immaterial': False, 'partial_date_precision': 'DD', 'unsure_region': True, 'partial_date': datetime.date(2007, 10, 24), 'pk': 12, "unsure_content": True,}
)
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'content', 'name': u'self'}))), bulk=False )
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'packaging', 'name': u'dvd box'}))), bulk=False )
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'papers', 'name': u'manual'}))), bulk=False )
release.release_regions.add( ReleaseRegion.objects.get(Q(**{'name': 'EU'})) )
specific = ReleaseSpecific.Software.objects.create(release=release, **{'publisher': Company.objects.get(Q(**{'name': u'Sony Computer Entertainment Europe'})), 'collection_label': None, 'porter': None})
release.system_specification = get_or_create_sysspec("PlayStation 2 game", ("PAL",))
release.save()

	#Buzz!: The Pop Quiz
release = Release.objects.create(created_by=get_userextension("ad"), concept=get_concept(u'Buzz!: The Pop Quiz'),
        **{'name': u'Buzz!: Le Quiz Pop', 'immaterial': False, 'partial_date_precision': 'YYYY', 'unsure_region': True, 'partial_date': datetime.date(2008, 1, 1), 'pk': 13, "unsure_content": True,}
)
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'content', 'name': u'self'}))), bulk=False )
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'packaging', 'name': u'dvd box'}))), bulk=False )
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'papers', 'name': u'manual'}))), bulk=False )
release.release_regions.add( ReleaseRegion.objects.get(Q(**{'name': 'EU'})) )
specific = ReleaseSpecific.Software.objects.create(release=release, **{'publisher': Company.objects.get(Q(**{'name': u'Sony Computer Entertainment Europe'})), 'collection_label': None, 'porter': None})
release.system_specification = get_or_create_sysspec("PlayStation 2 game", ("PAL",))
release.save()

	#Buzz! Buzzer
release = Release.objects.create(created_by=get_userextension("ad"), concept=get_concept(u'Buzz! Buzzer'),
                                  **{'pk': 14, 'version': '', 'unsure_region': True, 'name': u'"Buzz! Buzzers incl. 3 games (GiFi)"', 'immaterial': False}
)
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'content', 'name': u'self'})), note="1"), bulk=False )
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'content', 'name': u'self'})), note="2"), bulk=False )
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'content', 'name': u'self'})), note="3"), bulk=False )
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'content', 'name': u'self'})), note="4"), bulk=False )
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'content', 'name': u'receiver interface'}))), bulk=False )
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'packaging', 'name': u'transparent thermoplastic'}))), bulk=False )
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': 'packaging', 'name': 'printed cardboard inlay'}))), bulk=False )
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'papers', 'name': u'manual'}))), bulk=False )
ReleaseComposition.objects.create(from_release=release, to_release=Release.objects.get(Q(**{'pk': 11})))
ReleaseComposition.objects.create(from_release=release, to_release=Release.objects.get(Q(**{'pk': 12})))
ReleaseComposition.objects.create(from_release=release, to_release=Release.objects.get(Q(**{'pk': 13})))
release.release_regions.add( ReleaseRegion.objects.get(Q(**{'name': 'EU'})) )
specific = ReleaseSpecific.Hardware.objects.create(release=release, **{'manufacturer': None})
specific.colors.add(Color.objects.get(Q(**{'name': u'Black'})))
release.system_specification = get_or_create_sysspec("PlayStation 2 USB accessory", ("",))
release.save()

	#Virtua Cop 2
release = Release.objects.create(created_by=get_userextension("ad"), concept=get_concept(u'Virtua Cop 2'),
                                  **{'name': u'', 'immaterial': False, 'partial_date_precision': 'YYYY', 'unsure_region': True, 'partial_date': datetime.date(1996, 1, 1), 'pk': 15}
)
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'content', 'name': u'self'}))), bulk=False )
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'packaging', 'name': u'jewel box'}))), bulk=False )
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'papers', 'name': u'insert: jewel box'}))), bulk=False )
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'papers', 'name': u'manual'}))), bulk=False )
release.release_regions.add( ReleaseRegion.objects.get(Q(**{'name': 'EU'})) )
specific = ReleaseSpecific.Software.objects.create(release=release, **{'publisher': Company.objects.get(Q(**{'name': u'Sega'})), 'collection_label': None, 'porter': None})
release.system_specification = get_or_create_sysspec("Saturn game", ("PAL",))
release.save()

	#The House of the Dead
release = Release.objects.create(created_by=get_userextension("ad"), concept=get_concept(u'The House of the Dead'),
                                  **{'name': u'', 'immaterial': False, 'partial_date_precision': 'YYYY', 'unsure_region': True, 'partial_date': datetime.date(1998, 1, 1), 'pk': 16}
)
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'content', 'name': u'self'}))), bulk=False )
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'packaging', 'name': u'jewel box'}))), bulk=False )
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'papers', 'name': u'insert: jewel box'}))), bulk=False )
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'papers', 'name': u'manual'}))), bulk=False )
release.release_regions.add( ReleaseRegion.objects.get(Q(**{'name': 'EU'})) )
specific = ReleaseSpecific.Software.objects.create(release=release, **{'publisher': Company.objects.get(Q(**{'name': u'Sega'})), 'collection_label': None, 'porter': None})
release.system_specification = get_or_create_sysspec("Saturn game", ("PAL",))
release.save()

	#Dragon Ball Z: The Legend
release = Release.objects.create(created_by=get_userextension("ad"), concept=get_concept('Dragon Ball Z: The Legend'),
                                  **{'name': u'Dragon Ball Z The Legend', 'immaterial': False, 'partial_date_precision': 'YYYY', 'unsure_region': False, 'partial_date': datetime.date(1996, 1, 1), 'pk': 17}
)
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'content', 'name': u'self'}))), bulk=False )
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'packaging', 'name': u'dvd box'}))), bulk=False )
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'papers', 'name': u'manual'}))), bulk=False )
release.release_regions.add( ReleaseRegion.objects.get(Q(**{'name': 'ES'})) )
specific = ReleaseSpecific.Software.objects.create(release=release, **{'publisher': Company.objects.get(Q(**{'name': u'Bandai'})), 'collection_label': None, 'porter': None})
release.system_specification = get_or_create_sysspec("Saturn game", ("PAL",))
release.save()

	#Die Hard Arcade
release = Release.objects.create(created_by=get_userextension("ad"), concept=get_concept(u'Die Hard Arcade'),
                                  **{'name': u'', 'immaterial': False, 'partial_date_precision': 'YYYY', 'unsure_region': True, 'partial_date': datetime.date(1997, 1, 1), 'pk': 18}
)
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'content', 'name': u'self'}))), bulk=False )
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'packaging', 'name': u'dvd box'}))), bulk=False )
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'papers', 'name': u'manual'}))), bulk=False )
release.release_regions.add( ReleaseRegion.objects.get(Q(**{'name': 'EU'})) )
specific = ReleaseSpecific.Software.objects.create(release=release, **{'publisher': Company.objects.get(Q(**{'name': u'Sega'})), 'collection_label': None, 'porter': None})
release.system_specification = get_or_create_sysspec("Saturn game", ("PAL",))
release.save()

	#Virtua Cop
release = Release.objects.create(created_by=get_userextension("ad"), concept=get_concept(u'Virtua Cop'),
                                  **{'name': u'', 'immaterial': False, 'partial_date_precision': 'YYYY', 'unsure_region': True, 'partial_date': datetime.date(1995, 1, 1), 'pk': 19}
)
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'packaging', 'name': u'jewel box'}))), bulk=False )
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'papers', 'name': u'insert: jewel box'}))), bulk=False )
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'papers', 'name': u'manual'}))), bulk=False )
release.release_regions.add( ReleaseRegion.objects.get(Q(**{'name': 'EU'})) )
specific = ReleaseSpecific.Software.objects.create(release=release, **{'publisher': Company.objects.get(Q(**{'name': u'Sega'})), 'collection_label': None, 'porter': None})
release.system_specification = get_or_create_sysspec("Saturn game", ("PAL",))
release.save()

	#Virtua Gun
release = Release.objects.create(created_by=get_userextension("ad"), concept=get_concept(u'Virtua Gun'),
                                  **{'pk': 20, 'version': u'MK-80311', 'unsure_region': True, 'name': u'"Virtua Gun & Virtua Cop"', 'immaterial': False}
)
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'content', 'name': u'self'}))), bulk=False )
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'packaging', 'name': u'cardboard box'}))), bulk=False )
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'packaging', 'name': u'cardboard inlay non-decorative'}))), bulk=False )
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'papers', 'name': u'manual'}))), bulk=False )
ReleaseComposition.objects.create(from_release=release, to_release=Release.objects.get(Q(**{'pk': 19})))
release.release_regions.add( ReleaseRegion.objects.get(Q(**{'name': 'EU'})) )
specific = ReleaseSpecific.Hardware.objects.create(release=release, **{'manufacturer': Company.objects.get(Q(**{'name': u'Sega'}))})
specific.colors.add(Color.objects.get(Q(**{'name': u'Blue'})))
release.system_specification = get_or_create_sysspec("Saturn controller", ("",))
release.save()

	#Virtua Gun
release = Release.objects.create(created_by=get_userextension("ad"), concept=get_concept(u'Virtua Gun'),
                                  **{'pk': 21, 'version': u'MK-80311', 'unsure_region': True, 'name': u'"Virtua Gun & Virtua Cop 2"', 'immaterial': False}
)
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'content', 'name': u'self'}))), bulk=False )
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'packaging', 'name': u'cardboard box'}))), bulk=False )
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'packaging', 'name': u'cardboard inlay non-decorative'}))), bulk=False )
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'papers', 'name': u'manual'}))), bulk=False )
ReleaseComposition.objects.create(from_release=release, to_release=Release.objects.get(Q(**{'pk': 15})))
release.release_regions.add( ReleaseRegion.objects.get(Q(**{'name': 'EU'})) )
specific = ReleaseSpecific.Hardware.objects.create(release=release, **{'manufacturer': Company.objects.get(Q(**{'name': u'Sega'}))})
specific.colors.add(Color.objects.get(Q(**{'name': u'Blue'})))
release.system_specification = get_or_create_sysspec("Saturn controller", ("",))
release.save()

	#Virtua Gun
release = Release.objects.create(created_by=get_userextension("ad"), concept=get_concept(u'Virtua Gun'),
        **{'pk': 22, 'version': u'MK-80311', 'unsure_region': True, 'name': u'', 'immaterial': False, 'special_case_release': 'L', }
)
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'content', 'name': u'self'}))), bulk=False )
release.release_regions.add( ReleaseRegion.objects.get(Q(**{'name': 'EU'})) )
ReleaseDistinction.objects.create(release=release, distinction=Distinction.objects.get(name="iron sight"), value="narrow")
specific = ReleaseSpecific.Hardware.objects.create(release=release, **{'manufacturer': Company.objects.get(Q(**{'name': u'Sega'}))})
specific.colors.add(Color.objects.get(Q(**{'name': u'Blue'})))
release.system_specification = get_or_create_sysspec("Saturn controller", ("",))
release.save()

	#Virtua Gun
release = Release.objects.create(created_by=get_userextension("ad"), concept=get_concept(u'Virtua Gun'),
                                  **{'pk': 23, 'version': u'HSS-0122', 'unsure_region': False, 'name': u'', 'immaterial': False, 'special_case_release': 'L', }
)
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'content', 'name': u'self'}))), bulk=False )
release.release_regions.add( ReleaseRegion.objects.get(Q(**{'name': 'JP'})) )
specific = ReleaseSpecific.Hardware.objects.create(release=release, **{'manufacturer': Company.objects.get(Q(**{'name': u'Sega'}))})
specific.colors.add(Color.objects.get(Q(**{'name': u'Black'})))
release.system_specification = get_or_create_sysspec("Saturn controller", ("",))
release.save()

	#Worms
release = Release.objects.create(created_by=get_userextension("ad"), concept=get_concept(u'Worms'),
                                  **{'name': u'', 'immaterial': False, 'partial_date_precision': 'YYYY', 'unsure_region': True, 'partial_date': datetime.date(1997, 1, 1), 'pk': 24}
)
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'content', 'name': u'self'}))), bulk=False )
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'packaging', 'name': u'dvd box'}))), bulk=False )
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'papers', 'name': u'manual'}))), bulk=False )
release.release_regions.add( ReleaseRegion.objects.get(Q(**{'name': 'EU'})) )
specific = ReleaseSpecific.Software.objects.create(release=release, **{'publisher': Company.objects.get(Q(**{'name': u'Ocean Software'})), 'collection_label': None, 'porter': None})
release.system_specification = get_or_create_sysspec("Saturn game", ("PAL",))
release.save()

	#Sega Rally Championship
release = Release.objects.create(created_by=get_userextension("ad"), concept=get_concept(u'Sega Rally Championship'),
                                  **{'name': u'', 'immaterial': False, 'partial_date_precision': 'YYYY', 'unsure_region': True, 'partial_date': datetime.date(1995, 1, 1), 'pk': 25}
)
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'content', 'name': u'self'}))), bulk=False )
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'packaging', 'name': u'dvd box'}))), bulk=False )
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'papers', 'name': u'manual'}))), bulk=False )
release.release_regions.add( ReleaseRegion.objects.get(Q(**{'name': 'EU'})) )
specific = ReleaseSpecific.Software.objects.create(release=release, **{'publisher': Company.objects.get(Q(**{'name': u'Sega'})), 'collection_label': None, 'porter': None})
release.system_specification = get_or_create_sysspec("Saturn game", ("PAL",))
release.save()

	#Daytona USA
release = Release.objects.create(created_by=get_userextension("ad"), concept=get_concept(u'Daytona USA'),
                                  **{'name': u'Daytona USA Championship Circuit Edition', 'immaterial': False, 'partial_date_precision': 'YYYY', 'unsure_region': True, 'partial_date': datetime.date(1995, 1, 1), 'pk': 26}
)
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'content', 'name': u'self'}))), bulk=False )
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'packaging', 'name': u'dvd box'}))), bulk=False )
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'papers', 'name': u'manual'}))), bulk=False )
release.release_regions.add( ReleaseRegion.objects.get(Q(**{'name': 'EU'})) )
specific = ReleaseSpecific.Software.objects.create(release=release, **{'publisher': Company.objects.get(Q(**{'name': u'Sega'})), 'collection_label': None, 'porter': None})
release.system_specification = get_or_create_sysspec("Saturn game", ("PAL",))
release.save()

	#Marvel Super Heroes
release = Release.objects.create(created_by=get_userextension("ad"), concept=get_concept(u'Marvel Super Heroes'),
                                  **{'name': u'', 'immaterial': False, 'partial_date_precision': 'MM', 'unsure_region': True, 'partial_date': datetime.date(1997, 12, 1), 'pk': 27}
)
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'content', 'name': u'self'}))), bulk=False )
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'packaging', 'name': u'dvd box'}))), bulk=False )
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'papers', 'name': u'manual'}))), bulk=False )
release.release_regions.add( ReleaseRegion.objects.get(Q(**{'name': 'EU'})) )
specific = ReleaseSpecific.Software.objects.create(release=release, **{'publisher': Company.objects.get(Q(**{'name': u'Capcom'})), 'collection_label': None, 'porter': None})
release.system_specification = get_or_create_sysspec("Saturn game", ("PAL",))
release.save()

	#Sega Touring Car Championship
release = Release.objects.create(created_by=get_userextension("ad"), concept=get_concept(u'Sega Touring Car Championship'),
                                  **{'name': u'', 'immaterial': False, 'partial_date_precision': 'YYYY', 'unsure_region': True, 'partial_date': datetime.date(1997, 1, 1), 'pk': 28}
)
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'content', 'name': u'self'}))), bulk=False )
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'packaging', 'name': u'dvd box'}))), bulk=False )
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'papers', 'name': u'leaflet'}))), bulk=False )
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'papers', 'name': u'manual'}))), bulk=False )
release.release_regions.add( ReleaseRegion.objects.get(Q(**{'name': 'EU'})) )
specific = ReleaseSpecific.Software.objects.create(release=release, **{'publisher': Company.objects.get(Q(**{'name': u'Sega'})), 'collection_label': None, 'porter': None})
release.system_specification = get_or_create_sysspec("Saturn game", ("PAL",))
release.save()

	#Formula Karts Special Edition
release = Release.objects.create(created_by=get_userextension("ad"), concept=get_concept(u'Formula Karts Special Edition'),
                                  **{'name': u'', 'immaterial': False, 'partial_date_precision': 'YYYY', 'unsure_region': True, 'partial_date': datetime.date(1997, 1, 1), 'pk': 30}
)
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'content', 'name': u'self'}))), bulk=False )
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'packaging', 'name': u'dvd box'}))), bulk=False )
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'papers', 'name': u'manual'}))), bulk=False )
release.release_regions.add( ReleaseRegion.objects.get(Q(**{'name': 'EU'})) )
specific = ReleaseSpecific.Software.objects.create(release=release, **{'publisher': Company.objects.get(Q(**{'name': u'Sega'})), 'collection_label': None, 'porter': None})
release.system_specification = get_or_create_sysspec("Saturn game", ("PAL",))
release.save()

	#Sonic Jam
release = Release.objects.create(created_by=get_userextension("ad"), concept=get_concept(u'Sonic Jam'),
                                  **{'name': u'', 'immaterial': False, 'partial_date_precision': 'DD', 'unsure_region': True, 'partial_date': datetime.date(1997, 8, 28), 'pk': 31}
)
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'content', 'name': u'self'}))), bulk=False )
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'packaging', 'name': u'dvd box'}))), bulk=False )
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'papers', 'name': u'manual'}))), bulk=False )
release.release_regions.add( ReleaseRegion.objects.get(Q(**{'name': 'EU'})) )
specific = ReleaseSpecific.Software.objects.create(release=release, **{'publisher': Company.objects.get(Q(**{'name': u'Sega'})), 'collection_label': None, 'porter': None})
release.system_specification = get_or_create_sysspec("Saturn game", ("PAL",))
release.save()

	#Duke Nukem 3D
release = Release.objects.create(created_by=get_userextension("ad"), concept=get_concept(u'Duke Nukem 3D'),
                                  **{'name': u'', 'immaterial': False, 'partial_date_precision': 'YYYY', 'unsure_region': True, 'partial_date': datetime.date(1997, 1, 1), 'pk': 32}
)
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'content', 'name': u'self'}))), bulk=False )
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'packaging', 'name': u'dvd box'}))), bulk=False )
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'papers', 'name': u'manual'}))), bulk=False )
release.release_regions.add( ReleaseRegion.objects.get(Q(**{'name': 'EU'})) )
specific = ReleaseSpecific.Software.objects.create(release=release, **{'publisher': Company.objects.get(Q(**{'name': u'Sega'})), 'collection_label': None, 'porter': None})
release.system_specification = get_or_create_sysspec("Saturn game", ("PAL",))
release.save()

	#DoDonPachi
release = Release.objects.create(created_by=get_userextension("ad"), concept=get_concept(u'DoDonPachi'),
                                  **{'name': u'', 'immaterial': False, 'partial_date_precision': 'YYYY', 'unsure_region': False, 'partial_date': datetime.date(1998, 1, 1), 'pk': 33}
)
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'content', 'name': u'self'}))), bulk=False )
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'packaging', 'name': u'jewel box'}))), bulk=False )
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'packaging', 'name': u'spine card'}))), bulk=False )
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'papers', 'name': u'leaflet'}))), bulk=False )
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'papers', 'name': u'manual'}))), bulk=False )
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'papers', 'name': u'registration card'}))), bulk=False )
release.release_regions.add( ReleaseRegion.objects.get(Q(**{'name': 'JP'})) )
specific = ReleaseSpecific.Software.objects.create(release=release, **{'publisher': Company.objects.get(Q(**{'name': u'Atlus'})), 'collection_label': None, 'porter': None})
release.system_specification = get_or_create_sysspec("Saturn game", ("NTSC-J",))
release.save()

	#Resident Evil
release = Release.objects.create(created_by=get_userextension("ad"), concept=get_concept(u'Resident Evil'),
                                  **{'name': u'', 'immaterial': False, 'partial_date_precision': 'YYYY', 'unsure_region': True, 'partial_date': datetime.date(1997, 1, 1), 'pk': 34}
)
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'content', 'name': u'self'}))), bulk=False )
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'packaging', 'name': u'dvd box'}))), bulk=False )
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'papers', 'name': u'manual'}))), bulk=False )
release.release_regions.add( ReleaseRegion.objects.get(Q(**{'name': 'EU'})) )
specific = ReleaseSpecific.Software.objects.create(release=release, **{'publisher': Company.objects.get(Q(**{'name': u'Capcom'})), 'collection_label': None, 'porter': None})
release.system_specification = get_or_create_sysspec("Saturn game", ("PAL",))
release.save()

	#Virtua Cop
release = Release.objects.create(created_by=get_userextension("ad"), concept=get_concept(u'Virtua Cop'),
                                  **{'name': u'', 'immaterial': False, 'partial_date_precision': 'YYYY', 'unsure_region': True, 'partial_date': datetime.date(1995, 1, 1), 'pk': 35}
)
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'content', 'name': u'self'}))), bulk=False )
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'packaging', 'name': u'dvd box'}))), bulk=False )
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'papers', 'name': u'manual'}))), bulk=False )
release.release_regions.add( ReleaseRegion.objects.get(Q(**{'name': 'EU'})) )
specific = ReleaseSpecific.Software.objects.create(release=release, **{'publisher': Company.objects.get(Q(**{'name': u'Sega'})), 'collection_label': None, 'porter': None})
release.system_specification = get_or_create_sysspec("Saturn game", ("PAL",))
release.save()

	#Sega Saturn Control Pad
release = Release.objects.create(created_by=get_userextension("ad"), concept=get_concept('Sega Saturn Control Pad'),
                                  **{'name': u'', 'immaterial': False, 'unsure_region': True, 'version': u'Model 1', 'special_case_release': 'L', 'pk': 36}
)
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'content', 'name': u'self'}))), bulk=False )
release.release_regions.add( ReleaseRegion.objects.get(Q(**{'name': 'EU'})) )
specific = ReleaseSpecific.Hardware.objects.create(release=release, **{'manufacturer': Company.objects.get(Q(**{'name': u'Sega'}))})
specific.colors.add(Color.objects.get(Q(**{'name': u'Black'})))
release.system_specification = get_or_create_sysspec("Saturn controller", ("",))
release.save()

	#Sega Saturn Control Pad
release = Release.objects.create(created_by=get_userextension("ad"), concept=get_concept('Sega Saturn Control Pad'),
                                  **{'pk': 37, 'version': u'Model 2', 'unsure_region': False, 'name': u'', 'immaterial': False, 'special_case_release': 'C', }
)
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'content', 'name': u'self'}))), bulk=False )
specific = ReleaseSpecific.Hardware.objects.create(release=release, **{'manufacturer': Company.objects.get(Q(**{'name': u'Sega'}))})
specific.colors.add(Color.objects.get(Q(**{'name': u'Black'})))
release.system_specification = get_or_create_sysspec("Saturn controller", ("",))
release.save()

	#Pad Saturn ST.2
release = Release.objects.create(created_by=get_userextension("ad"), concept=get_concept(u'Pad Saturn ST.2'),
                                  **{'pk': 38, 'version': u'', 'unsure_region': True, 'name': u'', 'immaterial': False}
)
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'content', 'name': u'self'}))), bulk=False )
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'packaging', 'name': u'cardboard box'}))), bulk=False )
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'papers', 'name': u'manual'}))), bulk=False )
release.release_regions.add( ReleaseRegion.objects.get(Q(**{'name': 'EU'})) )
specific = ReleaseSpecific.Hardware.objects.create(release=release, **{'manufacturer': None})
specific.colors.add(Color.objects.get(Q(**{'name': u'Grey'})))
release.system_specification = get_or_create_sysspec("Saturn controller", ("",))
release.save()

	#3D Control Pad (Saturn)
release = Release.objects.create(created_by=get_userextension("ad"), concept=get_concept('3D Control Pad (Saturn)'),
                                  **{'name': u'"3D Pad Saturn & Nights"', 'immaterial': False, 'partial_date_precision': 'MM', 'unsure_region': True, 'partial_date': datetime.date(1996, 9, 1), 'version': u'', 'pk': 41}
)
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'content', 'name': u'self'}))), bulk=False )
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'packaging', 'name': u'cardboard box'}))), bulk=False )
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'packaging', 'name': u'baggies'}))), bulk=False )
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'packaging', 'name': u'disposable connector protection'}))), bulk=False )
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'packaging', 'name': u'cardboard inlay non-decorative'}))), bulk=False )
ReleaseComposition.objects.create(from_release=release, to_release=Release.objects.get(Q(**{'pk': 2})))
release.release_regions.add( ReleaseRegion.objects.get(Q(**{'name': 'EU'})) )
specific = ReleaseSpecific.Hardware.objects.create(release=release, **{'manufacturer': Company.objects.get(Q(**{'name': u'Sega'}))})
specific.colors.add(Color.objects.get(Q(**{'name': u'Black'})))
release.system_specification = get_or_create_sysspec("Saturn controller", ("",))
release.save()

	#Sega Saturn Bootleg Sampler
release = Release.objects.create(created_by=get_userextension("ad"), concept=get_concept(u'Sega Saturn Bootleg Sampler'),
                                  **{'name': u'', 'immaterial': False, 'partial_date_precision': 'YYYY', 'unsure_region': True, 'partial_date': datetime.date(1995, 1, 1), 'pk': 43}
)
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'content', 'name': u'self'}))), bulk=False )
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'packaging', 'name': u'jewel box'}))), bulk=False )
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'papers', 'name': u'leaflet'}))), bulk=False )
release.release_regions.add( ReleaseRegion.objects.get(Q(**{'name': 'EU'})) )
specific = ReleaseSpecific.Software.objects.create(release=release, **{'publisher': Company.objects.get(Q(**{'name': u'Sega'})), 'collection_label': None, 'porter': None})
specific = ReleaseSpecific.Demo.objects.create(release=release, **{'issue_number': None,})
specific.games_playable.add(*Concept.objects.filter(distinctive_name__in=["Bug!", "Clockwork Knight 2", "Sega Rally Championship", "World Series Baseball",]))
release.system_specification = get_or_create_sysspec("Saturn game", ("PAL",))
release.save()

	#Sega Saturn
release = Release.objects.create(created_by=get_userextension("ad"), concept=get_concept(u'Sega Saturn'),
                                  **{'pk': 42, 'version': u'Model 2', 'unsure_region': True, 'name': u'', 'immaterial': False}
)
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'content', 'name': u'self'}))), bulk=False )
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'packaging', 'name': u'cardboard box'}))), bulk=False )
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'packaging', 'name': u'baggies'}))), bulk=False )
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'packaging', 'name': u'disposable connector protection'}))), bulk=False )
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'packaging', 'name': u'cardboard inlay non-decorative'}))), bulk=False )
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'papers', 'name': u'manual'}))), bulk=False )
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'papers', 'name': u'warranty'}))), bulk=False )
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'content', 'name': u'cord-220v'}))), bulk=False )
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'content', 'name': u'scart'}))), bulk=False )
ReleaseComposition.objects.create(from_release=release, to_release=Release.objects.get(Q(**{'pk': 37})))
ReleaseComposition.objects.create(from_release=release, to_release=Release.objects.get(Q(**{'pk': 43})))
release.release_regions.add( ReleaseRegion.objects.get(Q(**{'name': 'EU'})) )
specific = ReleaseSpecific.Hardware.objects.create(release=release, **{'manufacturer': Company.objects.get(Q(**{'name': u'Sega'}))})
specific.colors.add(Color.objects.get(Q(**{'name': u'Black'})))
specific = ReleaseSpecific.Variant.objects.create(release=release, **{'system_variant': SystemVariant.objects.get(variant_name="Sega Saturn")})
release.system_specification = get_or_create_sysspec("Saturn console", ("PAL",))
release.save()

	#Jet Set Radio
release = Release.objects.create(created_by=get_userextension("ad"), concept=get_concept(u'Jet Set Radio'),
                                  **{'name': u'', 'immaterial': False, 'partial_date_precision': 'YYYY', 'unsure_region': True, 'partial_date': datetime.date(2000, 1, 1), 'pk': 44}
)
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'content', 'name': u'self'}))), bulk=False )
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'packaging', 'name': u'big-jewel box'}))), bulk=False )
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'papers', 'name': u'insert: jewel box'}))), bulk=False )
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'papers', 'name': u'manual'}))), bulk=False )
release.release_regions.add( ReleaseRegion.objects.get(Q(**{'name': 'EU'})) )
specific = ReleaseSpecific.Software.objects.create(release=release, **{'publisher': Company.objects.get(Q(**{'name': u'Sega'})), 'collection_label': None, 'porter': None})
release.system_specification = get_or_create_sysspec("Dreamcast game", ("PAL",))
release.save()

	#Sega Bass Fishing
release = Release.objects.create(created_by=get_userextension("ad"), concept=get_concept(u'Sega Bass Fishing'),
                                  **{'name': u'', 'immaterial': False, 'partial_date_precision': 'YYYY', 'unsure_region': True, 'partial_date': datetime.date(1999, 1, 1), 'pk': 45}
)
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'content', 'name': u'self'}))), bulk=False )
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'packaging', 'name': u'big-jewel box'}))), bulk=False )
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'papers', 'name': u'insert: jewel box'}))), bulk=False )
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'papers', 'name': u'manual'}))), bulk=False )
release.release_regions.add( ReleaseRegion.objects.get(Q(**{'name': 'EU'})) )
specific = ReleaseSpecific.Software.objects.create(release=release, **{'publisher': Company.objects.get(Q(**{'name': u'Sega'})), 'collection_label': None, 'porter': None})
release.system_specification = get_or_create_sysspec("Dreamcast game", ("PAL",))
release.save()

	#Crazy Taxi
release = Release.objects.create(created_by=get_userextension("ad"), concept=get_concept(u'Crazy Taxi'),
                                  **{'name': u'', 'immaterial': False, 'partial_date_precision': 'YYYY', 'unsure_region': True, 'partial_date': datetime.date(1999, 1, 1), 'pk': 46}
)
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'content', 'name': u'self'}))), bulk=False )
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'packaging', 'name': u'big-jewel box'}))), bulk=False )
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'papers', 'name': u'insert: jewel box'}))), bulk=False )
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'papers', 'name': u'manual'}))), bulk=False )
release.release_regions.add( ReleaseRegion.objects.get(Q(**{'name': 'EU'})) )
specific = ReleaseSpecific.Software.objects.create(release=release, **{'publisher': Company.objects.get(Q(**{'name': u'Sega'})), 'collection_label': None, 'porter': None})
release.system_specification = get_or_create_sysspec("Dreamcast game", ("PAL",))
release.save()

	#Confidential Mission
release = Release.objects.create(created_by=get_userextension("ad"), concept=get_concept(u'Confidential Mission'),
                                  **{'name': u'', 'immaterial': False, 'partial_date_precision': 'DD', 'unsure_region': True, 'partial_date': datetime.date(2001, 5, 25), 'pk': 47}
)
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'content', 'name': u'self'}))), bulk=False )
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'packaging', 'name': u'big-jewel box'}))), bulk=False )
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'papers', 'name': u'insert: jewel box'}))), bulk=False )
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'papers', 'name': u'manual'}))), bulk=False )
release.release_regions.add( ReleaseRegion.objects.get(Q(**{'name': 'EU'})) )
specific = ReleaseSpecific.Software.objects.create(release=release, **{'publisher': Company.objects.get(Q(**{'name': u'Sega'})), 'collection_label': None, 'porter': None})
release.system_specification = get_or_create_sysspec("Dreamcast game", ("PAL",))
release.save()

	#Skies of Arcadia
release = Release.objects.create(created_by=get_userextension("ad"), concept=get_concept(u'Skies of Arcadia'),
                                  **{'name': u'', 'immaterial': False, 'partial_date_precision': 'DD', 'unsure_region': True, 'partial_date': datetime.date(2001, 4, 27), 'pk': 48}
)
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'content', 'name': u'self'}))), bulk=False )
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'packaging', 'name': u'big-jewel box'}))), bulk=False )
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'papers', 'name': u'insert: jewel box'}))), bulk=False )
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'papers', 'name': u'manual'}))), bulk=False )
release.release_regions.add( ReleaseRegion.objects.get(Q(**{'name': 'EU'})) )
specific = ReleaseSpecific.Software.objects.create(release=release, **{'publisher': Company.objects.get(Q(**{'name': u'Sega'})), 'collection_label': None, 'porter': None})
release.system_specification = get_or_create_sysspec("Dreamcast game", ("PAL",))
release.save()

	#Capcom vs. SNK: Millennium Fight 2000
release = Release.objects.create(created_by=get_userextension("ad"), concept=get_concept(u'Capcom vs. SNK: Millennium Fight 2000'),
                                  **{'name': u'', 'immaterial': False, 'partial_date_precision': 'YYYY', 'unsure_region': False, 'partial_date': datetime.date(2000, 1, 1), 'pk': 49}
)
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'content', 'name': u'self'}))), bulk=False )
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'packaging', 'name': u'jewel box'}))), bulk=False )
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'papers', 'name': u'insert: jewel box'}))), bulk=False )
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'papers', 'name': u'leaflet'}))), bulk=False )
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'papers', 'name': u'manual'}))), bulk=False )
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'papers', 'name': u'registration card'}))), bulk=False )
release.release_regions.add( ReleaseRegion.objects.get(Q(**{'name': 'JP'})) )
specific = ReleaseSpecific.Software.objects.create(release=release, **{'publisher': Company.objects.get(Q(**{'name': u'Capcom'})), 'collection_label': None, 'porter': None})
release.system_specification = get_or_create_sysspec("Dreamcast game", ("NTSC-J",))
release.save()

	#FIFA 98
release = Release.objects.create(created_by=get_userextension("ad"), concept=get_concept(u'FIFA 98'),
                                  **{'name': u'', 'immaterial': False, 'partial_date_precision': 'YYYY', 'unsure_region': True, 'partial_date': datetime.date(1997, 1, 1), 'pk': 50}
)
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'content', 'name': u'self'}))), bulk=False )
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'packaging', 'name': u'cardboard box'}))), bulk=False )
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'papers', 'name': u'manual'}))), bulk=False )
release.release_regions.add( ReleaseRegion.objects.get(Q(**{'name': 'EU'})) )
specific = ReleaseSpecific.Software.objects.create(release=release, **{'publisher': Company.objects.get(Q(**{'name': u'Electronic Arts'})), 'collection_label': None, 'porter': None})
release.system_specification = get_or_create_sysspec("PC-CD", ("",))
release.save()

	#Dreamcast Vibration Pack
release = Release.objects.create(created_by=get_userextension("ad"), concept=get_concept('Dreamcast Vibration Pack'),
                                  **{'pk': 51, 'version': u'', 'unsure_region': True, 'name': u'', 'special_case_release': 'L', 'immaterial': False}
)
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'content', 'name': u'self'}))), bulk=False )
release.release_regions.add( ReleaseRegion.objects.get(Q(**{'name': 'EU'})) )
specific = ReleaseSpecific.Hardware.objects.create(release=release, **{'manufacturer': Company.objects.get(Q(**{'name': u'Sega'}))})
specific.colors.add(Color.objects.get(Q(**{'name': u'Grey'})))
release.system_specification = get_or_create_sysspec("Dreamcast controller accessory", ("",))
release.save()

	#Visual Memory Unit
release = Release.objects.create(created_by=get_userextension("ad"), concept=get_concept(u'Visual Memory Unit'),
                                  **{'pk': 52, 'version': u'', 'unsure_region': True, 'name': u'', 'immaterial': False}
)
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'content', 'name': u'self'}))), bulk=False )
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'content', 'name': u'intrinsic connector cap'}))), bulk=False )
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'packaging', 'name': u'cardboard box'}))), bulk=False )
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'packaging', 'name': u'cardboard inlay non-decorative'}))), bulk=False )
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'papers', 'name': u'manual'}))), bulk=False )
release.release_regions.add( ReleaseRegion.objects.get(Q(**{'name': 'EU'})) )
specific = ReleaseSpecific.Hardware.objects.create(release=release, **{'manufacturer': Company.objects.get(Q(**{'name': u'Sega'}))})
specific.colors.add(Color.objects.get(Q(**{'name': u'Grey'})))
specific = ReleaseSpecific.BackupMemory.objects.create(release=release, **{'capacity': 200, 'unit': StorageUnit.objects.get(name="block (Dreamcast)")})
release.system_specification = get_or_create_sysspec("Dreamcast controller accessory", ("",))
release.save()

	#Dreamkey
release = Release.objects.create(created_by=get_userextension("ad"), concept=get_concept(u'Dreamkey'),
                                  **{'pk': 54, 'version': u'1.5', 'unsure_region': True, 'name': u'', 'immaterial': False}
)
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'content', 'name': u'self'}))), bulk=False )
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'packaging', 'name': u'jewel box'}))), bulk=False )
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'papers', 'name': u'insert: jewel box'}))), bulk=False )
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'papers', 'name': u'manual'}))), bulk=False )
release.release_regions.add( ReleaseRegion.objects.get(Q(**{'name': 'EU'})) )
specific = ReleaseSpecific.Software.objects.create(release=release, **{'publisher': Company.objects.get(Q(**{'name': u'Sega'})), 'collection_label': None, 'porter': None})
release.system_specification = get_or_create_sysspec("Dreamcast game", ("PAL",))
release.save()

	#Dreamcast Controller
release = Release.objects.create(created_by=get_userextension("ad"), concept=get_concept('Dreamcast Controller'),
                                  **{'pk': 55, 'version': u'', 'unsure_region': False, 'name': u'', 'special_case_release': 'C', 'immaterial': False}
)
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'content', 'name': u'self'}))), bulk=False )
specific = ReleaseSpecific.Hardware.objects.create(release=release, **{'manufacturer': Company.objects.get(Q(**{'name': u'Sega'}))})
specific.colors.add(Color.objects.get(Q(**{'name': u'Grey'})))
release.system_specification = get_or_create_sysspec("Dreamcast controller", ("",))
release.save()

	#Quantum Fighterpad
release = Release.objects.create(created_by=get_userextension("ad"), concept=get_concept(u'Quantum Fighterpad'),
                                  **{'pk': 56, 'version': u'', 'unsure_region': True, 'name': u'', 'special_case_release': 'L', 'immaterial': False}
)
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'content', 'name': u'self'}))), bulk=False )
release.release_regions.add( ReleaseRegion.objects.get(Q(**{'name': 'EU'})) )
specific = ReleaseSpecific.Hardware.objects.create(release=release, **{'manufacturer': Company.objects.get(Q(**{'name': u'InterAct'}))})
specific.colors.add(Color.objects.get(Q(**{'name': u'White'})))
release.system_specification = get_or_create_sysspec("Dreamcast controller", ("",))
release.save()

	#Dream On Collection
release = Release.objects.create(created_by=get_userextension("ad"), concept=get_concept('Dream On Collection'),
                                  **{'pk': 57, 'unsure_region': True, 'name': u'', 'immaterial': False}
)
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'content', 'name': u'self'}))), bulk=False )
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'packaging', 'name': u'jewel box'}))), bulk=False )
release.release_regions.add( ReleaseRegion.objects.get(Q(**{'name': 'EU'})) )
specific = ReleaseSpecific.Software.objects.create(release=release, **{'publisher': Company.objects.get(Q(**{'name': u'Sega'})), 'collection_label': None, 'porter': None})
specific = ReleaseSpecific.Demo.objects.create(release=release, **{'issue_number': 4,})
release.system_specification = get_or_create_sysspec("Dreamcast game", ("PAL",))
release.save()

	#Sega Dreamcast
release = Release.objects.create(created_by=get_userextension("ad"), concept=get_concept(u'Sega Dreamcast'),
                                  **{'name': u'', 'immaterial': False, 'partial_date_precision': 'DD', 'unsure_region': True, 'partial_date': datetime.date(1999, 10, 14), 'version': u'', 'pk': 53}
)
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'content', 'name': u'self'}))), bulk=False )
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'packaging', 'name': u'cardboard box'}))), bulk=False )
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'packaging', 'name': u'baggies'}))), bulk=False )
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'packaging', 'name': u'cardboard inlay non-decorative'}))), bulk=False )
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'papers', 'name': u'manual'}))), bulk=False )
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'papers', 'name': u'warranty'}))), bulk=False )
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'content', 'name': u'cord-220v'}))), bulk=False )
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'content', 'name': u'scart'}))), bulk=False )
ReleaseComposition.objects.create(from_release=release, to_release=Release.objects.get(Q(**{'pk': 55})))
ReleaseComposition.objects.create(from_release=release, to_release=Release.objects.get(Q(**{'pk': 54})))
ReleaseComposition.objects.create(from_release=release, to_release=Release.objects.get(Q(**{'pk': 57})))
release.release_regions.add( ReleaseRegion.objects.get(Q(**{'name': 'EU'})) )
specific = ReleaseSpecific.Hardware.objects.create(release=release, **{'manufacturer': Company.objects.get(Q(**{'name': u'Sega'}))})
specific.colors.add(Color.objects.get(Q(**{'name': u'Grey'})))
specific = ReleaseSpecific.Variant.objects.create(release=release, **{'system_variant': SystemVariant.objects.get(variant_name="", system_concept=Concept.objects.get(distinctive_name="Sega Dreamcast"))})
release.system_specification = get_or_create_sysspec("Dreamcast console", ("PAL",))
release.save()

	#Visual Memory Unit
release = Release.objects.create(created_by=get_userextension("ad"), concept=get_concept(u'Visual Memory Unit'),
                                  **{'pk': 58, 'version': u'', 'unsure_region': True, 'name': u'', 'special_case_release': 'L', 'immaterial': False}
)
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'content', 'name': u'self'}))), bulk=False )
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'content', 'name': u'intrinsic connector cap'}))), bulk=False )
release.release_regions.add( ReleaseRegion.objects.get(Q(**{'name': 'EU'})) )
specific = ReleaseSpecific.Hardware.objects.create(release=release, **{'manufacturer': Company.objects.get(Q(**{'name': u'Sega'}))})
specific.colors.add(Color.objects.get(Q(**{'name': u'Grey'})))
specific = ReleaseSpecific.BackupMemory.objects.create(release=release, **{'capacity': 200, 'unit': StorageUnit.objects.get(name="block (Dreamcast)")})
release.system_specification = get_or_create_sysspec("Dreamcast controller accessory", ("",))
release.save()

	#The Lion King
release = Release.objects.create(created_by=get_userextension("ad"), concept=get_concept(u'The Lion King'),
                                  **{'name': u'', 'immaterial': False, 'unsure_region': True, 'special_case_release': 'L', 'pk': 59}
)
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'content', 'name': u'self'}))), bulk=False )
release.release_regions.add( ReleaseRegion.objects.get(Q(**{'name': 'EU'})) )
specific = ReleaseSpecific.Software.objects.create(release=release, **{'publisher': Company.objects.get(Q(**{'name': u'Virgin Interactive'})), 'collection_label': None, 'porter': None})
release.system_specification = get_or_create_sysspec("Game Gear game", ("",))
release.save()

	#Disney's Aladdin (SIMS)
release = Release.objects.create(created_by=get_userextension("ad"), concept=get_concept("Disney's Aladdin (SIMS)"),
                                  **{'name': u'', 'immaterial': False, 'unsure_region': True, 'special_case_release': 'L', 'pk': 60}
)
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'content', 'name': u'self'}))), bulk=False )
release.release_regions.add( ReleaseRegion.objects.get(Q(**{'name': 'EU'})) )
specific = ReleaseSpecific.Software.objects.create(release=release, **{'publisher': Company.objects.get(Q(**{'name': u'Sega'})), 'collection_label': None, 'porter': None})
release.system_specification = get_or_create_sysspec("Game Gear game", ("",))
release.save()

	#Sonic the Hedgehog 2 (8-bit)
release = Release.objects.create(created_by=get_userextension("ad"), concept=get_concept('Sonic the Hedgehog 2 (8-bit)'),
                                  **{'name': u'', 'immaterial': False, 'unsure_region': True, 'special_case_release': 'L', 'pk': 61}
)
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'content', 'name': u'self'}))), bulk=False )
release.release_regions.add( ReleaseRegion.objects.get(Q(**{'name': 'EU'})) )
specific = ReleaseSpecific.Software.objects.create(release=release, **{'publisher': Company.objects.get(Q(**{'name': u'Sega'})), 'collection_label': None, 'porter': None})
release.system_specification = get_or_create_sysspec("Game Gear game", ("",))
release.save()

	#Sega Game Pack 4 in 1
release = Release.objects.create(created_by=get_userextension("ad"), concept=get_concept(u'Sega Game Pack 4 in 1'),
                                  **{'name': u'', 'immaterial': False, 'unsure_region': True, 'special_case_release': 'L', 'pk': 62}
)
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'content', 'name': u'self'}))), bulk=False )
release.release_regions.add( ReleaseRegion.objects.get(Q(**{'name': 'EU'})) )
specific = ReleaseSpecific.Software.objects.create(release=release, **{'publisher': Company.objects.get(Q(**{'name': u'Sega'})), 'collection_label': None, 'porter': None})
release.system_specification = get_or_create_sysspec("Game Gear game", ("",))
release.save()

	#Alex Kidd in Miracle World
release = Release.objects.create(created_by=get_userextension("ad"), concept=get_concept(u'Alex Kidd in Miracle World'),
                                  **{'name': u'', 'immaterial': True, 'unsure_region': False, 'pk': 63}
)
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'papers', 'name': u'manual'}))), bulk=False )
specific = ReleaseSpecific.Software.objects.create(release=release, **{'publisher': Company.objects.get(Q(**{'name': u'Sega'})), 'collection_label': None, 'porter': None})

	#Operation Wolf
release = Release.objects.create(created_by=get_userextension("ad"), concept=get_concept(u'Operation Wolf'),
                                  **{'name': u'', 'immaterial': False, 'partial_date_precision': 'YYYY', 'unsure_region': True, 'partial_date': datetime.date(1991, 1, 1), 'pk': 64}
)
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'content', 'name': u'self'}))), bulk=False )
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'packaging', 'name': u'cartridge box'}))), bulk=False )
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'packaging', 'name': u'hang on tab'}))), bulk=False )
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'papers', 'name': u'manual'}))), bulk=False )
release.release_regions.add( ReleaseRegion.objects.get(Q(**{'name': 'EU'})) )
specific = ReleaseSpecific.Software.objects.create(release=release, **{'publisher': Company.objects.get(Q(**{'name': u'Taito'})), 'collection_label': None, 'porter': None})
release.system_specification = get_or_create_sysspec("Master System cartridge game", ("NTSC-U", "PAL",))
release.save()

	#Wheel Wii Sonic
release = Release.objects.create(created_by=get_userextension("ad"), concept=get_concept(u'Wheel Wii Sonic'),
                                  **{'pk': 65, 'version': u'', 'unsure_region': True, 'name': u'', 'special_case_release': 'L', 'immaterial': False}
)
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'content', 'name': u'self'}))), bulk=False )
release.release_regions.add( ReleaseRegion.objects.get(Q(**{'name': 'EU'})) )
specific = ReleaseSpecific.Hardware.objects.create(release=release, **{'manufacturer': Company.objects.get(Q(**{'name': u'Sega'}))})
specific.colors.add(Color.objects.get(Q(**{'name': u'Blue'})))
release.system_specification = get_or_create_sysspec("wiimote shell accessory", ("",))
release.save()

	#Master System Control Pad
release = Release.objects.create(created_by=get_userextension("ad"), concept=get_concept('Master System Control Pad'),
                                  **{'pk': 68, 'version': u'"Model 3"', 'unsure_region': False, 'name': u'', 'special_case_release': 'C', 'immaterial': False}
)
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'content', 'name': u'self'}))), bulk=False )
specific = ReleaseSpecific.Hardware.objects.create(release=release, **{'manufacturer': Company.objects.get(Q(**{'name': u'Sega'}))})
specific.colors.add(Color.objects.get(Q(**{'name': u'Black'})))
release.system_specification = get_or_create_sysspec("Master System controller", ("",))
release.save()

	#The Sega Light Phaser
release = Release.objects.create(created_by=get_userextension("ad"), concept=get_concept(u'The Sega Light Phaser'),
                                  **{'pk': 66, 'version': u'', 'unsure_region': True, 'name': u'', 'immaterial': False}
)
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'content', 'name': u'self'}))), bulk=False )
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'packaging', 'name': u'cardboard box'}))), bulk=False )
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'packaging', 'name': u'inlay polystyrene'}))), bulk=False )
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'papers', 'name': u'manual'}))), bulk=False )
release.release_regions.add( ReleaseRegion.objects.get(Q(**{'name': 'EU'})) )
specific = ReleaseSpecific.Hardware.objects.create(release=release, **{'manufacturer': Company.objects.get(Q(**{'name': u'Sega'}))})
specific.colors.add(Color.objects.get(Q(**{'name': u'Black'})))
release.system_specification = get_or_create_sysspec("Master System controller", ("NTSC-U", "PAL",))
release.save()

    #Sega Master System II
release = Release.objects.create(created_by=get_userextension("ad"), concept=get_concept(u'Sega Master System'),
                                  **{'pk': 67, 'version': u'', 'unsure_region': True, 'name': u'Master System II incl. Alex Kidd', 'immaterial': False}
)
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'content', 'name': u'self'}))), bulk=False )
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'packaging', 'name': u'cardboard box'}))), bulk=False )
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'packaging', 'name': u'inlay polystyrene'}))), bulk=False )
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'papers', 'name': u'leaflet'}))), bulk=False )
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'papers', 'name': u'manual'}))), bulk=False )
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'papers', 'name': u'warranty'}))), bulk=False )
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'content', 'name': u'cord-220v'}))), bulk=False )
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'content', 'name': u'scart'}))), bulk=False )
ReleaseComposition.objects.create(from_release=release, to_release=Release.objects.get(Q(**{'pk': 63})))
ReleaseComposition.objects.create(from_release=release, to_release=Release.objects.get(Q(**{'pk': 68})))
release.release_regions.add( ReleaseRegion.objects.get(Q(**{'name': 'FR'})) )
specific = ReleaseSpecific.Hardware.objects.create(release=release, **{'manufacturer': Company.objects.get(Q(**{'name': u'Sega'}))})
specific.colors.add(Color.objects.get(Q(**{'name': u'Black'})))
specific = ReleaseSpecific.Variant.objects.create(release=release, **{'system_variant': SystemVariant.objects.get(variant_name="Sega Master System II")})
release.system_specification = get_or_create_sysspec("Master System 2 console", ("NTSC-U", "PAL",))
release.save()

	#_COMBO
release = Release.objects.create(created_by=get_userextension("ad"), concept=get_concept('_COMBO'),
                                  **{'pk': 69, 'unsure_region': True, 'name': u'Sega Master System II Plus', 'immaterial': False}
)
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'packaging', 'name': u'cardboard box'}))), bulk=False )
ReleaseComposition.objects.create(from_release=release, to_release=Release.objects.get(Q(**{'pk': 67})))
ReleaseComposition.objects.create(from_release=release, to_release=Release.objects.get(Q(**{'pk': 66})))
ReleaseComposition.objects.create(from_release=release, to_release=Release.objects.get(Q(**{'pk': 64})))
release.release_regions.add( ReleaseRegion.objects.get(Q(**{'name': 'FR'})) )
specific = ReleaseSpecific.Combo.objects.create(release=release, **{'brand': Company.objects.get(Q(**{'name': u'Sega'}))})

	#Steering wheel Saturn Mad Catz
release = Release.objects.create(created_by=get_userextension("ad"), concept=get_concept(u'Steering wheel Saturn Mad Catz'),
                                  **{'pk': 70, 'version': u'', 'unsure_region': True, 'name': u'', 'immaterial': False}
)
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'content', 'name': u'self'}))), bulk=False )
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'packaging', 'name': u'cardboard box'}))), bulk=False )
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'packaging', 'name': u'baggies'}))), bulk=False )
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'papers', 'name': u'manual'}))), bulk=False )
release.release_regions.add( ReleaseRegion.objects.get(Q(**{'name': 'EU'})) )
specific = ReleaseSpecific.Hardware.objects.create(release=release, **{'manufacturer': Company.objects.get(Q(**{'name': u'Mad Catz'}))})
specific.colors.add(Color.objects.get(Q(**{'name': u'Black'})))
release.system_specification = get_or_create_sysspec("Saturn controller", ("",))
release.save()

	#BioShock 2
release = Release.objects.create(created_by=get_userextension("ad"), concept=get_concept(u'BioShock 2'),
        **{'name': u'BioShock 2 Special Edition', 'immaterial': False, 'partial_date_precision': 'DD', 'unsure_region': True, 'partial_date': datetime.date(2010, 2, 9), 'pk': 71, 'unsure_content': True}
)
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'content', 'name': u'self'}))), bulk=False )
release.release_regions.add( ReleaseRegion.objects.get(Q(**{'name': 'EU'})) )
specific = ReleaseSpecific.Software.objects.create(release=release, **{'publisher': Company.objects.get(Q(**{'name': u'2K'})), 'collection_label': None, 'porter': None})
release.system_specification = get_or_create_sysspec("PC-CD", ("",))
release.save()

	#Half-Life
release = Release.objects.create(created_by=get_userextension("ad"), concept=get_concept(u'Half-Life'),
                                  **{'pk': 72, 'unsure_region': False, 'name': u"Half-Life : Le Jeu de l'Ann\xe9e", 'immaterial': False}
)
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'content', 'name': u'self'}))), bulk=False )
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'packaging', 'name': u'cardboard box'}))), bulk=False )
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'packaging', 'name': u'jewel box'}))), bulk=False )
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'packaging', 'name': u'cardboard inlay non-decorative'}))), bulk=False )
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'papers', 'name': u'catalog'}))), bulk=False )
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'papers', 'name': u'insert: jewel box'}))), bulk=False )
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'papers', 'name': u'leaflet'}))), bulk=False )
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'papers', 'name': u'manual'}))), bulk=False )
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'papers', 'name': u'registration card'}))), bulk=False )
release.release_regions.add( ReleaseRegion.objects.get(Q(**{'name': 'FR'})) )
specific = ReleaseSpecific.Software.objects.create(release=release, **{'publisher': Company.objects.get(Q(**{'name': u'Sierra Entertainment'})), 'collection_label': None, 'porter': None})
release.system_specification = get_or_create_sysspec("PC-CD", ("",))
release.save()

	#Half-Life: Opposing Force
release = Release.objects.create(created_by=get_userextension("ad"), concept=get_concept(u'Half-Life: Opposing Force'),
                                  **{'pk': 73, 'unsure_region': False, 'name': u'', 'immaterial': False}
)
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'content', 'name': u'self'}))), bulk=False )
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'packaging', 'name': u'cardboard box'}))), bulk=False )
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'packaging', 'name': u'jewel box'}))), bulk=False )
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'packaging', 'name': u'cardboard inlay non-decorative'}))), bulk=False )
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'papers', 'name': u'catalog'}))), bulk=False )
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'papers', 'name': u'insert: jewel box'}))), bulk=False )
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'papers', 'name': u'manual'}))), bulk=False )
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'papers', 'name': u'registration card'}))), bulk=False )
release.release_regions.add( ReleaseRegion.objects.get(Q(**{'name': 'FR'})) )
specific = ReleaseSpecific.Software.objects.create(release=release, **{'publisher': Company.objects.get(Q(**{'name': u'Sierra Entertainment'})), 'collection_label': None, 'porter': None})
release.system_specification = get_or_create_sysspec("PC-CD", ("",))
release.save()

	#_COMBO
release = Release.objects.create(created_by=get_userextension("ad"), concept=get_concept('_COMBO'),
                                  **{'pk': 74, 'unsure_region': False, 'name': u'Half-Life Generation', 'immaterial': False}
)
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'packaging', 'name': u'sheath'}))), bulk=False )
ReleaseComposition.objects.create(from_release=release, to_release=Release.objects.get(Q(**{'pk': 72})))
ReleaseComposition.objects.create(from_release=release, to_release=Release.objects.get(Q(**{'pk': 73})))
release.release_regions.add( ReleaseRegion.objects.get(Q(**{'name': 'FR'})) )
specific = ReleaseSpecific.Combo.objects.create(release=release, **{'brand': Company.objects.get(Q(**{'name': u'Sierra Entertainment'}))})

	#Pole Position
release = Release.objects.create(created_by=get_userextension("ad"), concept=get_concept(u'Pole Position'),
                                  **{'name': u'', 'immaterial': False, 'unsure_region': True, 'special_case_release': 'L', 'pk': 75}
)
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'content', 'name': u'self'}))), bulk=False )
release.release_regions.add( ReleaseRegion.objects.get(Q(**{'name': 'EU'})) )
specific = ReleaseSpecific.Software.objects.create(release=release, **{'publisher': Company.objects.get(Q(**{'name': u'Atari'})), 'collection_label': None, 'porter': None})
release.system_specification = get_or_create_sysspec("Atari 2600 game", ("PAL",))
release.save()

	#Centipede
release = Release.objects.create(created_by=get_userextension("ad"), concept=get_concept(u'Centipede'),
                                  **{'name': u'', 'immaterial': False, 'unsure_region': True, 'special_case_release': 'L', 'pk': 76}
)
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'content', 'name': u'self'}))), bulk=False )
release.release_regions.add( ReleaseRegion.objects.get(Q(**{'name': 'EU'})) )
specific = ReleaseSpecific.Software.objects.create(release=release, **{'publisher': Company.objects.get(Q(**{'name': u'Atari'})), 'collection_label': None, 'porter': None})
release.system_specification = get_or_create_sysspec("Atari 2600 game", ("PAL",))
release.save()

	#Millennium Soldier: Expendable
release = Release.objects.create(created_by=get_userextension("ad"), concept=get_concept(u'Millennium Soldier: Expendable'),
                                  **{'pk': 77, 'unsure_region': False, 'name': u'', 'immaterial': False}
)
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'content', 'name': u'self'}))), bulk=False )
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'packaging', 'name': u'cardboard box'}))), bulk=False )
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'packaging', 'name': u'jewel box'}))), bulk=False )
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'packaging', 'name': u'cardboard inlay non-decorative'}))), bulk=False )
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'papers', 'name': u'insert: jewel box'}))), bulk=False )
release.release_regions.add( ReleaseRegion.objects.get(Q(**{'name': 'FR'})) )
collection = CollectionLabel.objects.create(name='Back to Games', company=Company.objects.get(Q(**{'name': u'Pointsoft'})))
specific = ReleaseSpecific.Software.objects.create(release=release, **{'publisher': Company.objects.get(Q(**{'name': u'Pointsoft'})), 'collection_label': collection, 'porter': None})
release.system_specification = get_or_create_sysspec("PC-CD", ("",))
release.save()

	#Action Replay Plus 4M (Saturn EMS)
release = Release.objects.create(created_by=get_userextension("ad"), concept=get_concept('Action Replay Plus 4M (Saturn EMS)'),
                                  **{'pk': 78, 'version': u'', 'unsure_region': True, 'name': u'Action Replay 4M Auto Plus', 'immaterial': False, 'alternative_distribution': True}
)
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'content', 'name': u'self'}))), bulk=False )
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'packaging', 'name': u'cardboard box'}))), bulk=False )
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'packaging', 'name': u'cardboard inlay non-decorative'}))), bulk=False )
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'papers', 'name': u'leaflet'}))), bulk=False )
#[REGION] no region
specific = ReleaseSpecific.Hardware.objects.create(release=release, **{'manufacturer': Company.objects.get(Q(**{'name': u'EMS'}))})
specific.colors.add(Color.objects.get(Q(**{'name': u'Grey'})))
specific = ReleaseSpecific.BackupMemory.objects.create(release=release, **{'capacity': 4, 'unit': StorageUnit.objects.get(name="megabyte")})
specific = ReleaseSpecific.RamMemory.objects.create(release=release, **{'capacity': 4, 'unit': StorageUnit.objects.get(name="megabyte")})
release.system_specification = get_or_create_sysspec("Saturn region-unlock cartridge", ("",))
release.save()

	#Titan Quest
release = Release.objects.create(created_by=get_userextension("ad"), concept=get_concept(u'Titan Quest'),
                                  **{'pk': 79, 'unsure_region': False, 'name': u'Titan Quest - Steel Book edition', 'immaterial': False}
)
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'content', 'name': u'self'}))), bulk=False )
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'packaging', 'name': u'dvd box'}))), bulk=False )
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'papers', 'name': u'leaflet'}))), bulk=False )
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'papers', 'name': u'manual'}))), bulk=False )
release.release_regions.add( ReleaseRegion.objects.get(Q(**{'name': 'FR'})) )
specific = ReleaseSpecific.Software.objects.create(release=release, **{'publisher': Company.objects.get(Q(**{'name': u'THQ'})), 'collection_label': None, 'porter': None})
release.system_specification = get_or_create_sysspec("PC-CD", ("",))
release.save()

	#Diablo II
release = Release.objects.create(created_by=get_userextension("ad"), concept=get_concept(u'Diablo II'),
                                  **{'pk': 80, 'unsure_region': True, 'name': u'', 'immaterial': False}
)
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'content', 'name': u'self'}))), bulk=False )
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'packaging', 'name': u'dvd box'}))), bulk=False )
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'papers', 'name': u'catalog'}))), bulk=False )
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'papers', 'name': u'manual'}))), bulk=False )
release.release_regions.add( ReleaseRegion.objects.get(Q(**{'name': 'EU'})) )
collection = CollectionLabel.objects.create(name='Best Seller Series', company=None)
specific = ReleaseSpecific.Software.objects.create(release=release, **{'publisher': Company.objects.get(Q(**{'name': u'Blizzard'})), 'collection_label': collection, 'porter': None})
release.system_specification = get_or_create_sysspec("PC-CD", ("",))
release.save()

	#Diablo II
release = Release.objects.create(created_by=get_userextension("ad"), concept=get_concept(u'Diablo II'),
                                  **{'name': u'', 'immaterial': False, 'partial_date_precision': 'DD', 'unsure_region': False, 'partial_date': datetime.date(2000, 6, 30), 'pk': 81, "unsure_content": True}
)
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'content', 'name': u'self'}))), bulk=False )
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'packaging', 'name': u'cardboard box'}))), bulk=False )
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'packaging', 'name': u'jewel box'}))), bulk=False )
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'papers', 'name': u'manual'}))), bulk=False )
release.release_regions.add( ReleaseRegion.objects.get(Q(**{'name': 'FR'})) )
specific = ReleaseSpecific.Software.objects.create(release=release, **{'publisher': Company.objects.get(Q(**{'name': u'Blizzard'})), 'collection_label': None, 'porter': None})
release.system_specification = get_or_create_sysspec("PC-CD", ("",))
release.save()

	#Wolfenstein 3D
release = Release.objects.create(created_by=get_userextension("ad"), concept=get_concept(u'Wolfenstein 3D'),
        **{'pk': 82, 'unsure_region': True, 'name': u'', 'immaterial': False, "unsure_content": True}
)
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'content', 'name': u'self'}))), bulk=False )
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'packaging', 'name': u'dvd box'}))), bulk=False )
release.release_regions.add( ReleaseRegion.objects.get(Q(**{'name': 'EU'})) )
collection = CollectionLabel.objects.create(name='Xplosiv', company=Company.objects.get(Q(**{'name': u'Activision'})))
specific = ReleaseSpecific.Software.objects.create(release=release, **{'publisher': Company.objects.get(Q(**{'name': u'Activision'})), 'collection_label': collection, 'porter': None})
release.system_specification = get_or_create_sysspec("PC-CD", ("",))
release.save()

	#Final Doom
release = Release.objects.create(created_by=get_userextension("ad"), concept=get_concept(u'Final Doom'),
                                  **{'name': u'', 'immaterial': False, 'partial_date_precision': 'DD', 'unsure_region': True, 'partial_date': datetime.date(1996, 5, 31), 'pk': 83, "unsure_content": True}
)
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'content', 'name': u'self'}))), bulk=False )
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'packaging', 'name': u'cardboard box'}))), bulk=False )
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'packaging', 'name': u'jewel box'}))), bulk=False )
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'papers', 'name': u'manual'}))), bulk=False )
release.release_regions.add( ReleaseRegion.objects.get(Q(**{'name': 'EU'})) )
specific = ReleaseSpecific.Software.objects.create(release=release, **{'publisher': Company.objects.get(Q(**{'name': u'GT Interactive'})), 'collection_label': None, 'porter': None})
release.system_specification = get_or_create_sysspec("PC-CD", ("",))
release.save()

    # MANUAL spit Warcraft II: Beyond the Dark Portal
release = Release.objects.create(created_by=get_userextension("ad"), concept=get_concept(u'Warcraft II: Beyond the Dark Portal'),
            **{'immaterial': False, 'partial_date_precision': 'YYYY', 'partial_date': datetime.date(1996, 1, 1), 'unsure_region': False, 'unsure_content': True, 'pk': 100})
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'content', 'name': u'self'}))), bulk=False )
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'packaging', 'name': u'jewel box'}))), bulk=False )
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'papers', 'name': u'insert: jewel box'}))), bulk=False )
release.release_regions.add( ReleaseRegion.objects.get(Q(**{'name': 'FR'})) )
specific = ReleaseSpecific.Software.objects.create(release=release, **{'publisher': Company.objects.get(Q(**{'name': u'Blizzard'})), 'collection_label': None, 'porter': None})
release.system_specification = get_or_create_sysspec("PC-CD", ("",))
release.save()

	#Warcraft II: Tides of Darkness
release = Release.objects.create(created_by=get_userextension("ad"), concept=get_concept(u'Warcraft II: Tides of Darkness'),
                                  **{'name': u'Warcraft II : Edition Deluxe', 'immaterial': False, 'partial_date_precision': 'YYYY', 'unsure_region': False, 'partial_date': datetime.date(1996, 1, 1), 'pk': 84, "unsure_content": True}
)
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'content', 'name': u'self'}))), bulk=False )
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'packaging', 'name': u'cardboard box'}))), bulk=False )
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'packaging', 'name': u'jewel box'}))), bulk=False )
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'papers', 'name': u'manual'})), note="Tides of Darkness"), bulk=False )
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'papers', 'name': u'manual'})), note="Edition Deluxe"), bulk=False )
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'papers', 'name': u'warranty'}))), bulk=False )
ReleaseComposition.objects.create(from_release=release, to_release=Release.objects.get(Q(**{'pk': 100})))
release.release_regions.add( ReleaseRegion.objects.get(Q(**{'name': 'FR'})) )
specific = ReleaseSpecific.Software.objects.create(release=release, **{'publisher': Company.objects.get(Q(**{'name': u'Blizzard'})), 'collection_label': None, 'porter': None})
release.system_specification = get_or_create_sysspec("PC-CD", ("",))
release.save()

	#Carmageddon II: Carpocalypse Now
release = Release.objects.create(created_by=get_userextension("ad"), concept=get_concept(u'Carmageddon II: Carpocalypse Now'),
                                  **{'pk': 85, 'unsure_region': True, 'name': u'', 'immaterial': False}
)
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'content', 'name': u'self'}))), bulk=False )
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'packaging', 'name': u'cardboard box'}))), bulk=False )
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'packaging', 'name': u'jewel box'}))), bulk=False )
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'packaging', 'name': u'sheath'}))), bulk=False )
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'packaging', 'name': u'cardboard inlay non-decorative'}))), bulk=False )
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'papers', 'name': u'leaflet'}))), bulk=False )
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'papers', 'name': u'manual'}))), bulk=False )
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'papers', 'name': u'registration card'}))), bulk=False )
release.release_regions.add( ReleaseRegion.objects.get(Q(**{'name': 'EU'})) )
specific = ReleaseSpecific.Software.objects.create(release=release, **{'publisher': Company.objects.get(Q(**{'name': u'SCI'})), 'collection_label': None, 'porter': None})
release.system_specification = get_or_create_sysspec("PC-CD", ("",))
release.save()

	#Torin's Passage
release = Release.objects.create(created_by=get_userextension("ad"), concept=get_concept(u"Torin's Passage"),
        **{'pk': 86, 'unsure_region': True, 'name': u'', 'immaterial': False, 'unsure_content': True}
)
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'content', 'name': u'self'}))), bulk=False )
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'packaging', 'name': u'jewel box'}))), bulk=False )
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'papers', 'name': u'manual: jewel box'}))), bulk=False )
release.release_regions.add( ReleaseRegion.objects.get(Q(**{'name': 'EU'})) )
specific = ReleaseSpecific.Software.objects.create(release=release, **{'publisher': Company.objects.get(Q(**{'name': u'Sierra Entertainment'})), 'collection_label': None, 'porter': None})
release.system_specification = get_or_create_sysspec("PC-CD", ("",))
release.save()

	#Loom
release = Release.objects.create(created_by=get_userextension("ad"), concept=get_concept(u'Loom'),
                                  **{'pk': 87, 'unsure_region': True, 'name': u'', 'immaterial': False, 'unsure_content': True}
)
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'content', 'name': u'self'}))), bulk=False )
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'packaging', 'name': u'jewel box'}))), bulk=False )
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'papers', 'name': u'manual: jewel box'}))), bulk=False )
release.release_regions.add( ReleaseRegion.objects.get(Q(**{'name': 'EU'})) )
specific = ReleaseSpecific.Software.objects.create(release=release, **{'publisher': Company.objects.get(Q(**{'name': u'Lucasfilm Games'})), 'collection_label': None, 'porter': None})
release.system_specification = get_or_create_sysspec("PC-CD", ("",))
release.save()

	#The Lost Mind of Dr. Brain
release = Release.objects.create(created_by=get_userextension("ad"), concept=get_concept(u'The Lost Mind of Dr. Brain'),
                                  **{'pk': 88, 'unsure_region': True, 'name': u'Dr. Brain a perdu la t\xeate !', 'immaterial': False, 'unsure_content': True}
)
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'content', 'name': u'self'}))), bulk=False )
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'packaging', 'name': u'jewel box'}))), bulk=False )
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'papers', 'name': u'manual: jewel box'}))), bulk=False )
release.release_regions.add( ReleaseRegion.objects.get(Q(**{'name': 'EU'})) )
specific = ReleaseSpecific.Software.objects.create(release=release, **{'publisher': Company.objects.get(Q(**{'name': u'Coktel Vision'})), 'collection_label': None, 'porter': None})
release.system_specification = get_or_create_sysspec("PC-CD", ("",))
release.save()

	#The Curse of Monkey Island
release = Release.objects.create(created_by=get_userextension("ad"), concept=get_concept(u'The Curse of Monkey Island'),
                                  **{'name': u'', 'immaterial': False, 'partial_date_precision': 'DD', 'unsure_region': True, 'partial_date': datetime.date(1998, 2, 20), 'pk': 89}
)
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'content', 'name': u'self'}))), bulk=False )
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'packaging', 'name': u'cardboard box'}))), bulk=False )
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'packaging', 'name': u'jewel box'}))), bulk=False )
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'papers', 'name': u'manual'}))), bulk=False )
release.release_regions.add( ReleaseRegion.objects.get(Q(**{'name': 'EU'})) )
specific = ReleaseSpecific.Software.objects.create(release=release, **{'publisher': Company.objects.get(Q(**{'name': u'LucasArts'})), 'collection_label': None, 'porter': None})
release.system_specification = get_or_create_sysspec("PC-CD", ("",))
release.save()

	#Nymphéas Photo CD
release = Release.objects.create(created_by=get_userextension("ad"), concept=get_concept(u'Nymph\xe9as Photo CD'),
                                  **{'name': u'', 'immaterial': False, 'partial_date_precision': 'YYYY', 'unsure_region': True, 'partial_date': datetime.date(1995, 1, 1), 'version': u'', 'pk': 92}
)
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'content', 'name': u'self'}))), bulk=False )
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'papers', 'name': u'manual'}))), bulk=False )
release.release_regions.add( ReleaseRegion.objects.get(Q(**{'name': 'EU'})) )
specific = ReleaseSpecific.Software.objects.create(release=release, **{'publisher': Company.objects.get(Q(**{'name': u'Sega'})), 'collection_label': None, 'porter': None})
specific = ReleaseSpecific.Media.objects.create(release=release)
specific.media_types.add(MediaType.objects.get(name="Image"))
release.system_specification = get_or_create_sysspec("Saturn game", ("PAL",))
release.save()

    #Photo CD Operating System (Saturn)
release = Release.objects.create(created_by=get_userextension("ad"), concept=get_concept('Photo CD Operating System (Saturn)'),
                                  **{'name': u'', 'immaterial': False, 'partial_date_precision': 'YYYY', 'unsure_region': True, 'partial_date': datetime.date(1995, 1, 1), 'version': u'', 'pk': 91}
)
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'content', 'name': u'self'}))), bulk=False )
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'packaging', 'name': u'dvd box'}))), bulk=False )
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'papers', 'name': u'manual'}))), bulk=False )
ReleaseComposition.objects.create(from_release=release, to_release=Release.objects.get(Q(**{'pk': 92})))
release.release_regions.add( ReleaseRegion.objects.get(Q(**{'name': 'EU'})) )
specific = ReleaseSpecific.Software.objects.create(release=release, **{'publisher': Company.objects.get(Q(**{'name': u'Sega'})), 'collection_label': None, 'porter': None})
release.system_specification = get_or_create_sysspec("Saturn game", ("PAL",))
release.save()

	#Wii Remote
release = Release.objects.create(created_by=get_userextension("ad"), concept=get_concept(u'Wii Remote'),
                                  **{'pk': 93, 'version': u'RVL-003', 'name': u'', 'special_case_release': 'C', 'immaterial': False}
)
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'content', 'name': u'self'}))), bulk=False )
specific = ReleaseSpecific.Hardware.objects.create(release=release, **{'manufacturer': Company.objects.get(Q(**{'name': u'Nintendo'}))})
specific.colors.add(Color.objects.get(Q(**{'name': u'Black'})))
release.system_specification = get_or_create_sysspec("wiimote controller", ("",))
release.save()

	#Nunchuk
release = Release.objects.create(created_by=get_userextension("ad"), concept=get_concept(u'Nunchuk'),
                                  **{'pk': 94, 'version': u'RVL-004', 'name': u'', 'special_case_release': 'C', 'immaterial': False}
)
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'content', 'name': u'self'}))), bulk=False )
specific = ReleaseSpecific.Hardware.objects.create(release=release, **{'manufacturer': Company.objects.get(Q(**{'name': u'Nintendo'}))})
specific.colors.add(Color.objects.get(Q(**{'name': u'Black'})))
release.system_specification = get_or_create_sysspec("wiimote expansion", ("",))
release.save()

	#Wii MotionPlus
release = Release.objects.create(created_by=get_userextension("ad"), concept=get_concept(u'Wii MotionPlus'),
                                  **{'pk': 95, 'version': u'RVL-026', 'name': u'', 'special_case_release': 'C', 'immaterial': False}
)
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'content', 'name': u'self'}))), bulk=False )
specific = ReleaseSpecific.Hardware.objects.create(release=release, **{'manufacturer': Company.objects.get(Q(**{'name': u'Nintendo'}))})
specific.colors.add(Color.objects.get(Q(**{'name': u'Black'})))
release.system_specification = get_or_create_sysspec("wiimote expansion", ("",))
release.save()

	#Wii Sports
release = Release.objects.create(created_by=get_userextension("ad"), concept=get_concept(u'Wii Sports'),
                                  **{'pk': 96, 'unsure_region': True, 'name': u'', 'immaterial': False}
)
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'content', 'name': u'self'}))), bulk=False )
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'packaging', 'name': u'cardboard cd sleeve'}))), bulk=False )
release.release_regions.add( ReleaseRegion.objects.get(Q(**{'name': 'EU'})) )
specific = ReleaseSpecific.Software.objects.create(release=release, **{'publisher': Company.objects.get(Q(**{'name': u'Nintendo'})), 'collection_label': None, 'porter': None})
release.system_specification = get_or_create_sysspec("Wii game", ("PAL",))
release.save()

	#Wii Sports Resort
release = Release.objects.create(created_by=get_userextension("ad"), concept=get_concept(u'Wii Sports Resort'),
                                  **{'pk': 97, 'unsure_region': True, 'name': u'', 'immaterial': False}
)
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'content', 'name': u'self'}))), bulk=False )
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'packaging', 'name': u'cardboard cd sleeve'}))), bulk=False )
release.release_regions.add( ReleaseRegion.objects.get(Q(**{'name': 'EU'})) )
specific = ReleaseSpecific.Software.objects.create(release=release, **{'publisher': Company.objects.get(Q(**{'name': u'Nintendo'})), 'collection_label': None, 'porter': None})
release.system_specification = get_or_create_sysspec("Wii game", ("PAL",))
release.save()

	#Wii
release = Release.objects.create(created_by=get_userextension("ad"), concept=get_concept(u'Wii'),
                                  **{'pk': 98, 'version': u'', 'unsure_region': True, 'name': u'Wii Sports Resort Pak', 'immaterial': False}
)
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'content', 'name': u'self'}))), bulk=False )
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'packaging', 'name': u'cardboard box'}))), bulk=False )
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'packaging', 'name': u'baggies'}))), bulk=False )
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'packaging', 'name': u'cardboard inlay non-decorative'}))), bulk=False )
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'papers', 'name': u'manual'}))), bulk=False )
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'papers', 'name': u'warranty'}))), bulk=False )
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'content', 'name': u'cord-220v'}))), bulk=False )
release.attributes.add( ReleaseAttribute(release=release, attribute=Attribute.objects.get(Q(**{'category__name': u'content', 'name': u'scart'}))), bulk=False )
ReleaseComposition.objects.create(from_release=release, to_release=Release.objects.get(Q(**{'pk': 96})))
ReleaseComposition.objects.create(from_release=release, to_release=Release.objects.get(Q(**{'pk': 97})))
ReleaseComposition.objects.create(from_release=release, to_release=Release.objects.get(Q(**{'pk': 93})))
ReleaseComposition.objects.create(from_release=release, to_release=Release.objects.get(Q(**{'pk': 94})))
ReleaseComposition.objects.create(from_release=release, to_release=Release.objects.get(Q(**{'pk': 95})))
release.release_regions.add( ReleaseRegion.objects.get(Q(**{'name': 'EU'})) )
specific = ReleaseSpecific.Hardware.objects.create(release=release, **{'manufacturer': Company.objects.get(Q(**{'name': u'Nintendo'}))})
specific.colors.add(Color.objects.get(Q(**{'name': u'Black'})))
specific = ReleaseSpecific.Variant.objects.create(release=release, **{'system_variant': SystemVariant.objects.get(variant_name="Wii")})
release.system_specification = get_or_create_sysspec("Wii console (GC)", ("PAL",))
release.save()
