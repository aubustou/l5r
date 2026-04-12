from __future__ import annotations
from ..common import Personality
from l5r_auto.clans import LionClan
from l5r_auto.keywords import Artisan, Experienced, HeadLibrarian, Hero, Paragon, Samurai, Scout, Shugenja, Tactician, TurquoiseChampion, Unique, Water
from l5r_auto.legality import CelestialEdition, EmperorEdition, ModernEdition
"<b>Reaction:</b> After another player's action targets Kakihara, give him a Force bonus equal to his Personal Honor."
Akodo_Kakihara = Personality(card_id=223, title='Akodo Kakihara', force=4, chi=3, personal_honor=4, gold_cost=7, honor_requirement=7, clan=[LionClan], keywords=[Paragon, Samurai], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
'<b>Tactical Open, :bow::</b> Give a target Personality +4F. You may discard a card to ignore the cost of bowing Kamina.'
Akodo_Kamina = Personality(card_id=224, title='Akodo Kamina', force=3, chi=4, personal_honor=3, gold_cost=7, honor_requirement=7, clan=[LionClan], keywords=[Tactician, Samurai], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
'Sugo has +4F while attacking.'
Ikoma_Sugo = Personality(card_id=3641, title='Ikoma Sugo', force=4, chi=3, personal_honor=2, gold_cost=8, honor_requirement=0, clan=[LionClan], keywords=[Hero, Samurai, Scout], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
'<b>Limited:</b> Create a 2F/2C/3PH <b>Lion Clan &#149; Samurai &#149; Ancestor &#149; Spirit</b> Personality.<br><b>Battle:</b> Bow your performing Ancestor Personality and target an enemy card without attachments: Destroy it. Gain 1 Honor.'
Kitsu_Akai = Personality(card_id=4371, title='Kitsu Akai', force=3, chi=4, personal_honor=4, gold_cost=10, honor_requirement=7, clan=[LionClan], keywords=[Shugenja, Water], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
'<b>Battle:</b> Bow or destroy your performing Ancestor Personality, and target an enemy card: Bow it. Gain 1 Honor.'
Kitsu_Fukui = Personality(card_id=4375, title='Kitsu Fukui', force=0, chi=3, personal_honor=3, gold_cost=5, honor_requirement=0, clan=[LionClan], keywords=[HeadLibrarian, Shugenja, Water], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
'Kasei has +2F while attacking.<br><b>Battle:</b> Target a defending Personality: Move him home.'
Matsu_Kasei_Experienced = Personality(card_id=4937, title='Matsu Kasei', force=4, chi=4, personal_honor=3, gold_cost=8, honor_requirement=6, clan=[LionClan], keywords=[Unique, Artisan, Experienced('1'), Samurai, TurquoiseChampion], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])