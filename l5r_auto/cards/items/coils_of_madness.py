from __future__ import annotations
from .common import Item
from l5r_auto.keywords import Armor, Experienced, Fire, Fudo, Kharmic, Koan, Unique, Weapon
from l5r_auto.legality import EmperorEdition, IvoryEdition, ModernEdition
'This Personality has <b>Fallen</b> and a maximum Personal Honor of 0.<br><b>Battle, :bow::</b> Give one or two target enemy cards a <b>Madness </b>token.'
Armor_of_the_Mad = Item(card_id=10529, title='Armor of the Mad', force=0, chi=0, gold_cost=4, focus_value=4, keywords=[Armor], traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
'<b>Maho Battle/Open, :gstar::</b> Target your dead Personality. Bring him into play if his Gold Cost is equal to or less than the amount paid. Lose 2 Honor. Destroy this Item.'
Blood_of_the_Preserver_Experienced = Item(card_id=10521, title='Blood of the Preserver', force=0, chi=0, gold_cost=4, focus_value=4, keywords=[Unique, Experienced('1')], traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
'<b>Limited:</b> If this Personality is unbowed, search your Fate deck for a card and put it into your hand. Bow this Personality. Destroy this Item.'
Heart_of_Fudo_Experienced_2 = Item(card_id=10523, title='Heart of Fudo', force=0, chi=0, gold_cost=4, focus_value=4, keywords=[Experienced('2'), Unique, Fudo], traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
'This Personality has Magistrate.<br><b>Battle:</b> Dishonor a target enemy Personality. If this Personality has the printed Magistrate keyword, you may take an additional action.'
Justice_of_the_Crane = Item(card_id=10528, title='Justice of the Crane', force=3, chi=1, gold_cost=4, focus_value=3, keywords=[Weapon], traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
'This Personality has <b>Shugenja</b>, may not have more Spells than Koan cards attached, and he need not bow for his Spells with an odd Focus Value <i><i><i><i>(0 is even)</i></i></i></i>.'
Koans_Jingasa = Item(card_id=10524, title="Koan's Jingasa", force=0, chi=1, gold_cost=0, focus_value=1, keywords=[Unique, Koan], traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
"This Personality has a Force bonus equal to the number of other Koan cards in this unit.<br>This Personality need not bow for his Spells with an even Focus Value <i><i><i><i>(0 is even)</i></i></i></i>.<br>Negate the first destruction each turn of cards in this unit from another player's card."
Koans_Robes = Item(card_id=10525, title="Koan's Robes", force=1, chi=1, gold_cost=6, focus_value=2, keywords=[Unique, Koan], traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
'<b>Open, :bow::</b> Give <b>Home</b> to one or more Spells in this unit, up to the number of Koan cards in this unit. <i><i><i>(Home actions may be used from home.)</i></i></i>'
Koans_Scroll_Satchel = Item(card_id=10526, title="Koan's Scroll Satchel", force=0, chi=0, gold_cost=4, focus_value=3, keywords=[Unique, Koan], traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
'<b>Fire Battle, :bow::</b> Ranged 3 Attack with +1 strength for each other Koan card in this unit.'
Koans_Staff = Item(card_id=10527, title="Koan's Staff", force=1, chi=1, gold_cost=3, focus_value=0, keywords=[Unique, Weapon, Fire, Koan], traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
'<i><i><i><i>(<b>Limited, :g2::</b> Discard a Kharmic card from your hand to draw a card.)</i></i></i></i>'
Parangu = Item(card_id=10530, title='Parangu', force=2, chi=0, gold_cost=2, focus_value=3, keywords=[Kharmic, Weapon], traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
'<b>Limited:</b> Bow one of your target unbowed Personalities. Remove this Item from the game. Create a copy of a target Personality, ignoring costs and restrictions. Bow the second target. He will not straighten, attack, or defend until after your next turn begins. Remove the copy from the game after your next turn begins.'
The_Egg_of_Pan_Ku_Experienced = Item(card_id=10522, title="The Egg of P'an Ku", force=0, chi=0, gold_cost=10, focus_value=4, keywords=[Unique, Experienced('1')], traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])