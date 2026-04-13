from __future__ import annotations
from ..common import Personality
from l5r_auto.clans import ShadowlandsFaction, Unaligned
from l5r_auto.keywords import Cavalry, Corrupter, Experienced, Gaijin, Nonhuman, Oni, Ronin, Samurai, Sensei, Shadowlands, Shugenja, Unique
from l5r_auto.legality import EmperorEdition, ModernEdition
'After Atosa enters play: Lose 2 Honor and discard all other Sensei Personalities you control.<br>Your Gaijin Personalities in and out of play <i>(including Atosa)</i> have your Clan alignment.'
Atosa = Personality(card_id=9854, title='Atosa', force=2, chi=3, personal_honor=0, gold_cost=6, honor_requirement=None, clan=[Unaligned], keywords=[Gaijin, Sensei], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'After Hitaka enters play: Lose 4 Honor.<br><b>Limited:</b> Target a non-Stronghold Jade card: Destroy it.<br><b>Limited:</b> Destroy Hitaka and target an Oni in your discard pile: Bring it into play, paying 9 less Gold.'
Chuda_Hitaka_Experienced = Personality(card_id=9855, title='Chuda Hitaka', force=4, chi=3, personal_honor=0, gold_cost=7, honor_requirement=None, clan=[Unaligned, ShadowlandsFaction], keywords=[Experienced('Hitaka'), Unique, Corrupter, Shadowlands, Shugenja], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'After Niiro enters play, lose 3 Honor.<br>Will not attach cards.<br><b>Battle:</b> Melee 5 Attack. Give the target a -5F token (if he is still in play).'
Niiro_no_Oni = Personality(card_id=9856, title='Niiro no Oni', force=6, chi=3, personal_honor=0, gold_cost=6, honor_requirement=None, clan=[Unaligned, ShadowlandsFaction], keywords=[Nonhuman, Oni, Shadowlands], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
Sanzoko = Personality(card_id=9858, title='Sanzoko', force=3, chi=2, personal_honor=1, gold_cost=3, honor_requirement=None, clan=[Unaligned], keywords=[Cavalry, Ronin, Samurai], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])