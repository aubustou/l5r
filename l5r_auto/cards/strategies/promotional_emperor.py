from __future__ import annotations
from .common import Strategy
from l5r_auto.keywords import Imperial, Kharmic, Ninja, Siege, Unique
from l5r_auto.legality import EmperorEdition, IvoryEdition, ModernEdition
'<b>Battle/Open:</b> You may discard a card. Draw cards until you have exactly two cards in your hand.'
A_Glimpse_of_Fate = Strategy(card_id=10597, title='A Glimpse of Fate', focus_value=2, traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
'As a Focus Effect, after this duel ends, bow its winner.<br><b>Battle:</b> Target your performing unbowed Personality to make a Melee Attack with strength equal to 4 plus the number of Sake tokens he has.'
Bar_Fight = Strategy(card_id=696, title='Bar Fight', gold_cost=0, focus_value=3, traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<b>Reaction:</b> After an action resolves that moved a Personality to or from the current battlefield, target your performing Personality. Move him to the current battlefield, or from the current battlefield to your home. Straighten his unit if this moved him.'
Closing_the_Gap = Strategy(card_id=9989, title='Closing the Gap', gold_cost=0, focus_value=3, keywords=[Unique], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<b>Battle:</b> Straighten a target Ring. Before this phase ends, put this Strategy into your hand.'
Elemental_Adroitness = Strategy(card_id=10600, title='Elemental Adroitness', focus_value=4, keywords=[Unique], traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
'<i>(<b>Limited, :g2::</b> Discard a Kharmic card from your hand to draw a card.)</i><br><b>Battle/Open:</b> Bow a target Fallen card.'
Fallen = Strategy(card_id=10598, title='Fallen', focus_value=3, keywords=[Kharmic], traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
'<b>Open:</b> Target a Holding in your discard pile: Bring it into play <i>(bowed)</i>, paying all costs.<br><b>Battle/Open:</b> Choose your performing Personality and target a Follower or Item in your discard pile: Attach it to him, paying all costs.'
Govern_the_Land = Strategy(card_id=2877, title='Govern the Land', gold_cost=0, focus_value=4, traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
"<b>Battle:</b> If you destroy the enemy army or Province in this battle's resolution, give a +1F/+1C token to each of your Personalities in your army <i>(at battle resolution)</i>."
Imminent_Victory = Strategy(card_id=10601, title='Imminent Victory', focus_value=4, traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
'<b>Limited:</b> If it is not your first turn: Starting with you, each player may create an unbowed Holding with the trait "Bow this card: Produce 2 Gold."'
Imperial_Charter = Strategy(card_id=9990, title='Imperial Charter', gold_cost=0, focus_value=1, keywords=[Imperial], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
"<b>Reaction:</b> Before another player's action resolves: Negate its effects that bow, destroy, or discard your Holdings, Regions, or Terrains in play.<br><b>Open:</b> Pay 2 Gold: Draw a card."
Interrogation = Strategy(card_id=10239, title='Interrogation', gold_cost=0, focus_value=4, traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<b>Ninja Open:</b> Bow your target unbowed Personality or Follower to look at the top three cards of a deck, or four if you bowed a Ninja. You may discard one of them. Put the rest back in any order. Lose 1 Honor.'
It_Was_a_Cat = Strategy(card_id=10415, title='It Was a Cat', gold_cost=0, focus_value=1, keywords=[Ninja], traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
'<b>Battle/Open:</b> Target a Unique Personality: Bow him.'
Legendary_Rivalry = Strategy(card_id=9991, title='Legendary Rivalry', gold_cost=0, focus_value=3, traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<b>Limited:</b> Search your Dynasty deck for a non-Unique Holding. Bring it into play <i>(bowed)</i>, paying all costs.'
Peace = Strategy(card_id=5895, title='Peace', gold_cost=0, focus_value=4, keywords=[Unique], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'Before you produce Gold to pay for a card with a base Gold Cost of 1 or greater: You may reduce the total Gold produced by 1; if you did, put a <b>Wealth</b> token on this card after the other card enters play.<br><b>Limited:</b> Put this card into play.<br><b>Reaction:</b> When paying a Gold cost, if this card is in play, discard it: Produce Gold equal to the number of Wealth tokens on it before you discarded it.'
Profits = Strategy(card_id=6075, title='Profits', gold_cost=0, focus_value=2, traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<b>Limited:</b> Target a Castle Holding in your discard pile: Put it into play, paying all costs.<br><b>Battle:</b> Even if you control no units at the current battlefield, bow your target Castle and target an enemy Personality: Move him home.'
Refortification = Strategy(card_id=6192, title='Re-fortification', gold_cost=0, focus_value=3, keywords=[Siege], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
"<b>Open:</b> If it is not the active player's first or second turn, discard a card and choose your performing discarded Personality: Bring him into play, paying all costs."
Renewal = Strategy(card_id=6261, title='Renewal', gold_cost=0, focus_value=4, keywords=[Unique], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<b>Open:</b> Discard a card and choose your performing dead Personality: Bring him into play, paying all costs.'
Resurrection = Strategy(card_id=6281, title='Resurrection', gold_cost=0, focus_value=4, keywords=[Unique], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
"<b>Battle:</b> Destroy any player's Terrain or Region at the current battlefield and target a Personality: His path is blocked. Bow him or move him home."
Sinkhole = Strategy(card_id=9986, title='Sinkhole', gold_cost=0, focus_value=2, traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<b>Battle:</b> Bow your performing Personality: Ranged 4 Attack with +1 strength if he is an Alchemist and +1 strength for each different element keyword in his unit.'
Tamori_Potion = Strategy(card_id=7788, title='Tamori Potion', gold_cost=0, focus_value=2, traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<b>Limited:</b> Target a Castle Holding: Permanently remove one of its non-Gold-producing traits or abilities.<br><b>Limited:</b> If you control a Personality, pay 4 Gold: Create a 4F/2C/0PH <b>Shadowlands &#149; Nonhuman &#149; Oni</b> Personality. Lose 3 Honor.'
Through_the_Breach = Strategy(card_id=9992, title='Through the Breach', gold_cost=0, focus_value=3, keywords=[Siege], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
"<b>Reaction:</b> After another player's action targets your Personality, bow or destroy his target Armor: Negate his destruction from the action's effects."
Well_Protected = Strategy(card_id=9288, title='Well Protected', gold_cost=0, focus_value=1, traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
"<b>Open:</b> Target a Fortress tile: Flip it face-up or face-down <i>(unless it is a player's last face-up Fortress)</i>."
Wildfire = Strategy(card_id=9993, title='Wildfire', gold_cost=0, focus_value=4, traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])