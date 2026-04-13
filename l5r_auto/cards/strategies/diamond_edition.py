from __future__ import annotations
from .common import Strategy
from l5r_auto.keywords import Iaijutsu, Kharmic, Terrain
from l5r_auto.legality import DiamondEdition, GoldEdition, ImperialEdition, IvoryEdition, JadeEdition, ModernEdition, OnyxEdition, TwentyFestivalsEdition
'Shadowlands Personalities and Followers at this battlefield have +1F.<br><b>Battle:</b> Destroy a Terrain <i>(if able)</i>. Put this Terrain into play.'
Corrupted_Ground = Strategy(card_id=1513, title='Corrupted Ground', focus_value=1, keywords=[Terrain], traits=[], abilities=[], legality=[ImperialEdition, GoldEdition, JadeEdition, DiamondEdition, OnyxEdition, TwentyFestivalsEdition])
'<b>Battle:</b> Give your target Personality +2F/+2C. Show your hand to all players.'
Destiny_Has_No_Secrets = Strategy(card_id=1982, title='Destiny Has No Secrets', focus_value=1, traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, ImperialEdition, OnyxEdition, DiamondEdition, ModernEdition])
'<b>Earth Kiho Battle:</b> Bow your target unbowed Monk or Shugenja. Bow a target enemy Follower or Personality without Followers.'
Fist_of_the_Earth = Strategy(card_id=2586, title='Fist of the Earth', focus_value=3, traits=[], abilities=[], legality=[TwentyFestivalsEdition, ImperialEdition, GoldEdition, JadeEdition, OnyxEdition, DiamondEdition, ModernEdition])
'<i>(<b>Repeatable Limited, :g2::</b> Discard a Kharmic card to draw a card.)</i><br>As a Focus Effect, when this duel resolves, both Personalities lose the duel. <i>(This is not a tie.)</i>'
Kharmic_Strike = Strategy(card_id=4334, title='Kharmic Strike', gold_cost=0, focus_value=0, keywords=[Kharmic], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, ImperialEdition, GoldEdition, JadeEdition, DiamondEdition, ModernEdition])
'Before this battle resolves, reduce to 2 the Force of each Personality at this battlefield. <br><b>Battle:</b> Destroy a Terrain <i>(if able)</i>. Put this Terrain into play.'
Narrow_Ground = Strategy(card_id=5512, title='Narrow Ground', focus_value=1, keywords=[Terrain], traits=[], abilities=[], legality=[ImperialEdition, GoldEdition, JadeEdition, DiamondEdition, OnyxEdition, TwentyFestivalsEdition])
'<b>Kiho Battle:</b> Target your unbowed Monk or Shugenja and an enemy Personality with lower Chi. Bow the enemy Personality, and bow your Personality unless the enemy is Shadowlands.'
Purity_of_Spirit = Strategy(card_id=6111, title='Purity of Spirit', focus_value=4, traits=[], abilities=[], legality=[TwentyFestivalsEdition, GoldEdition, JadeEdition, OnyxEdition, DiamondEdition, ModernEdition])
'You may focus this Strategy face-up to discard the last card the other player focused <i>(if any)</i>, then draw a card. Each player may focus one additional time this duel.'
Smoke_and_Mirrors = Strategy(card_id=7305, title='Smoke and Mirrors', focus_value=0, traits=[], abilities=[], legality=[TwentyFestivalsEdition, JadeEdition, OnyxEdition, DiamondEdition, ModernEdition])
"<b>Iaijutsu Battle:</b> Your target unbowed Personality challenges a target enemy Personality. If he is unbowed, he may refuse. If he does, move him home and bow him as he moves. Destroy the duel's loser."
Stand_Or_Run = Strategy(card_id=7463, title='Stand Or Run', gold_cost=0, focus_value=2, keywords=[Iaijutsu], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, JadeEdition, DiamondEdition, ModernEdition])
"<b>Limited:</b> Target a Samurai Personality who has not been targeted by a Today We Die this game. Until the game ends, he cannot Lobby, after the end of each of his controller's Action Phases, if he can legally assign, his controller must declare an attack and assign him, and give him a +1F/+1C token after each battle resolution he is in."
Today_We_Die = Strategy(card_id=8509, title='Today We Die', gold_cost=0, focus_value=1, traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, ImperialEdition, DiamondEdition, ModernEdition])
'<b>Battle/Open:</b> A target Personality has <b>a</b> minimum Chi of 1. Give him -2F/-2C.'
Uncertainty = Strategy(card_id=8948, title='Uncertainty', gold_cost=0, focus_value=1, traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, GoldEdition, JadeEdition, DiamondEdition, ModernEdition])