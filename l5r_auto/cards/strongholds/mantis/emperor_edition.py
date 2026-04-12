from __future__ import annotations
from ..common import Stronghold
from l5r_auto.clans import MantisClan
from l5r_auto.keywords import Experienced, Forest, Thunder
from l5r_auto.legality import CelestialEdition, EmperorEdition, ModernEdition
'<b>Recon Reaction:</b> After engaging: You have Reconnaissance at the current battlefield. Until this battle ends, your Ranged Attacks that do not destroy their target have the additional effects, "reduce the target\'s Force by the Ranged Attack\'s strength and you may take an additional Ranged Attack Battle action that may only target the same card".'
Koshin_Keep = Stronghold(card_id=4541, title='Koshin Keep', gold_production='4', starting_family_honor=2, province_strength=7, clan=[MantisClan], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
"<i>Your forests are maddening.</i> Negate the first movement each battle into attacking armies at your provinces' battlefields from other players' actions.<br><b>Limited:</b> Bow your target Forest to gain 1 Honor."
Kyuden_Kitsune_Experienced = Stronghold(card_id=4642, title='Kyuden Kitsune', gold_production='4', starting_family_honor=4, province_strength=7, clan=[MantisClan], keywords=[Experienced('1'), Forest], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
'<b>Reaction:</b> After you announce a Thunder Battle action: Its effects will not be negated or delayed.<br><b>Battle:</b> Choose your performing unbowed Personality and target an enemy Personality: Move him home.'
Suitengus_Torch = Stronghold(card_id=7623, title="Suitengu's Torch", gold_production='4', starting_family_honor=2, province_strength=7, clan=[MantisClan], keywords=[Thunder], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])