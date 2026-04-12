from __future__ import annotations
from ..common import Personality
from l5r_auto.clans import BrotherhoodOfShinsei, NagaFaction, ShadowlandsFaction, Unaligned
from l5r_auto.keywords import Actor, Banker, Cavalry, Courtier, Imperial, ImperialBankOfRokugan, Monk, Mountaineer, Naga, Nonhuman, Oni, Ronin, Samurai, Scout, Shadowlands, Shugenja, SoulOf, Unique
from l5r_auto.legality import CelestialEdition, DiamondEdition, EmperorEdition, ImperialEdition, IvoryEdition, JadeEdition, ModernEdition, SamuraiEdition, TwentyFestivalsEdition
'After Niiro enters play: Lose 2 Honor.'
Chuda_Niiro = Personality(card_id=1363, title='Chuda Niiro', force=4, chi=3, personal_honor=0, gold_cost=4, honor_requirement=None, clan=[Unaligned, ShadowlandsFaction], keywords=[Shadowlands, Shugenja], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'After Ekichu enters play: Lose 8 Honor.<br><b>Battle:</b> Target an enemy card: Bow it.<br><b>Battle:</b> Target an enemy card without attachments: Destroy it.<br><b>Battle:</b> Target an enemy Personality: Move him home.'
Ekichu_no_Oni = Personality(card_id=2286, title='Ekichu no Oni', force=10, chi=4, personal_honor=0, gold_cost=12, honor_requirement=None, clan=[Unaligned, ShadowlandsFaction], keywords=[Unique, Nonhuman, Oni, Shadowlands], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
'<b>Open:</b> Target your Personality: Genmyo copies one of his keywords.'
Genmyo = Personality(card_id=2793, title='Genmyo', force=3, chi=2, personal_honor=1, gold_cost=4, honor_requirement=None, clan=[Unaligned], keywords=[Actor, Ronin, SoulOf('Kyogen')], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'After Nosloc enters play, lose 4 Honor.'
Nosloc_no_Oni = Personality(card_id=5626, title='Nosloc no Oni', force=6, chi=4, personal_honor=0, gold_cost=6, honor_requirement=None, clan=[Unaligned, ShadowlandsFaction], keywords=[Cavalry, Nonhuman, Oni, Shadowlands], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, SamuraiEdition, ModernEdition])
'<b>Political Interrupt:</b> After you Recruit Demiyah, a target player gains or loses 1 Honor.'
Otomo_Demiyah = Personality(card_id=5812, title='Otomo Demiyah', force=2, chi=3, personal_honor=2, gold_cost=4, honor_requirement=None, clan=[Unaligned], keywords=[Courtier, Imperial], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, EmperorEdition, ModernEdition])
"<b>Recon Reaction:</b> After engaging at Qalyar's battlefield: You have Reconnaissance there. Give its province +2 or -2 strength."
Qalyar = Personality(card_id=6117, title='Qalyar', force=2, chi=3, personal_honor=2, gold_cost=3, honor_requirement=None, clan=[Unaligned, NagaFaction], keywords=[Mountaineer, Naga, Nonhuman, Scout], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<b>Reaction:</b> When paying a Gold cost, bow Washi: Produce 2 Gold.'
Seppun_Washi = Personality(card_id=6620, title='Seppun Washi', force=1, chi=3, personal_honor=2, gold_cost=6, honor_requirement=None, clan=[Unaligned], keywords=[Banker, Imperial, ImperialBankOfRokugan, Samurai, SoulOf('Seppun Ujifusa')], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'After Suiteiru enters play: Lose 4 Honor.<br><b>Open:</b> Destroy your target unbowed Personality: Create a number of 1F <b>Shadowlands &#149; Nonhuman &#149; Oni</b> Followers equal to his Chi. Attach them to one or more of your Personalities. Lose Honor equal to the number of Followers this created.'
Suiteiru_no_Oni = Personality(card_id=7618, title='Suiteiru no Oni', force=5, chi=3, personal_honor=0, gold_cost=8, honor_requirement=None, clan=[Unaligned, ShadowlandsFaction], keywords=[Nonhuman, Oni, Shadowlands], traits=[], abilities=[], legality=[EmperorEdition, DiamondEdition, ModernEdition])
"After Ugulu enters play: Lose 5 Honor.<br>Before a Human Personality moves to Ugulu's battlefield: Negate his movement."
Ugulu_no_Oni = Personality(card_id=8929, title='Ugulu no Oni', force=4, chi=2, personal_honor=0, gold_cost=4, honor_requirement=None, clan=[Unaligned, ShadowlandsFaction], keywords=[Nonhuman, Oni, Shadowlands], traits=[], abilities=[], legality=[EmperorEdition, ImperialEdition, JadeEdition, ModernEdition])
'<b>Reaction:</b> After one of your Rings enters play, bow Yung: Search your Fate deck for a Ring, show it, and put it in your hand.'
Yung = Personality(card_id=9697, title='Yung', force=0, chi=3, personal_honor=1, gold_cost=6, honor_requirement=5, clan=[Unaligned, BrotherhoodOfShinsei], keywords=[Unique, Monk, SoulOf('Yodin')], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])