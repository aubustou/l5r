from __future__ import annotations
from ..common import Stronghold
from l5r_auto.clans import ScorpionClan
from l5r_auto.keywords import Dojo
from l5r_auto.legality import CelestialEdition, EmperorEdition, ModernEdition
'After another player loses Honor from your Battle action: He loses 1 Honor.<br><b>Battle:</b> Even if this card is bowed, target an enemy Personality: Give him -4F. Bow him if he is dishonorable.'
Law_of_Darkness_Dojo = Stronghold(card_id=4676, title='Law of Darkness Dojo', gold_production='4', starting_family_honor=1, province_strength=7, clan=[ScorpionClan], keywords=[Dojo], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
"When a Lobby action checks Family Honor, your Honor is treated as 20 points higher.<br><b>Political Open:</b> Even if this card is bowed, target another player's Personality: After the next time this turn he is assigned, or an action that he performed ends, dishonor him and his controller loses 1 Honor."
Midday_Shadow_Court = Stronghold(card_id=5037, title='Midday Shadow Court', gold_production='4', starting_family_honor=1, province_strength=7, clan=[ScorpionClan], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
"<b>Political Reaction:</b> Before an action's resolution, choose your performing unbowed Courtier: Reduce any Honor gain or loss from the action's effects by 2.<br><b>Battle:</b> Choose your performing unbowed Personality: Melee 4 Attack, with +1 strength if he is Loyal."
Shiro_Chugo = Stronghold(card_id=7008, title='Shiro Chugo', gold_production='4', starting_family_honor=1, province_strength=7, clan=[ScorpionClan], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
"You do not lose Honor from Ninja cards you own.<br><b>Ninja Open:</b> Look at all face-down cards in one player's provinces.<br><b>Ninja Battle:</b> Choose your performing unbowed Ninja Personality: Ranged 4 Attack. You may move your Ninja home."
The_Otoro_Estate = Stronghold(card_id=8246, title='The Otoro Estate', gold_production='4', starting_family_honor=0, province_strength=7, clan=[ScorpionClan], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])