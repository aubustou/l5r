from __future__ import annotations
from .common import Follower
from l5r_auto.keywords import Cavalry, Imperial, Kolat, Ninja, Scout
from l5r_auto.legality import EmperorEdition, IvoryEdition, ModernEdition, TwentyFestivalsEdition
'This card has +1F for each other Brothers of the Great Lake in this army.<br><b>Battle:</b> Bow a target enemy card.'
Brothers_of_the_Great_Lake = Follower(card_id=10332, title='Brothers of the Great Lake', force=3, chi=0, personal_honor=0, gold_cost=4, focus_value=3, honor_requirement=0, traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<b>Battle, :bow::</b> If you are the Attacker, Melee 2 Attack.'
Cavalry_Flankers = Follower(card_id=10333, title='Cavalry Flankers', force=0, chi=0, personal_honor=0, gold_cost=0, focus_value=2, honor_requirement=0, keywords=[Cavalry], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'Melee and Ranged Attacks targeting this Follower have -3 strength.'
Destrier = Follower(card_id=10334, title='Destrier', force=2, chi=0, personal_honor=0, gold_cost=2, focus_value=2, honor_requirement=1, keywords=[Cavalry], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<b>Kolat Open, :bow::</b> If this Follower did not enter play this turn, straighten a target Holding with equal or lower Gold Cost.'
Disciples_of_Master_Coin = Follower(card_id=10335, title='Disciples of Master Coin', force=3, chi=0, personal_honor=0, gold_cost=4, focus_value=2, honor_requirement=0, keywords=[Kolat], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'Other Ninja in this army have +1F.<br>After an action resolves during which this Follower was destroyed, create a 4F/3C/0PH <b>Ninja</b> Personality with your Clan Alignment at any location.'
Goju_Kaxt = Follower(card_id=10336, title='Goju Kaxt', force=3, chi=0, personal_honor=0, gold_cost=6, focus_value=3, honor_requirement=0, keywords=[Ninja], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'This Personality has +1PH. <br>After the first time each phase a Political action targets this Personality, negate its remaining effects.'
Oriole_Imperial_Vanguard = Follower(card_id=10337, title='Oriole Imperial Vanguard', force=4, chi=0, gold_cost=7, focus_value=4, keywords=[Imperial], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, EmperorEdition, ModernEdition])
'<b>Political Limited:</b> Bow this card: Straighten this Personality. You may use his Political abilities that may only be used once per turn a second time <i>(this turn)</i>.'
Sycophants = Follower(card_id=10338, title='Sycophants', force=0, chi=0, personal_honor=0, gold_cost=5, focus_value=2, honor_requirement=0, traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'This Personality has <b>Naval</b> while he is Crane Clan.<br><b>Battle:</b> Target an enemy attachment: Destroy it.'
Ujis_Saboteurs = Follower(card_id=10339, title="Uji's Saboteurs", force=3, chi=0, personal_honor=0, gold_cost=4, focus_value=1, honor_requirement=1, keywords=[Scout], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])