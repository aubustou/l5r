from __future__ import annotations
from ..common import Personality
from l5r_auto.clans import CrabClan
from l5r_auto.keywords import Berserker, Commander, Courtier, Destined, Expendable, Experienced, Fallen, FavoredOfTheCelestialDragon, Merchant, Samurai, Scout, Siege, Tactician, Unique
from l5r_auto.legality import EmperorEdition, IvoryEdition, ModernEdition, OnyxEdition, TwentyFestivalsEdition
'Invest :g4:: Give Gojiro two +1F tokens. <i>(After this card enters play, you may also pay the Invest cost to get the effect, once.)</i><br>After Gojiro enters play, lose 1 Honor.'
Hida_Gojiro = Personality(card_id=10617, title='Hida Gojiro', force=3, chi=3, personal_honor=0, gold_cost=5, honor_requirement=None, clan=[CrabClan], keywords=[Berserker, Fallen], traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
'After the first time each phase Tadama is destroyed, bring him into play in your home, ignoring costs, and bow him.'
Hida_Tadama = Personality(card_id=10618, title='Hida Tadama', force=3, chi=3, personal_honor=2, gold_cost=7, honor_requirement=None, clan=[CrabClan], keywords=[Unique, Berserker, Commander, FavoredOfTheCelestialDragon, Samurai], traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
Kaiu_Sokakaze = Personality(card_id=10619, title='Kaiu Sokakaze', force=0, chi=2, personal_honor=3, gold_cost=4, honor_requirement=6, clan=[CrabClan], keywords=[Tactician, Samurai, Siege], traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
'<b>Battle:</b> Bow a target Spider Clan Personality or, if Chokichi has a Follower, bow a target enemy card without attachments.'
Toritaka_Chokichi_Experienced = Personality(card_id=10620, title='Toritaka Chokichi', force=4, chi=3, personal_honor=2, gold_cost=7, honor_requirement=4, clan=[CrabClan], keywords=[Unique, Experienced('1'), Samurai, Scout], traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
'<i>(Draw a card after you Recruit a Destined card.)</i><br><b>Battle, :bow::</b> Ranged 2 Attack <i>(Destroy a target enemy Follower or Personality without Followers with 2 or lower Force)</i>.'
Toritaka_Iabuchi = Personality(card_id=10621, title='Toritaka Iabuchi', force=3, chi=2, personal_honor=2, gold_cost=7, honor_requirement=3, clan=[CrabClan], keywords=[Destined, Samurai, Scout], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, EmperorEdition, OnyxEdition, ModernEdition])
'<i>(Draw a card after your Expendable card is destroyed.)</i>'
Yasuki_Daisuki = Personality(card_id=10622, title='Yasuki Daisuki', force=0, chi=1, personal_honor=1, gold_cost=2, honor_requirement=None, clan=[CrabClan], keywords=[Expendable, Courtier, Merchant], traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])