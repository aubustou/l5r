from __future__ import annotations
from .common import Sensei
from l5r_auto.keywords import AllClans, Crab, Crane, Dragon, Lion, Mantis, Phoenix, Scorpion, Spider, Unicorn
from l5r_auto.legality import ModernEdition, OnyxEdition, TwentyFestivalsEdition
'Iaijutsu actions you take are Ninja instead. Reduce your Honor losses from your Ninja cards by 2.<br><b>Interrupt, :bow::</b> After another player refuses a challenge or loses a duel from an action that targeted his Personality and your Ninja, give a -1F/-1C Poison token to his Personality.'
Aroru_Sensei = Sensei(card_id=12245, title='Aroru Sensei', gold_production='-1', starting_family_honor=-1, province_strength=0, traits=[], abilities=[], legality=[TwentyFestivalsEdition, ModernEdition])
'You Equip non-Water Spells for 1 more Gold. After your Water card moves a Personality, give your target Water Shugenja +1F. You may Equip Water Spells to your unbowed opposed Shugenja as a Battle action.'
Chukage_Sensei = Sensei(card_id=12246, title='Chukage Sensei', gold_production='+0', starting_family_honor=0, province_strength=0, traits=[], abilities=[], legality=[TwentyFestivalsEdition, ModernEdition])
"Your Stronghold has no abilities.<br><b>Limited, :bow::</b> Target your unbowed Thunder Personality. Bow a target card in a unit; the card's attachments, if any, must be bowed. If this bowed a Personality, bow your Thunder Personality."
Chuuna_Sensei = Sensei(card_id=12247, title='Chuuna Sensei', gold_production='+0', starting_family_honor=0, province_strength=0, traits=[], abilities=[], legality=[TwentyFestivalsEdition, ModernEdition])
"You may not bring Shadowlands cards into play.<br><b>Interrupt, :bow::</b> If the action targeted your Shugenja with an attached Earth Spell, the action's player discards a card after it resolves."
Daigo_Sensei = Sensei(card_id=12248, title='Daigo Sensei', gold_production='+0', starting_family_honor=-1, province_strength=-1, traits=[], abilities=[], legality=[TwentyFestivalsEdition, ModernEdition])
'Your non-Fortification Holdings enter play for 1 more Gold. Each Province you assigned a Personality to defend or with a Cavalry unit attacking it has +1 strength for each Fortification attached to it, and has a maximum strength equal to its printed strength +4.'
Dijuro_Sensei = Sensei(card_id=12249, title='Dijuro Sensei', gold_production='+0', starting_family_honor=0, province_strength=0, keywords=[Crane, Dragon, Phoenix, Scorpion], traits=[], abilities=[], legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition])
'Your Stronghold has no abilities. Your Magistrates have +1F while opposing any dishonorable Personalities. After each time your Battle action bows or destroys a dishonorable Personality, gain 1 Honor.'
Hakuseki_Sensei = Sensei(card_id=12250, title='Hakuseki Sensei', gold_production='+0', starting_family_honor=0, province_strength=0, traits=[], abilities=[], legality=[TwentyFestivalsEdition, ModernEdition])
'Your Stronghold has no abilities. When Recruiting Dragons, you may Proclaim them, and may compare their Honor Requirement to the total Force of your non-Shadowlands Personalities instead of to your Honor.'
Kiyoteru_Sensei = Sensei(card_id=12251, title='Kiyoteru Sensei', gold_production='+0', starting_family_honor=0, province_strength=0, keywords=[AllClans], traits=[], abilities=[], legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition])
'Reduce your Honor losses from your Duelists by 2.<br><b>Interrupt, :bow::</b> If the action creates a duel, after your Personality wins, give him "<b>Battle:</b> Fear equal to this Personality\'s Force."'
Sahara_Sensei = Sensei(card_id=12252, title='Sahara Sensei', gold_production='+0', starting_family_honor=0, province_strength=-1, traits=[], abilities=[], legality=[TwentyFestivalsEdition, ModernEdition])
'<b>Interrupt, :bow::</b> If the action is Battle and creates a duel, after your Personality wins it, give him a Force bonus equal to his Personal Honor.'
Seijuro_Sensei = Sensei(card_id=12253, title='Seijuro Sensei', gold_production='+0', starting_family_honor=0, province_strength=-1, traits=[], abilities=[], legality=[TwentyFestivalsEdition, ModernEdition])
"<b>Battle, :bow::</b> Bow your target unbowed Follower or Weapon. Melee Attack with strength equal to its Force <i>(An Item's Force is its Force Modifier)</i>."
Taitaken_Sensei = Sensei(card_id=12254, title='Taitaken Sensei', gold_production='+0', starting_family_honor=-1, province_strength=-1, keywords=[Crab, Lion, Mantis, Spider, Unicorn], traits=[], abilities=[], legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition])
"<b>Open, :bow::</b> Bow your target unbowed Magistrate. Rehonor and bow another player's target dishonorable Personality. Gain Honor equal to the second target's Personal Honor if his controller has more Honor than you."
Tselu_Sensei = Sensei(card_id=12255, title='Tselu Sensei', gold_production='+0', starting_family_honor=0, province_strength=-1, traits=[], abilities=[], legality=[TwentyFestivalsEdition, ModernEdition])
"Your Stronghold has no abilities.<br>After your action dishonors another player's Personality, gain 1 Honor."
Yodo_Sensei = Sensei(card_id=12256, title='Yodo Sensei', gold_production='+0', starting_family_honor=0, province_strength=2, traits=[], abilities=[], legality=[TwentyFestivalsEdition, ModernEdition])