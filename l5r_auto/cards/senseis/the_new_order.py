from __future__ import annotations
from .common import Sensei
from l5r_auto.keywords import AllClans, Crab, Crane, Dragon, Lion, Mantis, Phoenix, Scorpion, Spider, Unicorn
from l5r_auto.legality import IvoryEdition, ModernEdition, TwentyFestivalsEdition
'Your maximum hand size is equal to 6 plus the number of Temples you control, to a maximum of 10.<br><b>Battle/Open, :bow::</b> Straighten your target Monk or Shugenja.'
Brotherhood_Sensei = Sensei(card_id=12021, title='Brotherhood Sensei', gold_production='-1', starting_family_honor=0, province_strength=0, keywords=[Dragon, Phoenix, Spider, Unicorn], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition])
'Your Love Letter Personalities in and out of play have your Clan Alignment and you ignore their Honor Requirement. After your Iweko Miaka is destroyed, you lose the game.<br><b>Open, :bow::</b> Name a number and target another player. After each time his <i>(non-Focused)</i> card with that Focus Value is discarded from hand, gain an Affection token.'
Seppun_Tasuke = Sensei(card_id=12020, title='Seppun Tasuke', gold_production='-1', starting_family_honor=0, province_strength=0, keywords=[AllClans], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition])
'<b>Interrupt, :bow::</b> After the action Recruits a Ninja or Scout from a Province, refill it face-up.'
Shika_Sensei = Sensei(card_id=12019, title='Shika Sensei', gold_production='+0', starting_family_honor=-1, province_strength=-1, keywords=[Crab, Crane, Lion, Mantis, Scorpion], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition])