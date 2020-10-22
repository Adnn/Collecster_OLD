#!/usr/bin/env python

import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Collecster.settings")
django.setup()

from advideogame.models import *
from advideogame.configuration import *
from supervisor.models import *

def get_userextension(user_name):
    return UserExtension.objects.get(user__username=user_name)

def get_company(name):
    return Company.objects.get(name=name)

concept = Concept.objects.create(created_by=get_userextension("ad"), developer=get_company("id Software"), **{'distinctive_name': u'DOOM', 'primary_nature': u'GAME'})
url = ConceptUrl.objects.create(concept=concept, url="https://en.wikipedia.org/wiki/Doom_(1993_video_game)")

concept = Concept.objects.create(created_by=get_userextension("ad"), developer=get_company("id Software"), **{'distinctive_name': u'Thy Flesh Consumed', 'primary_nature': u'ADD_ON'})
url = ConceptUrl.objects.create(concept=concept, url="http://doomwiki.org/wiki/Thy_Flesh_Consumed")
relation = ConceptRelation.objects.create(concept=concept, relation="MAO", related_concept=Concept.objects.get(distinctive_name="DOOM"))

concept = Concept.objects.create(created_by=get_userextension("ad"), developer=get_company("Sonic Team"), **{'distinctive_name': u'Nights into Dreams', 'common_name': u'Nights', 'primary_nature': u'GAME'})

concept = Concept.objects.create(created_by=get_userextension("ad"), developer=get_company("Bandai"), **{'distinctive_name': u'Dragon Ball Z: Shin But\u014dden', 'common_name': u'DBZ Shin But\u014dden', 'primary_nature': u'GAME'})

concept = Concept.objects.create(created_by=get_userextension("ad"), developer=get_company("Sega-AM2"), **{'distinctive_name': u'Virtua Fighter 2', 'primary_nature': u'GAME'})

concept = Concept.objects.create(created_by=get_userextension("ad"), developer=get_company("Realtime Associates"), **{'distinctive_name': u'Bug!', 'primary_nature': u'GAME'})

concept = Concept.objects.create(created_by=get_userextension("ad"), developer=get_company("Realtime Associates"), **{'distinctive_name': u'Bug Too!', 'primary_nature': u'GAME'})

concept = Concept.objects.create(created_by=get_userextension("ad"), developer=get_company("Altron"), **{'distinctive_name': u'Mighty Hits', 'primary_nature': u'GAME'})

concept = Concept.objects.create(created_by=get_userextension("ad"), developer=get_company("New Horizon studios"), **{'distinctive_name': u'NightStone', 'primary_nature': u'GAME'})

concept = Concept.objects.create(created_by=get_userextension("ad"), developer=get_company("SCE London Studio"), **{'distinctive_name': u'Singstar Microphone', 'primary_nature': u'MICROPHONE'})
specific = ConceptSpecific.Remote.objects.create(concept=concept, **{'battery_type': None})
specific = ConceptSpecific.RemoteAccessory.objects.create(concept=concept, **{'wireless': False})

concept = Concept.objects.create(created_by=get_userextension("ad"), developer=get_company("Harmonix"), **{'distinctive_name': u'The Beatles: Rock Band', 'primary_nature': u'GAME'})

concept = Concept.objects.create(created_by=get_userextension("ad"), developer=get_company("Relentless Software"), **{'distinctive_name': u'Buzz!: Brain of...', 'primary_nature': u'GAME'})

concept = Concept.objects.create(created_by=get_userextension("ad"), developer=get_company("Relentless Software"), **{'distinctive_name': u'Buzz!: The Hollywood Quiz', 'primary_nature': u'GAME'})

concept = Concept.objects.create(created_by=get_userextension("ad"), developer=get_company("Relentless Software"), **{'distinctive_name': u'Buzz!: The Pop Quiz', 'primary_nature': u'GAME'})

concept = Concept.objects.create(created_by=get_userextension("ad"), **{'distinctive_name': u'Buzz! Buzzer', 'primary_nature': u'BUZZER'})
specific = ConceptSpecific.Remote.objects.create(concept=concept, **{'battery_type': None})
specific = ConceptSpecific.RemoteAccessory.objects.create(concept=concept, **{'wireless': False})

