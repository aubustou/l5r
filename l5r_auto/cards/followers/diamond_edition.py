from __future__ import annotations
from .common import Follower
from l5r_auto.keywords import Cavalry, Shugenja
from l5r_auto.legality import DiamondEdition, GoldEdition, ImperialEdition, IvoryEdition, JadeEdition, ModernEdition, OnyxEdition, TwentyFestivalsEdition
'<b>Battle:</b> Ranged 2 Attack <i>(Destroy a target enemy Follower or Personality without Followers with 2 or lower Force)</i>.'
Elite_Spearmen = Follower(card_id=2305, title='Elite Spearmen', force=2, chi=0, gold_cost=4, focus_value=3, traits=[], abilities=[], legality=[TwentyFestivalsEdition, GoldEdition, JadeEdition, OnyxEdition, DiamondEdition, ModernEdition])
"<i>(Followers cannot attach or cast Spells.)</i> <br>Attaches to a Phoenix Clan Personality for 1 less Gold. <br><b>Fire Battle, :bow::</b> Ranged Attack with strength equal to this Personality's Chi."
Firestorm_Legion = Follower(card_id=2578, title='Firestorm Legion', force=2, chi=0, gold_cost=6, focus_value=2, keywords=[Shugenja], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, GoldEdition, JadeEdition, DiamondEdition, ModernEdition])
Heavy_Cavalry = Follower(card_id=3040, title='Heavy Cavalry', force=4, chi=0, gold_cost=6, focus_value=2, keywords=[Cavalry], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, ImperialEdition, GoldEdition, JadeEdition, DiamondEdition, ModernEdition])