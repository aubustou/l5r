from __future__ import annotations
from .common import Item
from l5r_auto.keywords import Courage, Expendable, Gaijin, OneHanded, Peasant, Polearm, Standard, TwoHanded, Weapon
from l5r_auto.legality import ModernEdition, OnyxEdition, TwentyFestivalsEdition
'<b>Battle, :bow::</b> Bow a target enemy card. Destroy it if it is a One-Handed Weapon.'
Bisento = Item(card_id=12205, title='Bisento', force=2, chi=1, gold_cost=6, focus_value=2, keywords=[Weapon, Polearm, TwoHanded], traits=[], abilities=[], legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition])
"<i>(Draw a card after your Expendable card is destroyed.)</i><br>This Item has +1F while this Personality is a Kensai.<br><b>Battle:</b> Negate this Personality's current Force penalties."
Farmers_Kama = Item(card_id=12206, title="Farmer's Kama", force=1, chi=1, gold_cost=2, focus_value=1, keywords=[Expendable, Weapon, OneHanded, Peasant], traits=[], abilities=[], legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition])
'Fear effects targeting cards in this unit have -1 strength. Ranged Attacks targeting cards in this unit have +1 strength. While opposed, this Personality has +1PH and his Followers have +1F.'
OumaJirushi = Item(card_id=12207, title='Ouma-Jirushi', force=0, chi=0, gold_cost=1, focus_value=3, keywords=[Standard], traits=[], abilities=[], legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition])
'<b>Open:</b> Destroy a target Holding controlled by a player with four or more Holdings in play. Lose 2 Honor. Remove this Item from the game.'
Polvora_Cache = Item(card_id=12208, title='Polvora Cache', force=0, chi=0, gold_cost=4, focus_value=1, keywords=[Gaijin], traits=[], abilities=[], legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition])
'After this Item attaches, dishonor this Personality.<br><b>Battle, :bow::</b> Give a target enemy Follower or Personality -2F.'
Wooden_Nunchaku = Item(card_id=12209, title='Wooden Nunchaku', force=2, chi=0, gold_cost=2, focus_value=1, keywords=[Courage, Weapon, OneHanded, Peasant], traits=[], abilities=[], legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition])