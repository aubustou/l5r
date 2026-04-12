from __future__ import annotations
from ..common import Personality
from l5r_auto.clans import BrotherhoodOfShinsei, Unaligned
from l5r_auto.keywords import Cavalry, Commander, Courtier, Duelist, Fudo, Gaijin, Gunso, Herald, Imperial, Kensai, Kshatriya, Merchant, Monk, Paragon, Ronin, Samurai, Scout, Settler, Shugenja, Singular, Tactician, Unique, Void
from l5r_auto.legality import CelestialEdition, EmperorEdition, ModernEdition, OnyxEdition, TwentyFestivalsEdition
'<i>(Shugenja may attach and cast Spells.)</i><br>Enomoto has +1F/+2C while he has a Spell.'
Enomoto = Personality(card_id=2348, title='Enomoto', force=3, chi=2, personal_honor=2, gold_cost=5, honor_requirement=6, clan=[Unaligned], keywords=[Ronin, Shugenja, Void], traits=[], abilities=[], legality=[TwentyFestivalsEdition, CelestialEdition, OnyxEdition, ModernEdition])
'Attaches Heart of Fudo ignoring Gold cost.<br><b>Limited:</b> Discard Hyobuko: He searches for an ancient relic. Search your discard pile, then Fate deck, for a card titled Heart of Fudo. Show it and put it in your hand.'
Hyobuko = Personality(card_id=3534, title='Hyobuko', force=4, chi=4, personal_honor=1, gold_cost=6, honor_requirement=None, clan=[Unaligned, BrotherhoodOfShinsei], keywords=[Singular, Fudo, Monk, Shugenja, Void], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
'While Jahan is at the current battlefield, other players may not play Terrains.'
Jahan = Personality(card_id=4039, title='Jahan', force=3, chi=2, personal_honor=2, gold_cost=3, honor_requirement=None, clan=[Unaligned], keywords=[Gaijin, Kshatriya, Scout], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
'After the first time each turn a Political action targets Kamalakar: Negate its effects.<br><b>Battle:</b> Kamalakar confounds the enemy. Move Kamalakar home or to a battlefield with enemy units.'
Kamalakar = Personality(card_id=4253, title='Kamalakar', force=4, chi=4, personal_honor=3, gold_cost=10, honor_requirement=0, clan=[Unaligned], keywords=[Cavalry, Tactician, Unique, Courtier, Gaijin, Kshatriya], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
'<b>Iaijutsu Battle:</b> Target an enemy attachment: Destroy it.'
Masatane = Personality(card_id=4852, title='Masatane', force=4, chi=3, personal_honor=0, gold_cost=5, honor_requirement=None, clan=[Unaligned], keywords=[Duelist, Kensai, Ronin, Samurai], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
'<b>Open:</b> If Masaya is face-up in one of your provinces: Bring him into play, paying all costs and paying 2 less Gold. Before the turn ends, put him on top of your Dynasty deck.'
Masaya = Personality(card_id=4853, title='Masaya', force=3, chi=3, personal_honor=1, gold_cost=6, honor_requirement=0, clan=[Unaligned], keywords=[Ronin, Samurai], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
'<b>Favor Political Limited:</b> Discard the Imperial Favor to draw an additional card during your next End Phase.'
Miya_Masatsuko = Personality(card_id=5198, title='Miya Masatsuko', force=0, chi=3, personal_honor=3, gold_cost=5, honor_requirement=1, clan=[Unaligned], keywords=[Singular, Courtier, Herald, Imperial], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
Tadatsugu = Personality(card_id=7725, title='Tadatsugu', force=5, chi=4, personal_honor=3, gold_cost=7, honor_requirement=0, clan=[Unaligned], keywords=[Cavalry, Kensai, Paragon, Ronin, Samurai], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
'<b>Open:</b> Bow Tashiki and target a Market or Port Holding: Straighten it.'
Tashiki = Personality(card_id=7822, title='Tashiki', force=0, chi=3, personal_honor=1, gold_cost=3, honor_requirement=None, clan=[Unaligned], keywords=[Merchant, Settler], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
'<b>Battle:</b> Target an enemy Follower or Personality without Followers with Force equal to or lower than 4: Destroy it.'
Yotsu_Ueda = Personality(card_id=9680, title='Yotsu Ueda', force=5, chi=3, personal_honor=2, gold_cost=7, honor_requirement=0, clan=[Unaligned], keywords=[Kensai, Commander, Gunso, Samurai], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])