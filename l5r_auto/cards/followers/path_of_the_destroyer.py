from __future__ import annotations
from .common import Follower
from l5r_auto.keywords import Expendable, Spirit
from l5r_auto.legality import CelestialEdition, IvoryEdition, ModernEdition, TwentyFestivalsEdition
'<i>(Draw a card after your Expendable card dies.)</i><br><b>Tireless Battle:</b> Destroy this Follower <i>(Tireless actions can be taken even while bowed)</i>.'
Legion_of_Toshigoku = Follower(card_id=4703, title='Legion of Toshigoku', force=3, chi=0, gold_cost=4, focus_value=1, keywords=[Expendable, Spirit], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, CelestialEdition, ModernEdition])