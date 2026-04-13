from __future__ import annotations
from ..common import Personality
from l5r_auto.clans import BrotherhoodOfShinsei, PhoenixClan
from l5r_auto.keywords import Air, Duelist, Earth, ElementalMaster, Fire, Henshin, Inquisitor, Loyal, Magistrate, Monk, Samurai, Sensei, Shugenja, Unique, Void, Yojimbo
from l5r_auto.legality import EmperorEdition, ModernEdition
'<b>Reaction:</b> After your Ring or Henshin <i>(including Kikugoro)</i> enters play or overlays: Look at the top two cards of your Dynasty deck. You may put one of them at the bottom of the deck.'
Asako_Kikugoro = Personality(card_id=556, title='Asako Kikugoro', force=4, chi=1, personal_honor=2, gold_cost=6, honor_requirement=0, clan=[PhoenixClan, BrotherhoodOfShinsei], keywords=[Henshin, Monk, Void], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<b>Battle:</b> Target an enemy Personality: Bow him. You may target and straighten a Personality. If the enemy Personality is Kolat, Ninja, or Shadowlands, gain 2 Honor.'
Asako_Megu = Personality(card_id=561, title='Asako Megu', force=3, chi=4, personal_honor=3, gold_cost=7, honor_requirement=6, clan=[PhoenixClan], keywords=[Earth, Inquisitor, Magistrate, Shugenja], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<b>Limited:</b> Bow Koiso, destroy your Shugenja with the base Fire keyword, discard a card, and target a non-Unique card without attachments in a unit: Destroy it.<br><b>Battle:</b> Target a card without attachments in a unit: Destroy it.'
Isawa_Koiso = Personality(card_id=3849, title='Isawa Koiso', force=5, chi=4, personal_honor=2, gold_cost=11, honor_requirement=4, clan=[PhoenixClan], keywords=[Loyal, Unique, ElementalMaster, Fire, Shugenja], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<b>Battle:</b> Target an attachment or token at the current battlefield: Destroy it. If this destroyed a card or token, give Mina two +1F Fire tokens.'
Isawa_Mina = Personality(card_id=3861, title='Isawa Mina', force=4, chi=3, personal_honor=2, gold_cost=8, honor_requirement=4, clan=[PhoenixClan], keywords=[Fire, Shugenja], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'After Sanetomo enters play: Discard all your other Sensei Personalities.<br>Once per battle, one of your Phoenix Clan Shugenja may perform the Equip Battle action even if bowed and even if unopposed.'
Isawa_Sanetomo = Personality(card_id=3892, title='Isawa Sanetomo', force=3, chi=4, personal_honor=3, gold_cost=7, honor_requirement=6, clan=[PhoenixClan], keywords=[Loyal, Air, Sensei, Shugenja], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
Shiba_Toshisugo = Personality(card_id=6814, title='Shiba Toshisugo', force=5, chi=4, personal_honor=2, gold_cost=7, honor_requirement=6, clan=[PhoenixClan], keywords=[Duelist, Samurai, Yojimbo], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])