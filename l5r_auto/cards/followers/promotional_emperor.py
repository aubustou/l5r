from __future__ import annotations
from .common import Follower
from l5r_auto.keywords import Ashigaru, Assassin, Cavalry, DiscipleOfPanKu, Fallen, Fudo, Horse, Kharmic, Naga, Ninja, Nonhuman, Scout
from l5r_auto.legality import EmperorEdition, IvoryEdition, ModernEdition
"<b>Open:</b> Target another player's Follower or Personality. Switch the target's and this Follower's Force."
Daifuke = Follower(card_id=10235, title='Daifuke', force=3, chi=0, personal_honor=0, gold_cost=4, focus_value=0, honor_requirement=0, traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<b>Battle:</b> Ranged 3 Attack.'
Dark_Naga_Scouts = Follower(card_id=1839, title='Dark Naga Scouts', force=2, chi=0, personal_honor=0, gold_cost=2, focus_value=2, honor_requirement=0, keywords=[Naga, Nonhuman, Scout], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'This Follower has +1F while you control a Dojo.'
Family_Sensei = Follower(card_id=10592, title='Family Sensei', force=2, chi=0, gold_cost=2, focus_value=3, traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
'<b>Limited:</b> Destroy this Follower to target Fudo and give him two <b>Charging </b>tokens.'
Furugaro = Follower(card_id=10236, title='Furugaro', force=2, chi=0, personal_honor=0, gold_cost=2, focus_value=1, honor_requirement=0, keywords=[Fudo], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'Attaches to Kataoka ignoring costs.<br>Will only attach to a Human.<br>This Personality has <b>Cavalry</b>.'
Horse = Follower(card_id=10588, title='Horse', force=1, chi=0, gold_cost=3, focus_value=1, keywords=[Cavalry, Horse, Nonhuman], traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
'This Follower has +1F while you control a Market.'
Merchant_Guard = Follower(card_id=10589, title='Merchant Guard', force=2, chi=0, gold_cost=2, focus_value=3, traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
'After this Follower enters play, lose 1 Honor.<br><b>Limited:</b> Give a target card a <b>Madness </b>token.'
Pan_Ku_Cultist = Follower(card_id=10590, title="P'an Ku Cultist", force=3, chi=0, gold_cost=3, focus_value=2, keywords=[DiscipleOfPanKu, Fallen], traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
'<i><b>(Limited, :g2:: </b>Discard a Kharmic card from your hand to draw a card.)</i>'
Rice_Farmer = Follower(card_id=10587, title='Rice Farmer', force=2, chi=0, gold_cost=2, focus_value=2, keywords=[Kharmic, Ashigaru], traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
'<b>Reaction:</b> After a battle resolves, if this card\'s army destroyed a province, destroy this card: He plunders enough wealth to retire. Create a Holding with the trait, "Bow this card: Produce 2 Gold", and put it into play <i>(bowed)</i>.'
Treasure_Hunter = Follower(card_id=9966, title='Treasure Hunter', force=2, chi=0, personal_honor=0, gold_cost=2, focus_value=1, honor_requirement=0, keywords=[Scout], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<b>Assassin Ninja Limited:</b> Bow this Follower to destroy a target Follower. Destroy this Follower. Lose 2 Honor.'
Unseen_Assassins = Follower(card_id=10410, title='Unseen Assassins', force=2, chi=0, personal_honor=0, gold_cost=4, focus_value=1, honor_requirement=0, keywords=[Assassin, Ninja], traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])