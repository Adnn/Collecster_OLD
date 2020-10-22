#!/usr/bin/env python

import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Collecster.settings")
django.setup()

from advideogame.models import *
from advideogame.configuration import *
from supervisor.models import *

def get_bs(name):
    return BaseSystem.objects.get(name=name)

def get_sysmediapair(abbreviated_name):
    return SystemMediaPair.objects.get(abbreviated_name=abbreviated_name)

	#Master System cartridge game
interface_spec = InterfacesSpecification.objects.get(internal_name='Master System cartridge game', implicit_system=False)
base = BaseSystem.objects.get(name='Master System')
interface_detail = SystemInterfaceDetail.objects.get(interfaces_specification=interface_spec, advertised_system=base)
interface = RequiredInterface.objects.get(interface_detail_base=interface_detail, interface=get_sysmediapair('SMS-cart'), cardinality=1)
interface.on_tag = True
interface.save()

	#Master System Sega card game
interface_spec = InterfacesSpecification.objects.get(internal_name='Master System Sega card game', implicit_system=False)
base = BaseSystem.objects.get(name='Master System')
interface_detail = SystemInterfaceDetail.objects.get(interfaces_specification=interface_spec, advertised_system=base)
interface = RequiredInterface.objects.get(interface_detail_base=interface_detail, interface=get_sysmediapair('SMS-scard'), cardinality=1)
interface.on_tag = True
interface.save()

	#Saturn region-unlock cartridge
interface_spec = InterfacesSpecification.objects.create(internal_name='Saturn region-unlock cartridge', implicit_system=False)
base = BaseSystem.objects.get(name='Saturn')
interface_detail = SystemInterfaceDetail.objects.create(interfaces_specification=interface_spec, advertised_system=base)
RequiredInterface.objects.create(interface_detail_base=interface_detail, interface=get_sysmediapair('Sat-cart'), cardinality=1)
interface = ProvidedInterface.objects.create(interface_detail_base=interface_detail, interface=get_sysmediapair('Sat-disc'),
                                             reused_interface=get_sysmediapair('Sat-disc'), cardinality=1)
interface.regional_lockout_override.add(LockoutRegion.objects.get(region_name="PAL"))
interface.regional_lockout_override.add(LockoutRegion.objects.get(region_name="NTSC-U"))
interface.regional_lockout_override.add(LockoutRegion.objects.get(region_name="NTSC-J"))

	#PC-CD medias
def mark_pc_media_ontag(interface_spec, systemmedia_pair):
    base = BaseSystem.objects.get(name='Personal Computer')
    interface_spec = InterfacesSpecification.objects.get(internal_name=interface_spec, implicit_system=False)
    interface_detail = SystemInterfaceDetail.objects.get(interfaces_specification=interface_spec, advertised_system=base)
    interface = RequiredInterface.objects.get(interface_detail_base=interface_detail, interface=get_sysmediapair(systemmedia_pair), cardinality=1)
    interface.on_tag = True
    interface.save()

mark_pc_media_ontag("PC 5\"1/4 floppy", "PC-fd5")
mark_pc_media_ontag("PC 3\"1/2 floppy", "PC-fd3")
mark_pc_media_ontag("PC-CD", "PC-CD")
mark_pc_media_ontag("PC-DVD", "PC-DVD")
mark_pc_media_ontag("PC-BD", "PC-BD")
