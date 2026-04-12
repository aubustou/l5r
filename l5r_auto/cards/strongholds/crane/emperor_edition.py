from __future__ import annotations
from ..common import Stronghold
from l5r_auto.clans import CraneClan
from l5r_auto.keywords import Dojo, Experienced, Imperial, Temple
from l5r_auto.legality import EmperorEdition, ModernEdition
"<b>Recon Open:</b> Target one or two Provinces. You have Reconnaissance at their battlefields. After each Maneuvers Segment <i>(this turn)</i> there is an additional Maneuvers Segment in which only your Scout Personalities may be assigned and only to the targeted Provinces' battlefields."
Hidden_Falls_Dojo = Stronghold(card_id=3257, title='Hidden Falls Dojo', gold_production='4', starting_family_honor=5, province_strength=7, clan=[CraneClan], keywords=[Dojo], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'You may substitute discarding a Favor token from this card for discarding the Imperial Favor as a cost.<br>After you take the Imperial Favor: You may discard it; if you did, add a <b>Favor</b> token to this card.<br><b>Political Open:</b> Bow your performing honorable Courtier: Add a <b>Favor</b> token to this card.'
Kyuden_Otomo_Experienced = Stronghold(card_id=4646, title='Kyuden Otomo', gold_production='4', starting_family_honor=6, province_strength=6, clan=[CraneClan], keywords=[Experienced('1'), Imperial], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
"<b>Open:</b> Even if this card is bowed, bow your performing Shugenja and target another player's unbowed Personality: His controller may choose to bow him and negate his straightening <i>(this turn)</i>. If he did not choose this, gain 1 Honor."
Shinden_Asahina = Stronghold(card_id=6855, title='Shinden Asahina', gold_production='4', starting_family_honor=6, province_strength=6, clan=[CraneClan], keywords=[Temple], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
"<b>Iaijutsu Battle:</b> Even if this card is bowed, choose your performing unbowed Samurai and target another player's Personality: Your Samurai duels the Personality. Bow and dishonor the duel's loser. The winner's controller gains 1 Honor."
The_Aerie = Stronghold(card_id=7949, title='The Aerie', gold_production='4', starting_family_honor=6, province_strength=6, clan=[CraneClan], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])