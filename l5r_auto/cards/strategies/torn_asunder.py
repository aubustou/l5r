from __future__ import annotations
from .common import Strategy
from l5r_auto.keywords import BushidoVirtue, Courtesy, DarkVirtue, Determination, Favor, Fear, Iaijutsu, Imperial, Kata, Kiho, Maho, Ninja, Plague, Political, Port, Recon, Tattoo, Terrain, Void
from l5r_auto.legality import EmperorEdition, ModernEdition, OnyxEdition, TwentyFestivalsEdition
"<b>Battle/Open:</b> Target your Personality at any location. <i>He centers himself.</i> Negate other players' cards' effects that prevent him assigning, moving, or performing actions. If he is a Kensai, straighten his unit."
A_Cleansing_Breath = Strategy(card_id=10358, title='A Cleansing Breath', gold_cost=0, focus_value=4, traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<b>Reaction:</b> After a Personality with an Armor is targeted by a Melee or Ranged Attack, negate its effects.<br><b>Battle:</b> Give a target Personality with an attachment +2F.'
A_Close_Call = Strategy(card_id=10359, title='A Close Call', gold_cost=0, focus_value=1, traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<b>Favor Political Limited:</b> Target your performing unbowed non-Duelist Courtier Personality and discard the Imperial Favor to target a Personality with equal or lower Personal Honor. Destroy a non-Unique card in his unit without attachments. Dishonor him <i>(if he is still in play)</i>.'
A_Threat_Enacted = Strategy(card_id=10360, title='A Threat Enacted', gold_cost=4, focus_value=2, keywords=[Favor, Political], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<b>Battle:</b> Bow your target performing Personality to make a Ranged 3 Attack with +2 strength if your performer is a Scout. You may move him home.'
Ambush_Tactics = Strategy(card_id=10361, title='Ambush Tactics', gold_cost=0, focus_value=2, traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
"<b>Battle:</b> Straighten your target performing Personality. If another player's Battle action has destroyed one of your Personalities this battle, negate the performer's next destruction from cards' effects <i>(this turn)</i>."
Avenging_the_Fallen = Strategy(card_id=10362, title='Avenging the Fallen', gold_cost=0, focus_value=2, traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
"<b>Limited:</b> Target your performing unbowed Tattooed Personality to permanently give him <b>Stalwart </b><i>(Stalwart cards negate their first bowing each turn by other players' cards)</i>."
Bamboo_Tattoo = Strategy(card_id=10363, title='Bamboo Tattoo', gold_cost=0, focus_value=4, keywords=[Tattoo], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<b>Limited:</b> Target a bowed Personality: Put this card into play. While this card remains in play, negate the target\'s straightening, and his controller has the ability, "<b>Open:</b> Pay 4 Gold: Discard a Bonds of Hospitality."'
Bonds_of_Hospitality = Strategy(card_id=10364, title='Bonds of Hospitality', gold_cost=2, focus_value=2, keywords=[Political], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<b>Limited:</b> Bow your target performing Personality to permanently give him <b>Shadowlands </b>and three +1F tokens, straighten him before the turn ends, and lose 2 Honor.'
Calling_the_Darkness = Strategy(card_id=10365, title='Calling the Darkness', gold_cost=0, focus_value=3, traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<b>Absent Battle:</b> Target your performing Personality at any location who either is at, assigned to, or would be opposed at, the current battlefield. Move him there. If his printed Force is 7 or higher, straighten him.'
Charge_Into_Danger = Strategy(card_id=10366, title='Charge Into Danger', gold_cost=0, focus_value=1, traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
"<b>Limited:</b> Bow your target performing Samurai, target a face-up card in a Province, and choose another player. He may draw a card. Reduce the second target's Gold Cost <i>(this turn)</i> by 2, or 4 if the player drew a card."
Courteous_Gift = Strategy(card_id=10367, title='Courteous Gift', gold_cost=0, focus_value=4, keywords=[BushidoVirtue, Courtesy], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<b>Battle:</b> Straighten your target performing bowed Personality and give him +3F.'
Defensive_Stance = Strategy(card_id=10368, title='Defensive Stance', gold_cost=0, focus_value=4, traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<b>Open:</b> Until this phase ends or a player has discarded two cards from this effect, after each action other than this one resolves, its player discards a card.<br><b>Open:</b> Draw a card.'
Drain_of_Effort = Strategy(card_id=10369, title='Drain of Effort', gold_cost=2, focus_value=1, traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<b>Battle, :gstar::</b> If he would be opposed, Recruit your target performing discarded Yojimbo, paying 3 less Gold if you control a Courtier or Shugenja.'
Duty_Over_All_Things = Strategy(card_id=10370, title='Duty Over All Things', focus_value=4, traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
"<b>Battle:</b> Choose your performing unbowed Duelist and target an enemy Personality: Your Personality duels the target. Give the winner two +1F tokens. Destroy the duel's loser."
Eye_of_the_Sword = Strategy(card_id=10371, title='Eye of the Sword', gold_cost=0, focus_value=2, keywords=[Iaijutsu], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<b>Reaction:</b> After engaging, choose your performing Scout Personality at the current battlefield: You have Reconnaissance there. Attach a Follower to him from your hand or discard pile, paying all costs. If you did, draw an additional card during your next End Phase.'
Forest_Cover = Strategy(card_id=10372, title='Forest Cover', gold_cost=0, focus_value=2, keywords=[Recon], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
"<b>Open:</b> Target another player's Sensei Personality: Remove all traits and abilities from him <i>(this turn)</i>."
Forgotten_Teachings = Strategy(card_id=10373, title='Forgotten Teachings', gold_cost=0, focus_value=4, traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<b>Open:</b> Target two Personalities with the same Family name: They may not be assigned to the same battlefield.'
Generational_Gap = Strategy(card_id=10375, title='Generational Gap', gold_cost=1, focus_value=4, traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
"Negate Personalities' movement to or from this battlefield.<br><b>Battle:</b> If there is no Terrain in play at the current battlefield: Put this card into play there. You may take an additional Battle action."
Harbor_of_Kalanis_Landing = Strategy(card_id=10376, title="Harbor of Kalani's Landing", gold_cost=0, focus_value=1, keywords=[Port, Terrain], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<b>Open:</b> Choose your performing Monk: Permanently give him the trait, "You may bow this card instead of bowing a Ring to pay a cost."'
Harmony = Strategy(card_id=10377, title='Harmony', gold_cost=0, focus_value=0, keywords=[Kiho, Void], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
"<b>Open:</b> Choose your performing Personality: The Empress dispatches him to the Colonies. Negate other players' cards' effects that prevent him assigning. After the next time this turn an attack is declared, straighten his unit."
Imperial_Deployment = Strategy(card_id=10378, title='Imperial Deployment', gold_cost=0, focus_value=4, keywords=[Imperial], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
"<b>Reaction:</b> Before an action resolves, target a Personality: Negate his movement from the action's effects."
Improper_Papers = Strategy(card_id=10379, title='Improper Papers', gold_cost=0, focus_value=3, traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<b>Limited:</b> Target another player with 30 or more Family Honor: He commits a public breach of etiquette. He loses 5 Honor.'
Imprudent_Misstep = Strategy(card_id=10380, title='Imprudent Misstep', gold_cost=0, focus_value=2, keywords=[Political], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
"<b>Battle:</b> Bow your performing Courtier at any location and target one or more attacking cards, up to half of your Courtier's Chi, rounded down: Bow the targets."
In_the_Right = Strategy(card_id=10381, title='In the Right', gold_cost=0, focus_value=3, keywords=[Political], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
"<b>Limited:</b> Choose your performing unbowed Magistrate, target a Human Personality, and pay Gold equal to his unit's total Gold Cost, +8 unless he is dishonorable, Kolat, Ninja, or Shadowlands: He commits seppuku."
Kitsuki_Judgment = Strategy(card_id=10382, title='Kitsuki Judgment', gold_cost=0, focus_value=1, keywords=[Political], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
"<b>Battle/Open:</b> Destroy your performing Paragon and target one or two of your other Personalities: Give them +3F and <b>Stalwart</b> <i>(Stalwart cards negate their first bowing each turn by other players' cards)</i>."
Martyrs_Call = Strategy(card_id=10383, title="Martyr's Call", gold_cost=0, focus_value=2, traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<b>Battle:</b> Give two or more target opposed Personalities, each with a different Clan Alignment, +2F <i>(each)</i>.'
Mutual_Support = Strategy(card_id=10384, title='Mutual Support', focus_value=2, traits=[], abilities=[], legality=[TwentyFestivalsEdition, EmperorEdition, OnyxEdition, ModernEdition])
'<b>Limited:</b> Bow your performing Ninja Personality: The option to create an Attack Phase comes after the Dynasty Phase this turn.'
Nocturnal_Attack = Strategy(card_id=10385, title='Nocturnal Attack', gold_cost=0, focus_value=1, keywords=[Ninja], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<b>Battle:</b> Target two Personalities in the same army that do not share a Clan alignment: Give each target -3F.'
Now_We_Are_Enemies = Strategy(card_id=10386, title='Now We Are Enemies', gold_cost=0, focus_value=1, traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
"<b>Open:</b> If it is the active player's first or second turn: No Attack Phase may be declared.<br><b>Limited:</b> Target your discarded <i>(not dead)</i> Personality: Put him into one of your provinces, discarding any card currently there."
Overpower = Strategy(card_id=10387, title='Overpower', gold_cost=0, focus_value=4, traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'You may include up to seven copies of this card in your deck.<br><b>Battle:</b> Choose your performing unbowed Monk and target an enemy Personality or Follower: Give it -3F. If it has no attachments and you have played two or more other Pierce the Tapestry this battle, destroy it. If this did not destroy it, you may take an additional Battle action to play a Pierce the Tapestry.'
Pierce_the_Tapestery = Strategy(card_id=10388, title='Pierce the Tapestery', gold_cost=0, focus_value=1, keywords=[Kiho, Void], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
"<b>Open:</b> Choose your performing Personality and target a province: While at the province's battlefields, other players' Personalities and Followers have -1F and, if your performer is a Tactician, your Personalities and Followers have +1F."
Ready_the_Defenses = Strategy(card_id=10389, title='Ready the Defenses', gold_cost=0, focus_value=3, traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<b>Open:</b> Destroy your target non-Unique Holding: Create a 3F/3C/2PH <b>Samurai</b> Personality.'
Recruitment_Effort = Strategy(card_id=10390, title='Recruitment Effort', gold_cost=3, focus_value=2, traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<b>Open:</b> If <i>(and only if)</i> this card is in your discard pile, remove it from the game and target a player: He must choose and bow one of his unbowed Personalities, if possible. Gain 1 Honor.'
Scandalous_Gossip = Strategy(card_id=10391, title='Scandalous Gossip', gold_cost=1, focus_value=3, keywords=[Political], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
"<b>Battle:</b> Choose your performing unbowed Henshin and target a Personality: Switch the target's Force and Chi."
Shifting_Waves = Strategy(card_id=10392, title='Shifting Waves', gold_cost=0, focus_value=3, keywords=[Kiho], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
"<b>Battle/Open:</b> Destroy your performing Spirit Personality and target another Spirit Personality: Give it a permanent Force bonus equal to the performer's Force. It permanently copies the performer's abilities which do not themselves copy abilities. You may take an additional action."
Spiritual_Coalescence = Strategy(card_id=10393, title='Spiritual Coalescence', gold_cost=0, focus_value=3, traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'After a battle resolution ends in which you destroyed an army or province: Draw a card.<br><b>Limited:</b> Put this card into play. Discard all your other Kata in play.'
Spoils_of_Exploration = Strategy(card_id=10394, title='Spoils of Exploration', gold_cost=0, focus_value=3, keywords=[Kata], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<b>Open:</b> Bow and destroy your performing Shugenja and target a Personality: Give the target a -1F/-1C <b>Poison </b>token. Lose 3 Honor. Until the game ends, after each Events Phase begins, give the target a -1F/-1C <b>Poison</b> token.'
Suck_the_Marrow = Strategy(card_id=10395, title='Suck the Marrow', gold_cost=0, focus_value=0, keywords=[Maho, Plague], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
"<b>Open:</b> If it is not the active player's first turn, target a province: Cards will not enter play from the province <i>(this turn)</i>."
Sudden_Blockade = Strategy(card_id=10396, title='Sudden Blockade', gold_cost=3, focus_value=3, traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
"<b>Limited:</b> Choose your performing unbowed Commander, destroy his performing Follower, and target a Follower, or Personality without attachments, with Gold Cost equal to or less than twice your Follower's Gold Cost: Destroy the target."
Tactical_Sacrifice = Strategy(card_id=10397, title='Tactical Sacrifice', gold_cost=0, focus_value=2, traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<b>Battle:</b> Destroy your performing unbowed Courtier and target an enemy Personality: Dishonor him. You may target and destroy a card without attachments in his unit.'
The_Last_Move = Strategy(card_id=10398, title='The Last Move', gold_cost=0, focus_value=2, keywords=[Political], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<b>Battle/Open:</b> Choose your performing Personality and target your Personality: The performer permanently copies a keyword from target other than Courtier, Samurai, or Shugenja.<br><b>Limited:</b> Target your discarded Personality: Put him into your province <i>(face-up)</i> discarding the card currently there.'
The_Passing_of_Tradition = Strategy(card_id=10399, title='The Passing of Tradition', gold_cost=0, focus_value=2, traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<b>Battle:</b> Choose your performing unbowed Ninja Personality: Give each Personality and Follower opposing him -2F.'
Touch_of_the_Night = Strategy(card_id=10400, title='Touch of the Night', gold_cost=0, focus_value=2, keywords=[Fear, Ninja], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<b>Reaction:</b> When paying for a Personality with a Clan alignment different than your own: Produce 2 Gold.'
Truce = Strategy(card_id=10401, title='Truce', gold_cost=0, focus_value=2, traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<b>Reaction:</b> After a Ranged or Melee attack is targeted: Give it -2 strength.<br><b>Battle:</b> Choose your performing Personality: Move him to a battlefield where he would be opposed.'
Trusting_Instinct = Strategy(card_id=10402, title='Trusting Instinct', gold_cost=0, focus_value=1, traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
"After this battlefield's province is destroyed, if you are the Attacker: Draw a card, or two cards if your current army was ever opposed during this battle.<br><b>Battle:</b> If there is no Terrain in play at the current battlefield: Put this card into play there."
Vital_Pathways = Strategy(card_id=10403, title='Vital Pathways', gold_cost=0, focus_value=1, keywords=[Terrain], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
"Before this battle's resolution: Negate all Force bonuses from actions to cards at this battlefield.<br><b>Battle:</b> Even if you control no units at the current battlefield, if there is no Terrain in play there: Put this card into play there."
Warded_Premises = Strategy(card_id=10404, title='Warded Premises', gold_cost=0, focus_value=3, keywords=[Terrain], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<b>Reaction:</b> After a Battle action performed by your Samurai Personality resolves, if the action did not target an enemy card: Take an additional Battle action.'
Without_Mercy = Strategy(card_id=10405, title='Without Mercy', gold_cost=0, focus_value=1, keywords=[DarkVirtue, Determination], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])