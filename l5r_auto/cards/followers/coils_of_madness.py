from __future__ import annotations
from .common import Follower
from l5r_auto.keywords import Cavalry, DisciplesOfPanKu, Expendable, Fallen, Fudo, Imperial, Monk, Naga, Ninja, Nonhuman, Scout, Unique
from l5r_auto.legality import EmperorEdition, IvoryEdition, ModernEdition
"<b>Battle:</b> Discard the top card of a Fate deck. Give this Follower a Force bonus equal to the card's Focus Value."
Aberrations = Follower(card_id=10516, title='Aberrations', force=0, chi=0, gold_cost=2, focus_value=0, keywords=[DisciplesOfPanKu, Fallen], traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
'<i><i><i><i>(Draw a card after your Expendable card is destroyed.)</i></i></i></i>'
Fudos_Fiends = Follower(card_id=10514, title="Fudo's Fiends", force=2, chi=0, gold_cost=2, focus_value=3, keywords=[Expendable, Fudo, Monk], traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
'Will only attach to a Tactician.'
Lone_Sentry = Follower(card_id=10520, title='Lone Sentry', force=2, chi=0, gold_cost=1, focus_value=4, keywords=[Cavalry], traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
"<b>Battle:</b> Discard the top card of any Fate deck. Melee Attack with strength equal to the card's Focus Value."
Maddened_Horde = Follower(card_id=10518, title='Maddened Horde', force=4, chi=0, gold_cost=8, focus_value=4, keywords=[Unique, Fallen], traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
'<b>Battle:</b> Bow a target enemy attachment.'
Naga_Remnants = Follower(card_id=10513, title='Naga Remnants', force=2, chi=0, gold_cost=2, focus_value=1, keywords=[Naga, Nonhuman], traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
'<b>Engage:</b> You have Reconnaissance at this battlefield. If you are the Attacker, you have the first opportunity to take a Battle action or pass. You may target and give an enemy Personality or Follower -3F.<br>.'
Reconnaissance_Scouts = Follower(card_id=10519, title='Reconnaissance Scouts', force=3, chi=0, gold_cost=4, focus_value=2, keywords=[Scout], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'Will only attach to a Ninja. You may Equip this Follower as a <b>Battle</b> action. <br><b>Battle:</b> Destroy a target enemy card without attachments. Destroy this Follower.'
Shinobi_Vassal = Follower(card_id=10517, title='Shinobi Vassal', force=2, chi=0, gold_cost=2, focus_value=1, keywords=[Ninja], traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
'<b>Battle:</b> Destroy a target enemy card without attachments.<br>'
Thunderous_Legion = Follower(card_id=10515, title='Thunderous Legion', force=4, chi=0, gold_cost=6, focus_value=2, keywords=[Cavalry, Imperial], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])