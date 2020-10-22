#!/usr/bin/env python

import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Collecster.settings")
django.setup()

from advideogame.models import *
from advideogame.configuration import *

#import string

GENERIC_MARKER = 1

base_system_list = [
    ("Master System", "Sega", 3, "H", None, "SMS",
        [
            ("cartridge", False, "SMS-cart"),
            ("Sega card", False, "SMS-scard"),
            ("controller", False, "SMS-pad"),
        ],
        [
            ("% 1 console", {
                "provides": [1, 1, 2],
                "requires": [],
            }),
            ("% 2 console", {
                "provides": [1, 0, 2],
                "requires": [],
            }),
            ("% cartridge game", {
                "provides": [],
                "requires": [1, 0, 0],
            }),
            ("% Sega card game", {
                "provides": [],
                "requires": [0, 1, 0],
            }),
            ("% controller", {
                "provides": [],
                "requires": [0, 0, 1],
            }),
            ("% Sega card accessory", {
                "provides": [],
                "requires": [0, 1, 0],
            }),
        ],
    ),
    ("Game Gear", "Sega", 4, "H", None, "GG",
        [
            ("cartridge", False, "GG-cart"),
        ],
        [
            ("% console", {
                "provides": [1],
                "requires": [],
            }),
            ("% game", {
                "provides": [],
                "requires": [1],
            }),
        ],
    ),
    ("Mega Drive", "Sega", 4, "H", None, "MD",
        [
            ("cartridge", False, "MD-cart"),
            ("controller", False, "MD-pad"),
            ("expansion port", False, "MD-exp"),
        ],
        [
            ("% console", {
                "provides": [1, 2, 1],
                "requires": [],
            }),
            ("% game", {
                "provides": [],
                "requires": [1],
            }),
            ("% controller", {
                "provides": [],
                "requires": [0, 1, 0],
            }),
        ],
    ),
    ("Mega-CD", "Sega", 4, "H", "Mega Drive", "MCD",
        [
            ("CD-ROM", False, "MCD-disc"),
        ],
        [
            ("% console", {
                "provides": [1],
                "requires": ["MD-exp"],
            }),
            ("% game", {
                "provides": [],
                "requires": [1],
            }),
        ],
    ),
    ("32X", "Sega", 4, "H", "Mega Drive", "32X",
        [
            ("cartridge", False, "32X-cart"),
        ],
        [
            ("% console", {
                "provides": [1],
                "requires": ["MD-cart"],
            }),
            ("% game", {
                "provides": [],
                "requires": [1],
            }),
        ],
    ),
    ("Mega-CD 32X", "Sega", 4, "H", "Mega Drive", "MCD32X",
        [
            ("CD-ROM", False, "MCD32X-disc"),
        ],
        [
            ("% system", {
                "implicit_system": True,
                "provides": [1,],
                "requires": ["MCD-disc", "32X-cart", ],
            }),
            ("% game", {
                "requires": [1,],
            }),
        ],
    ),
    ("Saturn", "Sega", 5, "H", None, "Saturn",
        [
            ("CD-ROM", False, "Sat-disc"),
            ("controller", False, "Sat-pad"),
            ("cartridge slot", False, "Sat-cart"),
            ("internal expansion", False, "Sat-exp"),
        ],
        [
            ("% console", {
                "provides": [1, 2, 1, 1],
                "requires": [],
            }),
            ("% game", {
                "provides": [],
                "requires": [1],
            }),
            ("% controller", {
                "provides": [],
                "requires": [0, 1],
            }),
            ("% cartridge", {
                "provides": [],
                "requires": [0, 0, 1],
            }),
            ("% internal card", {
                "provides": [],
                "requires": [0, 0, 0, 1],
            }),
        ],
    ),
    ("Dreamcast", "Sega", 6, "H", None, "DC",
        [
            ("GD-ROM", False, "DC-disc"),
            ("controller", False, "DC-pad"),
            ("controller expansion slot", False, "DC-cslot"),
        ],
        [
            ("% console", {
                "provides": [1, 4],
                "requires": [],
            }),
            ("% game", {
                "provides": [],
                "requires": [1],
            }),
            ("% controller", {
                "provides": [0, 0, 2],
                "requires": [0, 1, 0],
            }),
            ("% controller accessory", {
                "provides": [0, 0, 0],
                "requires": [0, 0, 1],
            }),
        ],
    ),

    ("Nintendo Entertainment System", "Nintendo", 3, "H", None, "NES",
        [
            ("cartridge", False, "NES-cart"),
            ("controller", False, "NES-pad"),
        ],
        [
            ("% console", {
                "provides": [1, 2],
                "requires": [],
            }),
            ("% game", {
                "provides": [],
                "requires": [1],
            }),
            ("% controller", {
                "provides": [],
                "requires": [0, 1],
            }),
        ],
    ),
    ("Super Nintendo", "Nintendo", 4, "H", None, "SNES",
        [
            ("cartridge", False, "SNES-cart"),
            ("controller", False, "SNES-pad"),
        ],
        [
            ("% console", {
                "provides": [1, 2],
                "requires": [],
            }),
            ("% game", {
                "provides": [],
                "requires": [1],
            }),
            ("% controller", {
                "provides": [],
                "requires": [0, 1],
            }),
        ],
    ),
    ("Virtual Boy", "Nintendo", 5, "H", None, "Vboy",
        [
            ("cartridge", False, "Vboy-cart"),
            ("controller", False, "Vboy-pad"),
        ],
        [],
    ),
    ("Nintendo 64", "Nintendo", 5, "H", None, "N64",
        [
            ("cartridge", False, "N64-cart"),
            ("controller", False, "N64-pad"),
            ("memory expansion", False, "N64-mem"),
            ("controller expansion slot", False, "N64-cslot"),
        ],
        [
            ("% console", {
                "provides": [1, 4, 1],
                "requires": [],
            }),
            ("% game", {
                "provides": [],
                "requires": [1],
            }),
            ("% controller", {
                "provides": [0, 0, 0, 1],
                "requires": [0, 1, 0],
            }),
            ("% expansion accessory", {
                "provides": [],
                "requires": [0, 0, 1, 0],
            }),
            ("% controller accessory", {
                "provides": [],
                "requires": [0, 0, 0, 1],
            }),
        ],
    ),
    ("GameCube", "Nintendo", 6, "H", None, "GC",
        [
            ("miniDVD", False, "GC-disc"),
            ("controller", False, "GC-pad"),
            ("memory card", False, "GC-mcard"),
        ],
        [
            ("% console", {
                "provides": [1, 4, 2],
                "requires": [],
            }),
            ("% game", {
                "provides": [],
                "requires": [1],
            }),
            ("% controller", {
                "provides": [],
                "requires": [0, 1, 0],
            }),
            ("% storage accessory", {
                "provides": [],
                "requires": [0, 0, 1],
            }),
        ],
    ),
    ("Wii", "Nintendo", 7, "H", None, "Wii",
        [
            ("Wii disc", False, "Wii-disc"),
            ("controller", True, "Wii-pad"),
            ("USB", False, "Wii-USB"),
            ("controller expansion port", False, "Wii-cport"),
        ],
        [
            ("% console (GC)", {
                "provides": [1, 0, 2, "SDHC",],
                "requires": [],
                GENERIC_MARKER: {
                    "provides": [0, 4, ("GC-pad", 4), ],
                },
                "GameCube": {
                    "provides": [("GC-disc", 1, "Wii-disc"), ("GC-mcard", 2),],
                },
            }),
            ("% game", {
                "provides": [],
                "requires": [1],
            }),
            ("wiimote controller", {
                "provides": [0, 0, 0, 1],
                "requires": [0, 1],
            }),
            ("wiimote expansion", {
                "provides": [],
                "requires": [0, 0, 0, 1],
            }),
            ("wiimote shell accessory", {
                "provides": [],
                "requires": [],
            }),
        ],
    ),
    ("Wii U", "Nintendo", 8, "H", None, "WiiU",
        [
            ("Wii U disc", False, "WiiU-disc"),
            ("GamePad (screen)", True, "WiiU-pad"),
            ("USB", True, "WiiU-USB"),
        ],
        [
            ("% console", {
                "provides": [1, 1, 4, "SDHC",],
                "requires": [],
                GENERIC_MARKER: {
                    "provides": [("Wii-pad", 4),],
                },
                "Wii": {
                    "provides": [("Wii-disc", 1, "WiiU-disc"),],
                },
            }),
            ("% game", {
                "provides": [],
                "requires": [1],
            }),
            ("% GamePad", {
                "provides": [],
                "requires": [0, 1, 0],
            }),
        ],
    ),

    ("PlayStation", "Sony", 5, "H", None, "PS1",
        [
            ("CD-ROM", False, "PS1-disc"),
            ("controller", False, "PS1-pad"),
            ("memory card", False, "PS1-mcard"),
        ],
        [
            ("% console", {
                "provides": [1, 2, 2],
                "requires": [],
            }),
            ("% game", {
                "provides": [],
                "requires": [1],
            }),
            ("% controller", {
                "provides": [],
                "requires": [0, 1, 0],
            }),
            ("% memory card", {
                "provides": [],
                "requires": [0, 0, 1],
            }),
            ("% mutitap", {
                "provides": [0, 4, 4],
                "requires": [0, 1,],
            }),
        ],
    ),
    ("PlayStation 2", "Sony", 6, "H", None, "PS2",
        [
            ("DVD-ROM", False, "PS2-disc"),
            ("controller", False, "PS2-pad"),
            ("memory card", False, "PS2-mcard"),
            ("USB", False, "PS2-USB"),
        ],
        [
            ("% console", {
                "provides": [1, 0, 0, 2, "PS1-disc", ],
                "requires": [],
                GENERIC_MARKER: {
                    "provides": [0, 2, 2],
                },
                "PlayStation": {
                    "provides": [("PS1-disc", 1, "PS2-disc"),]
                },
            }),
            ("% game", {
                "provides": [],
                "requires": [1],
            }),
            ("% controller", {
                "provides": [],
                "requires": [0, 1, 0],
            }),
            ("% memory card", {
                "provides": [],
                "requires": [0, 0, 1],
            }),
            ("% USB accessory", {
                "provides": [],
                "requires": [0, 0, 0, 1],
            }),
        ],
    ),
    ("PlayStation 3", "Sony", 7, "H", None, "PS3",
        [
            ("Blu-ray", False, "PS3-disc"),
            ("controller", True, "PS3-pad"),
            ("USB", False, "PS3-USB"),
        ],
        [
            ("% console (PS2 PS1)", {
                "provides": [1, 0, 4,],
                "requires": [],
                GENERIC_MARKER: {
                    "provides": [0, 4, 0],
                },
                "PlayStation 2": {
                    "provides": [("PS2-disc", 1, "PS3-disc"),]
                },
                "PlayStation": {
                    "provides": [("PS1-disc", 1, "PS3-disc"),]
                },
            }),
            ("% console (PS1)", {
                "provides": [1, 0, 4,],
                "requires": [],
                GENERIC_MARKER: {
                    "provides": [0, 4, 0],
                },
                "PlayStation": {
                    "provides": [("PS1-disc", 1, "PS3-disc"),]
                },
            }),
            ("% game", {
                "provides": [],
                "requires": [1],
            }),
            ("% controller", {
                "provides": [],
                "requires": [0, 1, 0],
            }),
            ("% USB accessory", {
                "provides": [],
                "requires": [0, 0, 1],
            }),
        ],
    ),
    ("PlayStation 4", "Sony", 8, "H", None, "PS4",
        [
            ("Blu-ray", False, "PS4-disc"),
            ("controller", True, "PS4-pad"),
            ("USB", False, "PS4-USB"),
        ],
        [
            ("% console", {
                "provides": [1, 4, 2],
                "requires": [],
            }),
            ("% game", {
                "provides": [],
                "requires": [1],
            }),
            ("% controller", {
                "provides": [],
                "requires": [0, 1, 0],
            }),
        ],
    ),

    ("Xbox", "Microsoft", 6, "H", None, "Xbox",
        [
            ("DVD", False, "Xbox-disc"),
            ("controller", False, "Xbox-pad"),
        ],
        [
            ("% console", {
                "provides": [1, 4],
                "requires": [],
            }),
            ("% game", {
                "provides": [],
                "requires": [1],
            }),
            ("% controller", {
                "provides": [],
                "requires": [0, 1],
            }),
        ],
    ),
    ("Xbox 360", "Microsoft", 7, "H", None, "360",
        [
            ("DVD", False, "360-disc"),
            ("controller", True, "360-pad"),
            ("USB", False, "360-USB"),
        ],
        [
            ("% console (original)", {
                "provides": [1, 4, 3],
                "requires": [],
            }),
            ("% console (revision S)", {
                "provides": [1, 4, 5],
                "requires": [],
            }),
            ("% console (revision E)", {
                "provides": [1, 4, 4],
                "requires": [],
            }),
            ("% game", {
                "provides": [],
                "requires": [1],
            }),
            ("% controller", {
                "provides": [],
                "requires": [0, 1],
            }),
        ],
    ),
    ("Xbox One", "Microsoft", 8, "H", None, "X1",
        [
            ("Blu-ray", False, "X1-disc"),
            ("controller", True, "X1-pad"),
            ("USB", False, "X1-USB"),
        ],
        [
            ("% console", {
                "provides": [1, 4, 3],
                "requires": [],
            }),
            ("% game", {
                "provides": [],
                "requires": [1],
            }),
            ("% controller", {
                "provides": [],
                "requires": [0, 1],
            }),
        ],
    ),

    ("Atari 2600", "Atari", 2, "H", None, "2600",
        [
            ("cartridge", False, "2600-cart"),
            ("controller", False, "2600-pad"),
        ],
        [
            ("% console", {
                "provides": [1, 2],
                "requires": [],
            }),
            ("% game", {
                "provides": [],
                "requires": [1],
            }),
            ("% controller", {
                "provides": [],
                "requires": [0, 1],
            }),
        ]
    ),

    ("Personal Computer", "IBM", 0, "H", None, "PC",
        [
            ("8\" floppy", False, "PC-fd8"),
            ("5\"1/4 floppy", False, "PC-fd5"),
            ("3\"1/2 floppy", False, "PC-fd3"),
            ("CD-rom", False, "PC-CD"),
            ("DVD-rom", False, "PC-DVD"),
            ("Blu-ray", False, "PC-BD"),
            ("SD card", False, "SD"),
            ("SDHC card", False, "SDHC"),
            ("USB", False, "PC-USB"),
        ],
        [
            ("PC system", {
                "provides": [1, 1, 1, 1, 1, 1, 1, 1, 1, ],
            }),
            ("PC 5\"1/4 floppy", {
                "requires": [0, 1],
            }),
            ("PC 3\"1/2 floppy", {
                "requires": [0, 0, 1],
            }),
            ("PC-CD", {
                "requires": [0, 0, 0, 1],
            }),
            ("PC-DVD", {
                "requires": [0, 0, 0, 0, 1],
            }),
            ("PC-BD", {
                "requires": [0, 0, 0, 0, 0, 1],
            }),
        ],
    ),
]

def make_ispec_name(ispec_name, system_name):
    return ispec_name.replace("%", system_name)

def output_interface_spec(f, interface_detail_dict, bs, key, model_classname):
    if not key in interface_detail_dict:
        return
    for index, system_media in enumerate(interface_detail_dict[key]):
        reused_interface = None
        if isinstance(system_media, int):
            cardin = system_media
            abbr_name = bs[6][index][2]
        else:
            if isinstance(system_media, str):
                cardin = 1
                abbr_name = system_media
            else:
                cardin = system_media[1]
                abbr_name = system_media[0]
                if len(system_media) > 2:
                    reused_interface = system_media[2]
        if cardin is not 0:
            f.write(("{mdl}.objects.create(interface_detail_base=interface_detail, interface=get_sysmediapair({interface}), "
                                           "cardinality={cardin}{reused})\n")
                        .format(mdl=model_classname, interface=repr(abbr_name), cardin=cardin,
                                reused=", reused_interface=get_sysmediapair('{}')".format(reused_interface) if reused_interface else ""))

with open("import_interface_spec.py", "w") as f, open("import_base_system.py", "w") as f_sys:
    preamble = ("""#!/usr/bin/env python

import os, django
os.environ.setdefault(\"DJANGO_SETTINGS_MODULE\", \"Collecster.settings\")
django.setup()

from advideogame.models import *
from advideogame.configuration import *
from supervisor.models import *

def get_bs(name):
    return BaseSystem.objects.get(name=name)

def get_sysmediapair(abbreviated_name):
    return SystemMediaPair.objects.get(abbreviated_name=abbreviated_name)

""")

    f_sys.write(preamble)
    f.write(preamble)

    for bs in base_system_list:
        #
        # BaseSystem and SystemMediaPair
        #
        f_sys.write(("base_system = BaseSystem.objects.create(name={}, brand=Company.objects.get(name={}), generation={}"
                                                             ", destination={}, upgrade_for={}, abbreviated_name={})\n")
                        .format(repr(bs[0]), repr(bs[1]), bs[2], repr(bs[3]), "get_bs({})".format(repr(bs[4])) if bs[4] else None, repr(bs[5])))
        for smp in bs[6]:
            f_sys.write("SystemMediaPair.objects.create(system=base_system, media={}, wireless={}, abbreviated_name={})\n"
                            .format(repr(smp[0]), smp[1], repr(smp[2])))
        f_sys.write("\n")

        #
        # InterfaceSpecification
        #
        for interface_spec in bs[7]:
            f.write("\t#{}\n".format(make_ispec_name(interface_spec[0], bs[0]))) 

            interface_specification_dict = interface_spec[1]

            f.write("interface_spec = InterfacesSpecification.objects.create(internal_name={name}, implicit_system={impl})\n"
                        .format(name=repr(make_ispec_name(interface_spec[0], bs[0])),
                                impl=interface_specification_dict.get("implicit_system", False)))

            def write_interface_detail(advertised_system, interface_detail_dict, common_interface=False):
                if common_interface:
                    f.write("interface_detail = CommonInterfaceDetail.objects.create(interfaces_specification=interface_spec)\n"
                                .format())
                else:
                    f.write("base = BaseSystem.objects.get(name={})\n".format(repr(advertised_system)))
                    f.write("interface_detail = SystemInterfaceDetail.objects.create(interfaces_specification=interface_spec, advertised_system=base)\n"
                                .format())
                output_interface_spec(f, interface_detail_dict, bs, "provides", "ProvidedInterface")
                output_interface_spec(f, interface_detail_dict, bs, "requires", "RequiredInterface")

            if GENERIC_MARKER in interface_specification_dict:
                write_interface_detail(None, interface_specification_dict[GENERIC_MARKER], True)
            if any(kw in interface_specification_dict for kw in ("provides", "requires")):
                write_interface_detail(bs[0], interface_specification_dict, False)
            for sys_name in [sys_name for sys_name in interface_specification_dict if sys_name not in ("implicit_system", "provides", "requires", GENERIC_MARKER)]:
                write_interface_detail(sys_name, interface_specification_dict[sys_name], False)

            f.write("\n")