concept = Concept.objects.create(created_by=get_userextension("ad"), developer=get_company("Sega-AM2"), **{'distinctive_name': u'Virtua Cop 2', 'primary_nature': u'GAME'})

concept = Concept.objects.create(created_by=get_userextension("ad"), developer=get_company("Sega-AM2"), **{'distinctive_name': u'The House of the Dead', 'primary_nature': u'GAME'})

concept = Concept.objects.create(created_by=get_userextension("ad"), developer=get_company("Tose Software"), **{'distinctive_name': u'Dragon Ball Z: The Legend', 'common_name': u'DBZ: Legends ', 'primary_nature': u'GAME'})

concept = Concept.objects.create(created_by=get_userextension("ad"), developer=get_company("Sega-AM1"), **{'distinctive_name': u'Die Hard Arcade', 'primary_nature': u'GAME'})

concept = Concept.objects.create(created_by=get_userextension("ad"), developer=get_company("Sega"), **{'distinctive_name': u'Virtua Gun', 'primary_nature': u'GUN'})
specific = ConceptSpecific.Remote.objects.create(concept=concept, **{'battery_type': None})
specific = ConceptSpecific.RemoteAccessory.objects.create(concept=concept, **{'wireless': False})
specific = ConceptSpecific.Shell.objects.create(concept=concept, **{'is_shell': False})
specific = ConceptSpecific.Controller.objects.create(concept=concept, **{'rumble_feedback': False, 'autofire': False, 'slow': False, 'force_feedback': False})

concept = Concept.objects.create(created_by=get_userextension("ad"), developer=get_company("Sega-AM2"), **{'distinctive_name': u'Virtua Cop', 'primary_nature': u'GAME'})

concept = Concept.objects.create(created_by=get_userextension("ad"), developer=get_company("Team17"), **{'distinctive_name': u'Worms', 'primary_nature': u'GAME'})

concept = Concept.objects.create(created_by=get_userextension("ad"), developer=get_company("Sega-AM5"), **{'distinctive_name': u'Sega Rally Championship', 'common_name': u'Sega Rally', 'primary_nature': u'GAME'})

concept = Concept.objects.create(created_by=get_userextension("ad"), developer=get_company("Sega-AM2"), **{'distinctive_name': u'Daytona USA', 'primary_nature': u'GAME'})

concept = Concept.objects.create(created_by=get_userextension("ad"), developer=get_company("Capcom"), **{'distinctive_name': u'Marvel Super Heroes', 'primary_nature': u'GAME'})

concept = Concept.objects.create(created_by=get_userextension("ad"), developer=get_company("Sega-AM3"), **{'distinctive_name': u'Sega Touring Car Championship', 'common_name': u'Sega Touring Car', 'primary_nature': u'GAME'})

concept = Concept.objects.create(created_by=get_userextension("ad"), developer=get_company("Manic Media"), **{'distinctive_name': u'Formula Karts Special Edition', 'primary_nature': u'GAME'})

concept = Concept.objects.create(created_by=get_userextension("ad"), developer=get_company("Sonic Team"), **{'distinctive_name': u'Sonic Jam', 'primary_nature': u'GAME'})

concept = Concept.objects.create(created_by=get_userextension("ad"), developer=get_company("3D Realms"), **{'distinctive_name': u'Duke Nukem 3D', 'primary_nature': u'GAME'})

concept = Concept.objects.create(created_by=get_userextension("ad"), developer=get_company("Cave"), **{'distinctive_name': u'DoDonPachi', 'primary_nature': u'GAME'})

concept = Concept.objects.create(created_by=get_userextension("ad"), developer=get_company("Capcom"), **{'distinctive_name': u'Resident Evil', 'primary_nature': u'GAME'})

concept = Concept.objects.create(created_by=get_userextension("ad"), developer=get_company("Sega"), **{'distinctive_name': u'Sega Saturn Control Pad', 'common_name': u'Pad Saturn official', 'primary_nature': u'PAD'})
url = ConceptUrl.objects.create(concept=concept, url="https://segaretro.org/Control_Pad_(Saturn)")
specific = ConceptSpecific.Remote.objects.create(concept=concept, **{'battery_type': None})
specific = ConceptSpecific.RemoteAccessory.objects.create(concept=concept, **{'wireless': False})
specific = ConceptSpecific.Shell.objects.create(concept=concept, **{'is_shell': False})
specific = ConceptSpecific.Controller.objects.create(concept=concept, **{'rumble_feedback': False, 'autofire': False, 'slow': False, 'force_feedback': False})
specific = ConceptSpecific.DirectionalController.objects.create(concept=concept)
specific.direction_input_type.add(1)

concept = Concept.objects.create(created_by=get_userextension("ad"), **{'distinctive_name': u'Pad Saturn ST.2', 'primary_nature': u'PAD'})
specific = ConceptSpecific.Remote.objects.create(concept=concept, **{'battery_type': None})
specific = ConceptSpecific.RemoteAccessory.objects.create(concept=concept, **{'wireless': False})
specific = ConceptSpecific.Shell.objects.create(concept=concept, **{'is_shell': False})
specific = ConceptSpecific.Controller.objects.create(concept=concept, **{'rumble_feedback': False, 'autofire': False, 'slow': False, 'force_feedback': False})
specific = ConceptSpecific.DirectionalController.objects.create(concept=concept)
specific.direction_input_type.add(1)

concept = Concept.objects.create(created_by=get_userextension("ad"), developer=get_company("Sega"), **{'distinctive_name': u'3D Control Pad (Saturn)', 'primary_nature': 'PAD'})
url = ConceptUrl.objects.create(concept=concept, url="https://segaretro.org/3D_Control_Pad")
specific = ConceptSpecific.Remote.objects.create(concept=concept, **{'battery_type': None})
specific = ConceptSpecific.RemoteAccessory.objects.create(concept=concept, **{'wireless': False})
specific = ConceptSpecific.Shell.objects.create(concept=concept, **{'is_shell': False})
specific = ConceptSpecific.Controller.objects.create(concept=concept, **{'rumble_feedback': False, 'autofire': False, 'slow': False, 'force_feedback': False})
specific = ConceptSpecific.DirectionalController.objects.create(concept=concept)
specific.direction_input_type.add(1, 2)

concept = Concept.objects.create(created_by=get_userextension("ad"), developer=get_company("Sega"), **{'distinctive_name': u'Sega Saturn', 'common_name': u'Saturn', 'primary_nature': u'CONSOLE'})

concept = Concept.objects.create(created_by=get_userextension("ad"), developer=get_company("Sega"), **{'distinctive_name': u'Sega Saturn Bootleg Sampler', 'common_name': u'Bootleg Sampler', 'primary_nature': u'DEMO'})

concept = Concept.objects.create(created_by=get_userextension("ad"), developer=get_company("Sega"), **{'distinctive_name': u'Clockwork Knight 2', 'primary_nature': u'GAME'})

concept = Concept.objects.create(created_by=get_userextension("ad"), developer=get_company("Sega"), **{'distinctive_name': u'World Series Baseball', 'primary_nature': u'GAME'})

concept = Concept.objects.create(created_by=get_userextension("ad"), developer=get_company("Smilebit"), **{'distinctive_name': u'Jet Set Radio', 'primary_nature': u'GAME'})

concept = Concept.objects.create(created_by=get_userextension("ad"), developer=get_company("Wow Entertainment"), **{'distinctive_name': u'Sega Bass Fishing', 'primary_nature': u'GAME'})

concept = Concept.objects.create(created_by=get_userextension("ad"), developer=get_company("Hitmaker"), **{'distinctive_name': u'Crazy Taxi', 'primary_nature': u'GAME'})

concept = Concept.objects.create(created_by=get_userextension("ad"), developer=get_company("Hitmaker"), **{'distinctive_name': u'Confidential Mission', 'primary_nature': u'GAME'})

concept = Concept.objects.create(created_by=get_userextension("ad"), developer=get_company("Overworks"), **{'distinctive_name': u'Skies of Arcadia', 'primary_nature': u'GAME'})

concept = Concept.objects.create(created_by=get_userextension("ad"), developer=get_company("Capcom"), **{'distinctive_name': u'Capcom vs. SNK: Millennium Fight 2000', 'primary_nature': u'GAME'})

concept = Concept.objects.create(created_by=get_userextension("ad"), developer=get_company("EA Canada"), **{'distinctive_name': u'FIFA 98', 'primary_nature': u'GAME'})

concept = Concept.objects.create(created_by=get_userextension("ad"), developer=get_company("Sega"), **{'distinctive_name': u'Dreamcast Vibration Pack', 'primary_nature': 'RUMBLE_PACK'})
url = ConceptUrl.objects.create(concept=concept, url="https://segaretro.org/Jump_Pack")

