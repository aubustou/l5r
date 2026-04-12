from __future__ import annotations
from .common import Strategy
from l5r_auto.keywords import Air, Atemi, BushidoVirtue, DarkVirtue, Earth, Fire, Honesty, Iaijutsu, Kata, Kiho, Knowledge, Mountain, Ninja, Political, Recon, Siege, Tactical, Tattoo, Terrain, Void
from l5r_auto.legality import EmperorEdition, IvoryEdition, ModernEdition, OnyxEdition, TwentyFestivalsEdition
'<b>Fire Battle:</b> Target your performing unbowed Personality to make a Melee Attack with strength equal to 3 plus the number of Fire tokens on him and the number of Rings you control.'
Burning_Fury = Strategy(card_id=9896, title='Burning Fury', gold_cost=0, focus_value=2, keywords=[Fire], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<b>Battle:</b> Target your performing unbowed Magistrate to move home a target enemy Personality. If he is dishonorable, Kolat, Ninja, or Shadowlands, choose a player who gains or loses 2 Honor.'
Captured_Convict = Strategy(card_id=9897, title='Captured Convict', gold_cost=0, focus_value=3, traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
"<b>Political Battle:</b> Target your performing unbowed Courtier or Magistrate to dishonor a target Personality. His controller loses 1 Honor. After the next time <i>(this turn)</i> another player's action resolves that targeted your performer or a battle resolves which destroyed him, the second target's controller loses 2 Honor."
Cowed_and_Defeated = Strategy(card_id=9898, title='Cowed and Defeated', gold_cost=0, focus_value=2, keywords=[Political], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'As a Focus Effect: After this duel ends, choose a player who loses 2 Honor.<br><b>Reaction:</b> After one of your Personalities is destroyed: Create a <b>Maimed &#149; Retainer</b> Holding with the ability, "<b>Battle/Open:</b> Destroy this card and target a Personality: Straighten him. Rehonor him."'
Crippled_Sensei = Strategy(card_id=9899, title='Crippled Sensei', gold_cost=0, focus_value=3, traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'After an action resolves that one or more of your Personalities at the current battlefield performed: You may move any of those performers home.<br><b>Battle:</b> If there is no Terrain in play at the current battlefield: Put this card into play there. If you are the Defender, you may take an additional Battle action.'
Crowded_Streets = Strategy(card_id=9900, title='Crowded Streets', gold_cost=0, focus_value=1, keywords=[Terrain], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<b>Battle:</b> Target your performing Personality with 7 or more printed Force to negate all current and new Force penalties on him and effects which prevent him from contributing Force. He contributes Force even while bowed.'
Deep_Roots = Strategy(card_id=9901, title='Deep Roots', gold_cost=0, focus_value=2, traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<b>Absent Battle:</b> Move a target Personality <i>(at the current battlefield)</i> to an unresolved battlefield where he would be opposed. <i>(You may take Absent actions without presence.)</i>'
Defensive_Grill = Strategy(card_id=9902, title='Defensive Grill', gold_cost=0, focus_value=3, traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, EmperorEdition, ModernEdition])
"<b>Kiho Battle:</b> Target your performing unbowed Henshin to target an enemy card without attachments. Put it on top of its owner's deck."
Direct_the_Path = Strategy(card_id=9903, title='Direct the Path', gold_cost=0, focus_value=2, keywords=[Kiho], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
"As a Focus Effect, give +1 Focus Value to each of your focused cards.<br><b>Iaijutsu Battle/Limited:</b> Your target performing unbowed Personality challenges another player's target Personality. He may refuse; if he did, draw two cards. Bow the loser."
Duel_to_First_Blood = Strategy(card_id=9904, title='Duel to First Blood', gold_cost=0, focus_value=1, keywords=[Iaijutsu], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
"<b>Reaction:</b> After a Personality enters play, if his controller paid less than his base Gold Cost for him, bow your performing Merchant: The Personality's controller loses Honor equal to his base Personal Honor, or 3, whichever is lower.<br><b>Battle:</b> Pay Gold equal to a target unit's total Gold Cost minus 5: Move it home. Its controller loses 2 Honor."
Easy_Persuasion = Strategy(card_id=9905, title='Easy Persuasion', gold_cost=0, focus_value=2, traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'Before this battle resolves: If your army has more total Force than the enemy army, reduce the Force of each Personality and Follower in the enemy army to zero.<br><b>Battle:</b> If there is no Terrain in play at the current battlefield: Put this card into play there.'
Fields_of_Victory = Strategy(card_id=9906, title='Fields of Victory', gold_cost=0, focus_value=2, keywords=[Terrain], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<b>Open:</b> Choose your performing Personality: Show the top four cards of your Fate deck. You may attach one of them that is a Weapon to him, paying 4 less Gold. You may shuffle your deck. If you did not show a Weapon and he is a Kensai, draw a card.'
Forge_Your_Soul = Strategy(card_id=9907, title='Forge Your Soul', gold_cost=0, focus_value=2, traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<b>Open:</b> Target a Personality. <i>You deceive him with a forged order.</i> His controller puts all cards in his Provinces at the bottom of his Dynasty deck in any order, refilling them face-up.'
Forged_Documents = Strategy(card_id=9908, title='Forged Documents', gold_cost=0, focus_value=4, traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<b>Limited:</b> Choose your performing Samurai and show a Strategy in your hand: After the next time you resolve an action from a card with the Strategy\'s title this turn, if you have announced no other actions on Strategies between now and then, permanently give your Samurai the ability, "<b>Limited:</b> Gain 1 Honor."'
Forthrightness = Strategy(card_id=9909, title='Forthrightness', gold_cost=0, focus_value=2, keywords=[BushidoVirtue, Honesty], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
"You may only play one copy of Grief in reaction to any one resolution.<br><b>Reaction:</b> After an action resolves whose effects destroyed a player's Personality, target a Personality controlled by the same player: He is overcome with grief. Dishonor him. His controller loses Honor equal to his base Personal Honor."
Grief = Strategy(card_id=9910, title='Grief', gold_cost=0, focus_value=3, traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<b>Reaction:</b> After an action resolves which moved your Personality in a Ninja unit home: Move him to a different battlefield than the one from which he was moved home.'
I_Cast_Two_Shadows = Strategy(card_id=9911, title='I Cast Two Shadows', gold_cost=0, focus_value=3, keywords=[Ninja], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
"<b>Limited:</b> Choose your performing unbowed Courtier and target another player's Personality: That player may choose to discard a card at random from his hand. If he did not choose this, either gain 2 Honor, or the target's controller loses Honor equal to his base Personal Honor."
Kitsuki_Methods = Strategy(card_id=9912, title='Kitsuki Methods', gold_cost=0, focus_value=4, keywords=[Political], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<b>Battle/Open:</b> Choose your performing Personality with 7 or more base Force: His eyes go dead. Straighten him. Give him +3F. He may not perform actions. You may target and bow a card at his location.'
Kuons_Legacy = Strategy(card_id=9913, title="Kuon's Legacy", gold_cost=0, focus_value=2, traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<b>Battle:</b> Choose your performing unbowed Yojimbo: Melee 4 Attack. If you own a dead Courtier or Shugenja, you may target and destroy an attachment.'
Lessons_Never_Forgotten = Strategy(card_id=9914, title='Lessons Never Forgotten', gold_cost=0, focus_value=3, traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<b>Limited:</b> Choose your performing unbowed Samurai and you may bow him: He interrogates a witness. Look at the top 3 cards of any Fate deck. Put them back in any order. If you bowed your Samurai, put this card into your hand from your discard pile before this turn ends.'
Methodical_Questioning = Strategy(card_id=9915, title='Methodical Questioning', gold_cost=0, focus_value=3, keywords=[DarkVirtue, Knowledge], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<b>Battle:</b> Target an attachment: Destroy it.'
Never_Afraid = Strategy(card_id=9916, title='Never Afraid', gold_cost=0, focus_value=3, traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<b>Battle:</b> Choose your performing opposed Personality: Give him +2F, or +4F if he has an attachment.'
One_Shout = Strategy(card_id=9917, title='One Shout', gold_cost=0, focus_value=3, traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
"<b>Battle:</b> Choose your performing unbowed Paragon and target an enemy Personality: Reduce his Force by your Paragon's Force. Draw a card. You may take an additional Battle action. Lose 5 Honor."
Overcome_Adversity = Strategy(card_id=9918, title='Overcome Adversity', gold_cost=0, focus_value=2, traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'As a Focus Effect: After this duel ends, negate the effects of the next action performed by its winner.<br><b>Battle:</b> Choose your performing unbowed Monk and target an enemy Personality: Move him to a different battlefield. Bow him if he moved.'
Paralyzing_Touch = Strategy(card_id=9919, title='Paralyzing Touch', gold_cost=0, focus_value=1, keywords=[Atemi, Kiho], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<b>Battle:</b> Choose your performing unbowed Ninja Personality, bow him if he is not Shadowlands, and target a Personality: Before this battle resolves, give him -3C.'
Power_of_the_Night = Strategy(card_id=9920, title='Power of the Night', gold_cost=0, focus_value=2, keywords=[Ninja], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
"<b>Battle:</b> If any enemy units are at the current battlefield: Before this turn ends, gain 3 Honor if that battlefield's province has not been destroyed."
Preserving_Beauty = Strategy(card_id=9921, title='Preserving Beauty', gold_cost=0, focus_value=2, traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<b>Battle:</b> Give your target opposed Personality a Force bonus equal to his Personal Honor. Gain 2 Honor.'
Pure_Intent = Strategy(card_id=9922, title='Pure Intent', focus_value=1, traits=[], abilities=[], legality=[TwentyFestivalsEdition, EmperorEdition, OnyxEdition, ModernEdition])
"As a Focus Effect: After this duel ends, its winner's controller loses 1 Honor for each card he focused.<br><b>Open:</b> Target one or more Followers or Items in your discard pile: Attach them to any of your Personalities, paying all costs."
Regret = Strategy(card_id=9923, title='Regret', gold_cost=0, focus_value=1, traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
"<b>Battle:</b> Choose your performing Scout Personality and target an enemy Personality: Give him -4F. If you have Reconnaissance, you may target one of his attachments and put it in his owner's hand. You may move your Scout home."
Running_Battle = Strategy(card_id=9924, title='Running Battle', gold_cost=0, focus_value=3, traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<b>Battle:</b> Target an enemy Personality: Give him -5F. If his Force is now 0, his controller loses 1 Honor and you may target and dishonor a Personality.'
Scorn_the_Weak = Strategy(card_id=9925, title='Scorn the Weak', gold_cost=0, focus_value=1, traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<b>Limited:</b> Put this card into play. Discard all your other Kata in play. <br><b>Battle/Open:</b> If this card is in play, target your Personality and, if this is the Action Phase, discard a card: Straighten him.'
Serenity_in_Air = Strategy(card_id=9926, title='Serenity in Air', gold_cost=0, focus_value=3, keywords=[Air, Kata], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
"<b>Limited:</b> Choose your performing unbowed Ninja Personality and target another player's Personality: Create a battlefield <i>(not at any province)</i>. Assign your Personality to attack there. Assign the target to defend there, even if he is bowed. Fight a battle there, in which you have the first opportunity to take a Battle action or pass. Lose 5 Honor."
Shinobi_Assault = Strategy(card_id=9927, title='Shinobi Assault', gold_cost=4, focus_value=1, keywords=[Ninja], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
"<b>Reaction:</b> After another player's action targets your Courtier: Negate his dishonoring from the action's effects.<br><b>Open:</b> Choose your performing Courtier and target another player's Personality: Give him a Force penalty equal to your Courtier's Personal Honor. After each time he is assigned to attack this turn, gain 2 Honor."
Social_Grace = Strategy(card_id=9928, title='Social Grace', gold_cost=0, focus_value=3, keywords=[Political], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<b>Open:</b> Choose your performing Spirit Personality and target a Personality controlled by the active player: His controller must declare a normal attack this turn and assign the target <i>(if legal)</i>.'
Spiritual_Manipulation = Strategy(card_id=9929, title='Spiritual Manipulation', gold_cost=0, focus_value=3, traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<b>Reaction:</b> Before a battle resolves, choose your performing opposed Samurai Personality at the current battlefield: Give him +2F.'
Steady_Resolve = Strategy(card_id=9930, title='Steady Resolve', gold_cost=0, focus_value=2, traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<b>Reaction:</b> After a Ranged or Melee Attack is targeted: Give it -3 strength.<br><b>Battle:</b> Choose your performing defending Personality: Give him +5F. Straighten him before this battle resolves.'
Strong_Defenses = Strategy(card_id=9931, title='Strong Defenses', gold_cost=0, focus_value=1, keywords=[Siege], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<b>Limited:</b> Bow your performing Courtier and target a Personality: Dishonor him. Draw a card.'
Subtle_Games = Strategy(card_id=9932, title='Subtle Games', gold_cost=0, focus_value=1, keywords=[Political], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
"As a Focus Effect, give the duel's winner +3F. <br><b>Battle:</b> Target two Personalities controlled by the same player at different locations. Switch their locations. Straighten both their units as they move."
Sudden_Movement = Strategy(card_id=9933, title='Sudden Movement', gold_cost=0, focus_value=4, traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, EmperorEdition, ModernEdition])
'<b>Battle:</b> Choose your performing unbowed Tactician and target an enemy card without attachments: Destroy it.'
Tactical_Assault = Strategy(card_id=9934, title='Tactical Assault', gold_cost=0, focus_value=2, keywords=[Tactical], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<b>Battle/Open:</b> Choose your performing Commander and target one to three Personalities controlled by the same player: Straighten zero or more of their attachments, then transfer zero or more attachments among any of the targets.'
The_Game_Has_Changed = Strategy(card_id=9935, title='The Game Has Changed', gold_cost=0, focus_value=2, traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
"Battle: Choose your performing unbowed Monk and target another player's Personality: Move him to the current battlefield. If your Monk is not Earth, straighten the target's unit."
The_Lesson_of_Earth = Strategy(card_id=9936, title='The Lesson of Earth', gold_cost=0, focus_value=2, keywords=[Earth, Kiho], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<b>Limited:</b> Target a Celestial: Discard it.<br><b>Battle/Open:</b> Target a Personality with 3 or higher Chi: Give him -2C.'
Theological_Indecision = Strategy(card_id=9937, title='Theological Indecision', gold_cost=0, focus_value=2, traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<b>Limited:</b> Bow your performing Personality or Follower and target a Personality without attachments and with lower Force, or target a Follower: Bow it.'
Thuggish_Techniques = Strategy(card_id=9938, title='Thuggish Techniques', gold_cost=0, focus_value=3, traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
"<b>Battle:</b> Target your Paragon: Create a Personality with the same base Chi, Personal Honor and keywords as the target, and whose base Force equals that target's Personal Honor. Remove the Personality from the game after the battle ends."
TwoFold_Virtue = Strategy(card_id=9939, title='Two-Fold Virtue', gold_cost=3, focus_value=3, traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<b>Battle:</b> Choose your performing unbowed Personality and target an enemy card without attachments: Bow it. You may bow your Personality; if you did, draw a card.'
Unexpected = Strategy(card_id=9940, title='Unexpected', gold_cost=0, focus_value=1, traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<b>Battle/Open:</b> Target a Personality: His controller may choose to bow him. If he did not choose this, he must pass at his next opportunity this phase to take a Battle, Limited, or Open action.'
Unfortunate_Hesitation = Strategy(card_id=9941, title='Unfortunate Hesitation', gold_cost=0, focus_value=2, traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<b>Battle:</b> If there is no Terrain in play at the current battlefield, bow your performing Scout and target an enemy card without attachments: Destroy it. Put this card into play there.'
Unstable_Ground = Strategy(card_id=9942, title='Unstable Ground', gold_cost=0, focus_value=2, keywords=[Mountain, Terrain], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<b>Void Battle:</b> Target your performing unbowed Tattooed Personality, discard a card unless your Personality is Void, and remove this Strategy from the game to put a target a Tattoo Strategy in your discard pile into your hand. You may take an additional Battle action.'
Void_Tattoo = Strategy(card_id=9943, title='Void Tattoo', gold_cost=0, focus_value=3, keywords=[Tattoo, Void], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
"<b>Reaction:</b> After engaging, choose your performing Scout at the current battlefield and target a card in a unit there: You have Reconnaissance there. Abilities on cards <i>(now)</i> in the target's unit may not be used."
Watchers_in_the_Dark = Strategy(card_id=9944, title='Watchers in the Dark', gold_cost=0, focus_value=1, keywords=[Recon], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])