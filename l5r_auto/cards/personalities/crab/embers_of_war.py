from __future__ import annotations
from ..common import Personality
from l5r_auto.clans import CrabClan
from l5r_auto.keywords import Berserker, Courtier, FriendOfThunder, Kolat, Loyal, Merchant, Samurai, Scholar, Scout, Sensei, Siege, Tactician, TopazChampion, Unique
from l5r_auto.legality import EmperorEdition, IvoryEdition, ModernEdition, TwentyFestivalsEdition
"<b>Reaction:</b> After an action resolves that Bakishi performed and that destroyed a card at the current battlefield: The next time <i>(this turn)</i> another player's action targets Bakishi, negate its effects on him."
Hida_Bakishi = Personality(card_id=3075, title='Hida Bakishi', force=7, chi=2, personal_honor=0, gold_cost=9, honor_requirement=None, clan=[CrabClan], keywords=[Berserker, FriendOfThunder], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
"After Osote enters play, discard all your other Sensei Personalities.<br>After the first time each turn another player's action targets your Crab Clan Personality at Osote's location, the player discards a card after the action ends."
Hida_Osote = Personality(card_id=3165, title='Hida Osote', force=4, chi=3, personal_honor=1, gold_cost=7, honor_requirement=None, clan=[CrabClan], keywords=[Loyal, Samurai, Sensei], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
Hiruma_Moritoki = Personality(card_id=3307, title='Hiruma Moritoki', force=4, chi=3, personal_honor=2, gold_cost=6, honor_requirement=0, clan=[CrabClan], keywords=[Samurai, Scholar, Scout], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, EmperorEdition, ModernEdition])
"<b>Battle:</b> Ranged Attack with strength equal to the current battlefield's province's strength."
Kaiu_Onizuka = Personality(card_id=4131, title='Kaiu Onizuka', force=3, chi=3, personal_honor=2, gold_cost=7, honor_requirement=0, clan=[CrabClan], keywords=[Tactician, Unique, Samurai, Siege, TopazChampion], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<b>Limited:</b> If none of your provinces have been destroyed since your last turn began, or you are a Scorpion Clan player: Gain 2 Honor.<br><b>Battle:</b> Target an enemy card without attachments: Bow it.'
Kaiu_Tojikana = Personality(card_id=4145, title='Kaiu Tojikana', force=5, chi=3, personal_honor=3, gold_cost=9, honor_requirement=3, clan=[CrabClan], keywords=[Tactician, Samurai, Siege], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'Your Holdings enter play for 1 less Gold. <br><b>Economic Home Battle, :bow::</b> Target an enemy Personality. His controller may pay 4 Gold. If he does, he loses 1 Honor. If he does not, dishonor the target and move him home.'
Yasuki_Makoto = Personality(card_id=9449, title='Yasuki Makoto', force=2, chi=3, personal_honor=1, gold_cost=7, honor_requirement=None, clan=[CrabClan], keywords=[Courtier, Kolat, Merchant], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, EmperorEdition, ModernEdition])