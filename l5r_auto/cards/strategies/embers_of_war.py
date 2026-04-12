from __future__ import annotations
from .common import Strategy
from l5r_auto.keywords import Air, BushidoVirtue, DarkVirtue, Earth, Favor, Fear, Fire, Honesty, Iaijutsu, Imperial, Kata, Kiho, Kolat, Ninja, Perfection, Political, Recon, Riddle, Swamp, Tactical, Tattoo, Terrain, Unique, Void, Winter
from l5r_auto.legality import EmperorEdition, ModernEdition, OnyxEdition, TwentyFestivalsEdition
'<b>Open:</b> Target a Personality: Reduce his Force to 0. Lose 2 Honor.'
A_Weak_Poison = Strategy(card_id=99, title='A Weak Poison', gold_cost=2, focus_value=2, keywords=[Kolat], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
"<b>Political Reaction:</b> After another player's Political action targets your Personality, negate its effects.<br><b>Political Limited:</b> Target a Kolat, Ninja, Shadowlands, or dishonorable Personality. His controller loses Honor equal to his printed Personal Honor."
Astonishing_Accusation = Strategy(card_id=637, title='Astonishing Accusation', gold_cost=0, focus_value=2, keywords=[Political], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'As a Focus Effect: You may transfer a Spell from your Personality in this duel to another of your Shugenja at the same location.<br><b>Battle:</b> If you have not put cards into your hand this phase and you have attached a Spell this turn: Draw two cards.'
Broken_Cipher = Strategy(card_id=1151, title='Broken Cipher', gold_cost=0, focus_value=1, traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<b>Fire Kiho Limited:</b> Target your performing unbowed Monk to give him two +1F Fire tokens. <br><b>Fire Kiho Battle:</b> Target your performing unbowed Monk to bow a target enemy card without attachments. Destroy it if your Monk has any Fire tokens.'
Deadly_Discipline = Strategy(card_id=1880, title='Deadly Discipline', gold_cost=0, focus_value=2, keywords=[Fire, Kiho], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'After an action resolves: Bow any Personalities it moved. <i>(Reactions trigger after traits.)</i><br><b>Reaction:</b> After a Battle action resolves, if there are no Terrains in play at the current battlefield: Put this card into play there.'
Deep_Snows = Strategy(card_id=1921, title='Deep Snows', gold_cost=0, focus_value=1, keywords=[Terrain, Winter], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<b>Battle:</b> Choose your performing unbowed Paragon and target an enemy Personality: Move him home. If he moved, bow him and negate his <i>(future)</i> movement. Lose 2 Honor.'
Exploited_Advantage = Strategy(card_id=2413, title='Exploited Advantage', gold_cost=0, focus_value=2, traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
"<b>Battle:</b> Choose your performing unbowed Personality and target an enemy card with lower Gold Cost: Bow it. <br><b>Battle:</b> Choose your performing Personality: Negate all current and new Force penalties to him from actions. Negate all current and new effects from other players' cards that prevent him from contributing Force to his army."
Games_of_Will = Strategy(card_id=2771, title='Games of Will', gold_cost=0, focus_value=3, traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
"As a Focus Effect: After this duel ends, lower the Gold Cost of its winner to 0.<br><b>Battle:</b> Choose your performing unbowed Courtier or Magistrate and target a Personality: You may pay Gold equal to his unit's total Gold Cost minus 6. If you did, move him home. Otherwise, straighten his unit."
Greasing_the_Wheels = Strategy(card_id=2896, title='Greasing the Wheels', gold_cost=0, focus_value=3, traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<b>Battle:</b> Choose your performing Personality in a Ninja unit: Move him to the current battlefield. Straighten his unit if he moved.'
Help_from_the_Shadows = Strategy(card_id=3055, title='Help from the Shadows', gold_cost=0, focus_value=3, keywords=[Ninja], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<b>Battle:</b> Choose your performing unbowed Samurai and target an enemy Personality with equal or lower Personal Honor: Bow him. Gain 1 Honor, or 3 Honor if your Family Honor is 9 or less.'
Honest_Assessment = Strategy(card_id=3415, title='Honest Assessment', gold_cost=0, focus_value=4, keywords=[BushidoVirtue, Honesty], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
"<b>Reaction:</b> After another player's Melee or Ranged Attack targets your Ninja: Show the card in the current battlefield's province. If it is a Personality, negate the Melee or Ranged Attack's effects. <br><b>Battle:</b> Discard a card in the current battlefield's province. Draw a card."
Inciting_Mistrust = Strategy(card_id=3733, title='Inciting Mistrust', gold_cost=0, focus_value=3, keywords=[Ninja], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<b>Reaction:</b> After an action resolves, if its player has resolved two or more actions which put cards into his hand this phase: He discards two cards. <br><b>Battle:</b> If any enemy units are at the current battlefield, choose your performing Personality: Move him there. Straighten him if he moved.'
Indecision = Strategy(card_id=3736, title='Indecision', gold_cost=0, focus_value=4, traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<b>Reaction:</b> After another player announces a Reaction during the Combat Segment: Its effects will not negate other effects.'
Inexorable = Strategy(card_id=3739, title='Inexorable', gold_cost=0, focus_value=2, traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'As a Focus Effect: You may choose <i>(now)</i> to use the base Force of your Personality in this duel as his duel stat if he is at a battlefield.<br><b>Battle:</b> Choose your performing Personality: Straighten him. You may move him home.'
Killing_Intent = Strategy(card_id=4352, title='Killing Intent', gold_cost=0, focus_value=2, traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<b>Battle:</b> If any enemy units are at the current battlefield, choose your performing Kensai: Move him there. Straighten his unit if he moved.<br><b>Battle:</b> Choose your performing unbowed Kensai and target an enemy Personality with lower Force: Move him home.'
Moving_and_Unmoving = Strategy(card_id=5423, title='Moving and Unmoving', gold_cost=0, focus_value=2, traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<b>Battle/Limited:</b> Choose your performing Samurai: Give each Personality and Follower in his unit a Force bonus equal to its current Force. Before this turn ends, destroy his unit.'
Perfect_Sacrifice = Strategy(card_id=5923, title='Perfect Sacrifice', gold_cost=0, focus_value=2, keywords=[DarkVirtue, Perfection], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
"<b>Reaction:</b> After another player's action targets your Personality: Discard him.<br><b>Battle:</b> If there are any enemy units at the current battlefield: Create a 1F/1C/1PH <b>Monk</b> Personality on your side there. Remove him from the game when the turn ends."
Perplexing_Guests = Strategy(card_id=5928, title='Perplexing Guests', gold_cost=0, focus_value=1, traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<b>Battle/Open:</b> Bow your performing Ninja Personality and target a Personality: Bow him.'
Phantom_Visage = Strategy(card_id=5941, title='Phantom Visage', gold_cost=0, focus_value=1, keywords=[Fear, Ninja], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<b>Battle:</b> Give your target performing unbowed Tattooed Monk +3F. If he is Earth, you may target and bow an enemy card without attachments.'
Pillar_Tattoo = Strategy(card_id=5956, title='Pillar Tattoo', gold_cost=0, focus_value=3, keywords=[Earth, Tattoo], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
"<b>Battle:</b> Choose your performing unbowed Personality with 7 or higher base Force and target two enemy Personalities, each with unit Gold Cost lower than your performer's Gold Cost: Bow one of them. Ranged Attack with strength equal to the first target's Force, which may only target the other Personality <i>(if legal)</i>."
Power_of_Strength = Strategy(card_id=6034, title='Power of Strength', gold_cost=0, focus_value=1, traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<b>Battle:</b> Choose your performing unbowed Personality and target an enemy Personality with fewer keywords, ignoring "Soul of" keywords: Bow all cards without attachments in his unit.'
Preceding_Reputation = Strategy(card_id=6043, title='Preceding Reputation', gold_cost=0, focus_value=3, traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<b>Reaction:</b> After a Melee or Ranged Attack is targeted: Give it +2 or -2 strength.<br><b>Battle:</b> Ranged 3 Attack.'
Precision = Strategy(card_id=6047, title='Precision', gold_cost=0, focus_value=2, traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'As a Focus Effect, before your Personality in this duel is destroyed for losing it, you may destroy one of his Followers to negate his destruction.<br><b>Open:</b> Put one or two target Followers in your discard pile into your hand.'
Preserving_Forces = Strategy(card_id=6059, title='Preserving Forces', focus_value=2, traits=[], abilities=[], legality=[TwentyFestivalsEdition, EmperorEdition, OnyxEdition, ModernEdition])
'<b>Battle:</b> Choose your performing unbowed Magistrate and target an enemy Personality: Move him to the current battlefield. Straighten his unit unless he is dishonorable, Kolat, Ninja, or Shadowlands.'
Pronouncement_of_Guilt = Strategy(card_id=6077, title='Pronouncement of Guilt', gold_cost=0, focus_value=3, traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
"<b>Battle:</b> Choose your performing unbowed Personality and target an enemy Personality: Your Personality duels the target. Bow the duel's loser. Move him home."
Reckless_Duel = Strategy(card_id=6209, title='Reckless Duel', gold_cost=0, focus_value=4, keywords=[Iaijutsu], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
"<b>Battle:</b> Bow your performing Courtier at any location and target a Personality: Move him home.<br><b>Reaction:</b> Before another player's Battle action resolves, target a Personality: Negate his movement to the current battlefield from the action's effects."
Request_Authorization = Strategy(card_id=6265, title='Request Authorization', gold_cost=0, focus_value=3, keywords=[Political], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
"<b>Limited:</b> Bow your performing Henshin, remove this card from the game, and target a Personality that shares a keyword with your Henshin: Put all cards in the target's unit at the bottom of his owner's appropriate decks in any order."
Riddle_of_Rebirth = Strategy(card_id=6316, title='Riddle of Rebirth', gold_cost=0, focus_value=0, keywords=[Unique, Kiho, Riddle, Void], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
"<b>Battle:</b> Choose your performing unbowed Monk and target an enemy Personality: Move him home. If he moved and your Monk is Air, negate the Personality's <i>(future)</i> movement."
Ride_the_Breeze = Strategy(card_id=6317, title='Ride the Breeze', gold_cost=0, focus_value=2, keywords=[Air, Kiho], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
"<b>Reaction:</b> After engaging, if you are the Attacker, choose your performing unbowed Scout at the current battlefield: You have Reconnaissance there. Choose and look at two cards in the Defender's hand. You have the first chance to take a Battle action in this battle, which must be performed by that Scout."
Scouting_the_Pass = Strategy(card_id=6513, title='Scouting the Pass', gold_cost=0, focus_value=2, keywords=[Recon], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'As a Focus Effect, after this duel ends, if your Personality won it, gain 1 Honor.<br><b>Absent Battle:</b> If you are the Defender, look at the top four cards of your Dynasty deck. If one of them is a Personality, you may Recruit him, ignoring Gold cost. Put the remaining cards back in any order. Discard him after the battle ends.'
Searching_for_Answers = Strategy(card_id=6526, title='Searching for Answers', gold_cost=0, focus_value=4, traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'As a Focus Effect: Until this duel ends, give +1C to each Weapon attached to your Personality in this duel.<br><b>Battle/Open:</b> Target one or more of your Items: Straighten them. You may transfer them to other Personalities you control.'
Secret_Reserve = Strategy(card_id=6552, title='Secret Reserve', gold_cost=0, focus_value=3, traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<b>Limited:</b> If this card is in play: Look at the top card of any deck. You may put it at the bottom of that deck.<br><b>Limited:</b> Put this card into play. Discard all your other Kata <i>(in play)</i>.'
Seeking_the_Question = Strategy(card_id=6565, title='Seeking the Question', gold_cost=0, focus_value=3, keywords=[Kata, Void], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<b>Battle:</b> Choose your performing unbowed Courtier at any location and target an enemy Personality: Move him home. Gain 1 Honor.'
Sheathing_the_Sword = Strategy(card_id=6727, title='Sheathing the Sword', gold_cost=0, focus_value=1, keywords=[Political], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<b>Battle:</b> Choose one or two of your performing Personalities with 7 or higher base Force: Straighten them.'
Stand_as_the_Mountain = Strategy(card_id=7459, title='Stand as the Mountain', gold_cost=0, focus_value=2, traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<b>Open:</b> Target a Holding: Straighten it.<br><b>Limited:</b> Target a Celestial: Discard it.'
Stuck_in_Rokugan = Strategy(card_id=7593, title='Stuck in Rokugan', gold_cost=0, focus_value=2, keywords=[Winter], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<b>Reaction:</b> After engaging, choose your performing unbowed Scout at the current battlefield: You have Reconnaissance there. Ranged Attacks from your card effects during this battle have +2 strength.'
Surrounded = Strategy(card_id=7668, title='Surrounded!', gold_cost=0, focus_value=2, keywords=[Recon], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<b>Battle:</b> Choose your performing unbowed Tactician at any location and target an enemy Personality: Move him home. Bow him if he moved.'
Tactical_Trap = Strategy(card_id=7717, title='Tactical Trap', gold_cost=0, focus_value=4, keywords=[Tactical], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'Personalities and Followers have -1F. All players have the ability, "<b>Open:</b> Bow your Stronghold: Discard a card titled The Bite of Winter from play."<br><b>Limited:</b> Put this card into play.'
The_Bite_of_Winter = Strategy(card_id=7972, title='The Bite of Winter', gold_cost=0, focus_value=4, keywords=[Winter], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'As a Focus Effect: After this duel ends, if your Personality lost it, give one of your Personalities two +1F Revenge tokens.<br><b>Battle/Open:</b> Choose your performing Personality: Straighten his unit.'
The_Cycle_of_Vengeance = Strategy(card_id=8004, title='The Cycle of Vengeance', gold_cost=0, focus_value=2, traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
"<b>Favor Imperial Political Limited, :gstar::</b> Discard the Imperial Favor or bow a Personality with 5 or more Force to lose 2 Honor and destroy another player's target Personality whose unit has a total Gold Cost equal to or less than what you paid for this action; these effects will not be negated."
The_Heirs_Wrath = Strategy(card_id=8127, title="The Heir's Wrath", gold_cost=0, focus_value=4, keywords=[Unique, Favor, Imperial, Political], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<b>Favor Political Winter Limited:</b> Discard the Imperial Favor to destroy a target attachment.<br><b>Favor Political Winter Battle:</b> Choose your performing Courtier at any location and bow him or discard the Imperial Favor to bow a target enemy Personality. His controller loses 2 Honor.'
The_Hosts_Advantage = Strategy(card_id=8141, title="The Host's Advantage", gold_cost=0, focus_value=3, keywords=[Favor, Political, Winter], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
"<b>Reaction:</b> After engaging: The current battlefield's province has a maximum strength equal to its base strength until the end of the battle. Negate the next effect that would move one of your Personalities from its battlefield. After the next time this battle a Terrain enters play, destroy it."
The_Snow_Has_Teeth = Strategy(card_id=8342, title='The Snow Has Teeth', gold_cost=0, focus_value=1, keywords=[Winter], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'After this card enters play: Choose and bow an enemy card at the current battlefield.<br><b>Battle:</b> If there is no Terrain in play at the current battlefield: Put this card into play there.'
Thick_Marsh = Strategy(card_id=8445, title='Thick Marsh', gold_cost=0, focus_value=2, keywords=[Swamp, Terrain], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<b>Battle:</b> Choose your performing unbowed Spirit and target an enemy Personality: Bow him or destroy one of his attachments.'
Too_Much_for_Mortals = Strategy(card_id=8634, title='Too Much for Mortals', gold_cost=0, focus_value=2, traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<b>Limited:</b> Target a province whose player has two or more provinces: During your next normal Attack Phase <i>(this turn)</i>, create two battlefields associated with it instead of one.'
Two_Fronts = Strategy(card_id=8922, title='Two Fronts', gold_cost=0, focus_value=2, traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
"<b>Interrupt:</b> Negate your target Commander's movement from the action's effects.<br><b>Battle:</b> Take an additional action to use a printed ability on your target Follower, even if it is bowed or the ability has been used the maximum number of times this turn."
Unsafe_Passage = Strategy(card_id=9008, title='Unsafe Passage', focus_value=3, traits=[], abilities=[], legality=[TwentyFestivalsEdition, EmperorEdition, OnyxEdition, ModernEdition])
'<b>Battle:</b> Choose your performing Personality: Give him the ability, "<b>Battle:</b> Target an enemy Personality: Destroy him."'
Unstoppable_Strike = Strategy(card_id=9020, title='Unstoppable Strike', gold_cost=0, focus_value=2, traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
"<b>Battle:</b> Choose your performing unbowed Yojimbo, and target an enemy card with Force lower than your Yojimbo's Force plus the highest Chi among all Shugenja and Courtiers you control: Bow the target. Destroy it if it has no attachments."
Yojimbo_Assemble = Strategy(card_id=9507, title='Yojimbo Assemble', gold_cost=0, focus_value=3, traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
"<b>Open:</b> Choose your performing unbowed Paragon and target an attachment with Force equal to or lower than your Paragon's Personal Honor: Destroy it."
You_Are_Unworthy = Strategy(card_id=9683, title='You Are Unworthy', gold_cost=0, focus_value=2, traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])