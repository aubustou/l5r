from __future__ import annotations
from .common import Spell
from l5r_auto.keywords import Earth, Fire, Jade, Pearl, Ritual, Thunder, Water
from l5r_auto.legality import EmperorEdition, IvoryEdition, ModernEdition
"<b>Battle:</b> Bow this card and target an enemy Personality: Remove one of his abilities. If this Shugenja is Earth, reduce the target's Force to 0. If the target is an Oni, destroy it and this card."
Jade_Embrace = Spell(card_id=9985, title='Jade Embrace', gold_cost=0, focus_value=2, keywords=[Earth, Jade], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'This Shugenja has +4F.<br><b>Battle:</b> Bow this Shugenja unless he is Fire or Thunder and target an enemy card without attachments: Destroy it.'
Might_of_the_Sun = Spell(card_id=5046, title='Might of the Sun', gold_cost=7, focus_value=1, keywords=[Fire, Thunder], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<b>Battle:</b> Bow this card and target this Shugenja, or, if this Shugenja is Water, you may target another of your Personalities: Move the target to the current battlefield if he would be opposed there. Straighten him if he moved.'
Sanctuary_of_the_Waves = Spell(card_id=10238, title='Sanctuary of the Waves', gold_cost=0, focus_value=1, keywords=[Water], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<b>Battle/Open:</b> Destroy this card and target a Region or Terrain: Either destroy it or permanently remove its traits and abilities.'
Sea_Sky = Spell(card_id=9988, title='Sea & Sky', gold_cost=0, focus_value=2, keywords=[Pearl], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
"<b>Ritual Air Limited:</b> Bow one or more of your target unbowed Shugenja. Discard an equal number of cards from the top of your Fate deck. Bow zero or more target Personalities with total Chi less than the total of the cards' Focus Values. Destroy this Spell."
Sleep = Spell(card_id=10596, title='Sleep', gold_cost=4, focus_value=4, keywords=[Ritual], traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
'<b>Limited:</b> Bow this Shugenja to search your Fate deck for an Item, show it, and put it in your hand. Destroy this Spell.'
Summon_Fushicho = Spell(card_id=10414, title='Summon Fushicho', gold_cost=0, focus_value=3, traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
'You may Equip this Spell as a <b>Battle</b> action to your Earth Shugenja at any location.<br><b>Home Earth Battle:</b> Bow a target enemy card. Destroy this Spell. <br><i>(Home actions may be used from home.)</i>'
Trembling_Earth = Spell(card_id=10595, title='Trembling Earth', gold_cost=0, focus_value=2, traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])