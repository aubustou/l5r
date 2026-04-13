from __future__ import annotations
from .common import Item
from l5r_auto.keywords import Armor, HeavyWeapon, Imperial, OneHanded, Standard, Weapon
from l5r_auto.legality import CelestialEdition, EmperorEdition, IvoryEdition, LotusEdition, ModernEdition, SamuraiEdition, TwentyFestivalsEdition
'<b>Political Reaction:</b> After another player targets this Personality with an action, choose a player, who gains or loses 2 Honor.'
Armor_of_the_Heavens = Item(card_id=446, title='Armor of the Heavens', force=3, chi=0, gold_cost=4, focus_value=4, keywords=[Armor, Imperial], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, SamuraiEdition, ModernEdition])
"After this Item bows, straighten it.<br><b>Reaction, :gstar::</b> After the resolution of another player's action that destroyed this Item or its Personality, Equip this Item to your target performing Personality."
Blade_of_Perfection = Item(card_id=1010, title='Blade of Perfection', force=3, chi=1, gold_cost=4, focus_value=3, keywords=[Weapon], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
'<b>Reaction:</b> After this Personality is assigned: Give him a +1F token. Gain 1 Honor.'
Chrysanthemum_Blossom = Item(card_id=1340, title='Chrysanthemum Blossom', force=0, chi=0, gold_cost=1, focus_value=4, keywords=[Imperial], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, SamuraiEdition, ModernEdition])
"Your Personalities with your Clan alignment at this card's battlefield have +1F, or +2F if they have any Followers."
Clan_Standard = Item(card_id=1407, title='Clan Standard', force=1, chi=0, gold_cost=3, focus_value=4, keywords=[Standard], traits=[], abilities=[], legality=[EmperorEdition, LotusEdition, SamuraiEdition, ModernEdition])
'Negate all current and new Chi penalties on this Personality. <br>Negate any destruction of this card, except for its Personality being destroyed.'
Gift_Armor = Item(card_id=2798, title='Gift Armor', force=3, chi=0, gold_cost=4, focus_value=2, keywords=[Armor], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, SamuraiEdition, ModernEdition])
'This card has +1F while attached to a Kensai.<br><b>Reaction:</b> After engaging, choose your performing Personality at the current battlefield: Attach this card from your hand to him, paying all costs.'
Kensais_Blade = Item(card_id=4323, title="Kensai's Blade", force=2, chi=1, gold_cost=3, focus_value=3, keywords=[Weapon], traits=[], abilities=[], legality=[EmperorEdition, SamuraiEdition, ModernEdition])
'This card will not be transferred.<br>Attaches to a Paragon or Kensai paying 3 less Gold.'
Magayari = Item(card_id=4790, title='Maga-yari', force=3, chi=1, gold_cost=5, focus_value=3, keywords=[Weapon], traits=[], abilities=[], legality=[EmperorEdition, SamuraiEdition, ModernEdition])
'<b>Battle:</b> Draw a card.'
Modifications = Item(card_id=5214, title='Modifications', force=4, chi=1, gold_cost=7, focus_value=2, keywords=[Weapon], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
'Before this Personality focuses: You may give him +3 to his duel stat until the duel ends instead of focusing.'
Reserve_Weapon = Item(card_id=6269, title='Reserve Weapon', force=3, chi=0, gold_cost=3, focus_value=3, keywords=[Weapon], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<b>Battle:</b> Bow this card and target an enemy card without a Weapon or Armor: Bow it.'
Sasumata = Item(card_id=6478, title='Sasumata', force=2, chi=1, gold_cost=3, focus_value=3, keywords=[Weapon], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
'After this Personality enters a duel, the other Personality in the duel loses Duelist.'
Spiked_Tetsubo = Item(card_id=7411, title='Spiked Tetsubo', force=2, chi=1, gold_cost=3, focus_value=3, keywords=[Weapon, HeavyWeapon, OneHanded], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, EmperorEdition, LotusEdition, ModernEdition])
'<b>Battle:</b> Bow this card: Ranged 5 Attack.'
Tsuruchi_Daikyu = Item(card_id=8823, title='Tsuruchi Daikyu', force=5, chi=0, gold_cost=7, focus_value=3, keywords=[Weapon], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])