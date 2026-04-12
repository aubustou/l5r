from __future__ import annotations
from .common import Follower
from l5r_auto.keywords import Ashigaru, Cavalry, Courage, Destined, Expendable, Geisha, Jade, Maiko, Mercenary, Monk, Naga, Nonhuman, Pirate, Reserve, Ronin, Scout
from l5r_auto.legality import IvoryEdition, ModernEdition, TwentyFestivalsEdition
"You may destroy any player's Farm to ignore the Gold cost of Equipping this Follower.<br><b>Battle:</b> Give a target enemy Samurai -3F."
Colonial_Conscripts = Follower(card_id=11622, title='Colonial Conscripts', force=2, chi=0, gold_cost=2, focus_value=1, traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition])
'<i>(You may Equip a Reserve attachment, if it would be opposed, as a Battle action.)</i><br><b>Interrupt:</b> After you Equip this Follower, take an additional action.<br><b>Battle, :bow::</b> Ranged 2 Attack.'
Dark_Naga_Ambusher = Follower(card_id=11623, title='Dark Naga Ambusher', force=2, chi=0, gold_cost=4, focus_value=1, keywords=[Reserve, Naga, Nonhuman, Scout], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition])
"This Follower contributes Force even while bowed and it is considered to have 3 Chi when a Kiho checks a card's Chi."
Dragon_Elite_Inkyo = Follower(card_id=11624, title='Dragon Elite Inkyo', force=3, chi=0, gold_cost=5, focus_value=4, keywords=[Jade, Monk], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition])
'<i>(Draw a card after your Expendable card dies.)</i><br>After a Fear effect bows this Follower, destroy it.'
Front_Line_Fodder = Follower(card_id=11625, title='Front Line Fodder', force=3, chi=0, gold_cost=3, focus_value=1, keywords=[Expendable, Ashigaru], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition])
'<i>(<b>Repeatable Interrupt:</b> Discard a Courage card to give a Fear effect +2 or -2 strength.)</i><br>Fear effects, Melee Attacks, and Ranged Attacks targeting cards in this unit have -1 strength.'
Ichigos_Guard = Follower(card_id=11626, title="Ichigo's Guard", force=3, chi=0, gold_cost=4, focus_value=3, keywords=[Courage], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition])
'Fear effects, Melee Attacks, and Ranged Attacks targeting this Follower have -2 strength.<br><b>Battle:</b> Ranged 3 Attack.'
Legion_of_the_Khan = Follower(card_id=11627, title='Legion of the Khan', force=3, chi=0, gold_cost=8, focus_value=1, keywords=[Cavalry, Destined], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition])
'This Personality has <b>Resilient</b>. <i>(Once per game per card, a Resilient card does not die in battle resolution.)</i>'
Mercenary_Guard = Follower(card_id=11628, title='Mercenary Guard', force=2, chi=0, gold_cost=3, focus_value=3, keywords=[Expendable, Mercenary, Ronin], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition])
'<i>(Once per turn, as an <b>Absent Engage</b>, move your unbowed Personality in a Cavalry unit to the battle.)</i> <br><b>Battle:</b> Give a target enemy Follower or Personality -2F, or -3F if this Personality has moved this turn.'
Mounted_Skirmishers = Follower(card_id=11629, title='Mounted Skirmishers', force=2, chi=0, gold_cost=3, focus_value=2, keywords=[Cavalry], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition])
'<i>(<b>Repeatable Interrupt:</b> Discard a Courage card to give a Fear effect +2 or -2 strength.)</i><br><b>Battle:</b> Move home this unit and a target enemy unit with equal or lower total Force.'
Pursuit_Riders = Follower(card_id=11630, title='Pursuit Riders', force=2, chi=0, gold_cost=4, focus_value=3, keywords=[Cavalry, Courage, Reserve], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition])
'This Follower has +1F while you control a Port.<br><b>Battle, :bow::</b> Ranged 2 Attack.'
Sons_of_Gusai = Follower(card_id=11631, title='Sons of Gusai', force=1, chi=0, gold_cost=2, focus_value=1, keywords=[Mercenary, Pirate], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition])
'Invest :g1:: Search your deck for a Spider Elite Sohei, show it, and put it in your hand.<br><b>Battle:</b> Fear 3.'
Spider_Elite_Sohei = Follower(card_id=11632, title='Spider Elite Sohei', force=4, chi=0, gold_cost=8, focus_value=1, keywords=[Reserve, Monk], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition])
"<b>Open, :bow::</b> A target player shows a random card in his hand.<br><b>Open, :bow::</b> Turn a target card in another player's Province face-up."
Talented_Maiko = Follower(card_id=11633, title='Talented Maiko', force=0, chi=0, gold_cost=1, focus_value=3, keywords=[Geisha, Maiko], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition])