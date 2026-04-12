from __future__ import annotations
from ..common import Stronghold
from l5r_auto.clans import CraneClan
from l5r_auto.legality import EmperorEdition, ModernEdition
"After an action resolves that created a duel your Personality won during a Combat Segment, once per Personality per battle, negate his next bowing, movement, or destruction from other players' cards' effects."
Twin_Forks_City = Stronghold(card_id=9946, title='Twin Forks City', gold_production='4', starting_family_honor=6, province_strength=6, clan=[CraneClan], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])