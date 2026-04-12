from __future__ import annotations
from ..common import Personality
from l5r_auto.clans import ShadowlandsFaction, Unaligned
from l5r_auto.keywords import Alchemist, Ashigaru, Cavalry, Commander, Conqueror, DevourerOfGods, Duelist, Expendable, Experienced, Fudo, Gaijin, Goblin, Imperial, ImperialTreasurer, Kensai, Ningyo, Nonhuman, Pearl, Ronin, Samurai, Scout, Sensei, Shadowlands, Shugenja, Tactician, Unique
from l5r_auto.legality import EmperorEdition, IvoryEdition, ModernEdition
'<i><i><i><i>(Draw a card after your Expendable card is destroyed.)</i></i></i></i>'
Armed_Rice_Farmer = Personality(card_id=10584, title='Armed Rice Farmer', force=1, chi=1, personal_honor=0, gold_cost=2, honor_requirement=None, clan=[Unaligned], keywords=[Expendable, Ashigaru], traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
'<b>Battle:</b> Target an enemy attachment: Destroy it.'
Chikara_Experienced_2 = Personality(card_id=1319, title='Chikara', force=5, chi=4, personal_honor=2, gold_cost=7, honor_requirement=None, clan=[Unaligned], keywords=[Duelist, Experienced('2'), Kensai, Unique, Ronin, Samurai], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
"Fudo may not assign, and will not move, to battlefields unless it has 5 Charging tokens. After Fudo is assigned: Remove two of its Charging tokens.<br><b>Reaction:</b> Twice per turn, after an action targets Fudo, remove one of its Charging tokens: Negate the action's effects on it.<br><b>Limited:</b> Give Fudo two <b>Charging </b>tokens.<br><b>Battle:</b> Target an enemy unit: Destroy it."
Fudo_Experienced = Personality(card_id=2721, title='Fudo', force=12, chi=6, personal_honor=0, gold_cost=7, honor_requirement=None, clan=[Unaligned], keywords=[Conqueror, Unique, Experienced('1'), Fudo, Nonhuman], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
"<b>Iaijustu Limited:</b> Target another player's Personality: Fusako challenges the target. His controller may bow him; if he is now bowed, he may refuse the duel. Destroy the duel's loser."
Fusako = Personality(card_id=10232, title='Fusako', force=3, chi=3, personal_honor=3, gold_cost=7, honor_requirement=4, clan=[Unaligned], keywords=[Duelist, Unique, Ronin, Samurai], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'After you announce your Ritual action, until it finishes resolving, Gaijin Sorcerer counts as two Shugenja.'
Gaijin_Sorcerer = Personality(card_id=10585, title='Gaijin Sorcerer', force=0, chi=4, personal_honor=1, gold_cost=5, honor_requirement=None, clan=[Unaligned], keywords=[Gaijin, Shugenja], traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
'Enters play paying 1 less Gold if you are a Spider Clan player.<br>After Gakku enters play: Lose 3 Honor.<br><b>Battle:</b> Melee 7 Attack.'
Gakku_Experienced = Personality(card_id=2765, title='Gakku', force=7, chi=2, personal_honor=0, gold_cost=9, honor_requirement=None, clan=[Unaligned, ShadowlandsFaction], keywords=[Unique, DevourerOfGods, Experienced('1'), Goblin, Nonhuman, Scout, Shadowlands], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<b>Battle:</b> Target a Terrain: Destroy it. You may discard a card. If you did, search your Fate deck for a Terrain, show it, then take an additional Battle action to play it, if legal; if not, discard it.'
Gozu = Personality(card_id=2887, title='Gozu', force=2, chi=3, personal_honor=2, gold_cost=3, honor_requirement=None, clan=[Unaligned], keywords=[Ronin, Samurai, Scout], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'Enters play for 1 less Gold for each Farm other players control.'
Kataoka = Personality(card_id=10583, title='Kataoka', force=3, chi=1, personal_honor=1, gold_cost=5, honor_requirement=None, clan=[Unaligned], keywords=[Cavalry, Commander, Ronin, Samurai], traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
'<b>Open:</b> Give Mahatsu <b>Air</b>, <b>Earth</b>, <b>Fire</b>, or <b>Water</b>.'
Mahatsu = Personality(card_id=4796, title='Mahatsu', force=3, chi=3, personal_honor=1, gold_cost=3, honor_requirement=None, clan=[Unaligned], keywords=[Alchemist, Ronin, Shugenja], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
"<b>Battle:</b> Give your Followers in Barru's army +1F."
Seppun_Barru = Personality(card_id=10233, title='Seppun Barru', force=3, chi=3, personal_honor=2, gold_cost=4, honor_requirement=4, clan=[Unaligned], keywords=[Commander, Imperial, Samurai], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'Ichigo has +1F for each Dojo you control.'
Seppun_Ichigo = Personality(card_id=9957, title='Seppun Ichigo', force=2, chi=2, personal_honor=2, gold_cost=3, honor_requirement=0, clan=[Unaligned], keywords=[Imperial, Samurai], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'Your Holdings produce 1 additional Gold when they bow to produce Gold.'
Seppun_Ritisharu = Personality(card_id=9958, title='Seppun Ritisharu', force=0, chi=3, personal_honor=3, gold_cost=2, honor_requirement=0, clan=[Unaligned], keywords=[Unique, Imperial, ImperialTreasurer], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'After Tamahime enters play: Discard all your other Sensei Personalities.<br>Your other Ronin Personalities have <b>Tactician</b>.'
Tamahime = Personality(card_id=10194, title='Tamahime', force=3, chi=3, personal_honor=2, gold_cost=6, honor_requirement=0, clan=[Unaligned], keywords=[Tactician, Ronin, Samurai, Sensei], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'After Tamahime enters play or overlays: Discard all your other Sensei Personalities.<br>Your other Ronin Personalities have <b>Tactician</b>.<br>Your other Ronin cards enter play paying 1 less Gold.<br>Battle: Target an enemy card without attachments: Destroy it.'
Tamahime_Experienced = Personality(card_id=10193, title='Tamahime', force=5, chi=3, personal_honor=3, gold_cost=7, honor_requirement=2, clan=[Unaligned], keywords=[Tactician, Unique, Experienced('1'), Ronin, Samurai, Sensei], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<b>Battle:</b> Target an enemy card: Bow it.'
Tesskss = Personality(card_id=9959, title="Tess'kss", force=3, chi=3, personal_honor=0, gold_cost=4, honor_requirement=None, clan=[Unaligned], keywords=[Ningyo, Nonhuman, Pearl, Shugenja], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])