from __future__ import annotations
from ..common import Personality
from l5r_auto.clans import ShadowlandsFaction, Unaligned
from l5r_auto.keywords import Air, BakeKujira, Bashe, BatClan, Naval, Nonhuman, Oni, Shadowlands, Shugenja, Undead, Water
from l5r_auto.legality import CelestialEdition, EmperorEdition, IvoryEdition, ModernEdition, TwentyFestivalsEdition
'<i>(Shugenja may attach and cast Spells.)</i><br><b>Air Tireless Open:</b> Straighten Taruko. <i>(Tireless actions can be taken even while bowed.)</i>'
Komori_Taruko = Personality(card_id=4537, title='Komori Taruko', force=3, chi=4, personal_honor=2, gold_cost=5, honor_requirement=1, clan=[Unaligned], keywords=[Air, BatClan, Shugenja], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, EmperorEdition, CelestialEdition, ModernEdition])
'Will only enter play from a province.<br>After Raido enters play: Lose 6 Honor.<br>Raido may not perform Battle actions while your current army has higher total Force than the current enemy army.'
Raido_no_Oni = Personality(card_id=6142, title='Raido no Oni', force=10, chi=2, personal_honor=0, gold_cost=7, honor_requirement=None, clan=[Unaligned, ShadowlandsFaction], keywords=[Nonhuman, Oni, Shadowlands], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
'After The Great Death enters play: Create three 1F <b>Shadowlands &#149; Nonhuman &#149; Raptor &#149; Cavalry &#149; Undead</b> Followers, attach them to it, and lose 6 Honor.'
The_Great_Death = Personality(card_id=8110, title='The Great Death', force=6, chi=4, personal_honor=0, gold_cost=9, honor_requirement=None, clan=[Unaligned, ShadowlandsFaction], keywords=[Naval, BakeKujira, Nonhuman, Shadowlands, Undead, Water], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
"<b>Battle:</b> Target one or two attachments, or a Personality without attachments, with a total Force lower than The Red Hunger's Force: He swallows them whole. Destroy the targeted cards."
The_Red_Hunger = Personality(card_id=8283, title='The Red Hunger', force=7, chi=1, personal_honor=0, gold_cost=9, honor_requirement=None, clan=[Unaligned], keywords=[Bashe, Nonhuman], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])