from __future__ import annotations
from ..common import Personality
from l5r_auto.clans import BrotherhoodOfShinsei, DragonClan
from l5r_auto.keywords import Cavalry, Courtier, Duelist, Earth, Experienced, Imperial, Kensai, Loyal, Magistrate, Monk, Mountaineer, Samurai, Sensei, Shugenja, Tattooed, Unique, Water
from l5r_auto.legality import EmperorEdition, IvoryEdition, ModernEdition, TwentyFestivalsEdition
'<b>Iaijutsu Reaction:</b> After an action resolves during which Daisuke won a duel: Draw a card.'
Kitsuki_Daisuke_Experienced = Personality(card_id=4407, title='Kitsuki Daisuke', force=4, chi=4, personal_honor=4, gold_cost=7, honor_requirement=10, clan=[DragonClan], keywords=[Duelist, Unique, Courtier, Experienced('1'), Magistrate], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<b>Political Reaction:</b> After an action resolves during which Jakuei won a duel, take the Imperial Favor.<br><b>Favor Political Battle:</b> Bow a target enemy Personality. You may discard the Imperial Favor to move him home.'
Kitsuki_Jakuei = Personality(card_id=4416, title='Kitsuki Jakuei', force=3, chi=4, personal_honor=3, gold_cost=8, honor_requirement=5, clan=[DragonClan], keywords=[Duelist, Courtier, Imperial, Magistrate], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'After Hikaro enters play: Discard all your other Sensei Personalities.<br>Before you focus in a duel involving your Dragon Clan Personality: Once per duel, you may focus from your discard pile instead. Remove that card from the game after the duel ends.'
Mirumoto_Hikaro = Personality(card_id=5095, title='Mirumoto Hikaro', force=2, chi=5, personal_honor=2, gold_cost=7, honor_requirement=0, clan=[DragonClan], keywords=[Duelist, Loyal, Samurai, Sensei], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<b>Battle:</b> Target an enemy card with equal or lower Force: Bow it.'
Mirumoto_Kouzei = Personality(card_id=5125, title='Mirumoto Kouzei', force=5, chi=3, personal_honor=2, gold_cost=8, honor_requirement=4, clan=[DragonClan], keywords=[Kensai, Samurai], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<i><i>(Once per turn, as an Absent Engage, move your unbowed Personality in a Cavalry unit to this battle. Shugenja may attach and cast Spells.)</i></i>'
Tamori_Seiken = Personality(card_id=7790, title='Tamori Seiken', force=2, chi=3, personal_honor=3, gold_cost=4, honor_requirement=8, clan=[DragonClan], keywords=[Cavalry, Earth, Mountaineer, Shugenja], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, EmperorEdition, ModernEdition])
'<b>Battle:</b> Even if Rikyou is bowed, if any enemy units are at the current battlefield: Move him there. Straighten his unit if he moved.'
Togashi_Rikyou = Personality(card_id=8568, title='Togashi Rikyou', force=5, chi=3, personal_honor=1, gold_cost=8, honor_requirement=3, clan=[DragonClan, BrotherhoodOfShinsei], keywords=[Monk, Tattooed, Water], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])