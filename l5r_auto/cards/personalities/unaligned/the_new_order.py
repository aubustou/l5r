from __future__ import annotations
from dataclasses import dataclass
from l5r_auto.card import Ability, Trait
from l5r_auto.cards.personalities.common import Personality
from l5r_auto.clans import BrotherhoodOfShinsei, RatlingFaction, ShadowlandsFaction, Unaligned
from l5r_auto.keywords import Courtier, Experienced, Goblin, Heir, Imperial, Ishiken, Kolat, LoveLetter, MasterCoin, Merchant, Monk, Nonhuman, Ogre, OneTribe, Ratling, Resilient, Ronin, Scavenger, Scout, Shadowlands, Shugenja, Sinner, Unique, Void, Yojimbo
from l5r_auto.legality import IvoryEdition, ModernEdition, TwentyFestivalsEdition
Banished = Personality(id=11932, title='Banished', force=3, chi=3, honor_requirement=None, personal_honor=1, gold_cost=5, clan=[Unaligned], keywords=[Resilient, Ishiken, Ronin, Shugenja, Void], traits=[], abilities=[], legality=[ModernEdition, IvoryEdition, TwentyFestivalsEdition])
Brnn_Experienced = Personality(id=11933, title="Br'nn", force=2, chi=2, honor_requirement=None, personal_honor=1, gold_cost=4, clan=[Unaligned, RatlingFaction], keywords=[Experienced('1'), Nonhuman, OneTribe, Ratling, Scavenger, Scout], traits=[], abilities=[], legality=[ModernEdition, IvoryEdition, TwentyFestivalsEdition])
Iweko_Miaka_the_Princess = Personality(id=11934, title='Iweko Miaka, the Princess', force=0, chi=5, honor_requirement=12, personal_honor=4, gold_cost=6, clan=[Unaligned], keywords=[Unique, Heir, Imperial, LoveLetter], traits=[], abilities=[], legality=[ModernEdition, IvoryEdition, TwentyFestivalsEdition])
Keppo_Experienced = Personality(id=11936, title='Keppo', force=4, chi=2, honor_requirement=None, personal_honor=0, gold_cost=6, clan=[Unaligned, ShadowlandsFaction], keywords=[Experienced('1'), Goblin, Nonhuman, Scout, Shadowlands], traits=[], abilities=[], legality=[ModernEdition, IvoryEdition, TwentyFestivalsEdition])
Masajiro = Personality(id=11935, title='Masajiro', force=5, chi=2, honor_requirement=None, personal_honor=0, gold_cost=9, clan=[Unaligned, ShadowlandsFaction], keywords=[Nonhuman, Ogre, Shadowlands, Sinner, Yojimbo], traits=[], abilities=[], legality=[ModernEdition, IvoryEdition, TwentyFestivalsEdition])
The_Abbot_Experienced_3 = Personality(id=11937, title='The Abbot', force=2, chi=4, honor_requirement=None, personal_honor=1, gold_cost=7, clan=[Unaligned, BrotherhoodOfShinsei], keywords=[Experienced('3 Yasuki Jinn-Kuen'), Unique, Courtier, Kolat, MasterCoin, Merchant, Monk], traits=[], abilities=[], legality=[ModernEdition, IvoryEdition, TwentyFestivalsEdition])