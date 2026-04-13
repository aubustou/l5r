from __future__ import annotations
from ..common import Personality
from l5r_auto.clans import LionClan
from l5r_auto.keywords import Cavalry, Daimyo, Elite, Experienced, Imperial, Loyal, Paragon, Samurai, Scout, Sensei, Shugenja, SodanSenzo, Tactician, Unique, Water
from l5r_auto.legality import EmperorEdition, IvoryEdition, ModernEdition, TwentyFestivalsEdition
'After Tamisu enters play: Discard all your other Sensei Personalities.<br>After your Tactical, Bushido Virtue, or Terrain action resolves: Give a Lion Clan Personality +1F.'
Akodo_Tamisu = Personality(card_id=294, title='Akodo Tamisu', force=4, chi=3, personal_honor=2, gold_cost=7, honor_requirement=6, clan=[LionClan], keywords=[Loyal, Tactician, Samurai, Sensei], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'Uehara has +1F while he opposes a Phoenix Clan Personality.<br><b>Limited:</b> Look at the top card of your Fate deck. You may leave it there, discard it, or put it at the bottom of the deck.'
Akodo_Uehara = Personality(card_id=305, title='Akodo Uehara', force=1, chi=3, personal_honor=2, gold_cost=5, honor_requirement=6, clan=[LionClan], keywords=[Tactician, Samurai], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<b>Battle:</b> Target another Personality: Move him home or give him a Force bonus equal to his Personal Honor.'
Ikoma_Hakige = Personality(card_id=3607, title='Ikoma Hakige', force=4, chi=4, personal_honor=4, gold_cost=8, honor_requirement=12, clan=[LionClan], keywords=[Cavalry, Loyal, Unique, Daimyo, Paragon, Samurai], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<b>Battle:</b> You may discard a card: Ranged 4 Attack, with +2 strength if you discarded a card; if that card was a Terrain, draw a card.'
Ikoma_Shika_Experienced = Personality(card_id=3637, title='Ikoma Shika', force=5, chi=3, personal_honor=2, gold_cost=8, honor_requirement=4, clan=[LionClan], keywords=[Unique, Experienced('1'), Samurai, Scout], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
Ikoma_Sido = Personality(card_id=3640, title='Ikoma Sido', force=4, chi=3, personal_honor=3, gold_cost=6, honor_requirement=7, clan=[LionClan], keywords=[Paragon, Samurai], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'While you control a Terrain, your Ranged Attacks have +1 strength.<br><b>Battle:</b> Ranged 4 Attack.'
Ikoma_Yamahatsu = Personality(card_id=3660, title='Ikoma Yamahatsu', force=4, chi=3, personal_honor=2, gold_cost=7, honor_requirement=4, clan=[LionClan], keywords=[Elite, Imperial, Samurai, Scout], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<b>Home Battle, :bow::</b> Create a 2F/2C/3PH Lion <b>Clan &#149; Ancestor &#149; Samurai &#149; Spirit</b> Personality at the current battlefield. Remove him from the game after the battle ends. <i>(Home actions can be taken from home.)</i>'
Kitsu_Miro = Personality(card_id=4386, title='Kitsu Miro', force=3, chi=3, personal_honor=3, gold_cost=5, honor_requirement=6, clan=[LionClan], keywords=[Shugenja, SodanSenzo, Water], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, EmperorEdition, ModernEdition])