concept = Concept.objects.create(created_by=get_userextension("ad"), developer=get_company("Sega"), **{'distinctive_name': u'Dreamkey', 'primary_nature': u'WEB_BROWSER'})

concept = Concept.objects.create(created_by=get_userextension("ad"), developer=get_company("Sega"), **{'distinctive_name': u'Visual Memory Unit', 'common_name': u'VMU', 'primary_nature': u'MEMORYCARD'})
url = ConceptUrl.objects.create(concept=concept, url="https://en.wikipedia.org/wiki/VMU")
url = ConceptUrl.objects.create(concept=concept, url="https://segaretro.org/Visual_Memory_Unit")
add_nature = ConceptNature.objects.create(concept=concept, nature="SCREEN_INDIV")
specific = ConceptSpecific.Remote.objects.create(concept=concept, **{'battery_type': BatteryType.objects.get(code="CR2032")})
specific = ConceptSpecific.RemoteAccessory.objects.create(concept=concept, **{'wireless': False})
add_nature = ConceptNature.objects.create(concept=concept, nature="HANDHELD_CONSOLE")
specific = ConceptSpecific.Controller.objects.create(concept=concept, **{'rumble_feedback': False, 'autofire': False, 'slow': False, 'force_feedback': False})
specific = ConceptSpecific.DirectionalController.objects.create(concept=concept)
specific.direction_input_type.add(1)

concept = Concept.objects.create(created_by=get_userextension("ad"), developer=get_company("Sega"), **{'distinctive_name': "Dreamcast Controller", "common_name":u'Pad Dreamcast official', 'primary_nature': 'PAD'})
url = ConceptUrl.objects.create(concept=concept, url="https://segaretro.org/Dreamcast_Controller")
specific = ConceptSpecific.Remote.objects.create(concept=concept, **{'battery_type': None})
specific = ConceptSpecific.RemoteAccessory.objects.create(concept=concept, **{'wireless': False})
specific = ConceptSpecific.Shell.objects.create(concept=concept, **{'is_shell': False})
specific = ConceptSpecific.Controller.objects.create(concept=concept, **{'rumble_feedback': False, 'autofire': False, 'slow': False, 'force_feedback': False})
specific = ConceptSpecific.DirectionalController.objects.create(concept=concept)
specific.direction_input_type.add(1, 2)

concept = Concept.objects.create(created_by=get_userextension("ad"), developer=get_company("Sega"), **{'distinctive_name': u'Sega Dreamcast', 'common_name': u'Dreamcast', 'primary_nature': u'CONSOLE'})

concept = Concept.objects.create(created_by=get_userextension("ad"), developer=get_company("InterAct"), **{'distinctive_name': u'Quantum Fighterpad', 'common_name': u'Pad Dreamcast InterAct', 'primary_nature': 'PAD'})
specific = ConceptSpecific.Remote.objects.create(concept=concept, **{'battery_type': None})
specific = ConceptSpecific.RemoteAccessory.objects.create(concept=concept, **{'wireless': False})
specific = ConceptSpecific.Shell.objects.create(concept=concept, **{'is_shell': False})
specific = ConceptSpecific.Controller.objects.create(concept=concept, **{'rumble_feedback': False, 'autofire': False, 'slow': False, 'force_feedback': False})
specific = ConceptSpecific.DirectionalController.objects.create(concept=concept)
specific.direction_input_type.add(1, 2)

concept = Concept.objects.create(created_by=get_userextension("ad"), developer=get_company("Sega"), **{'distinctive_name': u'Dream On Collection', 'primary_nature': u'DEMO'})

concept = Concept.objects.create(created_by=get_userextension("ad"), developer=get_company("Westwood Studios"), **{'distinctive_name': u'The Lion King', 'primary_nature': u'GAME'})

concept = Concept.objects.create(created_by=get_userextension("ad"), developer=get_company("Aspect Co."), **{'distinctive_name': u'Sonic the Hedgehog 2 (8-bit)', 'common_name': u'Sonic 2', 'primary_nature': u'GAME'})
url = ConceptUrl.objects.create(concept=concept, url="https://en.wikipedia.org/wiki/Sonic_the_Hedgehog_2_(8-bit_video_game)")

