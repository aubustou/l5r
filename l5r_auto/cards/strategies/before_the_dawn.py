from __future__ import annotations
from .common import Strategy
from l5r_auto.keywords import Air, BushidoVirtue, DarkVirtue, Determination, Duty, Earth, Fear, Heroic, Iaijutsu, Kata, Kiho, Ninja, Political, Tattoo, Thunder, Void, Water
from l5r_auto.legality import CelestialEdition, EmperorEdition, IvoryEdition, ModernEdition, TwentyFestivalsEdition
"As a Focus Effect, you may substitute one of your Yojimbo Personalities for your Personality in this duel.<br><b>Reaction:</b> After another player's action destroys one of your Courtier or Shugenja Personalities, give your target performing Yojimbo Personality three +1F <b>Revenge </b>tokens."
A_Champion_in_Court = Strategy(card_id=6, title='A Champion in Court', gold_cost=0, focus_value=3, traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
'<b>Limited:</b> Target your performing Magistrate to rehonor a target dishonorable Personality and gain 2 Honor.'
A_Gentle_Word = Strategy(card_id=29, title='A Gentle Word', gold_cost=0, focus_value=4, traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
"<b>Battle:</b> Move your target Personality home. If he is a Scout, straighten his unit. Raise or lower the current province's strength by his Force."
Advance_Warning = Strategy(card_id=121, title='Advance Warning', gold_cost=0, focus_value=2, traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
"<b>Limited:</b> Bow your target performing Artisan Personality to create a Personality with the same printed Force, Chi, Personal Honor and keywords as a target non-Unique Personality. The created Personality permanently copies all the non-Unique Personality's abilities except those that copy abilities. Remove the created Personality from the game when your next turn begins."
Amazing_Feat = Strategy(card_id=340, title='Amazing Feat', gold_cost=0, focus_value=4, traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
'<b>Heroic Battle:</b> Target your performing unbowed Hero to target an enemy card. If it has no attachments, and is bowed or Nonhuman, destroy it. Bow it.'
Anger_Management = Strategy(card_id=406, title='Anger Management', gold_cost=0, focus_value=2, keywords=[Heroic], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
'<b>Battle/Open:</b> Target your performing Paragon and bow him unless this is the Attack Phase to bow a target Personality with lower Force and lose 3 Honor.'
Ascending_the_Ranks = Strategy(card_id=599, title='Ascending the Ranks', gold_cost=0, focus_value=2, traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
"<b>Battle:</b> Take an additional action to use a Limited or Open Recon ability as a Battle action, which must target the current battlefield's province. If you do, draw a card after the action's resolution."
Beyond_the_Line = Strategy(card_id=967, title='Beyond the Line', gold_cost=0, focus_value=2, traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
'<b>Battle/Open:</b> Target two or three of your performing Samurai. Each of them has +1F and the ability, "<b>Battle:</b> Ranged 4 Attack" while in an army with one or more of the others.'
Brothers_in_Battle = Strategy(card_id=1164, title='Brothers in Battle', gold_cost=0, focus_value=3, keywords=[BushidoVirtue, Duty], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
'<b>Fear Battle:</b> Target your performing Shadowlands Personality and remove a target dead Personality in any discard pile from the game to give your Personality +3F, or +4F if he is Undead.'
Consuming_Weakness = Strategy(card_id=1467, title='Consuming Weakness', gold_cost=0, focus_value=1, keywords=[Fear], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
'<b>Battle:</b> Destroy a target Terrain.<br><b>Tactical Battle:</b> Target your performing unbowed Tactician to give a target Follower or Personality -6F and bow it.'
Control_the_Board = Strategy(card_id=1486, title='Control the Board', gold_cost=0, focus_value=3, traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
'<b>Heroic Battle:</b> Give your target performing unbowed Hero +2F for each Personality you control not at the current battlefield.'
Defending_Their_Home = Strategy(card_id=1930, title='Defending Their Home', gold_cost=0, focus_value=3, keywords=[Heroic], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
'You have the ability, "<b>Political Reaction:</b> Before you gain Honor during your turn, bow your target performing Courtier to negate the gain and choose a player who loses 2 Honor."<br><b>Political Limited:</b> Put this card into play. Discard your other Kata in play.'
Destructive_Priorities = Strategy(card_id=1983, title='Destructive Priorities', gold_cost=0, focus_value=1, keywords=[Kata, Political], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
'<b>Political Reaction:</b> After engaging, bow your target performing Magistrate to move home a target enemy dishonorable Personality at the current battlefield. If this moved him, bow his unit, and his controller loses 2 Honor.'
Detained = Strategy(card_id=1984, title='Detained', gold_cost=2, focus_value=3, keywords=[Political], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
"<b>Battle:</b> Even if you control no units at the current battlefield, pay Gold equal to a target Personality or unit's total Gold cost minus 4: Bow it."
Disgraceful_Conduct = Strategy(card_id=2020, title='Disgraceful Conduct', gold_cost=0, focus_value=2, traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
'<b>Political Battle:</b> Bow your target performing Courtier at any location to move home a target enemy Personality with equal or lower Personal Honor. Destroy him if he has no attachments. Gain 2 Honor.'
Dismissing_the_Cur = Strategy(card_id=2027, title='Dismissing the Cur', gold_cost=0, focus_value=2, keywords=[Political], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
'<b>Battle:</b> Bow your performing Scout and target an enemy card: Bow it. The enemy leader discards a card of his choice, or a random card if you have Reconnaissance.'
Disrupting_Communication = Strategy(card_id=2035, title='Disrupting Communication', gold_cost=0, focus_value=1, traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
'<b>Political Limited:</b> Bow your target unbowed Courtier. A target player gains or loses 2 Honor.'
Favors = Strategy(card_id=2492, title='Favors', gold_cost=0, focus_value=2, keywords=[Political], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, EmperorEdition, CelestialEdition, ModernEdition])
'<b>Battle:</b> Choose your performing unbowed Duelist and target an enemy Personality with equal or lower Chi: Move him home. If he moved, choose a player, who gains or loses 2 Honor.'
Fear_Me = Strategy(card_id=2493, title='Fear Me!', gold_cost=0, focus_value=4, keywords=[Fear, Iaijutsu], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
"<b>Open:</b> Choose your performing Samurai and target another player's Personality or Follower: Negate the effects of the next action performed by the targeted card <i>(this turn)</i>. Bow it if it has no attachments and is not a Samurai."
Firm_Censure = Strategy(card_id=2580, title='Firm Censure', gold_cost=0, focus_value=1, traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
'<b>Reaction:</b> Before an Event resolves: Negate its effects.<br><b>Battle:</b> Choose your performing Personality: Move him home. Straighten his unit if he moved.'
Forging_Destiny = Strategy(card_id=2652, title='Forging Destiny', gold_cost=0, focus_value=4, traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
'<b>Battle:</b> If your current army has more units than the current enemy army, bow your two performing Nonhumans and target an enemy unit: Destroy it.'
Fury_of_a_Mob = Strategy(card_id=2738, title='Fury of a Mob', gold_cost=0, focus_value=1, traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
'<b>Battle:</b> Choose your performing Berserker, bow him unless he was not in play when this Combat Segment began, and target an enemy card without attachments and with equal or lower Force: Destroy it.'
Headbutt = Strategy(card_id=3010, title='Headbutt', gold_cost=0, focus_value=1, traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
"<b>Reaction:</b> After another player targets your Paragon with a Battle action performed by a Personality with lower Personal Honor: The action's costs are ignored and its effects are negated. That player may take an additional Battle action."
Iron_Will = Strategy(card_id=3813, title='Iron Will', gold_cost=0, focus_value=3, traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
'<b>Reaction:</b> After the resolution of a Battle action that destroyed one of your Deathseekers: Create a 2F/2C/0PH <b>Lion Clan &#149; Samurai &#149; Deathseeker</b> Personality at the current battlefield. Gain 1 Honor.'
Measure_of_Devotion = Strategy(card_id=5013, title='Measure of Devotion', gold_cost=0, focus_value=3, traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
'<b>Open:</b> If you control a Personality, target a Personality and pay Gold equal to the number of Personalities you control, or 4, whichever is higher: The targeted Personality may not assign to battlefields.'
Necessary_Evil = Strategy(card_id=5524, title='Necessary Evil', gold_cost=0, focus_value=1, traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
"<b>Reaction:</b> After an attacking player announces a Battle action before the Defender's first normal opportunity to act or pass: Negate its effects.<br><b>Open:</b> Choose your performing dishonorable Personality: Rehonor him. After the next time <i>(this turn)</i> you lose Honor from another player's card effect, give him three +1F <b>Revenge</b> tokens."
No_Time_for_Games = Strategy(card_id=5605, title='No Time for Games', gold_cost=0, focus_value=4, keywords=[Political], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
'As a Focus Effect: Give your Personality in this duel <b>Tactician</b>.<br><b>Battle/Open:</b> Choose your performing Duelist: Give him a Force bonus equal to his own base Chi.'
Of_One_Instant = Strategy(card_id=5668, title='Of One Instant', gold_cost=0, focus_value=4, keywords=[Iaijutsu], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
'<b>Battle:</b> If the enemy leader has taken any Battle actions during this battle: You may take two additional Battle actions after this one. You will not take any other additional Battle actions this battle.'
One_Action_Two_Strikes = Strategy(card_id=5706, title='One Action, Two Strikes', gold_cost=0, focus_value=1, traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
'<b>Battle/Open:</b> Choose your performing Kensai: Straighten his unit if he has a Weapon. You may attach a Weapon to him from your discard pile, paying all costs and paying 2 less Gold.'
Readied_Steel = Strategy(card_id=6195, title='Readied Steel', gold_cost=0, focus_value=3, traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
"<b>Battle:</b> Bow your performing Personality and target an enemy card without attachments: Bow it. Destroy it if it is an attachment or its base Gold Cost is 0. Before this battle's resolution, straighten your Personality."
Reckless_Rush = Strategy(card_id=6211, title='Reckless Rush', gold_cost=0, focus_value=3, traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
"<b>Battle:</b> Choose your performing unbowed Samurai and target an enemy card without attachments: Bow it. Destroy it if another player's action has destroyed one of your Personalities since the end of your last Battle action this battle."
Revenge = Strategy(card_id=6302, title='Revenge', gold_cost=0, focus_value=3, keywords=[DarkVirtue, Determination], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
'<b>Limited:</b> Bow your performing Courtier and target a Holding: Until the game ends, after each time it bows or an ability on it resolves, its controller loses 1 Honor.'
Scars_of_War = Strategy(card_id=6490, title='Scars of War', gold_cost=2, focus_value=1, keywords=[Political], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
"As a Focus Effect: After this duel ends, the loser's controller draws a card.<br><b>Battle:</b> Choose your performing Personality: Rehonor him. If he is opposed, straighten him. You may move him home."
Shadow_Tactics = Strategy(card_id=6662, title='Shadow Tactics', gold_cost=0, focus_value=2, traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
'<b>Battle:</b> Choose your performing Monk: Negate all current Force penalties on him from actions. If he has a Weapon, negate the next card effect that moves him home or bows him.'
Show_of_Restraint = Strategy(card_id=7197, title='Show of Restraint', gold_cost=0, focus_value=3, keywords=[Kiho], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
"<b>Limited:</b> Choose your performing Ninja Personality and target a non-Unique Personality: Your Ninja permanently copies the Personality's base keywords, except Clan Champion, Daimyo, or Shugenja, and permanently copies his base abilities which do not themselves copy abilities."
Sly_Deceiver = Strategy(card_id=7301, title='Sly Deceiver', gold_cost=0, focus_value=4, keywords=[Ninja], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
'<b>Limited:</b> Choose your performing unbowed Personality: If he is a Kensai, permanently give him the ability, "<b>Battle:</b> Bow one of this Personality\'s Weapons and target an enemy card without attachments: Destroy it." Otherwise, permanently give him <b>Kensai</b>.'
Spirit_of_the_Blade = Strategy(card_id=7421, title='Spirit of the Blade', gold_cost=0, focus_value=4, traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
'<b>Limited:</b> Choose your performing unbowed Personality: If he is a Ninja, permanently give him the ability, "<b>Ninja Battle:</b> Target two Personalities controlled by the same player at different locations: Switch their locations." Otherwise, permanently give him <b>Ninja</b>.'
Spirit_of_the_Shadows = Strategy(card_id=7427, title='Spirit of the Shadows', gold_cost=0, focus_value=4, traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
'<b>Limited:</b> Choose your performing unbowed Personality: If he is a Magistrate, permanently give him +1C and the ability, "<b>Political Open:</b> If it is not your turn, bow this Personality and target a dishonorable Personality: Bow him." Otherwise, permanently give him <b>Magistrate</b>.'
Spirit_of_the_Truth = Strategy(card_id=7428, title='Spirit of the Truth', gold_cost=0, focus_value=4, traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
'<b>Limited:</b> Choose your performing unbowed Personality: If he is a Commander, permanently give him the ability, "<b>Battle:</b> Bow one of this Personality\'s performing Followers and target an enemy card without attachments: Destroy it." Otherwise, permanently give him <b>Commander</b>.'
Spirit_of_the_Warrior = Strategy(card_id=7429, title='Spirit of the Warrior', gold_cost=0, focus_value=4, traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
'<b>Reaction:</b> After engaging, choose your performing Personality at the current battlefield and target an attachment in your hand: Attach it to your Personality, paying all costs and paying 4 less Gold if he is a Commander.'
Stockpiled_Resources = Strategy(card_id=7492, title='Stockpiled Resources', gold_cost=0, focus_value=3, traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
'<b>Battle:</b> Choose your performing Monk, who must be unbowed unless he is Earth, and target an enemy Personality or Follower: Bow it.'
Strength_of_the_Mountain = Strategy(card_id=7557, title='Strength of the Mountain', gold_cost=0, focus_value=2, keywords=[Earth, Kiho], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
'<b>Battle/Open:</b> Straighten all of your Rings. You may put a Ring in your Fate discard pile into your hand. You may take an additional action appropriate to this phase.'
String_of_Victories = Strategy(card_id=7588, title='String of Victories', gold_cost=0, focus_value=4, traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
"<b>Limited:</b> Choose your performing Courtier and target another player's dishonorable Personality: He is asked to make a sacrifice. The player may show you his hand. If he does, you may discard a card from it. If he does not choose this, his Personality will not be affected by the rulebook seppuku action."
The_Price_of_Honor = Strategy(card_id=8268, title='The Price of Honor', gold_cost=0, focus_value=1, keywords=[Political], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
'<b>Battle:</b> Move your performing Ninja Personality home and target an enemy card: Bow it. Negate its next straightening <i>(this turn)</i>.'
The_Second_Feint = Strategy(card_id=8305, title='The Second Feint', gold_cost=0, focus_value=2, keywords=[Ninja], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
'<b>Battle:</b> Choose your performing Battle Maiden and target an enemy Personality: Move your Battle Maiden to the current battlefield. Straighten her if she moved. Give the enemy Personality -3F.'
The_Sound_of_Thunder = Strategy(card_id=8347, title='The Sound of Thunder', gold_cost=0, focus_value=2, traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
'<b>Limited:</b> Choose your performing unbowed Personality: If he is a Tactician, permanently give him the ability, "<b>Tactical Battle:</b> Bow this Personality: Draw a card." Otherwise, permanently give him <b>Tactician</b>.'
The_Spirit_of_Knowledge = Strategy(card_id=8353, title='The Spirit of Knowledge', gold_cost=0, focus_value=4, traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
'<b>Open:</b> Bow your performing Monk unless he is Void: He meditates. Put a Kiho Strategy in your discard pile into your hand.'
The_World_Disappears = Strategy(card_id=8436, title='The World Disappears', gold_cost=0, focus_value=3, keywords=[Kiho, Void], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
'<b>Open:</b> Choose your performing unbowed Monk: Give him <b>Cavalry</b>. If you control any Rings or he is Air, give him +4F.'
Thoughts_of_Wind = Strategy(card_id=8452, title='Thoughts of Wind', gold_cost=0, focus_value=4, keywords=[Air, Kiho], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
'<b>Water Battle:</b> Target your performing unbowed Tattooed Personality to move home a target an enemy Personality. This movement will not be negated if your Personality is Water. After this moves the enemy Personality, bow his unit.'
Tsunami_Tattoo = Strategy(card_id=8793, title='Tsunami Tattoo', gold_cost=0, focus_value=2, keywords=[Tattoo, Water], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
'<b>Battle:</b> Choose your performing unbowed Samurai and target an enemy card: Bow it.'
Unorthodox_Attack = Strategy(card_id=8999, title='Unorthodox Attack', gold_cost=0, focus_value=3, traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
'<b>Battle:</b> Choose your performing opposed unbowed Thunder Personality: Raise his Force to 6. You may target and bow an enemy card with lower Force and no attachments.'
Visage_of_the_Orochi = Strategy(card_id=9168, title='Visage of the Orochi', gold_cost=0, focus_value=1, keywords=[Fear, Thunder], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])