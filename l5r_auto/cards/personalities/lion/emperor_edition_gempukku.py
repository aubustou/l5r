from __future__ import annotations
from ..common import Personality
from l5r_auto.clans import LionClan
from l5r_auto.keywords import Experienced, Legendary, Lion, Nonhuman, Scout, Unique
from l5r_auto.legality import EmperorEdition, ModernEdition
"<b>Recon Reaction:</b> After engaging at Jade's Roar's battlefield: You have <b>Reconnaissance </b>there. You have the first opportunity to take a Battle action in this battle, which must be a Terrain action."
Jades_Roar_Experienced = Personality(card_id=10223, title="Jade's Roar", force=4, chi=2, personal_honor=0, gold_cost=7, honor_requirement=None, clan=[LionClan], keywords=[Experienced('Pride of the Hand'), Unique, Legendary, Lion, Nonhuman, Scout], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])