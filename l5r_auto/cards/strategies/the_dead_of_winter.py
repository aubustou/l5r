from __future__ import annotations
from .common import Strategy
from l5r_auto.keywords import Bushido, Honesty, Virtue
from l5r_auto.legality import CelestialEdition, IvoryEdition, ModernEdition, TwentyFestivalsEdition
'<b>Bushido Virtue Open:</b> Rehonor a target Samurai. <br><b>Bushido Virtue Open:</b> Target your unbowed Samurai. Show a Strategy in your hand. Once this turn, while you are the Defender, you may take a Battle action from that card as an Engage action.'
Open_Emotion = Strategy(card_id=5760, title='Open Emotion', gold_cost=0, focus_value=3, keywords=[Bushido, Honesty, Virtue], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, CelestialEdition, ModernEdition])