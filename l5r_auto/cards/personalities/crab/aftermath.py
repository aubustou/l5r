from __future__ import annotations
from ..common import Personality
from l5r_auto.clans import CrabClan, ShadowlandsFaction
from l5r_auto.keywords import Berserker, Courtier, Destined, Experienced, Hero, Imperial, Kolat, Merchant, Mutant, Nonhuman, Reserve, Samurai, Scout, Shadowlands, Siege, Tactician, Unique
from l5r_auto.legality import EmperorEdition, IvoryEdition, ModernEdition, OnyxEdition, TwentyFestivalsEdition
'Will not attack or defend with other Personalities, and other Personalities will not attack or defend with Kaiji.<br>Kaiji has +2F while unopposed, or +1F for each Personality opposing him with 6 or lower printed Force.'
Hida_Kaiji_Experienced = Personality(card_id=10831, title='Hida Kaiji', force=7, chi=2, personal_honor=0, gold_cost=12, honor_requirement=None, clan=[CrabClan], keywords=[Unique, Berserker, Experienced('1'), Mutant, Nonhuman], traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
'<i>(Draw a card after you Recruit a Destined card. You may Recruit a Reserve Personality, if they would be opposed, as an Absent Battle action.)</i>'
Hida_Kurabi = Personality(card_id=10832, title='Hida Kurabi', force=3, chi=2, personal_honor=0, gold_cost=6, honor_requirement=None, clan=[CrabClan], keywords=[Destined, Reserve, Berserker, Hero, Imperial], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, EmperorEdition, OnyxEdition, ModernEdition])
'Invest :g1:: Create a 0F Follower attach it to Koru. <i>(After this card enters play, you may also pay the Invest cost to get the effect, once.)</i>'
Hiruma_Koru = Personality(card_id=10833, title='Hiruma Koru', force=3, chi=4, personal_honor=1, gold_cost=5, honor_requirement=None, clan=[CrabClan], keywords=[Samurai, Scout], traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
'<b>Battle:</b> Destroy a target enemy attachment.'
Kaiu_Esumi_Experienced = Personality(card_id=10834, title='Kaiu Esumi', force=3, chi=3, personal_honor=2, gold_cost=9, honor_requirement=5, clan=[CrabClan], keywords=[Tactician, Unique, Experienced('1'), Samurai, Siege], traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
"<b>Battle:</b> Discard a card to bow a target enemy card with Force equal to or lower than the discarded card's Focus Value."
Kaiu_Gorobei = Personality(card_id=10835, title='Kaiu Gorobei', force=3, chi=4, personal_honor=3, gold_cost=5, honor_requirement=3, clan=[CrabClan], keywords=[Samurai, Siege], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, EmperorEdition, OnyxEdition, ModernEdition])
'<b>Political Limited, :g3::</b> Dishonor a target Personality.'
Yasuki_Jiro = Personality(card_id=10836, title='Yasuki Jiro', force=1, chi=3, personal_honor=1, gold_cost=5, honor_requirement=None, clan=[CrabClan, ShadowlandsFaction], keywords=[Courtier, Kolat, Merchant, Shadowlands], traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])