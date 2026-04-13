from __future__ import annotations
from ..common import Personality
from l5r_auto.clans import BrotherhoodOfShinsei, ShadowlandsFaction, SpiderClan
from l5r_auto.keywords import Air, Cavalry, Commander, Conqueror, Courtier, Daimyo, Experienced, Fallen, Kensai, Loyal, Magistrate, Monk, MonkeyClan, Samurai, Shadowlands, TheMetalStorm, TheWhisper, Unique
from l5r_auto.legality import EmperorEdition, IvoryEdition, ModernEdition
'After Arakan enters play, lose 2 Honor.<br><b>Maho Battle/Limited, :gstar::</b> Equip a non-Unique Follower in your discard pile to Arakan or Zansho.  Permanently give the Follower <b>Shadowlands &#149; Undead</b>. Lose 2 Honor.'
Daigotsu_Arakan_Experienced = Personality(card_id=10485, title='Daigotsu Arakan', force=6, chi=3, personal_honor=0, gold_cost=9, honor_requirement=None, clan=[SpiderClan, ShadowlandsFaction], keywords=[Conqueror, Unique, Commander, Experienced('1'), Samurai, Shadowlands], traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
"After Gyoken enters play, lose 3 Honor.<br>Negate Gyoken's first destruction each game from another player's card."
Daigotsu_Gyoken_Experienced_3 = Personality(card_id=10487, title='Daigotsu Gyoken', force=6, chi=3, personal_honor=0, gold_cost=9, honor_requirement=None, clan=[SpiderClan, ShadowlandsFaction], keywords=[Conqueror, Experienced('3'), Unique, Commander, Fallen, Samurai, Shadowlands], traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
'After Nishiguchi enters play, lose 2 Honor.<br><b>Battle:</b> Give a target enemy Personality a Force penalty equal to the number of <b>Madness </b>tokens he has.'
Nishiguchi = Personality(card_id=10488, title='Nishiguchi', force=3, chi=3, personal_honor=0, gold_cost=5, honor_requirement=None, clan=[SpiderClan, BrotherhoodOfShinsei], keywords=[Kensai, Fallen, Monk], traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
'After you Proclaim Susumu Takuan, gain 2 Honor.<br><b>Political Limited, :bow::</b> Take the Imperial Favor.'
Susumu_Kuroko = Personality(card_id=10489, title='Susumu Kuroko', force=2, chi=4, personal_honor=3, gold_cost=6, honor_requirement=1, clan=[SpiderClan], keywords=[Loyal, Unique, Courtier, Daimyo, Magistrate], traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
'Saiga has +1F/+1C for each of his Weapons.'
Toku_Saiga_the_Metal_Storm = Personality(card_id=10490, title='Toku Saiga, the Metal Storm', force=3, chi=2, personal_honor=2, gold_cost=5, honor_requirement=None, clan=[SpiderClan], keywords=[Kensai, Unique, MonkeyClan, Samurai, TheMetalStorm], traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
'Yunmen enters play ignoring Gold Cost if you control the Ring of Air.<br><b>Air Open, :bow::</b> Give one to three target cards <b>Cavalry</b>.'
Yunmen_the_Whisper = Personality(card_id=10491, title='Yunmen, the Whisper', force=1, chi=3, personal_honor=3, gold_cost=5, honor_requirement=0, clan=[SpiderClan, BrotherhoodOfShinsei], keywords=[Cavalry, Unique, Air, Monk, TheWhisper], traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])