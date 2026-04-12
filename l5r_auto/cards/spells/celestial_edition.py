from __future__ import annotations
from .common import Spell
from l5r_auto.keywords import Fire, Maho
from l5r_auto.legality import CelestialEdition, GoldEdition, ImperialEdition, IvoryEdition, JadeEdition, ModernEdition, SamuraiEdition, TwentyFestivalsEdition
'<b>Fire Battle, :bow::</b> Ranged 2 Attack. <i>(Destroy a target enemy Follower, or Personality without Followers, with 2 or lower Force.)</i><br><b>Fire Battle:</b> Bow this Shugenja to make a Ranged 6 Attack. Destroy this Shugenja.'
Fueling_the_Flames = Spell(card_id=2724, title='Fueling the Flames', gold_cost=0, focus_value=1, keywords=[Fire], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, CelestialEdition, ModernEdition])
'<b>Maho Limited:</b> Bow this Shugenja and destroy this Spell to destroy a target bowed Personality with equal or lower Chi.'
Touch_of_Death = Spell(card_id=8692, title='Touch of Death', gold_cost=8, focus_value=4, keywords=[Maho], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, ImperialEdition, CelestialEdition, GoldEdition, JadeEdition, SamuraiEdition, ModernEdition])