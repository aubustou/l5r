from __future__ import annotations
from .common import Spell
from l5r_auto.keywords import Armor, Courage, Earth, Expendable
from l5r_auto.legality import ModernEdition, OnyxEdition, TwentyFestivalsEdition
'<i>(A Personality can only have one Armor.)</i><br>Before this Spell is destroyed, give it Expendable if this Shugenja is Earth.<br>This Shugenja has +3F during the Combat Segment <i>(before battle resolution)</i>.'
Armor_of_the_Emperor = Spell(card_id=12210, title='Armor of the Emperor', gold_cost=0, focus_value=4, keywords=[Armor, Courage, Earth], traits=[], abilities=[], legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition])
"This Shugenja has +2F.<br><b>Earth Jade Battle, :bow::</b> Melee Attack equal to this Shugenja's Chi, +1 if he is Earth, +1 if the target is Shadowlands."
Divide_Into_Ash = Spell(card_id=12211, title='Divide Into Ash', gold_cost=5, focus_value=1, traits=[], abilities=[], legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition])
"<b>Air Interrupt, :bow::</b> You may choose new targets of any of the action's Melee or Ranged Attacks, and if this Shugenja is Air, those targets may be in the army of the player taking the action."
Favor_of_the_Air_Spirits = Spell(card_id=12212, title='Favor of the Air Spirits', gold_cost=2, focus_value=4, traits=[], abilities=[], legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition])
"This Shugenja has +1F, or +2F if he is Water.<br><b>Water Engage, :bow::</b> Negate a target Personality's next movement. After each time his controller resolves an action that targeted him or came from a card in his unit, give him -2F."
Frozen_Tomb = Spell(card_id=12213, title='Frozen Tomb', gold_cost=1, focus_value=2, traits=[], abilities=[], legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition])
'<b>Thunder Battle, :bow::</b> Fear 2 <i>(Bow a target enemy Follower or Personality without Followers with 2 or lower Force)</i>. After this bows the target, give this Personality +1F, or +2F if he is Thunder.'
Heart_Thunder = Spell(card_id=12214, title='Heart Thunder', gold_cost=0, focus_value=3, traits=[], abilities=[], legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition])
"A Holding may only be targeted by one Mark of Heaven's Favor per game.<br><b>Air Open, :bow::</b> Permanently increase a positive numeral on a target Holding by one <i>(2 is a numeral, two is not)</i>. Remove this Spell from the game."
Mark_of_Heavens_Favor = Spell(card_id=12215, title="Mark of Heaven's Favor", gold_cost=0, focus_value=4, traits=[], abilities=[], legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition])
'<b>Water Battle, :bow::</b> Target your Personality, and another of your Personalities at a different location. Switch their locations. Straighten their units as they move.'
Pull_of_the_Tides = Spell(card_id=12216, title='Pull of the Tides', gold_cost=0, focus_value=3, traits=[], abilities=[], legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition])
'You may Equip this Spell from your discard pile to a Void or Magistrate Shugenja.<br><b>Open, :bow::</b> Target a Personality. You suspect him of the taint. He has <b>Shadowlands </b>while you are taking actions <i>(this turn)</i>.'
See_The_Many_Faces = Spell(card_id=12217, title='See The Many Faces', gold_cost=1, focus_value=4, keywords=[Expendable], traits=[], abilities=[], legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition])
'Attaches to a Thunder Shugenja for 1 less Gold.<br><b>Thunder Open, :bow::</b> Give this Shugenja +2F and Conqueror.'
Thunder_Dragons_Child = Spell(card_id=12218, title="Thunder Dragon's Child", gold_cost=4, focus_value=3, traits=[], abilities=[], legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition])
'<b>Thunder Battle, :bow::</b> Ranged 3 Attack. Bow the target if it is still in play and this Shugenja is Thunder. Destroy this Spell.'
Thunderers_Embrace = Spell(card_id=12219, title="Thunderer's Embrace", gold_cost=0, focus_value=3, traits=[], abilities=[], legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition])