from __future__ import annotations
from .common import Sensei
from l5r_auto.keywords import Crab, Crane, Dragon, Lion, Mantis, Phoenix, Scorpion, Spider, Unicorn
from l5r_auto.legality import IvoryEdition, ModernEdition, TwentyFestivalsEdition
'Your Personalities with 3 or more Chi have <b>Tactician</b>. Unless they have the printed Tactician keyword, they do not have the Tactical Advantage ability.'
Aranai_Sensei = Sensei(card_id=11810, title='Aranai Sensei', gold_production='+0', starting_family_honor=-1, province_strength=-1, keywords=[Crab, Lion, Mantis, Spider, Unicorn], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition])
'<b>Political Dynasty, :bow::</b> Target a non-Unique Courtier in your Province with a Clan Alignment you do not control. Permanently give him your Clan Alignment. Ignore his Honor Requirement <i>(this turn)</i>.'
Suikihime_Sensei = Sensei(card_id=11811, title='Suikihime Sensei', gold_production='-1', starting_family_honor=0, province_strength=0, keywords=[Crane, Dragon, Phoenix, Scorpion], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition])