from __future__ import annotations
from .common import Strategy
from l5r_auto.keywords import BushidoVirtue, Compassion, Control, DarkVirtue, Experienced, Favor, Fire, Iaijutsu, Kata, Kiho, Ninja, Political, Revenge, Tattoo, Terrain, Unique
from l5r_auto.legality import EmperorEdition, IvoryEdition, ModernEdition, TwentyFestivalsEdition
"You may only play one copy of Advanced Intelligence per battle.<br><b>Reaction:</b> After a Recon Strategy's action resolves: Draw one card for each action from a Recon Strategy you have taken this battle."
Advanced_Intelligence = Strategy(card_id=10135, title='Advanced Intelligence', gold_cost=0, focus_value=1, traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
"<b>Iaijutsu Revenge Reaction:</b> After another player's performed Limited or Open action resolves which caused you an Honor loss, target your performing unbowed Duelist to target and have him challenge the action's performer. Destroy the loser. Give the winner two +1F <b>Revenge </b>tokens."
An_Insult_Answered = Strategy(card_id=10136, title='An Insult Answered', gold_cost=0, focus_value=3, keywords=[Iaijutsu, Revenge], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
"<b>Battle:</b> Target an enemy Personality whose unit's total Gold cost is 10 or lower: He defects. Take control of him <i>(he joins your army)</i>. Dishonor him. Destroy any of his Followers whose Honor Requirement he now fails to meet. Give control of him to his owner before the turn ends."
Black_Marketeering = Strategy(card_id=10137, title='Black Marketeering', gold_cost=10, focus_value=2, traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
"<b>Open:</b> Until the turn ends, Rings will not enter play if their owner has already put a Ring into play this turn.<br><b>Limited:</b> Target an Event in another player's discard pile. End all of its ongoing effects. Shuffle it into its owner's deck."
Brotherhood_Schism = Strategy(card_id=10138, title='Brotherhood Schism', gold_cost=0, focus_value=3, traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
"As a Focus Effect, after this duel ends, straighten a Personality.<br><b>Battle/Open:</b> Target your performing Yojimbo. The next time <i>(this turn)</i> another player's action would target one of your Personalities, it targets the Yojimbo instead, if legal. You may take an additional action."
Ceaseless_Vigil = Strategy(card_id=10139, title='Ceaseless Vigil', gold_cost=0, focus_value=4, traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
"<b>Open:</b> Target another player's face-up Personality in or out of play: Permanently give him <b>Overconfident </b><i>(each other player may draw a card after an Overconfident card enters or leaves play)</i>."
Courting_Trouble = Strategy(card_id=10140, title='Courting Trouble', gold_cost=0, focus_value=4, traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<b>Limited:</b> Permanently give each of your provinces +1 strength.'
Debt_to_the_Kaiu = Strategy(card_id=10141, title='Debt to the Kaiu', gold_cost=0, focus_value=2, traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
"<b>Battle:</b> Target an attacking Follower or Personality without attachments: It does not contribute Force to its army's total Force this battle."
Defensive_Blockade = Strategy(card_id=10142, title='Defensive Blockade', gold_cost=0, focus_value=3, traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<b>Battle:</b> Target your unbowed attacking Personality. Move a target enemy Personality at any location to the current battlefield. Straighten him as he moves.'
Determined_Challenge = Strategy(card_id=10143, title='Determined Challenge', gold_cost=0, focus_value=3, traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, EmperorEdition, ModernEdition])
'<b>Fire Limited:</b> Target your performing unbowed Tattooed Personality who has not performed an action from a Dragon Tattoo this game. <i>He is imbued with the mystical power of the Dragon.</i> Permanently give him the ability, "<b>Fire Limited:</b> Give this Personality a +1F Fire token."'
Dragon_Tattoo_Experienced = Strategy(card_id=10144, title='Dragon Tattoo', gold_cost=0, focus_value=2, keywords=[Experienced('1'), Fire, Tattoo], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<b>Battle, :g2::</b> Target your performing Personality. Create a 2F Ronin Follower and attach it to him.'
Dubious_Resources = Strategy(card_id=10145, title='Dubious Resources', gold_cost=2, focus_value=1, traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'As a Focus Effect, after this duel ends, bow the winner.<br><b>Limited:</b> Target your performing Paragon. He may assign even if bowed. Give him <b>Elite </b><i>(Elite cards contribute Force even if bowed)</i>.'
Embracing_Battle = Strategy(card_id=10146, title='Embracing Battle', gold_cost=0, focus_value=2, traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
"<b>Open:</b> Choose your performing unbowed Personality and target another player's unbowed Personality: Neither may perform actions this phase."
Exchange_of_Letters = Strategy(card_id=10147, title='Exchange of Letters', gold_cost=1, focus_value=4, traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
"As a Focus Effect: After this duel ends, if your Personality won it, you may give a Personality -4F.<br><b>Open:</b> Target another player's Personality: After the next time this turn he is assigned to attack or is destroyed, gain 2 Honor."
Fair_Warning = Strategy(card_id=10149, title='Fair Warning', gold_cost=0, focus_value=3, traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<b>Battle:</b> Choose your performing unbowed Monk: After the next time <i>(this turn)</i> an action targets him, you may choose either to negate its effects on your Monk, or to bow the unit of one Personality that performed it after the action resolves. You may take an additional Battle action.'
Grappling_the_Snake = Strategy(card_id=10150, title='Grappling the Snake', gold_cost=0, focus_value=1, keywords=[Kiho], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<b>Battle:</b> Choose your performing Commander and target a Follower in your hand or discard pile: Attach it to him, ignoring costs. Destroy it before this battle resolves. You may take an additional Battle action.'
Harsh_Taskmaster = Strategy(card_id=10151, title='Harsh Taskmaster', gold_cost=0, focus_value=1, traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<b>Open:</b> Target a Personality: After the next time this turn he is assigned to attack, dishonor him and his controller loses Honor equal to his base Personal Honor.<br><b>Open:</b> Each of your provinces has +2 strength for each dishonorable Personality attacking it.'
Imperial_Protection = Strategy(card_id=10152, title='Imperial Protection', gold_cost=0, focus_value=3, keywords=[Political], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
"<b>Battle:</b> Bow your performing Courtier at any location and target an enemy Personality: Bow him. Give this battlefield's province a strength bonus equal to your Courtier's Chi."
Incriminating_Testimony = Strategy(card_id=10153, title='Incriminating Testimony', gold_cost=0, focus_value=2, keywords=[Political], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<b>Limited:</b> Choose your performing unbowed Magistrate and target one or two Personalities: Dishonor them. Draw an additional card during your next End Phase.'
Ingenuity = Strategy(card_id=10154, title='Ingenuity', gold_cost=0, focus_value=3, keywords=[Political], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
"<b>Battle:</b> Choose your performing Personality and a Battle Strategy in another player's discard pile: Its abilities may be used an additional time this turn. Your Personality copies a keyword on an enemy Personality. You may take an additional action to play the Strategy for one of its actions. After it resolves, remove it from the game."
Learning = Strategy(card_id=10155, title='Learning', gold_cost=0, focus_value=2, traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<b>Open:</b> Choose your performing unbowed Henshin and target a Personality: Permanently give him, or remove from him, <b>Cavalry</b>, <b>Naval</b>, or <b>Tactician</b>.'
Manipulate_Energies = Strategy(card_id=10156, title='Manipulate Energies', gold_cost=0, focus_value=4, keywords=[Kiho], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
"<b>Limited:</b> Choose your performing Samurai and target another player's Personality: Neither Personality may be assigned to battlefields."
Martial_Manipulation = Strategy(card_id=10157, title='Martial Manipulation', gold_cost=0, focus_value=3, keywords=[Control, DarkVirtue], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<b>Battle:</b> Choose your performing unbowed Ninja: Ranged 4 Attack. The next time this battle the enemy leader takes a Battle action, if it can legally target the Ninja, it must target him.'
Metsubushi = Strategy(card_id=10158, title='Metsubushi', gold_cost=0, focus_value=3, keywords=[Ninja], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<b>Open:</b> Choose your performing Tactician and target your Personality: He may assign even if bowed. Give him <b>Elite </b><i>(Elite cards contribute Force even if bowed)</i>.'
Military_Promotion = Strategy(card_id=10159, title='Military Promotion', gold_cost=0, focus_value=3, traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
"<b>Political Open:</b> Target your Personality. Take the Imperial Favor. <br><b>Favor Political Battle/Open:</b> Discard the Imperial Favor to straighten your target Personality's unit."
My_Lords_Favor = Strategy(card_id=10160, title="My Lord's Favor", gold_cost=0, focus_value=4, keywords=[Favor, Political], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, EmperorEdition, ModernEdition])
'<b>Limited:</b> Choose your performing unbowed Personality with the base Ninja keyword: He infiltrates the enemy ranks. Permanently give him the trait, "After a Straighten Phase begins: Choose your bowed non-Ninja Personality. Negate his straightening this phase." Give control of him to another player.'
Only_a_Shadow = Strategy(card_id=10161, title='Only a Shadow', gold_cost=0, focus_value=3, keywords=[Ninja], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
"<b>Open:</b> Target another player's Personality: Permanently give him <b>Brash </b><i>(the Defender may draw a card after a Brash card is assigned to attack)</i>."
Out_of_My_Sight = Strategy(card_id=10162, title='Out of My Sight!', gold_cost=0, focus_value=4, traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<b>Battle:</b> Bow your performing Scout and target a face-up Scout Personality in your province: Bring the target into play at the current battlefield, paying all costs. If you have Reconnaissance, you may take an additional Battle action.'
Requesting_Reinforcements = Strategy(card_id=10163, title='Requesting Reinforcements', gold_cost=0, focus_value=2, traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
"<b>Battle:</b> Choose your performing Personality: The next time this battle another player's Battle action would target one of your cards, it targets your performer, if legal. If he has 7 or more base Force, you may take an additional Battle action <i>(after this action ends)</i>."
Ruthless_Onslaught = Strategy(card_id=10164, title='Ruthless Onslaught', gold_cost=0, focus_value=1, traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
"<b>Open:</b> If it is not your turn and the active player controls any Personalities, choose your performing unbowed Spirit: After the next Dynasty Phase begins, if it was opposed this turn, gain 2 Honor, and if no units were assigned to attack this turn, gain 3 Honor if your Honor is lower than each other player's."
Sentinel_Spirit = Strategy(card_id=10165, title='Sentinel Spirit', gold_cost=0, focus_value=3, traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
"<b>Limited:</b> Choose your performing unbowed Courtier: After this action ends <i>(and this card is in your discard pile)</i>, gain 1 Honor for each card titled Sharing Gossip in all players' discard piles."
Sharing_Gossip = Strategy(card_id=10166, title='Sharing Gossip', gold_cost=0, focus_value=1, keywords=[Political], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<b>Battle:</b> Target your defending Personality: Give him and each of his Followers +3F.'
Shield_Formation = Strategy(card_id=10167, title='Shield Formation', gold_cost=0, focus_value=3, traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
"<b>Battle:</b> If there is no Terrain in play at the current battlefield: Put this card into play there.<br><b>Reaction:</b> If this card is in play, when another player's action would target one of your Personalities, choose your performing Personality: The action targets him instead, if legal."
Shifting_Terrain = Strategy(card_id=10168, title='Shifting Terrain', gold_cost=0, focus_value=2, keywords=[Terrain], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<b>Limited:</b> Put this card into play. Discard all your other Kata in play.<br><b>Battle:</b> If this card is in play, choose your performing Personality: Move him home. If he moved, straighten his unit.'
Sound_the_Retreat = Strategy(card_id=10169, title='Sound the Retreat', gold_cost=0, focus_value=3, keywords=[Kata], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<b>Battle:</b> Ranged 1 Attack. If the Ranged Attack destroyed a card, draw a card; if it destroyed a Follower, you may take an additional Battle action.'
Sticks_and_Stones = Strategy(card_id=10170, title='Sticks and Stones', gold_cost=0, focus_value=0, traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<b>Limited:</b> Choose your performing unbowed honorable Personality and target a Personality with lower base Personal Honor: Dishonor or rehonor the target.'
Testimony = Strategy(card_id=10171, title='Testimony', gold_cost=0, focus_value=2, keywords=[Political], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
"<b>Battle:</b> Ranged 3 Attack with +1 strength for each Follower in the target's unit."
The_Arrows_Eye = Strategy(card_id=10172, title="The Arrow's Eye", gold_cost=0, focus_value=3, traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<b>Limited:</b> If another player has 40 or more Honor, has five Rings in play, or you have -20 or lower Honor: The Dynasty Phase comes before the Attack Phase this turn.<br><b>Battle:</b> Draw a card.'
The_Deciding_Moment = Strategy(card_id=10119, title='The Deciding Moment', gold_cost=0, focus_value=4, keywords=[Unique], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
"As a Focus Effect: You may discard your Personality in this duel <i>(ending the duel without resolution)</i>.<br><b>Battle:</b> Even if you control no units at the current battlefield, choose your performing Monk at any location and bow your target Ring: Give the current battlefield's province +3 or -3 strength."
Turning_Away = Strategy(card_id=10173, title='Turning Away', gold_cost=0, focus_value=2, keywords=[Kiho], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<b>Reaction:</b> Before a Proclaim action resolves: Negate its effects.'
Turning_the_Story = Strategy(card_id=10174, title='Turning the Story', gold_cost=0, focus_value=3, keywords=[Political], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<b>Battle:</b> Choose your performing Kensai: You may take two additional Battle actions from cards in his unit. Other actions will not give you new additional Battle actions this battle.'
Two_Hands = Strategy(card_id=10175, title='Two Hands', gold_cost=0, focus_value=2, traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<b>Battle:</b> Bow your performing Personality or Follower: Ranged 4 Attack.<br><b>Battle:</b> If this card is in your discard pile, bow your performing Personality or Follower: Ranged 4 Attack. Remove this card from the game.'
Two_Stings = Strategy(card_id=10176, title='Two Stings', gold_cost=0, focus_value=1, traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<b>Battle:</b> Target an enemy Personality or Follower: Give it -4F.'
Unexpected_Obstacle = Strategy(card_id=10177, title='Unexpected Obstacle', gold_cost=0, focus_value=4, traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<b>Open:</b> Target a Ring which did not last enter play by its own text: This is not true enlightenment. Permanently remove its abilities.<br><b>Limited:</b> Target one or more cards in your provinces: Discard them. Refill the provinces face-up from the bottom of your deck.'
Unsettling_Doubts = Strategy(card_id=10178, title='Unsettling Doubts', gold_cost=0, focus_value=1, traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<b>Open:</b> Each player may only take two more non-Reaction actions this phase.<br><b>Limited:</b> Pay 2 Gold: Draw a card.'
Urgency = Strategy(card_id=10179, title='Urgency', gold_cost=0, focus_value=3, keywords=[Political], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<b>Battle:</b> Choose your performing unbowed Personality and target an enemy Personality with lower Chi: Move him home.'
Vengeful_Dismissal = Strategy(card_id=10180, title='Vengeful Dismissal', gold_cost=0, focus_value=3, traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<b>Open:</b> If it is not your turn, choose another player: You come across some starving peasants in need. You, then the player, each pay zero or more Gold. Whoever paid more Gold gains Honor equal to the difference between the two amounts paid, or 4, whichever is less.'
Virtuous_Charity = Strategy(card_id=10181, title='Virtuous Charity', gold_cost=0, focus_value=3, keywords=[BushidoVirtue, Compassion], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
"Before an action's effect destroys a card in a unit: Negate the destruction.<br><b>Battle:</b> If there is no Terrain in play at the current battlefield: Put this card into play there."
Wide_Valley = Strategy(card_id=10182, title='Wide Valley', gold_cost=0, focus_value=1, keywords=[Terrain], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])