from __future__ import annotations
from .common import Item
from l5r_auto.keywords import Cursed, Experienced, Pearl, Unique, Weapon
from l5r_auto.legality import CelestialEdition, EmperorEdition, ModernEdition
"<b>Limited:</b> Destroy this card and target a Personality in any player's discard pile: Bring him into play <i>(under your control)</i>, paying all costs, but paying 4 less Gold if the Personality is Nonhuman."
Black_Pearl_Experienced = Item(card_id=993, title='Black Pearl', force=0, chi=1, gold_cost=4, focus_value=4, keywords=[Unique, Experienced('1'), Pearl], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
'<b>Battle:</b> Any number of times per turn, give this Personality -1C: Ranged 3 Attack.<br><b>Battle:</b> Bow this card, give this Personality -1C, and target an enemy card without attachments: Remove it from the game.'
Cursed_Relic = Item(card_id=1607, title='Cursed Relic', force=4, chi=0, gold_cost=8, focus_value=1, keywords=[Weapon, Cursed], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
'<b>Battle/Open:</b> Bow this card: Straighten this Personality.'
Pearl_of_Embers = Item(card_id=5902, title='Pearl of Embers', force=0, chi=1, gold_cost=0, focus_value=1, keywords=[Pearl], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])