from __future__ import annotations
from .common import Spell
from l5r_auto.keywords import Air, Earth, Fire, Forest, Kami, Maho, Ritual, Thunder, Unique, Void, Water
from l5r_auto.legality import CelestialEdition, DiamondEdition, EmperorEdition, GoldEdition, ImperialEdition, IvoryEdition, JadeEdition, LotusEdition, ModernEdition, OnyxEdition, SamuraiEdition, TwentyFestivalsEdition
'<b>Ritual Limited:</b> Bow this Shugenja and 0 or more of your other target performing Shugenja and remove this card from the game to target a Personality. If the total Chi of all your performing Shugenja is higher than three times the Chi of the Personality, remove him <i>(and his attachments)</i> from the game.'
Capturing_the_Soul = Spell(card_id=1216, title='Capturing the Soul', gold_cost=2, focus_value=1, keywords=[Ritual], traits=[], abilities=[], legality=[EmperorEdition, JadeEdition, ModernEdition])
"<b>Earth Forest Open:</b> Target one or two of your performing unbowed Nonhuman Spirit Personalities, bow this Shugenja, and destroy this Spell to target another player's unbowed Personality and create a battlefield. Negate all movement to it. Assign the other player's Personality to attack there; he will not be destroyed during the battle's Combat Segment. Assign the performing Spirits to defend there. Fight a battle there."
Chikushudos_Trickery = Spell(card_id=1323, title="Chikushudo's Trickery", gold_cost=0, focus_value=2, keywords=[Earth, Forest], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<b>Battle:</b> Destroy this card: Ranged 4 Attack, or Ranged 5 Attack if the performing Shugenja is Fire.'
Cleansing_the_Path = Spell(card_id=1416, title='Cleansing the Path', gold_cost=0, focus_value=3, keywords=[Fire], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
'If this Shugenja is Fire, Ranged Attacks from actions in this unit have +1 strength.<br><b>Fire Battle, :bow::</b> Give this Shugenja +3F.'
Conflagration = Spell(card_id=1449, title='Conflagration', gold_cost=2, focus_value=2, traits=[], abilities=[], legality=[TwentyFestivalsEdition, EmperorEdition, OnyxEdition, ModernEdition])
"<b>Open:</b> Bow this card: Choose one or two of your provinces. After the first time this turn a Personality assigns or moves to an attacking army at one of those provinces' battlefields, gain 2 Honor."
Consecration = Spell(card_id=1458, title='Consecration', gold_cost=2, focus_value=3, keywords=[Earth], traits=[], abilities=[], legality=[EmperorEdition, SamuraiEdition, ModernEdition])
'<b>Limited:</b> Bow this Shugenja, destroy this card, and discard your hand <i>(even if empty)</i>: Draw four cards.'
Contemplate_the_Void = Spell(card_id=1471, title='Contemplate the Void', gold_cost=6, focus_value=4, keywords=[Void], traits=[], abilities=[], legality=[EmperorEdition, ImperialEdition, DiamondEdition, ModernEdition])
'<b>Political Limited:</b> Bow this Shugenja and destroy this card: Gain 4 Honor.'
Hanabi = Spell(card_id=2954, title='Hanabi', gold_cost=7, focus_value=2, keywords=[Unique], traits=[], abilities=[], legality=[EmperorEdition, GoldEdition, ModernEdition])
"<b>Limited:</b> Bow this Shugenja and destroy your target Human Personality: Search your Dynasty deck or discard pile for a non-Unique Oni with Gold Cost lower than or equal to the Human's Gold Cost plus the performer's Chi. Put the Oni into play, ignoring Gold cost. Lose 2 Honor."
I_Give_You_My_Name = Spell(card_id=3541, title='I Give You My Name', gold_cost=3, focus_value=3, keywords=[Maho], traits=[], abilities=[], legality=[EmperorEdition, GoldEdition, DiamondEdition, ModernEdition])
"While this Shugenja is Earth, this card's Battle ability may be used even if this unit is not at the current battlefield.<br><b>Battle:</b> Bow this Shugenja if he is home, bow this card and target an attacking Personality: Move him home."
Obscured_Pathways = Spell(card_id=5649, title='Obscured Pathways', gold_cost=0, focus_value=3, keywords=[Earth, Forest], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'This Personality has +2F. <br><b>Battle:</b> Bow this card and target a defending Personality: Move him home.'
Scouring_Flood = Spell(card_id=6502, title='Scouring Flood', gold_cost=2, focus_value=3, keywords=[Water], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, SamuraiEdition, ModernEdition])
'<b>Air Battle:</b> Bow this Shugenja to move home a target attacking Personality and himself, and gain 2 Honor.'
Seeking_the_Way = Spell(card_id=6567, title='Seeking the Way', gold_cost=2, focus_value=4, keywords=[Air], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, EmperorEdition, LotusEdition, SamuraiEdition, ModernEdition])
'<b>Limited:</b> Bow this Shugenja and target your Personality: Create a 1F <b>Shadowlands &#149; Nonhuman &#149; Spirit &#149; Swamp</b> Spirit Follower and attach it to him.'
Summon_Swamp_Spirits = Spell(card_id=7633, title='Summon Swamp Spirits', gold_cost=2, focus_value=3, keywords=[Maho], traits=[], abilities=[], legality=[EmperorEdition, ImperialEdition, ModernEdition])
"<b>Battle/Open:</b> Bow this card: Raise this Shugenja's Force by his Chi.<br><b>Battle:</b> Bow this card and target one or two Samurai: Raise each target's Force by this Shugenja's Chi."
The_Kamis_Blessing = Spell(card_id=8175, title="The Kami's Blessing", gold_cost=3, focus_value=3, keywords=[Kami], traits=[], abilities=[], legality=[EmperorEdition, LotusEdition, SamuraiEdition, ModernEdition])
'<b>Battle:</b> Bow this card: Ranged 4 Attack, or Ranged 6 Attack if this Shugenja is Thunder.'
Thunders_Favor = Spell(card_id=8473, title="Thunder's Favor", gold_cost=3, focus_value=2, keywords=[Thunder], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, SamuraiEdition, ModernEdition])
'<b>Battle:</b> Bow this Shugenja and target an enemy Personality: Move him home; if this Shugenja is Water, this movement will not be negated. If the target moved, bow him and negate his <i>(future)</i> movement.'
Unnatural_Flood = Spell(card_id=8997, title='Unnatural Flood', gold_cost=0, focus_value=4, keywords=[Unique, Water], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
'<b>Limited:</b> Bow this Shugenja and destroy this Spell to search your Fate deck for a card and put it in your hand.'
Walking_the_Way = Spell(card_id=9196, title='Walking the Way', gold_cost=4, focus_value=3, traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, EmperorEdition, LotusEdition, ImperialEdition, CelestialEdition, GoldEdition, JadeEdition, SamuraiEdition, DiamondEdition, ModernEdition])
'While this Shugenja is defending, he has +3F.<br>While this Shugenja is Earth and you are the Defender, you decide the order in which battles resolve.'
Warded_Paths = Spell(card_id=9228, title='Warded Paths', gold_cost=0, focus_value=2, keywords=[Earth], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])