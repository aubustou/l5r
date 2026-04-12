from __future__ import annotations
from ..common import Personality
from l5r_auto.clans import BrotherhoodOfShinsei, DragonClan, SpiritFaction
from l5r_auto.keywords import Courtier, Duelist, Earth, Experienced, Golem, Kensai, Magistrate, Monk, Nonhuman, Protector, Samurai, Shugenja, Spirit, Tactician, Tattooed, Unique, Void, Yojimbo
from l5r_auto.legality import EmperorEdition, ModernEdition, OnyxEdition, TwentyFestivalsEdition
"<b>Political Open, :bow::</b> A target Personality's printed abilities may not be used. You may ignore this action's cost of bowing Yoyugi if the target is non-Unique or Unicorn Clan."
Kitsuki_Yoyugi = Personality(card_id=9817, title='Kitsuki Yoyugi', force=3, chi=4, personal_honor=3, gold_cost=7, honor_requirement=5, clan=[DragonClan], keywords=[Duelist, Courtier, Magistrate], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<b>Battle:</b> Target a Personality with lower Force: Bow or straighten him.'
Mirumoto_Mitoshi = Personality(card_id=9818, title='Mirumoto Mitoshi', force=4, chi=3, personal_honor=2, gold_cost=7, honor_requirement=0, clan=[DragonClan], keywords=[Kensai, Samurai], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
"<b>Reaction:</b> After another player's action targets your Personality at Rokai's location, destroy Rokai: Negate your Personality's destruction from the action's effects."
Mirumoto_Rokai = Personality(card_id=9819, title='Mirumoto Rokai', force=3, chi=2, personal_honor=3, gold_cost=6, honor_requirement=0, clan=[DragonClan], keywords=[Samurai, Yojimbo], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'Shugorei has -2F while it is your turn.<br><b>Limited:</b> If you are a Dragon Clan player and none of your provinces have been destroyed since your last turn ended: Gain 2 Honor.'
Shugorei = Personality(card_id=9820, title='Shugorei', force=5, chi=2, personal_honor=2, gold_cost=7, honor_requirement=None, clan=[DragonClan, SpiritFaction], keywords=[Earth, Golem, Nonhuman, Protector, Shugenja, Spirit], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
"<i>(Battle: Discard a card to give this Tactician a Force bonus equal to the card's Focus Value.)</i> <br><b>Battle, :bow::</b> If Kasuru is attacking, draw a card. You may discard a card to straighten Kasuru."
Togashi_Kasuru = Personality(card_id=9821, title='Togashi Kasuru', force=3, chi=3, personal_honor=1, gold_cost=7, honor_requirement=0, clan=[DragonClan, BrotherhoodOfShinsei], keywords=[Tactician, Monk, Tattooed, Void], traits=[], abilities=[], legality=[TwentyFestivalsEdition, EmperorEdition, OnyxEdition, ModernEdition])
"While Korimi is defending, negate her bowing from other players' actions.<br><b>Battle:</b> Target an enemy card without unbowed attachments: Bow the target. You may discard a Kiho or Tattoo Strategy; if you did, destroy the target."
Togashi_Korimi_Experienced = Personality(card_id=9822, title='Togashi Korimi', force=6, chi=4, personal_honor=2, gold_cost=10, honor_requirement=4, clan=[DragonClan, BrotherhoodOfShinsei], keywords=[Unique, Earth, Experienced('1'), Monk, Tattooed], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])