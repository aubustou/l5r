from __future__ import annotations
from .common import Sensei
from l5r_auto.keywords import AllClans, Crab, Crane, Dragon, Lion, Mantis, Phoenix, Scorpion, Spider, Unicorn
from l5r_auto.legality import ModernEdition, OnyxEdition, TwentyFestivalsEdition
'You may include four copies of each non-Unique Ashigaru Personality in your deck. Your non-Ashigaru Personalities in and out of play have +1 Gold Cost. You can not play Oath of Fealty.<br><b>Open, :bow:, :g2::</b> If you control an Ashigaru Personality, create a 0F/1C/0PH <b>Ashigaru &#149; Conscript</b> Personality.'
Hikahime_Sensei = Sensei(card_id=12417, title='Hikahime Sensei', gold_production='-1', starting_family_honor=-2, province_strength=0, keywords=[AllClans], traits=[], abilities=[], legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition])
'You may not take more than six actions from Events per game.<br><b>Open, :bow::</b> If you have taken an action from an Event in your Province this turn, turn a card in your Provinces face-up.'
Hira_Sensei = Sensei(card_id=12418, title='Hira Sensei', gold_production='+0', starting_family_honor=0, province_strength=-1, keywords=[Crane, Mantis, Phoenix], traits=[], abilities=[], legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition])
"After an enemy card is destroyed during a battle, if the destruction was not from another player's card effect, gain 1 Honor."
Ichigo_Sensei = Sensei(card_id=12419, title='Ichigo Sensei', gold_production='+0', starting_family_honor=0, province_strength=-1, keywords=[Crab, Dragon, Lion, Scorpion, Unicorn], traits=[], abilities=[], legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition])
'You may only Recruit Shadowlands Personalities. You do not lose Honor from your Shadowlands Followers and Human Shadowlands Personalities. Fear actions from your Spider Clan Personalities and Stronghold destroy attachments after bowing them.'
Yajinden_Sensei = Sensei(card_id=12420, title='Yajinden Sensei', gold_production='+0', starting_family_honor=-2, province_strength=-1, keywords=[Spider], traits=[], abilities=[], legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition])