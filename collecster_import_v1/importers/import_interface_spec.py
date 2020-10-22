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

	#Master System 1 console
interface_spec = InterfacesSpecification.objects.create(internal_name='Master System 1 console', implicit_system=False)
base = BaseSystem.objects.get(name='Master System')
interface_detail = SystemInterfaceDetail.objects.create(interfaces_specification=interface_spec, advertised_system=base)
ProvidedInterface.objects.create(interface_detail_base=interface_detail, interface=get_sysmediapair('SMS-cart'), cardinality=1)
ProvidedInterface.objects.create(interface_detail_base=interface_detail, interface=get_sysmediapair('SMS-scard'), cardinality=1)
ProvidedInterface.objects.create(interface_detail_base=interface_detail, interface=get_sysmediapair('SMS-pad'), cardinality=2)

	#Master System 2 console
interface_spec = InterfacesSpecification.objects.create(internal_name='Master System 2 console', implicit_system=False)
base = BaseSystem.objects.get(name='Master System')
interface_detail = SystemInterfaceDetail.objects.create(interfaces_specification=interface_spec, advertised_system=base)
ProvidedInterface.objects.create(interface_detail_base=interface_detail, interface=get_sysmediapair('SMS-cart'), cardinality=1)
ProvidedInterface.objects.create(interface_detail_base=interface_detail, interface=get_sysmediapair('SMS-pad'), cardinality=2)

	#Master System cartridge game
interface_spec = InterfacesSpecification.objects.create(internal_name='Master System cartridge game', implicit_system=False)
base = BaseSystem.objects.get(name='Master System')
interface_detail = SystemInterfaceDetail.objects.create(interfaces_specification=interface_spec, advertised_system=base)
RequiredInterface.objects.create(interface_detail_base=interface_detail, interface=get_sysmediapair('SMS-cart'), cardinality=1)

	#Master System Sega card game
interface_spec = InterfacesSpecification.objects.create(internal_name='Master System Sega card game', implicit_system=False)
base = BaseSystem.objects.get(name='Master System')
interface_detail = SystemInterfaceDetail.objects.create(interfaces_specification=interface_spec, advertised_system=base)
RequiredInterface.objects.create(interface_detail_base=interface_detail, interface=get_sysmediapair('SMS-scard'), cardinality=1)

	#Master System controller
interface_spec = InterfacesSpecification.objects.create(internal_name='Master System controller', implicit_system=False)
base = BaseSystem.objects.get(name='Master System')
interface_detail = SystemInterfaceDetail.objects.create(interfaces_specification=interface_spec, advertised_system=base)
RequiredInterface.objects.create(interface_detail_base=interface_detail, interface=get_sysmediapair('SMS-pad'), cardinality=1)

	#Master System Sega card accessory
interface_spec = InterfacesSpecification.objects.create(internal_name='Master System Sega card accessory', implicit_system=False)
base = BaseSystem.objects.get(name='Master System')
interface_detail = SystemInterfaceDetail.objects.create(interfaces_specification=interface_spec, advertised_system=base)
RequiredInterface.objects.create(interface_detail_base=interface_detail, interface=get_sysmediapair('SMS-scard'), cardinality=1)

	#Game Gear console
interface_spec = InterfacesSpecification.objects.create(internal_name='Game Gear console', implicit_system=False)
base = BaseSystem.objects.get(name='Game Gear')
interface_detail = SystemInterfaceDetail.objects.create(interfaces_specification=interface_spec, advertised_system=base)
ProvidedInterface.objects.create(interface_detail_base=interface_detail, interface=get_sysmediapair('GG-cart'), cardinality=1)

	#Game Gear game
interface_spec = InterfacesSpecification.objects.create(internal_name='Game Gear game', implicit_system=False)
base = BaseSystem.objects.get(name='Game Gear')
interface_detail = SystemInterfaceDetail.objects.create(interfaces_specification=interface_spec, advertised_system=base)
RequiredInterface.objects.create(interface_detail_base=interface_detail, interface=get_sysmediapair('GG-cart'), cardinality=1)

	#Mega Drive console
interface_spec = InterfacesSpecification.objects.create(internal_name='Mega Drive console', implicit_system=False)
base = BaseSystem.objects.get(name='Mega Drive')
interface_detail = SystemInterfaceDetail.objects.create(interfaces_specification=interface_spec, advertised_system=base)
ProvidedInterface.objects.create(interface_detail_base=interface_detail, interface=get_sysmediapair('MD-cart'), cardinality=1)
ProvidedInterface.objects.create(interface_detail_base=interface_detail, interface=get_sysmediapair('MD-pad'), cardinality=2)
ProvidedInterface.objects.create(interface_detail_base=interface_detail, interface=get_sysmediapair('MD-exp'), cardinality=1)

	#Mega Drive game
interface_spec = InterfacesSpecification.objects.create(internal_name='Mega Drive game', implicit_system=False)
base = BaseSystem.objects.get(name='Mega Drive')
interface_detail = SystemInterfaceDetail.objects.create(interfaces_specification=interface_spec, advertised_system=base)
RequiredInterface.objects.create(interface_detail_base=interface_detail, interface=get_sysmediapair('MD-cart'), cardinality=1)

	#Mega Drive controller
interface_spec = InterfacesSpecification.objects.create(internal_name='Mega Drive controller', implicit_system=False)
base = BaseSystem.objects.get(name='Mega Drive')
interface_detail = SystemInterfaceDetail.objects.create(interfaces_specification=interface_spec, advertised_system=base)
RequiredInterface.objects.create(interface_detail_base=interface_detail, interface=get_sysmediapair('MD-pad'), cardinality=1)

	#Mega-CD console
interface_spec = InterfacesSpecification.objects.create(internal_name='Mega-CD console', implicit_system=False)
base = BaseSystem.objects.get(name='Mega-CD')
interface_detail = SystemInterfaceDetail.objects.create(interfaces_specification=interface_spec, advertised_system=base)
ProvidedInterface.objects.create(interface_detail_base=interface_detail, interface=get_sysmediapair('MCD-disc'), cardinality=1)
RequiredInterface.objects.create(interface_detail_base=interface_detail, interface=get_sysmediapair('MD-exp'), cardinality=1)

	#Mega-CD game
interface_spec = InterfacesSpecification.objects.create(internal_name='Mega-CD game', implicit_system=False)
base = BaseSystem.objects.get(name='Mega-CD')
interface_detail = SystemInterfaceDetail.objects.create(interfaces_specification=interface_spec, advertised_system=base)
RequiredInterface.objects.create(interface_detail_base=interface_detail, interface=get_sysmediapair('MCD-disc'), cardinality=1)

	#32X console
interface_spec = InterfacesSpecification.objects.create(internal_name='32X console', implicit_system=False)
base = BaseSystem.objects.get(name='32X')
interface_detail = SystemInterfaceDetail.objects.create(interfaces_specification=interface_spec, advertised_system=base)
ProvidedInterface.objects.create(interface_detail_base=interface_detail, interface=get_sysmediapair('32X-cart'), cardinality=1)
RequiredInterface.objects.create(interface_detail_base=interface_detail, interface=get_sysmediapair('MD-cart'), cardinality=1)

	#32X game
interface_spec = InterfacesSpecification.objects.create(internal_name='32X game', implicit_system=False)
base = BaseSystem.objects.get(name='32X')
interface_detail = SystemInterfaceDetail.objects.create(interfaces_specification=interface_spec, advertised_system=base)
RequiredInterface.objects.create(interface_detail_base=interface_detail, interface=get_sysmediapair('32X-cart'), cardinality=1)

	#Mega-CD 32X system
interface_spec = InterfacesSpecification.objects.create(internal_name='Mega-CD 32X system', implicit_system=True)
base = BaseSystem.objects.get(name='Mega-CD 32X')
interface_detail = SystemInterfaceDetail.objects.create(interfaces_specification=interface_spec, advertised_system=base)
ProvidedInterface.objects.create(interface_detail_base=interface_detail, interface=get_sysmediapair('MCD32X-disc'), cardinality=1)
RequiredInterface.objects.create(interface_detail_base=interface_detail, interface=get_sysmediapair('MCD-disc'), cardinality=1)
RequiredInterface.objects.create(interface_detail_base=interface_detail, interface=get_sysmediapair('32X-cart'), cardinality=1)

	#Mega-CD 32X game
interface_spec = InterfacesSpecification.objects.create(internal_name='Mega-CD 32X game', implicit_system=False)
base = BaseSystem.objects.get(name='Mega-CD 32X')
interface_detail = SystemInterfaceDetail.objects.create(interfaces_specification=interface_spec, advertised_system=base)
RequiredInterface.objects.create(interface_detail_base=interface_detail, interface=get_sysmediapair('MCD32X-disc'), cardinality=1)

	#Saturn console
interface_spec = InterfacesSpecification.objects.create(internal_name='Saturn console', implicit_system=False)
base = BaseSystem.objects.get(name='Saturn')
interface_detail = SystemInterfaceDetail.objects.create(interfaces_specification=interface_spec, advertised_system=base)
ProvidedInterface.objects.create(interface_detail_base=interface_detail, interface=get_sysmediapair('Sat-disc'), cardinality=1)
ProvidedInterface.objects.create(interface_detail_base=interface_detail, interface=get_sysmediapair('Sat-pad'), cardinality=2)
ProvidedInterface.objects.create(interface_detail_base=interface_detail, interface=get_sysmediapair('Sat-cart'), cardinality=1)
ProvidedInterface.objects.create(interface_detail_base=interface_detail, interface=get_sysmediapair('Sat-exp'), cardinality=1)

	#Saturn game
interface_spec = InterfacesSpecification.objects.create(internal_name='Saturn game', implicit_system=False)
base = BaseSystem.objects.get(name='Saturn')
interface_detail = SystemInterfaceDetail.objects.create(interfaces_specification=interface_spec, advertised_system=base)
RequiredInterface.objects.create(interface_detail_base=interface_detail, interface=get_sysmediapair('Sat-disc'), cardinality=1)

	#Saturn controller
interface_spec = InterfacesSpecification.objects.create(internal_name='Saturn controller', implicit_system=False)
base = BaseSystem.objects.get(name='Saturn')
interface_detail = SystemInterfaceDetail.objects.create(interfaces_specification=interface_spec, advertised_system=base)
RequiredInterface.objects.create(interface_detail_base=interface_detail, interface=get_sysmediapair('Sat-pad'), cardinality=1)

	#Saturn cartridge
interface_spec = InterfacesSpecification.objects.create(internal_name='Saturn cartridge', implicit_system=False)
base = BaseSystem.objects.get(name='Saturn')
interface_detail = SystemInterfaceDetail.objects.create(interfaces_specification=interface_spec, advertised_system=base)
RequiredInterface.objects.create(interface_detail_base=interface_detail, interface=get_sysmediapair('Sat-cart'), cardinality=1)

	#Saturn internal card
interface_spec = InterfacesSpecification.objects.create(internal_name='Saturn internal card', implicit_system=False)
base = BaseSystem.objects.get(name='Saturn')
interface_detail = SystemInterfaceDetail.objects.create(interfaces_specification=interface_spec, advertised_system=base)
RequiredInterface.objects.create(interface_detail_base=interface_detail, interface=get_sysmediapair('Sat-exp'), cardinality=1)

	#Dreamcast console
interface_spec = InterfacesSpecification.objects.create(internal_name='Dreamcast console', implicit_system=False)
base = BaseSystem.objects.get(name='Dreamcast')
interface_detail = SystemInterfaceDetail.objects.create(interfaces_specification=interface_spec, advertised_system=base)
ProvidedInterface.objects.create(interface_detail_base=interface_detail, interface=get_sysmediapair('DC-disc'), cardinality=1)
ProvidedInterface.objects.create(interface_detail_base=interface_detail, interface=get_sysmediapair('DC-pad'), cardinality=4)

	#Dreamcast game
interface_spec = InterfacesSpecification.objects.create(internal_name='Dreamcast game', implicit_system=False)
base = BaseSystem.objects.get(name='Dreamcast')
interface_detail = SystemInterfaceDetail.objects.create(interfaces_specification=interface_spec, advertised_system=base)
RequiredInterface.objects.create(interface_detail_base=interface_detail, interface=get_sysmediapair('DC-disc'), cardinality=1)

	#Dreamcast controller
interface_spec = InterfacesSpecification.objects.create(internal_name='Dreamcast controller', implicit_system=False)
base = BaseSystem.objects.get(name='Dreamcast')
interface_detail = SystemInterfaceDetail.objects.create(interfaces_specification=interface_spec, advertised_system=base)
ProvidedInterface.objects.create(interface_detail_base=interface_detail, interface=get_sysmediapair('DC-cslot'), cardinality=2)
RequiredInterface.objects.create(interface_detail_base=interface_detail, interface=get_sysmediapair('DC-pad'), cardinality=1)

	#Dreamcast controller accessory
interface_spec = InterfacesSpecification.objects.create(internal_name='Dreamcast controller accessory', implicit_system=False)
base = BaseSystem.objects.get(name='Dreamcast')
interface_detail = SystemInterfaceDetail.objects.create(interfaces_specification=interface_spec, advertised_system=base)
RequiredInterface.objects.create(interface_detail_base=interface_detail, interface=get_sysmediapair('DC-cslot'), cardinality=1)

	#Nintendo Entertainment System console
interface_spec = InterfacesSpecification.objects.create(internal_name='Nintendo Entertainment System console', implicit_system=False)
base = BaseSystem.objects.get(name='Nintendo Entertainment System')
interface_detail = SystemInterfaceDetail.objects.create(interfaces_specification=interface_spec, advertised_system=base)
ProvidedInterface.objects.create(interface_detail_base=interface_detail, interface=get_sysmediapair('NES-cart'), cardinality=1)
ProvidedInterface.objects.create(interface_detail_base=interface_detail, interface=get_sysmediapair('NES-pad'), cardinality=2)

	#Nintendo Entertainment System game
interface_spec = InterfacesSpecification.objects.create(internal_name='Nintendo Entertainment System game', implicit_system=False)
base = BaseSystem.objects.get(name='Nintendo Entertainment System')
interface_detail = SystemInterfaceDetail.objects.create(interfaces_specification=interface_spec, advertised_system=base)
RequiredInterface.objects.create(interface_detail_base=interface_detail, interface=get_sysmediapair('NES-cart'), cardinality=1)

	#Nintendo Entertainment System controller
interface_spec = InterfacesSpecification.objects.create(internal_name='Nintendo Entertainment System controller', implicit_system=False)
base = BaseSystem.objects.get(name='Nintendo Entertainment System')
interface_detail = SystemInterfaceDetail.objects.create(interfaces_specification=interface_spec, advertised_system=base)
RequiredInterface.objects.create(interface_detail_base=interface_detail, interface=get_sysmediapair('NES-pad'), cardinality=1)

	#Super Nintendo console
interface_spec = InterfacesSpecification.objects.create(internal_name='Super Nintendo console', implicit_system=False)
base = BaseSystem.objects.get(name='Super Nintendo')
interface_detail = SystemInterfaceDetail.objects.create(interfaces_specification=interface_spec, advertised_system=base)
ProvidedInterface.objects.create(interface_detail_base=interface_detail, interface=get_sysmediapair('SNES-cart'), cardinality=1)
ProvidedInterface.objects.create(interface_detail_base=interface_detail, interface=get_sysmediapair('SNES-pad'), cardinality=2)

	#Super Nintendo game
interface_spec = InterfacesSpecification.objects.create(internal_name='Super Nintendo game', implicit_system=False)
base = BaseSystem.objects.get(name='Super Nintendo')
interface_detail = SystemInterfaceDetail.objects.create(interfaces_specification=interface_spec, advertised_system=base)
RequiredInterface.objects.create(interface_detail_base=interface_detail, interface=get_sysmediapair('SNES-cart'), cardinality=1)

	#Super Nintendo controller
interface_spec = InterfacesSpecification.objects.create(internal_name='Super Nintendo controller', implicit_system=False)
base = BaseSystem.objects.get(name='Super Nintendo')
interface_detail = SystemInterfaceDetail.objects.create(interfaces_specification=interface_spec, advertised_system=base)
RequiredInterface.objects.create(interface_detail_base=interface_detail, interface=get_sysmediapair('SNES-pad'), cardinality=1)

	#Nintendo 64 console
interface_spec = InterfacesSpecification.objects.create(internal_name='Nintendo 64 console', implicit_system=False)
base = BaseSystem.objects.get(name='Nintendo 64')
interface_detail = SystemInterfaceDetail.objects.create(interfaces_specification=interface_spec, advertised_system=base)
ProvidedInterface.objects.create(interface_detail_base=interface_detail, interface=get_sysmediapair('N64-cart'), cardinality=1)
ProvidedInterface.objects.create(interface_detail_base=interface_detail, interface=get_sysmediapair('N64-pad'), cardinality=4)
ProvidedInterface.objects.create(interface_detail_base=interface_detail, interface=get_sysmediapair('N64-mem'), cardinality=1)

	#Nintendo 64 game
interface_spec = InterfacesSpecification.objects.create(internal_name='Nintendo 64 game', implicit_system=False)
base = BaseSystem.objects.get(name='Nintendo 64')
interface_detail = SystemInterfaceDetail.objects.create(interfaces_specification=interface_spec, advertised_system=base)
RequiredInterface.objects.create(interface_detail_base=interface_detail, interface=get_sysmediapair('N64-cart'), cardinality=1)

	#Nintendo 64 controller
interface_spec = InterfacesSpecification.objects.create(internal_name='Nintendo 64 controller', implicit_system=False)
base = BaseSystem.objects.get(name='Nintendo 64')
interface_detail = SystemInterfaceDetail.objects.create(interfaces_specification=interface_spec, advertised_system=base)
ProvidedInterface.objects.create(interface_detail_base=interface_detail, interface=get_sysmediapair('N64-cslot'), cardinality=1)
RequiredInterface.objects.create(interface_detail_base=interface_detail, interface=get_sysmediapair('N64-pad'), cardinality=1)

	#Nintendo 64 expansion accessory
interface_spec = InterfacesSpecification.objects.create(internal_name='Nintendo 64 expansion accessory', implicit_system=False)
base = BaseSystem.objects.get(name='Nintendo 64')
interface_detail = SystemInterfaceDetail.objects.create(interfaces_specification=interface_spec, advertised_system=base)
RequiredInterface.objects.create(interface_detail_base=interface_detail, interface=get_sysmediapair('N64-mem'), cardinality=1)

	#Nintendo 64 controller accessory
interface_spec = InterfacesSpecification.objects.create(internal_name='Nintendo 64 controller accessory', implicit_system=False)
base = BaseSystem.objects.get(name='Nintendo 64')
interface_detail = SystemInterfaceDetail.objects.create(interfaces_specification=interface_spec, advertised_system=base)
RequiredInterface.objects.create(interface_detail_base=interface_detail, interface=get_sysmediapair('N64-cslot'), cardinality=1)

	#GameCube console
interface_spec = InterfacesSpecification.objects.create(internal_name='GameCube console', implicit_system=False)
base = BaseSystem.objects.get(name='GameCube')
interface_detail = SystemInterfaceDetail.objects.create(interfaces_specification=interface_spec, advertised_system=base)
ProvidedInterface.objects.create(interface_detail_base=interface_detail, interface=get_sysmediapair('GC-disc'), cardinality=1)
ProvidedInterface.objects.create(interface_detail_base=interface_detail, interface=get_sysmediapair('GC-pad'), cardinality=4)
ProvidedInterface.objects.create(interface_detail_base=interface_detail, interface=get_sysmediapair('GC-mcard'), cardinality=2)

	#GameCube game
interface_spec = InterfacesSpecification.objects.create(internal_name='GameCube game', implicit_system=False)
base = BaseSystem.objects.get(name='GameCube')
interface_detail = SystemInterfaceDetail.objects.create(interfaces_specification=interface_spec, advertised_system=base)
RequiredInterface.objects.create(interface_detail_base=interface_detail, interface=get_sysmediapair('GC-disc'), cardinality=1)

	#GameCube controller
interface_spec = InterfacesSpecification.objects.create(internal_name='GameCube controller', implicit_system=False)
base = BaseSystem.objects.get(name='GameCube')
interface_detail = SystemInterfaceDetail.objects.create(interfaces_specification=interface_spec, advertised_system=base)
RequiredInterface.objects.create(interface_detail_base=interface_detail, interface=get_sysmediapair('GC-pad'), cardinality=1)

	#GameCube storage accessory
interface_spec = InterfacesSpecification.objects.create(internal_name='GameCube storage accessory', implicit_system=False)
base = BaseSystem.objects.get(name='GameCube')
interface_detail = SystemInterfaceDetail.objects.create(interfaces_specification=interface_spec, advertised_system=base)
RequiredInterface.objects.create(interface_detail_base=interface_detail, interface=get_sysmediapair('GC-mcard'), cardinality=1)

	#Wii console (GC)
interface_spec = InterfacesSpecification.objects.create(internal_name='Wii console (GC)', implicit_system=False)
interface_detail = CommonInterfaceDetail.objects.create(interfaces_specification=interface_spec)
ProvidedInterface.objects.create(interface_detail_base=interface_detail, interface=get_sysmediapair('Wii-pad'), cardinality=4)
ProvidedInterface.objects.create(interface_detail_base=interface_detail, interface=get_sysmediapair('GC-pad'), cardinality=4)
base = BaseSystem.objects.get(name='Wii')
interface_detail = SystemInterfaceDetail.objects.create(interfaces_specification=interface_spec, advertised_system=base)
ProvidedInterface.objects.create(interface_detail_base=interface_detail, interface=get_sysmediapair('Wii-disc'), cardinality=1)
ProvidedInterface.objects.create(interface_detail_base=interface_detail, interface=get_sysmediapair('Wii-USB'), cardinality=2)
ProvidedInterface.objects.create(interface_detail_base=interface_detail, interface=get_sysmediapair('SDHC'), cardinality=1)
base = BaseSystem.objects.get(name='GameCube')
interface_detail = SystemInterfaceDetail.objects.create(interfaces_specification=interface_spec, advertised_system=base)
ProvidedInterface.objects.create(interface_detail_base=interface_detail, interface=get_sysmediapair('GC-disc'), cardinality=1, reused_interface=get_sysmediapair('Wii-disc'))
ProvidedInterface.objects.create(interface_detail_base=interface_detail, interface=get_sysmediapair('GC-mcard'), cardinality=2)

	#Wii game
interface_spec = InterfacesSpecification.objects.create(internal_name='Wii game', implicit_system=False)
base = BaseSystem.objects.get(name='Wii')
interface_detail = SystemInterfaceDetail.objects.create(interfaces_specification=interface_spec, advertised_system=base)
RequiredInterface.objects.create(interface_detail_base=interface_detail, interface=get_sysmediapair('Wii-disc'), cardinality=1)

	#wiimote controller
interface_spec = InterfacesSpecification.objects.create(internal_name='wiimote controller', implicit_system=False)
base = BaseSystem.objects.get(name='Wii')
interface_detail = SystemInterfaceDetail.objects.create(interfaces_specification=interface_spec, advertised_system=base)
ProvidedInterface.objects.create(interface_detail_base=interface_detail, interface=get_sysmediapair('Wii-cport'), cardinality=1)
RequiredInterface.objects.create(interface_detail_base=interface_detail, interface=get_sysmediapair('Wii-pad'), cardinality=1)

	#wiimote expansion
interface_spec = InterfacesSpecification.objects.create(internal_name='wiimote expansion', implicit_system=False)
base = BaseSystem.objects.get(name='Wii')
interface_detail = SystemInterfaceDetail.objects.create(interfaces_specification=interface_spec, advertised_system=base)
RequiredInterface.objects.create(interface_detail_base=interface_detail, interface=get_sysmediapair('Wii-cport'), cardinality=1)

	#wiimote shell accessory
interface_spec = InterfacesSpecification.objects.create(internal_name='wiimote shell accessory', implicit_system=False)
base = BaseSystem.objects.get(name='Wii')
interface_detail = SystemInterfaceDetail.objects.create(interfaces_specification=interface_spec, advertised_system=base)

	#Wii U console
interface_spec = InterfacesSpecification.objects.create(internal_name='Wii U console', implicit_system=False)
interface_detail = CommonInterfaceDetail.objects.create(interfaces_specification=interface_spec)
ProvidedInterface.objects.create(interface_detail_base=interface_detail, interface=get_sysmediapair('Wii-pad'), cardinality=4)
base = BaseSystem.objects.get(name='Wii U')
interface_detail = SystemInterfaceDetail.objects.create(interfaces_specification=interface_spec, advertised_system=base)
ProvidedInterface.objects.create(interface_detail_base=interface_detail, interface=get_sysmediapair('WiiU-disc'), cardinality=1)
ProvidedInterface.objects.create(interface_detail_base=interface_detail, interface=get_sysmediapair('WiiU-pad'), cardinality=1)
ProvidedInterface.objects.create(interface_detail_base=interface_detail, interface=get_sysmediapair('WiiU-USB'), cardinality=4)
ProvidedInterface.objects.create(interface_detail_base=interface_detail, interface=get_sysmediapair('SDHC'), cardinality=1)
base = BaseSystem.objects.get(name='Wii')
interface_detail = SystemInterfaceDetail.objects.create(interfaces_specification=interface_spec, advertised_system=base)
ProvidedInterface.objects.create(interface_detail_base=interface_detail, interface=get_sysmediapair('Wii-disc'), cardinality=1, reused_interface=get_sysmediapair('WiiU-disc'))

	#Wii U game
interface_spec = InterfacesSpecification.objects.create(internal_name='Wii U game', implicit_system=False)
base = BaseSystem.objects.get(name='Wii U')
interface_detail = SystemInterfaceDetail.objects.create(interfaces_specification=interface_spec, advertised_system=base)
RequiredInterface.objects.create(interface_detail_base=interface_detail, interface=get_sysmediapair('WiiU-disc'), cardinality=1)

	#Wii U GamePad
interface_spec = InterfacesSpecification.objects.create(internal_name='Wii U GamePad', implicit_system=False)
base = BaseSystem.objects.get(name='Wii U')
interface_detail = SystemInterfaceDetail.objects.create(interfaces_specification=interface_spec, advertised_system=base)
RequiredInterface.objects.create(interface_detail_base=interface_detail, interface=get_sysmediapair('WiiU-pad'), cardinality=1)

	#PlayStation console
interface_spec = InterfacesSpecification.objects.create(internal_name='PlayStation console', implicit_system=False)
base = BaseSystem.objects.get(name='PlayStation')
interface_detail = SystemInterfaceDetail.objects.create(interfaces_specification=interface_spec, advertised_system=base)
ProvidedInterface.objects.create(interface_detail_base=interface_detail, interface=get_sysmediapair('PS1-disc'), cardinality=1)
ProvidedInterface.objects.create(interface_detail_base=interface_detail, interface=get_sysmediapair('PS1-pad'), cardinality=2)
ProvidedInterface.objects.create(interface_detail_base=interface_detail, interface=get_sysmediapair('PS1-mcard'), cardinality=2)

	#PlayStation game
interface_spec = InterfacesSpecification.objects.create(internal_name='PlayStation game', implicit_system=False)
base = BaseSystem.objects.get(name='PlayStation')
interface_detail = SystemInterfaceDetail.objects.create(interfaces_specification=interface_spec, advertised_system=base)
RequiredInterface.objects.create(interface_detail_base=interface_detail, interface=get_sysmediapair('PS1-disc'), cardinality=1)

	#PlayStation controller
interface_spec = InterfacesSpecification.objects.create(internal_name='PlayStation controller', implicit_system=False)
base = BaseSystem.objects.get(name='PlayStation')
interface_detail = SystemInterfaceDetail.objects.create(interfaces_specification=interface_spec, advertised_system=base)
RequiredInterface.objects.create(interface_detail_base=interface_detail, interface=get_sysmediapair('PS1-pad'), cardinality=1)

	#PlayStation memory card
interface_spec = InterfacesSpecification.objects.create(internal_name='PlayStation memory card', implicit_system=False)
base = BaseSystem.objects.get(name='PlayStation')
interface_detail = SystemInterfaceDetail.objects.create(interfaces_specification=interface_spec, advertised_system=base)
RequiredInterface.objects.create(interface_detail_base=interface_detail, interface=get_sysmediapair('PS1-mcard'), cardinality=1)

	#PlayStation mutitap
interface_spec = InterfacesSpecification.objects.create(internal_name='PlayStation mutitap', implicit_system=False)
base = BaseSystem.objects.get(name='PlayStation')
interface_detail = SystemInterfaceDetail.objects.create(interfaces_specification=interface_spec, advertised_system=base)
ProvidedInterface.objects.create(interface_detail_base=interface_detail, interface=get_sysmediapair('PS1-pad'), cardinality=4)
ProvidedInterface.objects.create(interface_detail_base=interface_detail, interface=get_sysmediapair('PS1-mcard'), cardinality=4)
RequiredInterface.objects.create(interface_detail_base=interface_detail, interface=get_sysmediapair('PS1-pad'), cardinality=1)

	#PlayStation 2 console
interface_spec = InterfacesSpecification.objects.create(internal_name='PlayStation 2 console', implicit_system=False)
interface_detail = CommonInterfaceDetail.objects.create(interfaces_specification=interface_spec)
ProvidedInterface.objects.create(interface_detail_base=interface_detail, interface=get_sysmediapair('PS2-pad'), cardinality=2)
ProvidedInterface.objects.create(interface_detail_base=interface_detail, interface=get_sysmediapair('PS2-mcard'), cardinality=2)
base = BaseSystem.objects.get(name='PlayStation 2')
interface_detail = SystemInterfaceDetail.objects.create(interfaces_specification=interface_spec, advertised_system=base)
ProvidedInterface.objects.create(interface_detail_base=interface_detail, interface=get_sysmediapair('PS2-disc'), cardinality=1)
ProvidedInterface.objects.create(interface_detail_base=interface_detail, interface=get_sysmediapair('PS2-USB'), cardinality=2)
ProvidedInterface.objects.create(interface_detail_base=interface_detail, interface=get_sysmediapair('PS1-disc'), cardinality=1)
base = BaseSystem.objects.get(name='PlayStation')
interface_detail = SystemInterfaceDetail.objects.create(interfaces_specification=interface_spec, advertised_system=base)
ProvidedInterface.objects.create(interface_detail_base=interface_detail, interface=get_sysmediapair('PS1-disc'), cardinality=1, reused_interface=get_sysmediapair('PS2-disc'))

	#PlayStation 2 game
interface_spec = InterfacesSpecification.objects.create(internal_name='PlayStation 2 game', implicit_system=False)
base = BaseSystem.objects.get(name='PlayStation 2')
interface_detail = SystemInterfaceDetail.objects.create(interfaces_specification=interface_spec, advertised_system=base)
RequiredInterface.objects.create(interface_detail_base=interface_detail, interface=get_sysmediapair('PS2-disc'), cardinality=1)

	#PlayStation 2 controller
interface_spec = InterfacesSpecification.objects.create(internal_name='PlayStation 2 controller', implicit_system=False)
base = BaseSystem.objects.get(name='PlayStation 2')
interface_detail = SystemInterfaceDetail.objects.create(interfaces_specification=interface_spec, advertised_system=base)
RequiredInterface.objects.create(interface_detail_base=interface_detail, interface=get_sysmediapair('PS2-pad'), cardinality=1)

	#PlayStation 2 memory card
interface_spec = InterfacesSpecification.objects.create(internal_name='PlayStation 2 memory card', implicit_system=False)
base = BaseSystem.objects.get(name='PlayStation 2')
interface_detail = SystemInterfaceDetail.objects.create(interfaces_specification=interface_spec, advertised_system=base)
RequiredInterface.objects.create(interface_detail_base=interface_detail, interface=get_sysmediapair('PS2-mcard'), cardinality=1)

	#PlayStation 2 USB accessory
interface_spec = InterfacesSpecification.objects.create(internal_name='PlayStation 2 USB accessory', implicit_system=False)
base = BaseSystem.objects.get(name='PlayStation 2')
interface_detail = SystemInterfaceDetail.objects.create(interfaces_specification=interface_spec, advertised_system=base)
RequiredInterface.objects.create(interface_detail_base=interface_detail, interface=get_sysmediapair('PS2-USB'), cardinality=1)

	#PlayStation 3 console (PS2 PS1)
interface_spec = InterfacesSpecification.objects.create(internal_name='PlayStation 3 console (PS2 PS1)', implicit_system=False)
interface_detail = CommonInterfaceDetail.objects.create(interfaces_specification=interface_spec)
ProvidedInterface.objects.create(interface_detail_base=interface_detail, interface=get_sysmediapair('PS3-pad'), cardinality=4)
base = BaseSystem.objects.get(name='PlayStation 3')
interface_detail = SystemInterfaceDetail.objects.create(interfaces_specification=interface_spec, advertised_system=base)
ProvidedInterface.objects.create(interface_detail_base=interface_detail, interface=get_sysmediapair('PS3-disc'), cardinality=1)
ProvidedInterface.objects.create(interface_detail_base=interface_detail, interface=get_sysmediapair('PS3-USB'), cardinality=4)
base = BaseSystem.objects.get(name='PlayStation')
interface_detail = SystemInterfaceDetail.objects.create(interfaces_specification=interface_spec, advertised_system=base)
ProvidedInterface.objects.create(interface_detail_base=interface_detail, interface=get_sysmediapair('PS1-disc'), cardinality=1, reused_interface=get_sysmediapair('PS3-disc'))
base = BaseSystem.objects.get(name='PlayStation 2')
interface_detail = SystemInterfaceDetail.objects.create(interfaces_specification=interface_spec, advertised_system=base)
ProvidedInterface.objects.create(interface_detail_base=interface_detail, interface=get_sysmediapair('PS2-disc'), cardinality=1, reused_interface=get_sysmediapair('PS3-disc'))

	#PlayStation 3 console (PS1)
interface_spec = InterfacesSpecification.objects.create(internal_name='PlayStation 3 console (PS1)', implicit_system=False)
interface_detail = CommonInterfaceDetail.objects.create(interfaces_specification=interface_spec)
ProvidedInterface.objects.create(interface_detail_base=interface_detail, interface=get_sysmediapair('PS3-pad'), cardinality=4)
base = BaseSystem.objects.get(name='PlayStation 3')
interface_detail = SystemInterfaceDetail.objects.create(interfaces_specification=interface_spec, advertised_system=base)
ProvidedInterface.objects.create(interface_detail_base=interface_detail, interface=get_sysmediapair('PS3-disc'), cardinality=1)
ProvidedInterface.objects.create(interface_detail_base=interface_detail, interface=get_sysmediapair('PS3-USB'), cardinality=4)
base = BaseSystem.objects.get(name='PlayStation')
interface_detail = SystemInterfaceDetail.objects.create(interfaces_specification=interface_spec, advertised_system=base)
ProvidedInterface.objects.create(interface_detail_base=interface_detail, interface=get_sysmediapair('PS1-disc'), cardinality=1, reused_interface=get_sysmediapair('PS3-disc'))

	#PlayStation 3 game
interface_spec = InterfacesSpecification.objects.create(internal_name='PlayStation 3 game', implicit_system=False)
base = BaseSystem.objects.get(name='PlayStation 3')
interface_detail = SystemInterfaceDetail.objects.create(interfaces_specification=interface_spec, advertised_system=base)
RequiredInterface.objects.create(interface_detail_base=interface_detail, interface=get_sysmediapair('PS3-disc'), cardinality=1)

	#PlayStation 3 controller
interface_spec = InterfacesSpecification.objects.create(internal_name='PlayStation 3 controller', implicit_system=False)
base = BaseSystem.objects.get(name='PlayStation 3')
interface_detail = SystemInterfaceDetail.objects.create(interfaces_specification=interface_spec, advertised_system=base)
RequiredInterface.objects.create(interface_detail_base=interface_detail, interface=get_sysmediapair('PS3-pad'), cardinality=1)

	#PlayStation 3 USB accessory
interface_spec = InterfacesSpecification.objects.create(internal_name='PlayStation 3 USB accessory', implicit_system=False)
base = BaseSystem.objects.get(name='PlayStation 3')
interface_detail = SystemInterfaceDetail.objects.create(interfaces_specification=interface_spec, advertised_system=base)
RequiredInterface.objects.create(interface_detail_base=interface_detail, interface=get_sysmediapair('PS3-USB'), cardinality=1)

	#PlayStation 4 console
interface_spec = InterfacesSpecification.objects.create(internal_name='PlayStation 4 console', implicit_system=False)
base = BaseSystem.objects.get(name='PlayStation 4')
interface_detail = SystemInterfaceDetail.objects.create(interfaces_specification=interface_spec, advertised_system=base)
ProvidedInterface.objects.create(interface_detail_base=interface_detail, interface=get_sysmediapair('PS4-disc'), cardinality=1)
ProvidedInterface.objects.create(interface_detail_base=interface_detail, interface=get_sysmediapair('PS4-pad'), cardinality=4)
ProvidedInterface.objects.create(interface_detail_base=interface_detail, interface=get_sysmediapair('PS4-USB'), cardinality=2)

	#PlayStation 4 game
interface_spec = InterfacesSpecification.objects.create(internal_name='PlayStation 4 game', implicit_system=False)
base = BaseSystem.objects.get(name='PlayStation 4')
interface_detail = SystemInterfaceDetail.objects.create(interfaces_specification=interface_spec, advertised_system=base)
RequiredInterface.objects.create(interface_detail_base=interface_detail, interface=get_sysmediapair('PS4-disc'), cardinality=1)

	#PlayStation 4 controller
interface_spec = InterfacesSpecification.objects.create(internal_name='PlayStation 4 controller', implicit_system=False)
base = BaseSystem.objects.get(name='PlayStation 4')
interface_detail = SystemInterfaceDetail.objects.create(interfaces_specification=interface_spec, advertised_system=base)
RequiredInterface.objects.create(interface_detail_base=interface_detail, interface=get_sysmediapair('PS4-pad'), cardinality=1)

	#Xbox console
interface_spec = InterfacesSpecification.objects.create(internal_name='Xbox console', implicit_system=False)
base = BaseSystem.objects.get(name='Xbox')
interface_detail = SystemInterfaceDetail.objects.create(interfaces_specification=interface_spec, advertised_system=base)
ProvidedInterface.objects.create(interface_detail_base=interface_detail, interface=get_sysmediapair('Xbox-disc'), cardinality=1)
ProvidedInterface.objects.create(interface_detail_base=interface_detail, interface=get_sysmediapair('Xbox-pad'), cardinality=4)

	#Xbox game
interface_spec = InterfacesSpecification.objects.create(internal_name='Xbox game', implicit_system=False)
base = BaseSystem.objects.get(name='Xbox')
interface_detail = SystemInterfaceDetail.objects.create(interfaces_specification=interface_spec, advertised_system=base)
RequiredInterface.objects.create(interface_detail_base=interface_detail, interface=get_sysmediapair('Xbox-disc'), cardinality=1)

	#Xbox controller
interface_spec = InterfacesSpecification.objects.create(internal_name='Xbox controller', implicit_system=False)
base = BaseSystem.objects.get(name='Xbox')
interface_detail = SystemInterfaceDetail.objects.create(interfaces_specification=interface_spec, advertised_system=base)
RequiredInterface.objects.create(interface_detail_base=interface_detail, interface=get_sysmediapair('Xbox-pad'), cardinality=1)

	#Xbox 360 console (original)
interface_spec = InterfacesSpecification.objects.create(internal_name='Xbox 360 console (original)', implicit_system=False)
base = BaseSystem.objects.get(name='Xbox 360')
interface_detail = SystemInterfaceDetail.objects.create(interfaces_specification=interface_spec, advertised_system=base)
ProvidedInterface.objects.create(interface_detail_base=interface_detail, interface=get_sysmediapair('360-disc'), cardinality=1)
ProvidedInterface.objects.create(interface_detail_base=interface_detail, interface=get_sysmediapair('360-pad'), cardinality=4)
ProvidedInterface.objects.create(interface_detail_base=interface_detail, interface=get_sysmediapair('360-USB'), cardinality=3)

	#Xbox 360 console (revision S)
interface_spec = InterfacesSpecification.objects.create(internal_name='Xbox 360 console (revision S)', implicit_system=False)
base = BaseSystem.objects.get(name='Xbox 360')
interface_detail = SystemInterfaceDetail.objects.create(interfaces_specification=interface_spec, advertised_system=base)
ProvidedInterface.objects.create(interface_detail_base=interface_detail, interface=get_sysmediapair('360-disc'), cardinality=1)
ProvidedInterface.objects.create(interface_detail_base=interface_detail, interface=get_sysmediapair('360-pad'), cardinality=4)
ProvidedInterface.objects.create(interface_detail_base=interface_detail, interface=get_sysmediapair('360-USB'), cardinality=5)

	#Xbox 360 console (revision E)
interface_spec = InterfacesSpecification.objects.create(internal_name='Xbox 360 console (revision E)', implicit_system=False)
base = BaseSystem.objects.get(name='Xbox 360')
interface_detail = SystemInterfaceDetail.objects.create(interfaces_specification=interface_spec, advertised_system=base)
ProvidedInterface.objects.create(interface_detail_base=interface_detail, interface=get_sysmediapair('360-disc'), cardinality=1)
ProvidedInterface.objects.create(interface_detail_base=interface_detail, interface=get_sysmediapair('360-pad'), cardinality=4)
ProvidedInterface.objects.create(interface_detail_base=interface_detail, interface=get_sysmediapair('360-USB'), cardinality=4)

	#Xbox 360 game
interface_spec = InterfacesSpecification.objects.create(internal_name='Xbox 360 game', implicit_system=False)
base = BaseSystem.objects.get(name='Xbox 360')
interface_detail = SystemInterfaceDetail.objects.create(interfaces_specification=interface_spec, advertised_system=base)
RequiredInterface.objects.create(interface_detail_base=interface_detail, interface=get_sysmediapair('360-disc'), cardinality=1)

	#Xbox 360 controller
interface_spec = InterfacesSpecification.objects.create(internal_name='Xbox 360 controller', implicit_system=False)
base = BaseSystem.objects.get(name='Xbox 360')
interface_detail = SystemInterfaceDetail.objects.create(interfaces_specification=interface_spec, advertised_system=base)
RequiredInterface.objects.create(interface_detail_base=interface_detail, interface=get_sysmediapair('360-pad'), cardinality=1)

	#Xbox One console
interface_spec = InterfacesSpecification.objects.create(internal_name='Xbox One console', implicit_system=False)
base = BaseSystem.objects.get(name='Xbox One')
interface_detail = SystemInterfaceDetail.objects.create(interfaces_specification=interface_spec, advertised_system=base)
ProvidedInterface.objects.create(interface_detail_base=interface_detail, interface=get_sysmediapair('X1-disc'), cardinality=1)
ProvidedInterface.objects.create(interface_detail_base=interface_detail, interface=get_sysmediapair('X1-pad'), cardinality=4)
ProvidedInterface.objects.create(interface_detail_base=interface_detail, interface=get_sysmediapair('X1-USB'), cardinality=3)

	#Xbox One game
interface_spec = InterfacesSpecification.objects.create(internal_name='Xbox One game', implicit_system=False)
base = BaseSystem.objects.get(name='Xbox One')
interface_detail = SystemInterfaceDetail.objects.create(interfaces_specification=interface_spec, advertised_system=base)
RequiredInterface.objects.create(interface_detail_base=interface_detail, interface=get_sysmediapair('X1-disc'), cardinality=1)

	#Xbox One controller
interface_spec = InterfacesSpecification.objects.create(internal_name='Xbox One controller', implicit_system=False)
base = BaseSystem.objects.get(name='Xbox One')
interface_detail = SystemInterfaceDetail.objects.create(interfaces_specification=interface_spec, advertised_system=base)
RequiredInterface.objects.create(interface_detail_base=interface_detail, interface=get_sysmediapair('X1-pad'), cardinality=1)

	#Atari 2600 console
interface_spec = InterfacesSpecification.objects.create(internal_name='Atari 2600 console', implicit_system=False)
base = BaseSystem.objects.get(name='Atari 2600')
interface_detail = SystemInterfaceDetail.objects.create(interfaces_specification=interface_spec, advertised_system=base)
ProvidedInterface.objects.create(interface_detail_base=interface_detail, interface=get_sysmediapair('2600-cart'), cardinality=1)
ProvidedInterface.objects.create(interface_detail_base=interface_detail, interface=get_sysmediapair('2600-pad'), cardinality=2)

	#Atari 2600 game
interface_spec = InterfacesSpecification.objects.create(internal_name='Atari 2600 game', implicit_system=False)
base = BaseSystem.objects.get(name='Atari 2600')
interface_detail = SystemInterfaceDetail.objects.create(interfaces_specification=interface_spec, advertised_system=base)
RequiredInterface.objects.create(interface_detail_base=interface_detail, interface=get_sysmediapair('2600-cart'), cardinality=1)

	#Atari 2600 controller
interface_spec = InterfacesSpecification.objects.create(internal_name='Atari 2600 controller', implicit_system=False)
base = BaseSystem.objects.get(name='Atari 2600')
interface_detail = SystemInterfaceDetail.objects.create(interfaces_specification=interface_spec, advertised_system=base)
RequiredInterface.objects.create(interface_detail_base=interface_detail, interface=get_sysmediapair('2600-pad'), cardinality=1)

	#PC system
interface_spec = InterfacesSpecification.objects.create(internal_name='PC system', implicit_system=False)
base = BaseSystem.objects.get(name='Personal Computer')
interface_detail = SystemInterfaceDetail.objects.create(interfaces_specification=interface_spec, advertised_system=base)
ProvidedInterface.objects.create(interface_detail_base=interface_detail, interface=get_sysmediapair('PC-fd8'), cardinality=1)
ProvidedInterface.objects.create(interface_detail_base=interface_detail, interface=get_sysmediapair('PC-fd5'), cardinality=1)
ProvidedInterface.objects.create(interface_detail_base=interface_detail, interface=get_sysmediapair('PC-fd3'), cardinality=1)
ProvidedInterface.objects.create(interface_detail_base=interface_detail, interface=get_sysmediapair('PC-CD'), cardinality=1)
ProvidedInterface.objects.create(interface_detail_base=interface_detail, interface=get_sysmediapair('PC-DVD'), cardinality=1)
ProvidedInterface.objects.create(interface_detail_base=interface_detail, interface=get_sysmediapair('PC-BD'), cardinality=1)
ProvidedInterface.objects.create(interface_detail_base=interface_detail, interface=get_sysmediapair('SD'), cardinality=1)
ProvidedInterface.objects.create(interface_detail_base=interface_detail, interface=get_sysmediapair('SDHC'), cardinality=1)
ProvidedInterface.objects.create(interface_detail_base=interface_detail, interface=get_sysmediapair('PC-USB'), cardinality=1)

	#PC 5"1/4 floppy
interface_spec = InterfacesSpecification.objects.create(internal_name='PC 5"1/4 floppy', implicit_system=False)
base = BaseSystem.objects.get(name='Personal Computer')
interface_detail = SystemInterfaceDetail.objects.create(interfaces_specification=interface_spec, advertised_system=base)
RequiredInterface.objects.create(interface_detail_base=interface_detail, interface=get_sysmediapair('PC-fd5'), cardinality=1)

	#PC 3"1/2 floppy
interface_spec = InterfacesSpecification.objects.create(internal_name='PC 3"1/2 floppy', implicit_system=False)
base = BaseSystem.objects.get(name='Personal Computer')
interface_detail = SystemInterfaceDetail.objects.create(interfaces_specification=interface_spec, advertised_system=base)
RequiredInterface.objects.create(interface_detail_base=interface_detail, interface=get_sysmediapair('PC-fd3'), cardinality=1)

	#PC-CD
interface_spec = InterfacesSpecification.objects.create(internal_name='PC-CD', implicit_system=False)
base = BaseSystem.objects.get(name='Personal Computer')
interface_detail = SystemInterfaceDetail.objects.create(interfaces_specification=interface_spec, advertised_system=base)
RequiredInterface.objects.create(interface_detail_base=interface_detail, interface=get_sysmediapair('PC-CD'), cardinality=1)

	#PC-DVD
interface_spec = InterfacesSpecification.objects.create(internal_name='PC-DVD', implicit_system=False)
base = BaseSystem.objects.get(name='Personal Computer')
interface_detail = SystemInterfaceDetail.objects.create(interfaces_specification=interface_spec, advertised_system=base)
RequiredInterface.objects.create(interface_detail_base=interface_detail, interface=get_sysmediapair('PC-DVD'), cardinality=1)

	#PC-BD
interface_spec = InterfacesSpecification.objects.create(internal_name='PC-BD', implicit_system=False)
base = BaseSystem.objects.get(name='Personal Computer')
interface_detail = SystemInterfaceDetail.objects.create(interfaces_specification=interface_spec, advertised_system=base)
RequiredInterface.objects.create(interface_detail_base=interface_detail, interface=get_sysmediapair('PC-BD'), cardinality=1)

