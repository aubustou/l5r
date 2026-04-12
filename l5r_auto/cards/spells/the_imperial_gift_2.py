from __future__ import annotations
from .common import Spell
from l5r_auto.keywords import Water
from l5r_auto.legality import CelestialEdition, IvoryEdition, ModernEdition, TwentyFestivalsEdition
'<b>Water Battle, :bow::</b> Bow a target enemy card without attachments, or bow this Shugenja to bow a target enemy card with attachments.'
Suitengus_Embrace = Spell(card_id=7620, title="Suitengu's Embrace", gold_cost=0, focus_value=3, keywords=[Water], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, CelestialEdition, ModernEdition])