concept = Concept.objects.create(created_by=get_userextension("ad"), developer=get_company("SIMS"), **{'distinctive_name': u"Disney's Aladdin (SIMS)", 'common_name': u'Aladdin', 'primary_nature': u'GAME'})
url = ConceptUrl.objects.create(concept=concept, url="https://en.wikipedia.org/wiki/Disney%27s_Aladdin_(1994_video_game)")

concept = Concept.objects.create(created_by=get_userextension("ad"), developer=get_company("Sega"), **{'distinctive_name': u'Sega Game Pack 4 in 1', 'primary_nature': u'GAME'})

concept = Concept.objects.create(created_by=get_userextension("ad"), developer=get_company("Taito"), **{'distinctive_name': u'Operation Wolf', 'primary_nature': u'GAME'})

concept = Concept.objects.create(created_by=get_userextension("ad"), developer=get_company("Sega"), **{'distinctive_name': u'The Sega Light Phaser', 'common_name': u'Light Phaser', 'primary_nature': u'GUN'})
url = ConceptUrl.objects.create(concept=concept, url="https://segaretro.org/Light_Phaser")
specific = ConceptSpecific.Remote.objects.create(concept=concept, **{'battery_type': None})
specific = ConceptSpecific.RemoteAccessory.objects.create(concept=concept, **{'wireless': False})
specific = ConceptSpecific.Shell.objects.create(concept=concept, **{'is_shell': False})
specific = ConceptSpecific.Controller.objects.create(concept=concept, **{'rumble_feedback': False, 'autofire': False, 'slow': False, 'force_feedback': False})

concept = Concept.objects.create(created_by=get_userextension("ad"), developer=get_company("Sega"), **{'distinctive_name': u'Alex Kidd in Miracle World', 'common_name': u'Alex Kidd', 'primary_nature': u'GAME'})

concept = Concept.objects.create(created_by=get_userextension("ad"), developer=get_company("Sega"), **{'distinctive_name': u'Sega Master System', 'common_name': u'Master System', 'primary_nature': u'CONSOLE'})
url = ConceptUrl.objects.create(concept=concept, url="https://en.wikipedia.org/wiki/Master_System")

concept = Concept.objects.create(created_by=get_userextension("ad"), developer=get_company("Sega"), **{'distinctive_name': "Master System Control Pad", "common_name": u'Pad Master System official', 'primary_nature': u'PAD'})
url = ConceptUrl.objects.create(concept=concept, url="http://segaretro.org/Control_Pad_(Master_System)")
specific = ConceptSpecific.Remote.objects.create(concept=concept, **{'battery_type': None})
specific = ConceptSpecific.RemoteAccessory.objects.create(concept=concept, **{'wireless': False})
specific = ConceptSpecific.Shell.objects.create(concept=concept, **{'is_shell': False})
specific = ConceptSpecific.Controller.objects.create(concept=concept, **{'rumble_feedback': False, 'autofire': False, 'slow': False, 'force_feedback': False})
specific = ConceptSpecific.DirectionalController.objects.create(concept=concept)
specific.direction_input_type.add(1)

concept = Concept.objects.create(created_by=get_userextension("ad"), developer=get_company("Mad Catz"), **{'distinctive_name': u'Steering wheel Saturn Mad Catz', 'primary_nature': u'STEERINGWHEEL'})
specific = ConceptSpecific.Remote.objects.create(concept=concept, **{'battery_type': None})
specific = ConceptSpecific.RemoteAccessory.objects.create(concept=concept, **{'wireless': False})
specific = ConceptSpecific.Shell.objects.create(concept=concept, **{'is_shell': False})
specific = ConceptSpecific.Controller.objects.create(concept=concept, **{'rumble_feedback': False, 'autofire': False, 'slow': False, 'force_feedback': False})

concept = Concept.objects.create(created_by=get_userextension("ad"), developer=get_company("2K"), **{'distinctive_name': u'BioShock 2', 'primary_nature': u'GAME'})

concept = Concept.objects.create(created_by=get_userextension("ad"), developer=get_company("Valve"), **{'distinctive_name': u'Half-Life', 'primary_nature': u'GAME'})

