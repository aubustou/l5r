from __future__ import annotations
from .common import Spell
from l5r_auto.keywords import Air, Earth, Experienced, Fear, Fire, Maho, Thunder, Void, Water
from l5r_auto.legality import EmperorEdition, IvoryEdition, ModernEdition, TwentyFestivalsEdition
"<b>Earth Limited:</b> Bow this Shugenja to target your Spirit Personality. You may destroy this Spell if your Shugenja is Earth. If you destroyed this Spell, gain Honor equal to the Spirit's Personal Honor; otherwise, gain 1 Honor."
Beseech_Sakkaku = Spell(card_id=9884, title='Beseech Sakkaku', gold_cost=1, focus_value=1, keywords=[Earth], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'While this Shugenja is Shadowlands, your opposed Nonhumans have +1F.<br><b>Maho Open, :bow::</b> Give your target performing Nonhuman the ability, "<b>Battle:</b> Melee Attack with strength equal to this card\'s Force." Lose 3 Honor.'
Channel_the_Moon = Spell(card_id=9885, title='Channel the Moon', gold_cost=2, focus_value=2, keywords=[Maho], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<b>Battle:</b> If this Shugenja is opposed, destroy this card: Create a 2F/2C/3PH <b>Samurai &#149; Ancestor &#149; Spirit</b> Personality with your Clan alignment at the current battlefield. If this Shugenja is Water and defending, create two such Personalities instead.'
Our_Ancestors_Call = Spell(card_id=9886, title="Our Ancestor's Call", gold_cost=0, focus_value=2, keywords=[Water], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'Attaches to an Air Shugenja paying 2 less Gold.<br><b>Reaction:</b> Before an action resolves, bow this card: Negate its effects which give Kolat, Ninja, or Shadowlands to Personalities you control.'
Purify_the_Soul = Spell(card_id=9887, title='Purify the Soul', gold_cost=2, focus_value=4, keywords=[Air], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
"While this Shugenja is Air or Fire, he has +1F.<br><b>Battle:</b> Target a Terrain and destroy this card: Destroy the Terrain.<br><b>Open:</b> Target a Region and destroy this card: The Region's abilities may not be used.<br><b>Limited:</b> Target a Holding and destroy this card: Bow the Holding."
Set_the_Fields_Aflame = Spell(card_id=9888, title='Set the Fields Aflame', gold_cost=0, focus_value=2, keywords=[Air, Fire], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<b>Battle:</b> Bow this Shugenja, or bow this card if he is Earth, and target an enemy card without attachments: Destroy it.'
The_Earths_Hunger = Spell(card_id=9889, title="The Earth's Hunger", gold_cost=1, focus_value=3, keywords=[Earth], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'While this Shugenja is Water, he has +2F.<br><b>Reaction:</b> After engaging, if this Shugenja is not at the current battlefield, target your Personality there: Before this battle resolves, move the target home, and if he moved, move this Shugenja to the current battlefield.'
The_Wave_Persists = Spell(card_id=9890, title='The Wave Persists', gold_cost=2, focus_value=1, keywords=[Water], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'This Shugenja has +3F.<br>While this Shugenja is Thunder, battle resolution will not bow cards in this unit.'
Thunders_Stamina = Spell(card_id=9891, title="Thunder's Stamina", gold_cost=2, focus_value=1, keywords=[Thunder], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
"<b>Void Battle, :bow::</b> Give a target enemy Personality or Follower -2F. If this Shugenja is Void, one ability in the target's unit cannot be used."
Touch_the_Emptiness = Spell(card_id=9892, title='Touch the Emptiness', gold_cost=0, focus_value=3, keywords=[Void], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, EmperorEdition, ModernEdition])
'Before this Shugenja, or any Personality if this Shugenja is Air, is destroyed by a Battle action, you may destroy this Spell to negate it. <br><b>Air Battle:</b> Move this Shugenja home.'
Ward_of_Air = Spell(card_id=9893, title='Ward of Air', gold_cost=0, focus_value=4, keywords=[Air], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, EmperorEdition, ModernEdition])
'After this card enters play, if this Shugenja is Air: Gain 1 Honor.<br><b>Limited:</b> Once per game: Create a +1F/+1C <b>Air &#149; Weapon</b> Item with the ability, "<b>Battle:</b> Give each Personality and Follower in the enemy army -1F" and attach it to one of your Personalities.'
Yari_of_Air_Experienced = Spell(card_id=9894, title='Yari of Air', gold_cost=0, focus_value=3, keywords=[Air, Experienced('1')], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<b>Battle:</b> Target an enemy Personality with lower Chi than this Shugenja: Give the target -4F. If this Shugenja is Air, actions the target performs may not target this Shugenja.'
Your_Hearts_Enemy = Spell(card_id=9895, title="Your Heart's Enemy", gold_cost=0, focus_value=3, keywords=[Air, Fear], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])