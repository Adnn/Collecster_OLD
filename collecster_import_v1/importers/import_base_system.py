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

base_system = BaseSystem.objects.create(name='Master System', brand=Company.objects.get(name='Sega'), generation=3, destination='H', upgrade_for=None, abbreviated_name='SMS')
SystemMediaPair.objects.create(system=base_system, media='cartridge', wireless=False, abbreviated_name='SMS-cart')
SystemMediaPair.objects.create(system=base_system, media='Sega card', wireless=False, abbreviated_name='SMS-scard')
SystemMediaPair.objects.create(system=base_system, media='controller', wireless=False, abbreviated_name='SMS-pad')

base_system = BaseSystem.objects.create(name='Game Gear', brand=Company.objects.get(name='Sega'), generation=4, destination='H', upgrade_for=None, abbreviated_name='GG')
SystemMediaPair.objects.create(system=base_system, media='cartridge', wireless=False, abbreviated_name='GG-cart')

base_system = BaseSystem.objects.create(name='Mega Drive', brand=Company.objects.get(name='Sega'), generation=4, destination='H', upgrade_for=None, abbreviated_name='MD')
SystemMediaPair.objects.create(system=base_system, media='cartridge', wireless=False, abbreviated_name='MD-cart')
SystemMediaPair.objects.create(system=base_system, media='controller', wireless=False, abbreviated_name='MD-pad')
SystemMediaPair.objects.create(system=base_system, media='expansion port', wireless=False, abbreviated_name='MD-exp')

base_system = BaseSystem.objects.create(name='Mega-CD', brand=Company.objects.get(name='Sega'), generation=4, destination='H', upgrade_for=get_bs('Mega Drive'), abbreviated_name='MCD')
SystemMediaPair.objects.create(system=base_system, media='CD-ROM', wireless=False, abbreviated_name='MCD-disc')

base_system = BaseSystem.objects.create(name='32X', brand=Company.objects.get(name='Sega'), generation=4, destination='H', upgrade_for=get_bs('Mega Drive'), abbreviated_name='32X')
SystemMediaPair.objects.create(system=base_system, media='cartridge', wireless=False, abbreviated_name='32X-cart')

base_system = BaseSystem.objects.create(name='Mega-CD 32X', brand=Company.objects.get(name='Sega'), generation=4, destination='H', upgrade_for=get_bs('Mega Drive'), abbreviated_name='MCD32X')
SystemMediaPair.objects.create(system=base_system, media='CD-ROM', wireless=False, abbreviated_name='MCD32X-disc')

base_system = BaseSystem.objects.create(name='Saturn', brand=Company.objects.get(name='Sega'), generation=5, destination='H', upgrade_for=None, abbreviated_name='Saturn')
SystemMediaPair.objects.create(system=base_system, media='CD-ROM', wireless=False, abbreviated_name='Sat-disc')
SystemMediaPair.objects.create(system=base_system, media='controller', wireless=False, abbreviated_name='Sat-pad')
SystemMediaPair.objects.create(system=base_system, media='cartridge slot', wireless=False, abbreviated_name='Sat-cart')
SystemMediaPair.objects.create(system=base_system, media='internal expansion', wireless=False, abbreviated_name='Sat-exp')

base_system = BaseSystem.objects.create(name='Dreamcast', brand=Company.objects.get(name='Sega'), generation=6, destination='H', upgrade_for=None, abbreviated_name='DC')
SystemMediaPair.objects.create(system=base_system, media='GD-ROM', wireless=False, abbreviated_name='DC-disc')
SystemMediaPair.objects.create(system=base_system, media='controller', wireless=False, abbreviated_name='DC-pad')
SystemMediaPair.objects.create(system=base_system, media='controller expansion slot', wireless=False, abbreviated_name='DC-cslot')

base_system = BaseSystem.objects.create(name='Nintendo Entertainment System', brand=Company.objects.get(name='Nintendo'), generation=3, destination='H', upgrade_for=None, abbreviated_name='NES')
SystemMediaPair.objects.create(system=base_system, media='cartridge', wireless=False, abbreviated_name='NES-cart')
SystemMediaPair.objects.create(system=base_system, media='controller', wireless=False, abbreviated_name='NES-pad')

base_system = BaseSystem.objects.create(name='Super Nintendo', brand=Company.objects.get(name='Nintendo'), generation=4, destination='H', upgrade_for=None, abbreviated_name='SNES')
SystemMediaPair.objects.create(system=base_system, media='cartridge', wireless=False, abbreviated_name='SNES-cart')
SystemMediaPair.objects.create(system=base_system, media='controller', wireless=False, abbreviated_name='SNES-pad')

base_system = BaseSystem.objects.create(name='Virtual Boy', brand=Company.objects.get(name='Nintendo'), generation=5, destination='H', upgrade_for=None, abbreviated_name='Vboy')
SystemMediaPair.objects.create(system=base_system, media='cartridge', wireless=False, abbreviated_name='Vboy-cart')
SystemMediaPair.objects.create(system=base_system, media='controller', wireless=False, abbreviated_name='Vboy-pad')

base_system = BaseSystem.objects.create(name='Nintendo 64', brand=Company.objects.get(name='Nintendo'), generation=5, destination='H', upgrade_for=None, abbreviated_name='N64')
SystemMediaPair.objects.create(system=base_system, media='cartridge', wireless=False, abbreviated_name='N64-cart')
SystemMediaPair.objects.create(system=base_system, media='controller', wireless=False, abbreviated_name='N64-pad')
SystemMediaPair.objects.create(system=base_system, media='memory expansion', wireless=False, abbreviated_name='N64-mem')
SystemMediaPair.objects.create(system=base_system, media='controller expansion slot', wireless=False, abbreviated_name='N64-cslot')

base_system = BaseSystem.objects.create(name='GameCube', brand=Company.objects.get(name='Nintendo'), generation=6, destination='H', upgrade_for=None, abbreviated_name='GC')
SystemMediaPair.objects.create(system=base_system, media='miniDVD', wireless=False, abbreviated_name='GC-disc')
SystemMediaPair.objects.create(system=base_system, media='controller', wireless=False, abbreviated_name='GC-pad')
SystemMediaPair.objects.create(system=base_system, media='memory card', wireless=False, abbreviated_name='GC-mcard')

base_system = BaseSystem.objects.create(name='Wii', brand=Company.objects.get(name='Nintendo'), generation=7, destination='H', upgrade_for=None, abbreviated_name='Wii')
SystemMediaPair.objects.create(system=base_system, media='Wii disc', wireless=False, abbreviated_name='Wii-disc')
SystemMediaPair.objects.create(system=base_system, media='controller', wireless=True, abbreviated_name='Wii-pad')
SystemMediaPair.objects.create(system=base_system, media='USB', wireless=False, abbreviated_name='Wii-USB')
SystemMediaPair.objects.create(system=base_system, media='controller expansion port', wireless=False, abbreviated_name='Wii-cport')

base_system = BaseSystem.objects.create(name='Wii U', brand=Company.objects.get(name='Nintendo'), generation=8, destination='H', upgrade_for=None, abbreviated_name='WiiU')
SystemMediaPair.objects.create(system=base_system, media='Wii U disc', wireless=False, abbreviated_name='WiiU-disc')
SystemMediaPair.objects.create(system=base_system, media='GamePad (screen)', wireless=True, abbreviated_name='WiiU-pad')
SystemMediaPair.objects.create(system=base_system, media='USB', wireless=True, abbreviated_name='WiiU-USB')

base_system = BaseSystem.objects.create(name='PlayStation', brand=Company.objects.get(name='Sony'), generation=5, destination='H', upgrade_for=None, abbreviated_name='PS1')
SystemMediaPair.objects.create(system=base_system, media='CD-ROM', wireless=False, abbreviated_name='PS1-disc')
SystemMediaPair.objects.create(system=base_system, media='controller', wireless=False, abbreviated_name='PS1-pad')
SystemMediaPair.objects.create(system=base_system, media='memory card', wireless=False, abbreviated_name='PS1-mcard')

base_system = BaseSystem.objects.create(name='PlayStation 2', brand=Company.objects.get(name='Sony'), generation=6, destination='H', upgrade_for=None, abbreviated_name='PS2')
SystemMediaPair.objects.create(system=base_system, media='DVD-ROM', wireless=False, abbreviated_name='PS2-disc')
SystemMediaPair.objects.create(system=base_system, media='controller', wireless=False, abbreviated_name='PS2-pad')
SystemMediaPair.objects.create(system=base_system, media='memory card', wireless=False, abbreviated_name='PS2-mcard')
SystemMediaPair.objects.create(system=base_system, media='USB', wireless=False, abbreviated_name='PS2-USB')

base_system = BaseSystem.objects.create(name='PlayStation 3', brand=Company.objects.get(name='Sony'), generation=7, destination='H', upgrade_for=None, abbreviated_name='PS3')
SystemMediaPair.objects.create(system=base_system, media='Blu-ray', wireless=False, abbreviated_name='PS3-disc')
SystemMediaPair.objects.create(system=base_system, media='controller', wireless=True, abbreviated_name='PS3-pad')
SystemMediaPair.objects.create(system=base_system, media='USB', wireless=False, abbreviated_name='PS3-USB')

base_system = BaseSystem.objects.create(name='PlayStation 4', brand=Company.objects.get(name='Sony'), generation=8, destination='H', upgrade_for=None, abbreviated_name='PS4')
SystemMediaPair.objects.create(system=base_system, media='Blu-ray', wireless=False, abbreviated_name='PS4-disc')
SystemMediaPair.objects.create(system=base_system, media='controller', wireless=True, abbreviated_name='PS4-pad')
SystemMediaPair.objects.create(system=base_system, media='USB', wireless=False, abbreviated_name='PS4-USB')

base_system = BaseSystem.objects.create(name='Xbox', brand=Company.objects.get(name='Microsoft'), generation=6, destination='H', upgrade_for=None, abbreviated_name='Xbox')
SystemMediaPair.objects.create(system=base_system, media='DVD', wireless=False, abbreviated_name='Xbox-disc')
SystemMediaPair.objects.create(system=base_system, media='controller', wireless=False, abbreviated_name='Xbox-pad')

base_system = BaseSystem.objects.create(name='Xbox 360', brand=Company.objects.get(name='Microsoft'), generation=7, destination='H', upgrade_for=None, abbreviated_name='360')
SystemMediaPair.objects.create(system=base_system, media='DVD', wireless=False, abbreviated_name='360-disc')
SystemMediaPair.objects.create(system=base_system, media='controller', wireless=True, abbreviated_name='360-pad')
SystemMediaPair.objects.create(system=base_system, media='USB', wireless=False, abbreviated_name='360-USB')

base_system = BaseSystem.objects.create(name='Xbox One', brand=Company.objects.get(name='Microsoft'), generation=8, destination='H', upgrade_for=None, abbreviated_name='X1')
SystemMediaPair.objects.create(system=base_system, media='Blu-ray', wireless=False, abbreviated_name='X1-disc')
SystemMediaPair.objects.create(system=base_system, media='controller', wireless=True, abbreviated_name='X1-pad')
SystemMediaPair.objects.create(system=base_system, media='USB', wireless=False, abbreviated_name='X1-USB')

base_system = BaseSystem.objects.create(name='Atari 2600', brand=Company.objects.get(name='Atari'), generation=2, destination='H', upgrade_for=None, abbreviated_name='2600')
SystemMediaPair.objects.create(system=base_system, media='cartridge', wireless=False, abbreviated_name='2600-cart')
SystemMediaPair.objects.create(system=base_system, media='controller', wireless=False, abbreviated_name='2600-pad')

base_system = BaseSystem.objects.create(name='Personal Computer', brand=Company.objects.get(name='IBM'), generation=0, destination='H', upgrade_for=None, abbreviated_name='PC')
SystemMediaPair.objects.create(system=base_system, media='8" floppy', wireless=False, abbreviated_name='PC-fd8')
SystemMediaPair.objects.create(system=base_system, media='5"1/4 floppy', wireless=False, abbreviated_name='PC-fd5')
SystemMediaPair.objects.create(system=base_system, media='3"1/2 floppy', wireless=False, abbreviated_name='PC-fd3')
SystemMediaPair.objects.create(system=base_system, media='CD-rom', wireless=False, abbreviated_name='PC-CD')
SystemMediaPair.objects.create(system=base_system, media='DVD-rom', wireless=False, abbreviated_name='PC-DVD')
SystemMediaPair.objects.create(system=base_system, media='Blu-ray', wireless=False, abbreviated_name='PC-BD')
SystemMediaPair.objects.create(system=base_system, media='SD card', wireless=False, abbreviated_name='SD')
SystemMediaPair.objects.create(system=base_system, media='SDHC card', wireless=False, abbreviated_name='SDHC')
SystemMediaPair.objects.create(system=base_system, media='USB', wireless=False, abbreviated_name='PC-USB')

