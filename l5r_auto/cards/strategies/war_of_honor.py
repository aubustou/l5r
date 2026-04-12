from __future__ import annotations
from .common import Strategy
from l5r_auto.keywords import BushidoVirtue, Duty, Kiho, Political, Void
from l5r_auto.legality import CelestialEdition, EmperorEdition, ModernEdition, SamuraiEdition
'<b>Battle:</b> Give your target performing Monk a Force bonus equal to his Chi <i>(until the turn ends)</i>. You may take an additional Battle action.'
A_Warriors_Wisdom = Strategy(card_id=98, title="A Warrior's Wisdom", gold_cost=0, focus_value=4, traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
'<b>Battle:</b> Target an allying Personality: Dishonor him. Move him home. His controller loses 2 Honor.'
Begone_Fool = Strategy(card_id=946, title='Begone, Fool!', gold_cost=0, focus_value=3, keywords=[Political], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
'<b>Battle:</b> Target your performing unbowed Monk to bow a target enemy Personality with equal or lower Chi.'
Chokehold = Strategy(card_id=1336, title='Chokehold', gold_cost=0, focus_value=2, traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
'<b>Battle:</b> In turn order, starting with you, each player targets and moves home one of his Personalities at the current battlefield. Then, gain Honor equal to the number of Personalities this moved.'
Desperate_Mediation = Strategy(card_id=1974, title='Desperate Mediation', gold_cost=0, focus_value=2, keywords=[Political], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
'Before an End Phase begins, if this card is in your discard pile: You may put it in your hand.'
Embracing_Virtue = Strategy(card_id=2313, title='Embracing Virtue', gold_cost=0, focus_value=2, keywords=[BushidoVirtue, Duty], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
"<b>Battle:</b> Dishonor your performing unbowed Personality and target a Personality: Dishonor him. His controller loses 2 Honor. Neither Personality contributes Force in this battle's resolution."
Game_of_Sincerity = Strategy(card_id=2769, title='Game of Sincerity', gold_cost=0, focus_value=2, keywords=[Political], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, SamuraiEdition, ModernEdition])
'<b>Battle:</b> Choose your performing unbowed Samurai and target an allying unit: Move it home. Gain 3 Honor.'
Prideful_Allies = Strategy(card_id=6065, title='Prideful Allies', gold_cost=0, focus_value=2, keywords=[BushidoVirtue], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
'<b>Battle:</b> Choose your performing unbowed Magistrate Personality and target an enemy dishonorable Personality: Reduce his Force to 0 <i>(until the turn ends)</i>. Give your Magistrate a Force bonus equal to the amount of Force the Personality lost <i>(until the turns ends)</i>.'
Shameful_Death = Strategy(card_id=6697, title='Shameful Death', gold_cost=0, focus_value=3, traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
'<b>Battle:</b> In turn order, starting with you, each player targets and moves one of his Personalities at the current battlefield home. Then, choose a player who loses Honor equal to the number of Personalities this moved.'
Shameful_Rebuke = Strategy(card_id=6699, title='Shameful Rebuke', gold_cost=0, focus_value=2, keywords=[Political], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
'<b>Battle/Open:</b> Choose your performing unbowed Monk and target one to three Personalities controlled by other players: Give one of them -1F <i>(until the turn ends)</i>. Give a second different Personality you targeted -2F <i>(until the turn ends)</i>. Give a third different Personality you targeted -3F <i>(until the turn ends)</i>.'
Striking_Through_the_Void = Strategy(card_id=7587, title='Striking Through the Void', gold_cost=0, focus_value=3, keywords=[Kiho, Void], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
"<b>Battle:</b> Bow your performing Personality or Follower: Ranged 2 Attack, with +2 strength if your Personality or your Follower's Personality is a Paragon. Gain 1 Honor."
The_Lions_Charge = Strategy(card_id=8200, title="The Lion's Charge", gold_cost=0, focus_value=2, traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])