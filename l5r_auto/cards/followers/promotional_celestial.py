from __future__ import annotations
from .common import Follower
from l5r_auto.keywords import Cavalry, Elite, Fudo, Gaijin, Imperial, Scout
from l5r_auto.legality import CelestialEdition, EmperorEdition, IvoryEdition, ModernEdition, OnyxEdition, TwentyFestivalsEdition
'<b>Battle:</b> Bow a target attachment or a target dishonorable Personality.'
Bounty_Hunter = Follower(card_id=1119, title='Bounty Hunter', force=3, chi=0, gold_cost=4, focus_value=4, traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, EmperorEdition, CelestialEdition, ModernEdition])
'This Follower will not be transferred.<br>After each turn begins, give this Personality a -1C token.<br><b>Limited, :gstar::</b> If this Follower is in your hand, Equip it to a target Personality you do not control.'
Cultist_Infiltrator = Follower(card_id=1595, title='Cultist Infiltrator', force=3, chi=0, personal_honor=0, gold_cost=3, focus_value=2, honor_requirement=0, traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
'Equips to a Nonhuman Fudo Personality ignoring Gold cost.<br>This Follower has +1F for each other Fudo card you control.'
Fudo_Cultist = Follower(card_id=2722, title='Fudo Cultist', force=2, chi=0, personal_honor=0, gold_cost=3, focus_value=2, honor_requirement=0, keywords=[Fudo], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
'After the resolution of a Recon action you took: Give this card +1F.'
Master_Scouts = Follower(card_id=4867, title='Master Scouts', force=2, chi=0, personal_honor=0, gold_cost=3, focus_value=3, honor_requirement=1, keywords=[Elite, Gaijin, Scout], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
"This Personality has <b>Conqueror</b>. <br><i>(A Conqueror's unit doesn't bow after battle.)</i>"
Mounted_Support = Follower(card_id=5417, title='Mounted Support', force=3, chi=0, gold_cost=5, focus_value=2, keywords=[Cavalry], traits=[], abilities=[], legality=[TwentyFestivalsEdition, CelestialEdition, OnyxEdition, ModernEdition])
'<i>(Elite cards contribute Force even if bowed.)</i><br>This Personality has <b>Elite</b>.'
Seppun_Heavy_Elite = Follower(card_id=6596, title='Seppun Heavy Elite', force=2, chi=0, personal_honor=0, gold_cost=3, focus_value=3, honor_requirement=0, keywords=[Elite, Imperial], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
'Attaches to Yotsu Ueda paying 2 less Gold.<br><b>Battle:</b> Target an attachment: Bow or straighten it.'
Yotsu_Uedas_Chosen = Follower(card_id=9681, title="Yotsu Ueda's Chosen", force=3, chi=0, personal_honor=0, gold_cost=4, focus_value=2, honor_requirement=1, traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])