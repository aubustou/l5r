from __future__ import annotations
from ..common import Stronghold
from l5r_auto.clans import SpiderClan
from l5r_auto.legality import EmperorEdition, ModernEdition
'You do not lose Honor from Spider Clan and Fate cards you own.<br>You may use the rulebook Conquest ability twice per turn during the same battle.<br>Equipping Followers is a Battle/Limited ability for you.'
The_Plain_of_Glass = Stronghold(card_id=8260, title='The Plain of Glass', gold_production='4', starting_family_honor=0, province_strength=7, clan=[SpiderClan], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])