concept = Concept.objects.create(created_by=get_userextension("ad"), developer=get_company("Gearbox Software"), **{'distinctive_name': u'Half-Life: Opposing Force', 'common_name': u'Opposing Force', 'primary_nature': u'ADD_ON'})
relation = ConceptRelation.objects.create(concept=concept, relation="MAO", related_concept=Concept.objects.get(distinctive_name="Half-Life"))

concept = Concept.objects.create(created_by=get_userextension("ad"), developer=get_company("Namco"), **{'distinctive_name': u'Pole Position', 'primary_nature': u'GAME'})

concept = Concept.objects.create(created_by=get_userextension("ad"), developer=get_company("Atari"), **{'distinctive_name': u'Centipede', 'primary_nature': u'GAME'})

concept = Concept.objects.create(created_by=get_userextension("ad"), developer=get_company("Rage Software"), **{'distinctive_name': u'Millennium Soldier: Expendable', 'common_name': u'Expendable', 'primary_nature': u'GAME'})

concept = Concept.objects.create(created_by=get_userextension("ad"), developer=get_company("EMS"), **{'distinctive_name': u'Action Replay Plus 4M (Saturn EMS)', 'primary_nature': u'CHEAT_DEV'})
add_nature = ConceptNature.objects.create(concept=concept, nature="MEMORYCARD")
add_nature = ConceptNature.objects.create(concept=concept, nature="RAM_PACK")
add_nature = ConceptNature.objects.create(concept=concept, nature="REGION_UNLOCK")

concept = Concept.objects.create(created_by=get_userextension("ad"), developer=get_company("Iron Lore Entertainment"), **{'distinctive_name': u'Titan Quest', 'primary_nature': u'GAME'})

concept = Concept.objects.create(created_by=get_userextension("ad"), developer=get_company("Blizzard"), **{'distinctive_name': u'Diablo II', 'primary_nature': u'GAME'})

concept = Concept.objects.create(created_by=get_userextension("ad"), developer=get_company("id Software"), **{'distinctive_name': u'Wolfenstein 3D', 'primary_nature': u'GAME'})

concept = Concept.objects.create(created_by=get_userextension("ad"), developer=get_company("id Software"), **{'distinctive_name': u'Final Doom', 'primary_nature': u'GAME'})

concept = Concept.objects.create(created_by=get_userextension("ad"), developer=get_company("Blizzard"), **{'distinctive_name': u'Warcraft II: Tides of Darkness', 'common_name': u'Warcraft II', 'primary_nature': u'GAME'})

concept = Concept.objects.create(created_by=get_userextension("ad"), developer=get_company("Cyberlore Studios"), **{'distinctive_name': u'Warcraft II: Beyond the Dark Portal', 'primary_nature': u'ADD_ON'})

concept = Concept.objects.create(created_by=get_userextension("ad"), developer=get_company("Stainless Games"), **{'distinctive_name': u'Carmageddon II: Carpocalypse Now', 'common_name': u'Carmageddon II', 'primary_nature': u'GAME'})

concept = Concept.objects.create(created_by=get_userextension("ad"), developer=get_company("Sierra Entertainment"), **{'distinctive_name': u"Torin's Passage", 'primary_nature': u'GAME'})

concept = Concept.objects.create(created_by=get_userextension("ad"), developer=get_company("Lucasfilm Games"), **{'distinctive_name': u'Loom', 'primary_nature': u'GAME'})

concept = Concept.objects.create(created_by=get_userextension("ad"), developer=get_company("Sierra Entertainment"), **{'distinctive_name': u'The Lost Mind of Dr. Brain', 'primary_nature': u'GAME'})

concept = Concept.objects.create(created_by=get_userextension("ad"), developer=get_company("LucasArts"), **{'distinctive_name': u'The Curse of Monkey Island', 'primary_nature': u'GAME'})

concept = Concept.objects.create(created_by=get_userextension("ad"), developer=get_company("Sega"), **{'distinctive_name': u'Photo CD Operating System (Saturn)', 'primary_nature': u'OS'})
url = ConceptUrl.objects.create(concept=concept, url="https://segaretro.org/Photo_CD_Operating_System")
url = ConceptUrl.objects.create(concept=concept, url="http://www.satakore.com/sega-saturn-game,,MK81681-50,,Photo-CD-Operating-System-EUR.html")

concept = Concept.objects.create(created_by=get_userextension("ad"), developer=get_company("Sega"), **{'distinctive_name': u'Nymph\xe9as Photo CD', 'primary_nature': u'MEDIA'})

