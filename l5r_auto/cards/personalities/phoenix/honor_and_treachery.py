from __future__ import annotations
from ..common import Personality
from l5r_auto.clans import PhoenixClan
from l5r_auto.keywords import ClanChampion, Commander, Daimyo, Duelist, Earth, Experienced, Fire, FirestormLegion, Loyal, Samurai, ShibasSoul, Shugenja, SoulOf, Stalwart, Unique, Yojimbo
from l5r_auto.legality import EmperorEdition, ModernEdition, OnyxEdition, TwentyFestivalsEdition
'<i>(Shugenja may attach and cast Spells.)</i><br>Nairuko has +2F while she has a Spell.'
Isawa_Nairuko = Personality(card_id=10242, title='Isawa Nairuko', force=2, chi=3, personal_honor=3, gold_cost=6, honor_requirement=2, clan=[PhoenixClan], keywords=[Earth, Shugenja, SoulOf('Isawa Mariko')], traits=[], abilities=[], legality=[TwentyFestivalsEdition, EmperorEdition, OnyxEdition, ModernEdition])
'<b>Battle:</b> Bow Taiken: Ranged 4 Attack.'
Isawa_Taiken = Personality(card_id=10243, title='Isawa Taiken', force=3, chi=3, personal_honor=3, gold_cost=7, honor_requirement=4, clan=[PhoenixClan], keywords=[Duelist, Fire, FirestormLegion, Shugenja, SoulOf('Isawa Kokuten')], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
"<i>(Stalwart cards negate their first bowing each turn by other players' cards.)</i>"
Shiba_Jikaro = Personality(card_id=10244, title='Shiba Jikaro', force=3, chi=3, personal_honor=3, gold_cost=6, honor_requirement=6, clan=[PhoenixClan], keywords=[Stalwart, Samurai, Yojimbo], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
"<b>Battle:</b> Target your Personality: Move him to Mitsushen's battlefield. If he moved, straighten his unit."
Shiba_Mitsushen = Personality(card_id=10245, title='Shiba Mitsushen', force=5, chi=4, personal_honor=3, gold_cost=9, honor_requirement=4, clan=[PhoenixClan], keywords=[Unique, Commander, Samurai], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<b>Battle:</b> Twice per turn, target a card in a unit: Straighten it. It may use its abilities a second time this turn.'
Shiba_Tsukimi_Experienced_35 = Personality(card_id=10246, title='Shiba Tsukimi', force=6, chi=5, personal_honor=4, gold_cost=10, honor_requirement=6, clan=[PhoenixClan], keywords=[Duelist, Experienced('3.5'), Loyal, Unique, ClanChampion, Daimyo, Samurai, ShibasSoul], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])