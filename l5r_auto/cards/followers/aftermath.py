from __future__ import annotations
from .common import Follower
from l5r_auto.keywords import Ashigaru, Cavalry, Expendable, Gaijin, Horse, Nonhuman, Reserve, Ronin, Scout, Shadowlands, Undead, Yodotai
from l5r_auto.legality import EmperorEdition, IvoryEdition, ModernEdition, OnyxEdition, TwentyFestivalsEdition
'After this Follower enters play, target one or two of your Personalities. Create and attach a 1F Ronin Follower to each of them.'
Band_of_Brothers = Follower(card_id=10891, title='Band of Brothers', force=2, chi=0, gold_cost=8, focus_value=2, keywords=[Ronin], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, EmperorEdition, OnyxEdition, ModernEdition])
"<b>Limited:</b> Straighten another player's target Holding with Gold Cost equal to or lower than this Follower's Force. You, and not its owner, may use its Gold-producing and cost-reducing traits <i>(this turn)</i> as if you controlled it."
Black_Riders = Follower(card_id=10892, title='Black Riders', force=2, chi=0, gold_cost=5, focus_value=3, keywords=[Cavalry], traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
'Will only attach to a Human.<br>This Personality has <b>Conqueror</b>.'
Commanders_Steed = Follower(card_id=10893, title="Commander's Steed", force=2, chi=0, gold_cost=4, focus_value=3, keywords=[Cavalry, Horse, Nonhuman], traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
'<b>Political Open, :bow::</b> Increase the next Honor gain or loss <i>(this turn)</i> from your cards by 1 <i>(Proclaiming gains are not from your cards)</i>.'
Court_Scribe = Follower(card_id=10894, title='Court Scribe', force=0, chi=0, gold_cost=4, focus_value=3, traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
'This Follower has +2F while defending.<br>After this Follower is destroyed during battle, gain 1 Honor.'
Disciples_of_Ganesh = Follower(card_id=10895, title='Disciples of Ganesh', force=1, chi=0, gold_cost=2, focus_value=4, keywords=[Gaijin], traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
'<i>(You may Equip a Reserve attachment, if it would be opposed, as a <b>Battle</b> action.)</i>'
Floating_Reserve = Follower(card_id=10896, title='Floating Reserve', force=2, chi=0, gold_cost=2, focus_value=2, keywords=[Reserve], traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
'<i>(Draw a card after your Expendable card dies.)</i>'
Front_Rank_Troops = Follower(card_id=10897, title='Front Rank Troops', force=4, chi=0, gold_cost=7, focus_value=4, keywords=[Expendable], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, EmperorEdition, OnyxEdition, ModernEdition])
"After this Follower enters play, lose 3 Honor.<br>Before the first time this game another player's card destroys this Follower, negate the destruction."
Legion_of_the_Fallen = Follower(card_id=10898, title='Legion of the Fallen', force=3, chi=0, gold_cost=4, focus_value=1, keywords=[Nonhuman, Shadowlands, Undead], traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
"After this Follower enters play, lose 3 Honor.<br><b>Battle, :bow::</b> Melee Attack with strength equal to this Follower's Force."
Leguluss_Legion = Follower(card_id=10899, title="Legulus's Legion", force=3, chi=0, gold_cost=5, focus_value=2, keywords=[Gaijin, Yodotai], traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
'<b>Home Battle/Open:</b> Transfer this card to your target Personality. <i>(Home actions may be used from home.)</i>'
LongRange_Scouts = Follower(card_id=10900, title='Long-Range Scouts', force=3, chi=0, gold_cost=5, focus_value=1, keywords=[Cavalry, Scout], traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
'Melee Attacks may not target this Follower.'
Seasoned_Ashigaru = Follower(card_id=10901, title='Seasoned Ashigaru', force=1, chi=0, gold_cost=1, focus_value=1, keywords=[Ashigaru], traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
'Other Followers in this unit have +1F.'
Senior_Infantry_Legion = Follower(card_id=10902, title='Senior Infantry Legion', force=3, chi=0, gold_cost=6, focus_value=2, traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])