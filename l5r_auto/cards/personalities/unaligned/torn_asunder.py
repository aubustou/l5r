from __future__ import annotations
from ..common import Personality
from l5r_auto.clans import ShadowlandsFaction, Unaligned
from l5r_auto.keywords import CaptainOfTheTachikaze, Commander, Duelist, Elite, Imperial, Mercenary, Naval, Nonhuman, Oni, Paragon, Ronin, Samurai, Shadowlands, Shugenja, Unique, Yojimbo
from l5r_auto.legality import EmperorEdition, ModernEdition
'After Kaito enters play: Lose 2 Honor.<br>Kaito has +3GC while the effects of a Spell action he performed are resolving.'
Chuda_Kaito = Personality(card_id=10320, title='Chuda Kaito', force=0, chi=2, personal_honor=0, gold_cost=2, honor_requirement=None, clan=[Unaligned, ShadowlandsFaction], keywords=[Shadowlands, Shugenja], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
"Human Personalities in Chun's army have <b>Naval</b>."
Chun = Personality(card_id=10321, title='Chun', force=3, chi=2, personal_honor=1, gold_cost=5, honor_requirement=None, clan=[Unaligned], keywords=[Naval, CaptainOfTheTachikaze, Mercenary], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<i>(Elite cards contribute Force even if bowed.)</i><br>After Mumoku enters play, lose 4 Honor.<br>While Mumoku is attacking at a battlefield, its Province has a maximum strength equal to its printed strength.'
Mumoku_no_Oni = Personality(card_id=10322, title='Mumoku no Oni', force=10, chi=3, personal_honor=0, gold_cost=11, honor_requirement=None, clan=[Unaligned, ShadowlandsFaction], keywords=[Elite, Nonhuman, Oni, Shadowlands], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
"<b>Reaction:</b> When another player's action would target Tamahime: It targets Riku instead, if legal.<br><b>Battle:</b> Target an enemy Personality: Riku duels him. Destroy the duel's loser."
Riku = Personality(card_id=10323, title='Riku', force=3, chi=5, personal_honor=3, gold_cost=7, honor_requirement=4, clan=[Unaligned], keywords=[Duelist, Unique, Commander, Ronin, Samurai, Yojimbo], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
"<b>Reaction:</b> Before an action resolves that targeted a Personality at Ryota's location: He enters any duel created by its effects instead of the target."
Seppun_Ryota = Personality(card_id=10324, title='Seppun Ryota', force=3, chi=3, personal_honor=3, gold_cost=5, honor_requirement=5, clan=[Unaligned], keywords=[Duelist, Imperial, Paragon, Samurai, Yojimbo], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])