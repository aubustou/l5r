from __future__ import annotations
from ..common import Stronghold
from l5r_auto.clans import MantisClan
from l5r_auto.legality import EmperorEdition, ModernEdition
'<b>Limited:</b> Create an additional Attack Phase, during which battle resolution does not destroy defending armies or Provinces and does not bow your Mantis Clan Magistrates or your attachments. After it ends, if you won any of its battles <i>(even against no units at resolution)</i>, you may target a Personality or Holding, bow it, and negate its straightening until after your next turn begins.'
Aramasus_Legacy = Stronghold(card_id=10184, title="Aramasu's Legacy", gold_production='4', starting_family_honor=2, province_strength=7, clan=[MantisClan], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])