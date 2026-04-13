from __future__ import annotations
from ..common import Personality
from l5r_auto.clans import UnicornClan
from l5r_auto.keywords import BattleMaiden, Cavalry, Commander, CommanderOfThe9thLegion, Courtier, Destined, Experienced, Imperial, Liaison, Reserve, Samurai, Scout, Shugenja, Unique, Water
from l5r_auto.legality import EmperorEdition, IvoryEdition, ModernEdition, OnyxEdition, TwentyFestivalsEdition
'<b>Open, :bow::</b>  The active player must choose and bow one of his unbowed Personalities.'
Ide_Mutsuken = Personality(card_id=10885, title='Ide Mutsuken', force=2, chi=5, personal_honor=4, gold_cost=8, honor_requirement=4, clan=[UnicornClan], keywords=[Unique, Courtier, Imperial, Liaison], traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
'<b>Limited:</b> If Wattu is face-up in your Province, put him in your discard pile, honorably dead. If there are no other dead copies of Wattu there, refill the Province face-up.'
Iuchi_Wattu = Personality(card_id=10886, title='Iuchi Wattu', force=4, chi=4, personal_honor=2, gold_cost=9, honor_requirement=4, clan=[UnicornClan], keywords=[Shugenja, Water], traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
"<b>Battle:</b> Discard a card to give a target enemy Follower or Personality a Force penalty equal to the card's Focus Value."
Moto_Paikao = Personality(card_id=10887, title='Moto Paikao', force=3, chi=3, personal_honor=2, gold_cost=5, honor_requirement=3, clan=[UnicornClan], keywords=[Commander, Samurai], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, EmperorEdition, OnyxEdition, ModernEdition])
'<b>Battle:</b> Target two Personalities at different locations controlled by the same player. Switch their locations. After they move, straighten their units if you do not control them.'
Shinjo_Kinto_Experienced_2 = Personality(card_id=10888, title='Shinjo Kinto', force=4, chi=4, personal_honor=3, gold_cost=9, honor_requirement=None, clan=[UnicornClan], keywords=[Cavalry, Experienced('2'), Unique, Commander, CommanderOfThe9thLegion, Imperial, Samurai, Scout], traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
'<b>Battle, :bow::</b> Melee 3 Attack.'
Shinjo_Sujikaro = Personality(card_id=10889, title='Shinjo Sujikaro', force=4, chi=2, personal_honor=2, gold_cost=8, honor_requirement=4, clan=[UnicornClan], keywords=[Cavalry, Samurai], traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
'<i>(Once per turn, as an Absent Engage, move your unbowed Personality in a Cavalry unit to the battle. Draw a card after you Recruit a Destined card. You may Recruit a Reserve Personality, if they would be opposed, as an Absent Battle action.)</i>'
Utaku_Sakiko = Personality(card_id=10890, title='Utaku Sakiko', force=3, chi=3, personal_honor=3, gold_cost=8, honor_requirement=4, clan=[UnicornClan], keywords=[Cavalry, Destined, Reserve, BattleMaiden, Samurai], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, EmperorEdition, OnyxEdition, ModernEdition])