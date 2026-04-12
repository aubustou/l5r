from __future__ import annotations
from ..common import Personality
from l5r_auto.clans import BrotherhoodOfShinsei, PhoenixClan
from l5r_auto.keywords import Air, Alchemist, Daimyo, Duelist, Earth, Experienced, Fire, Henshin, Inquisitor, LegionOfFlame, Loyal, Magistrate, Monk, Nonhuman, Ryu, Samurai, Shugenja, Unique, Void, Water, Yojimbo
from l5r_auto.legality import EmperorEdition, ModernEdition
'<b>Earth Void Battle/Open, :gstar::</b> Equip a target non-Unique Spell in your discard pile or under your Stronghold to Kurou. You may take an additional action to use an ability on the Spell. Remove it from the game before the turn ends.'
Agasha_Kurou = Personality(card_id=9835, title='Agasha Kurou', force=5, chi=4, personal_honor=3, gold_cost=10, honor_requirement=6, clan=[PhoenixClan], keywords=[Loyal, Unique, Alchemist, Daimyo, Earth, Shugenja, Void], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<b>Open:</b> Give Hayate <b>Cavalry</b>, <b>Naval</b>, or <b>Tactician</b>.'
Asako_Hayate = Personality(card_id=9836, title='Asako Hayate', force=4, chi=4, personal_honor=3, gold_cost=8, honor_requirement=4, clan=[PhoenixClan, BrotherhoodOfShinsei], keywords=[Henshin, Monk, Water], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<b>Open:</b> Target a Personality: If he is Kolat, Ninja, or Shadowlands, his base abilities may not be used. Give him <b>Kolat</b>, <b>Ninja</b>, or <b>Shadowlands</b>.'
Asako_Jirou = Personality(card_id=9837, title='Asako Jirou', force=2, chi=4, personal_honor=4, gold_cost=7, honor_requirement=8, clan=[PhoenixClan], keywords=[Air, Inquisitor, Magistrate, Shugenja], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
Isawa_Hinata = Personality(card_id=9838, title='Isawa Hinata', force=3, chi=3, personal_honor=2, gold_cost=5, honor_requirement=2, clan=[PhoenixClan], keywords=[Fire, Shugenja], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'Will not attach Followers or Items.<br><b>Absent Tireless Battle:</b> If Natsumi would be opposed, move it to the current battlefield. After this moves it, straighten its unit.'
Natsumi = Personality(card_id=9839, title='Natsumi', force=3, chi=4, personal_honor=3, gold_cost=7, honor_requirement=5, clan=[PhoenixClan], keywords=[Nonhuman, Ryu, Shugenja, Water], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
"<b>Battle:</b> Target an enemy Personality: Kudome duels him. Destroy the duel's loser. Give Kudome a +1F Fire token if she won and you control a Shugenja."
Shiba_Kudome_Experienced = Personality(card_id=9840, title='Shiba Kudome', force=4, chi=4, personal_honor=3, gold_cost=8, honor_requirement=6, clan=[PhoenixClan], keywords=[Duelist, Loyal, Unique, Experienced('1'), Fire, LegionOfFlame, Samurai, Yojimbo], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'Shirou has +2F while you control a Shugenja.<br><b>Battle:</b> Melee 4 Attack.'
Shiba_Shirou = Personality(card_id=9841, title='Shiba Shirou', force=3, chi=4, personal_honor=3, gold_cost=8, honor_requirement=3, clan=[PhoenixClan], keywords=[Duelist, Samurai, Yojimbo], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])