concept = Concept.objects.create(created_by=get_userextension("ad"), developer=get_company("Nintendo"), **{'distinctive_name': u'Wii Remote', 'common_name': u'Wiimote', 'primary_nature': 'MOTION_SENSING'})
url = ConceptUrl.objects.create(concept=concept, url="https://en.wikipedia.org/wiki/Wii_Remote")
specific = ConceptSpecific.Remote.objects.create(concept=concept, **{'battery_type': BatteryType.objects.get(code="AA")})
specific = ConceptSpecific.RemoteAccessory.objects.create(concept=concept, **{'wireless': True})
specific = ConceptSpecific.Shell.objects.create(concept=concept, **{'is_shell': False})
specific = ConceptSpecific.Controller.objects.create(concept=concept, **{'rumble_feedback': True, 'autofire': False, 'slow': False, 'force_feedback': False})
add_nature = ConceptNature.objects.create(concept=concept, nature="PAD")
specific = ConceptSpecific.DirectionalController.objects.create(concept=concept)
specific.direction_input_type.add(1)

concept = Concept.objects.create(created_by=get_userextension("ad"), developer=get_company("Nintendo"), **{'distinctive_name': u'Nunchuk', 'primary_nature': 'PAD'})
url = ConceptUrl.objects.create(concept=concept, url="https://en.wikipedia.org/wiki/Wii_Remote#Nunchuk")
specific = ConceptSpecific.Remote.objects.create(concept=concept, **{'battery_type': None})
specific = ConceptSpecific.RemoteAccessory.objects.create(concept=concept, **{'wireless': False})
specific = ConceptSpecific.Shell.objects.create(concept=concept, **{'is_shell': False})
specific = ConceptSpecific.Controller.objects.create(concept=concept, **{'rumble_feedback': False, 'autofire': False, 'slow': False, 'force_feedback': False})
specific = ConceptSpecific.DirectionalController.objects.create(concept=concept)
specific.direction_input_type.add(2)
add_nature = ConceptNature.objects.create(concept=concept, nature="MOTION_SENSING")

concept = Concept.objects.create(created_by=get_userextension("ad"), developer=get_company("Nintendo"), **{'distinctive_name': u'Wii MotionPlus', 'primary_nature': 'MOTION_SENSING'})
url = ConceptUrl.objects.create(concept=concept, url="https://en.wikipedia.org/wiki/Wii_MotionPlus")
specific = ConceptSpecific.Remote.objects.create(concept=concept, **{'battery_type': None})
specific = ConceptSpecific.RemoteAccessory.objects.create(concept=concept, **{'wireless': False})
specific = ConceptSpecific.Shell.objects.create(concept=concept, **{'is_shell': False})
specific = ConceptSpecific.Controller.objects.create(concept=concept, **{'rumble_feedback': False, 'autofire': False, 'slow': False, 'force_feedback': False})

concept = Concept.objects.create(created_by=get_userextension("ad"), developer=get_company("Nintendo"), **{'distinctive_name': u'Wii Sports', 'primary_nature': u'GAME'})

concept = Concept.objects.create(created_by=get_userextension("ad"), developer=get_company("Nintendo"), **{'distinctive_name': u'Wii Sports Resort', 'primary_nature': u'GAME'})

concept = Concept.objects.create(created_by=get_userextension("ad"), developer=get_company("Nintendo"), **{'distinctive_name': u'Wii', 'primary_nature': u'CONSOLE'})

concept = Concept.objects.create(created_by=get_userextension("ad"), developer=get_company("Sega"), **{'distinctive_name': u'Wheel Wii Sonic', 'primary_nature': u'STEERINGWHEEL'})
specific = ConceptSpecific.Remote.objects.create(concept=concept, **{'battery_type': None})
specific = ConceptSpecific.RemoteAccessory.objects.create(concept=concept, **{'wireless': False})
specific = ConceptSpecific.Shell.objects.create(concept=concept, **{'is_shell': True})
specific = ConceptSpecific.Controller.objects.create(concept=concept, **{'rumble_feedback': False, 'autofire': False, 'slow': False, 'force_feedback': False})
relation = ConceptRelation.objects.create(concept=concept, relation="REQ", related_concept=Concept.objects.get(distinctive_name="Wii Remote"))
