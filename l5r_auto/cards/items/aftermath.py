from __future__ import annotations
from .common import Item
from l5r_auto.keywords import Armor, Nemuranai, Ninja, OneHanded, Sword, Weapon
from l5r_auto.legality import EmperorEdition, IvoryEdition, ModernEdition, OnyxEdition, TwentyFestivalsEdition
'After your turn begins, give this Personality a +1F <b>Obsession</b> token; then, if he has more Obsession tokens than printed Chi, destroy him.'
Dagger_of_Crystal_Wind = Item(card_id=10903, title='Dagger of Crystal Wind', force=0, chi=1, gold_cost=1, focus_value=1, keywords=[Weapon, Nemuranai], traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
"As a Focus Effect, the duel's winner may take an additional action.<br>Ranged and Melee Attacks targeting this Personality have -2 strength. <br>Before another player's card destroys this Personality during the Action Phase, negate the destruction and destroy this Item."
Fortunes_Charm = Item(card_id=10904, title="Fortune's Charm", force=0, chi=0, gold_cost=0, focus_value=4, keywords=[Nemuranai], traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
'<b>Engage, :bow::</b> Give a target enemy Personality or Follower -2F.'
Khalimpehjiak = Item(card_id=10905, title='Khalimpeh-jiak', force=2, chi=0, gold_cost=3, focus_value=2, keywords=[Weapon], traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
'<b>Multiplayer Open, :bow::</b> Target a player. Until your next turn begins, each of you must invite the other to ally <i>(if legal)</i>, and during Maneuvers, the invited one must assign a unit to an army where the other has a unit, and may not assign units elsewhere.'
Ningens_Treatise_on_the_Nezumi = Item(card_id=10906, title="Ningen's 'Treatise on the Nezumi'", force=0, chi=0, gold_cost=3, focus_value=4, traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
"<i>(A Personality can only have one Armor.)</i><br>Before another player's card destroys this Personality, destroy this Item instead."
Ominous_Armor = Item(card_id=10907, title='Ominous Armor', force=2, chi=0, gold_cost=3, focus_value=1, keywords=[Armor], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, EmperorEdition, OnyxEdition, ModernEdition])
'This Personality has +1F while he is Siege.<br><b>Battle, :bow::</b> Give this Province +2 strength.'
Stonemasons_Hammer = Item(card_id=10908, title="Stonemason's Hammer", force=2, chi=0, gold_cost=4, focus_value=2, keywords=[Weapon], traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
"<b>Battle, :bow::</b> Actions from cards in a target Personality's unit may not target cards in this unit."
Tankoji = Item(card_id=10909, title='Tankoji', force=1, chi=0, gold_cost=2, focus_value=3, keywords=[Weapon], traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
'<b>Ninja Battle, :bow::</b> Melee 3 Attack <i>(Destroy a target enemy Follower or Personality without Followers with 3 or lower Force)</i>.'
Tiger_Claw = Item(card_id=10910, title='Tiger Claw', force=2, chi=0, gold_cost=5, focus_value=1, keywords=[Weapon, Ninja, OneHanded], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, EmperorEdition, OnyxEdition, ModernEdition])
'<b>:bow::</b> Produce 2 Gold.'
Tsujikens_Coin = Item(card_id=10911, title="Tsujiken's Coin", force=0, chi=0, gold_cost=3, focus_value=1, traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
'<b>Battle:</b> Discard a card to straighten this Personality.<br><b>Home Battle:</b> If this Personality would be opposed, discard a card to move him to the current battlefield.'
Versatile_Blade = Item(card_id=10912, title='Versatile Blade', force=2, chi=1, gold_cost=4, focus_value=4, keywords=[Weapon, OneHanded, Sword], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, EmperorEdition, OnyxEdition, ModernEdition])