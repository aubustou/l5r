from __future__ import annotations
from .common import Spell
from l5r_auto.keywords import Air, Earth, Fire, Iaijutsu, Maho, Void, Water
from l5r_auto.legality import EmperorEdition, IvoryEdition, ModernEdition, OnyxEdition, TwentyFestivalsEdition
'<b>Water Battle, :bow::</b> Move this Shugenja from the current battlefield to an adjacent battlefield.'
Befriend_the_Tides = Spell(card_id=10708, title='Befriend the Tides', gold_cost=1, focus_value=3, keywords=[Water], traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
'<b>Earth Limited, :bow::</b> If this Shugenja is Human, permanently give him <b>Nonhuman, </b>+2F, and the ability, "<b>Battle:</b> Bow a target enemy card with lower Force." Destroy this Spell. Lose 1 Honor.'
Cast_Aside_Appearances = Spell(card_id=10703, title='Cast Aside Appearances', gold_cost=4, focus_value=4, keywords=[Earth], traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
"<b>Air Limited, :bow::</b> This Spell may remain bowed. Create a 0F <b>Illusion &#149; Nonhuman &#149; Cavalry &#149; Shugenja</b> Personality with this Shugenja's Chi and Personal Honor. After the next time this game this Spell straightens or leaves play, remove the Illusion from the game."
Constructing_the_Self = Spell(card_id=10700, title='Constructing the Self', gold_cost=4, focus_value=3, keywords=[Air], traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
"<b>Fire Iaijutsu Battle, :bow::</b> This Shugenja challenges a target enemy Personality. During the duel, if this Shugenja is Fire, he has <b>Duelist</b>. Bow the duel's loser. Destroy this Spell."
Focus_on_the_Flame = Spell(card_id=10710, title='Focus on the Flame', gold_cost=0, focus_value=4, keywords=[Fire, Iaijutsu], traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
"<b>Open:</b> Target your created Spirit Personality. Create a Personality that permanently copies the target's printed keywords, traits, abilities, and stats. Destroy this Spell."
Gates_of_Chikushudo = Spell(card_id=10707, title='Gates of Chikushudo', gold_cost=4, focus_value=1, traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
'<b>Earth Battle, :bow::</b> Bow a target enemy Follower or Personality with 4 or lower Force.'
Kiyoshis_Wrath = Spell(card_id=10701, title="Kiyoshi's Wrath", gold_cost=0, focus_value=2, traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, EmperorEdition, OnyxEdition, ModernEdition])
'<b>Home Water Battle, :bow::</b> Move your target Spirit Personality at any location to the current battlefield. <i>(Home actions may be taken from home.)</i>'
My_Ancestors_Steed = Spell(card_id=10705, title="My Ancestor's Steed", gold_cost=2, focus_value=1, keywords=[Water], traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
'This Shugenja has <b>Shadowlands</b>.<br><b>Maho Limited, :bow::</b> Remove a target token from a Personality and give him a -1C <b>Plague</b> token. Lose 1 Honor.'
Poison_the_Cup = Spell(card_id=10702, title='Poison the Cup', gold_cost=2, focus_value=1, keywords=[Maho], traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
'<b>Fire Interrupt, :bow::</b> Give a Melee or Ranged Attack +2 strength.<br><b>Fire Battle:</b> Ranged 0 Attack.'
Steal_the_Candles_Flame = Spell(card_id=10704, title="Steal the Candle's Flame", gold_cost=0, focus_value=3, traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, EmperorEdition, OnyxEdition, ModernEdition])
'<b>Void Limited, :bow::</b> Turn a card in a Province face-up <i>(if needed)</i> and give it <b>Kharmic</b>. <i>(<b>Repeatable Limited, :g2::</b> Discard a Kharmic card from your Province and refill it face-up.)</i>'
Study_the_Wheel = Spell(card_id=10706, title='Study the Wheel', gold_cost=0, focus_value=2, keywords=[Void], traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
'<b>Battle/Open:</b> Target your Ring in your discard pile or in play. Straighten it or put it in your hand. Destroy this Spell.'
The_Tao_of_Fudo = Spell(card_id=10709, title='The Tao of Fudo', gold_cost=2, focus_value=3, traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
'<b>Thunder Battle:</b> Target a Spell at this battlefield or a Thunder Spell at any location. This Spell copies an ability from the target that does not itself copy abilities <i>(this turn)</i>.'
The_Thunder_Resounds = Spell(card_id=10699, title='The Thunder Resounds', gold_cost=0, focus_value=1, traits=[], abilities=[], legality=[TwentyFestivalsEdition, EmperorEdition, OnyxEdition, ModernEdition])