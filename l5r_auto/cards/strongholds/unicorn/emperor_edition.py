from __future__ import annotations
from ..common import Stronghold
from l5r_auto.clans import UnicornClan
from l5r_auto.keywords import Experienced, Temple
from l5r_auto.legality import EmperorEdition, ModernEdition
'<b>Battle:</b> Target your performing unbowed Personality to move home a target Personality with as many or fewer Followers attached; this will not be negated or delayed.'
Journeys_End_Keep = Stronghold(card_id=4059, title="Journey's End Keep", gold_production='5', starting_family_honor=4, province_strength=7, clan=[UnicornClan], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'After you destroy a province or army in battle resolution as the Attacker: Gain Honor equal to the number of your Battle Maidens at the current battlefield.'
Plains_of_the_Maiden = Stronghold(card_id=5982, title='Plains of the Maiden', gold_production='5', starting_family_honor=5, province_strength=7, clan=[UnicornClan], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<b>Tactical Limited:</b> Choose your performing Tactician: He may not be assigned to attack this turn. Draw a card.'
The_Khans_Estate = Stronghold(card_id=8182, title="The Khan's Estate", gold_production='5', starting_family_honor=4, province_strength=7, clan=[UnicornClan], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<b>Limited:</b> Target a discarded Personality: He becomes honorably dead.<br><b>Battle/Open:</b> If you own a dead Personality, choose your performing unbowed Shugenja and target a Personality: Straighten him. You may bow him if this is the Combat Segment.'
The_Temple_of_Death_Experienced = Stronghold(card_id=8373, title='The Temple of Death', gold_production='5', starting_family_honor=4, province_strength=7, clan=[UnicornClan], keywords=[Experienced('1'), Temple], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])