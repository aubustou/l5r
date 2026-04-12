from __future__ import annotations
from .common import Item
from l5r_auto.keywords import Armor, Shadowlands, Siege, Thunder, Unique, Weapon
from l5r_auto.legality import EmperorEdition, ModernEdition
"Attaches to Hida Chiyurei paying 2 less Gold.<br>Melee Attacks this Personality performs may be compared against the target's base Force."
Chiyureis_Axe = Item(card_id=10340, title="Chiyurei's Axe", force=3, chi=0, gold_cost=4, focus_value=2, keywords=[Weapon], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'This Personality has <b>Kolat</b>.<br><b>Open:</b> If it is not your turn, bow this card and choose a player: He chooses and bows one of his unbowed Personalities.'
Kages_Teachings = Item(card_id=10341, title="Kage's Teachings", force=0, chi=0, gold_cost=4, focus_value=2, keywords=[Unique], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<b>Limited:</b> If this card is in your hand, target your dead Personality who was in play during your last turn: Bring him into play, ignoring costs and restrictions, and permanently give him <b><b>Shadowlands &#149; Undead</b></b>. Attach this card to him <i>(you must pay its cost)</i>. Lose 3 Honor.'
Panekis_Mask = Item(card_id=10342, title="Paneki's Mask", force=0, chi=1, gold_cost=4, focus_value=4, keywords=[Unique, Shadowlands], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<b>Battle:</b> Bow this card and target a Region <i>(at any location)</i> or a Terrain: Destroy it.<br><b>Battle:</b> Bow this card: Ranged 4 Attack, with +1 strength if this Personality is Siege or Earth.'
Renyus_Wrath = Item(card_id=10343, title="Renyu's Wrath", force=4, chi=0, gold_cost=6, focus_value=4, keywords=[Unique, Siege], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<b>Battle:</b> Three times per turn: Give this Personality +1F.'
Sturdy_Armor = Item(card_id=10344, title='Sturdy Armor', force=2, chi=0, gold_cost=4, focus_value=2, keywords=[Armor], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
"Negate other players' cards' effects that prevent this Personality performing actions.<br><b>Battle/Open:</b> Target your Personality at any location: Transfer this card to him."
Thunder_Bow = Item(card_id=10345, title='Thunder Bow', force=3, chi=0, gold_cost=4, focus_value=2, keywords=[Weapon, Thunder], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])