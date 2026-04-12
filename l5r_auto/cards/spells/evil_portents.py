from __future__ import annotations
from .common import Spell
from l5r_auto.keywords import Courage, Expendable, Honor, Resilient
from l5r_auto.legality import ModernEdition, OnyxEdition, TwentyFestivalsEdition
"<b>Fire Battle, :bow::</b> You may target your Samurai. Ranged Attack equal to this Shugenja's Chi or the Samurai's Chi, +2 if this Shugenja is Fire <i>(Destroy a target enemy Follower or Personality without Followers with Force equal to or lower than the Ranged Attack's strength)</i>."
Calling_on_the_Sun = Spell(card_id=12522, title='Calling on the Sun', gold_cost=3, focus_value=1, traits=[], abilities=[], legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition])
"<i>(Repeatable Interrupt: Discard an Honor card to give an Honor gain or loss +1 or -1.)</i><br><b>Air Open, :bow::</b> Bow this Shugenja to give a target Personality a Force penalty equal to this Shugenja's Chi. Gain 1 Honor if this Shugenja is Air."
Compassions_Invocation = Spell(card_id=12523, title="Compassion's Invocation", gold_cost=3, focus_value=3, keywords=[Honor], traits=[], abilities=[], legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition])
"<b>Earth Interrupt, :bow::</b> If the action is another player's, negate this caster's movement from it.<br><b>Earth Battle, :bow::</b> If this Shugenja is Earth and opposed, give him +1F for each Earth card in this unit."
Earths_Inevitability = Spell(card_id=12524, title="Earth's Inevitability", gold_cost=0, focus_value=3, traits=[], abilities=[], legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition])
"<i>(Repeatable Interrupt: Discard an Honor card to give an Honor gain or loss +1 or -1.)</i> <br><b>Earth Battle, :bow::</b> Raise or lower the current Province's strength by the number of Earth Followers or Spells <i>(your choice)</i> in this unit, plus 2 if this Shugenja is Earth and opposed."
Eternally_Unyielding = Spell(card_id=12525, title='Eternally Unyielding', gold_cost=3, focus_value=4, keywords=[Honor], traits=[], abilities=[], legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition])
'<i>(Draw a card after your Expendable card is destroyed. Once per game per card, a Resilient card does not die in battle resolution.)</i><br>This Shugenja has Resilient while they are Water.<br><b>Water Battle, :bow::</b> Fear 3.'
Inazumas_Caress = Spell(card_id=12526, title="Inazuma's Caress", gold_cost=0, focus_value=1, keywords=[Expendable, Resilient], traits=[], abilities=[], legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition])
'<b>Thunder Battle, :bow::</b> Fear 4 that may, if this caster is Thunder, target a Personality with Followers <i>(Bow a target enemy Follower or Personality without Followers with 4 or lower Force)</i>.'
Primal_Tempest = Spell(card_id=12527, title='Primal Tempest', gold_cost=0, focus_value=3, traits=[], abilities=[], legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition])
'<b>Maho Repeatable Open, :g*::</b> Bow this Shugenja and destroy your target Human Personality to search your Dynasty discard pile, then deck, for an Oni Personality and Recruit it. Lose 3 Honor. <i>(Repeatable actions may be taken any number of times per turn.)</i>'
Ritual_of_Naming = Spell(card_id=12528, title='Ritual of Naming', gold_cost=3, focus_value=1, traits=[], abilities=[], legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition])
'<b>Void Battle/Engage, :bow::</b> Give your target Personality +3F. If this Shugenja is Void, abilities on the target may be used a second time this turn.'
The_Tapestrys_Flowing_Pattern = Spell(card_id=12529, title="The Tapestry's Flowing Pattern", gold_cost=3, focus_value=3, traits=[], abilities=[], legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition])
'You may Equip this Spell from your discard pile, bowed, to an Air Shugenja if you control a Library or Temple Holding.<br><b>Air Open, :bow::</b> Bow this Shugenja to gain 1 Honor. Destroy this Spell.'
The_Winds_Clarity = Spell(card_id=12530, title="The Wind's Clarity", gold_cost=0, focus_value=0, keywords=[Honor], traits=[], abilities=[], legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition])
'<b>Open, :bow::</b> Give your target Personality Expendable. <i>(Draw a card after your Expendable card dies.)</i>'
The_Worlds_Essence = Spell(card_id=12531, title="The World's Essence", gold_cost=0, focus_value=3, traits=[], abilities=[], legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition])
'<i>(Repeatable Interrupt: Discard a Courage card to give a Fear effect +2 or -2 strength.)</i><br><b>Thunder Battle, :bow::</b> Ranged 2 Attack. Then, if this Shugenja is Thunder, Fear 2. Neither of these effects may be combined.'
Thunders_Resplendent_Gift = Spell(card_id=12532, title="Thunder's Resplendent Gift", gold_cost=1, focus_value=2, keywords=[Courage], traits=[], abilities=[], legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition])
'This action has Home while this Shugenja is Water. <i>(Home actions may be taken from home.)</i><br><b>Water Battle, :bow::</b> Move a target Personality to an adjacent, unresolved battlefield.'
Wrath_of_Suitengu = Spell(card_id=12533, title='Wrath of Suitengu', gold_cost=0, focus_value=3, traits=[], abilities=[], legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition])