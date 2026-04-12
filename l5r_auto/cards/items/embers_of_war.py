from __future__ import annotations
from .common import Item
from l5r_auto.keywords import AkkuaiUo, Armor, Enginoshi, Experienced, Imperial, Shinrai, Unique, Weapon
from l5r_auto.legality import EmperorEdition, ModernEdition
"Melee Attacks targeting cards in this unit have -2 strength.<br><b>Reaction:</b> Before another player's action resolves, negate this Personality's movement from the action's effects."
Armor_of_the_Uruwashii = Item(card_id=453, title='Armor of the Uruwashii', force=3, chi=0, gold_cost=4, focus_value=2, keywords=[Armor, Imperial], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'Will only attach to a Lion Clan Personality.<br>This card has +1F for each Lion Clan Personality you control.<br>After this card enters play: Gain 2 Honor.<br><b>Battle:</b> Create a 2F/2C/3PH Lion <b>Clan &#149; Samurai &#149; Ancestor &#149; Spirit</b> Personality at the current battlefield.'
Celestial_Sword_of_the_Lion_Experienced = Item(card_id=1268, title='Celestial Sword of the Lion', force=1, chi=1, gold_cost=8, focus_value=4, keywords=[Unique, Weapon, Experienced('1'), Shinrai], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'Will only attach to a Unicorn Clan Personality.<br>This card has +1F for each Unicorn Clan Personality you control.<br>After this card enters play: Gain 2 Honor.<br><b>Battle:</b> Target an enemy card: Bow it. Destroy it if it is not Cavalry and has no attachments.'
Celestial_Sword_of_the_Unicorn_Experienced = Item(card_id=1273, title='Celestial Sword of the Unicorn', force=1, chi=1, gold_cost=8, focus_value=4, keywords=[Unique, Weapon, Enginoshi, Experienced('1')], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<b>Political Open, :bow::</b> Take the Imperial Favor.'
Dazzling_Attire = Item(card_id=1875, title='Dazzling Attire', force=0, chi=0, gold_cost=0, focus_value=3, traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
"Other players' cards' effects will not discard cards from your hand.<br>Your maximum hand size is increased by 1.<br>Other players' maximum hand sizes are reduced by 1, to a minimum of 7."
Pillowbook = Item(card_id=5958, title='Pillowbook', force=0, chi=0, gold_cost=0, focus_value=2, traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<b>Battle:</b> Melee 4 Attack, or Melee 5 Attack if the target is Cavalry.'
SankakuYari = Item(card_id=6469, title='Sankaku-Yari', force=5, chi=0, gold_cost=6, focus_value=1, keywords=[Weapon], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'As a Focus Effect: After this duel ends, you may attach this card to one of your Personalities, ignoring Gold cost.<br><b>Battle:</b> Target an enemy Personality or Follower: Give it -5F.'
Shamsir = Item(card_id=6702, title='Shamsir', force=3, chi=1, gold_cost=4, focus_value=1, keywords=[Weapon], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'As a Focus Effect: You may transfer an attachment from your Personality in this duel to another of your Personalities.<br><b>Battle:</b> Target an enemy card without attachments: Bow it. Destroy it if this Personality is a Berserker.'
Splintered_Weapon = Item(card_id=7435, title='Splintered Weapon', force=3, chi=0, gold_cost=4, focus_value=1, keywords=[Weapon], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'Will only attach to a Spider Clan Personality.<br>This card has +1F for each Spider Clan Personality you control.<br>After this card enters play: Gain 2 Honor.<br><b>Battle:</b> Target a card in a unit: You may destroy it if it is bowed or an attachment. Bow it. Straighten this Personality.'
The_Ancestral_Sword_of_Hantei_Experienced = Item(card_id=7958, title='The Ancestral Sword of Hantei', force=1, chi=1, gold_cost=8, focus_value=4, keywords=[Unique, Weapon, AkkuaiUo, Experienced('1')], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])