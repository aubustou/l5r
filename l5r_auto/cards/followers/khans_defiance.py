from __future__ import annotations
from .common import Follower
from l5r_auto.keywords import Ronin
from l5r_auto.legality import EmperorEdition, IvoryEdition, LotusEdition, ModernEdition, SamuraiEdition, TwentyFestivalsEdition
'Before this Personality enters a duel to which he was challenged, create a 2F/3C/2PH <b>Samurai &#149; Yojimbo &#149; Duelist</b> Personality at his location, who enters the duel instead. After the duel ends, remove him from the game, and destroy this Follower if you lost.'
Watch_Commander = Follower(card_id=9245, title='Watch Commander', force=2, chi=0, gold_cost=3, focus_value=4, traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, LotusEdition, SamuraiEdition, ModernEdition])
'Will only attach to a Samurai. <br>After an Attack Phase ends: Straighten this unit.'
Wave_Man = Follower(card_id=9255, title='Wave Man', force=2, chi=0, personal_honor=0, gold_cost=4, focus_value=1, honor_requirement=0, keywords=[Ronin], traits=[], abilities=[], legality=[EmperorEdition, LotusEdition, SamuraiEdition, ModernEdition])