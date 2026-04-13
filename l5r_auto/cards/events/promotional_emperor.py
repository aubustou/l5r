from __future__ import annotations
from .common import Event
from l5r_auto.keywords import Festival, Forest, Ritual, Unique
from l5r_auto.legality import EmperorEdition, IvoryEdition, ModernEdition
'<b>Limited:</b> After each battle resolution <i>(this turn)</i> in which your army destroyed an enemy army or Province, give each of your Personalities in that army a +1F/+1C token.'
A_Great_Victory = Event(card_id=10568, title='A Great Victory', traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
'After you reveal cards in your Provinces at the start of your turn, if this Event is face-up in one of them, until your next turn begins, after each time a player creates an Attack Phase, destroy his rightmost Province.'
Diplomacy_Talks = Event(card_id=10230, title='Diplomacy Talks', keywords=[Unique], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
"After you reveal cards in your Provinces at the start of your turn, if this Event is face-up in one of them, until your next turn begins, before the first time each turn another player's card's effect destroys one or more of your Personalities, negate the destruction."
Expansion = Event(card_id=2409, title='Expansion', keywords=[Unique, Forest], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<b>Limited:</b> Until your next turn begins, your Personalities have +1F while in an army with another Personality with the same Family Name.'
Family_Maneuvers = Event(card_id=10407, title='Family Maneuvers', traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
"<b>Limited:</b> Give all other players' non-Unique Holdings -1 Gold Production until your next turn begins."
Frost_Dragon_Festival = Event(card_id=10570, title='Frost Dragon Festival', keywords=[Unique, Festival], traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
'<b>Limited:</b> Give your non-Unique Holdings +1 Gold Production until your next turn begins.'
Inaris_Festival = Event(card_id=10569, title="Inari's Festival", keywords=[Unique, Festival], traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
'<b>Limited:</b> Permanently give your target Personality <b>Conqueror</b>.'
Legionnaires_Appointment = Event(card_id=10566, title="Legionnaire's Appointment", keywords=[Unique], traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
'<b>Limited:</b> Until your turn begins three turns from now begins, each player may put no more than one Ring into play per turn.'
Losing_the_Way = Event(card_id=10565, title='Losing the Way', keywords=[Unique], traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
'After you reveal cards in your Provinces at the start of your turn, if this Event is face-up in one of them, <i>the cultists of Ruhmal are restless</i>; until your next turn begins, after each time a card effect destroys a Personality, the player who last controlled him discards a card.'
Ritual_of_Sacrifice = Event(card_id=6356, title='Ritual of Sacrifice', keywords=[Unique, Ritual], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'After you reveal cards in your Provinces at the start of your turn, if this Event is face-up in one of them, after your next Dynasty Phase ends, if you did not put any cards in your hand since the resolution of this Event, draw two cards.'
Tales_of_Valor = Event(card_id=9949, title='Tales of Valor', keywords=[Unique], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'After you reveal cards in your Provinces at the start of your turn, if this Event is face-up in one of them, choose one of your Courtiers in play. Permanently give him +1PH and the ability, "<b>Political Open:</b> This Personality copies one of another target Personality\'s Political abilities which does not itself copy abilities."'
The_Amethyst_Championship = Event(card_id=7955, title='The Amethyst Championship', keywords=[Unique], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'After you reveal cards in your Provinces at the start of your turn, if this Event is face-up in one of them, choose one of your Personalities in play. Permanently give him Imperial &#149; Magistrate and the ability, "<b>Tireless Battle/Open:</b> Straighten a target Personality."'
The_Emerald_Championship = Event(card_id=8049, title='The Emerald Championship', keywords=[Unique], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<b>Limited:</b> Destroy all Madness tokens.'
The_Fever_Breaks = Event(card_id=10567, title='The Fever Breaks', keywords=[Unique], traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
'After you reveal cards in your Provinces at the start of your turn, if this Event is face-up in one of them, choose one of your Shugenja in play. Permanently give him the traits, "Shadowlands Personalities and Followers have -1F while at this Personality\'s location" and "After the resolution of an action from a Spell, straighten this Personality."'
The_Jade_Championship = Event(card_id=8163, title='The Jade Championship', keywords=[Unique], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'After you reveal cards in your Provinces at the start of your turn, if this Event is face-up in one of them, choose one of your Personalities in play. Permanently give him +1F, Shadowlands, and the ability, "<b>Battle:</b> Target an enemy card with lower Force. Bow it. Destroy it if it is an attachment."'
The_Obsidian_Championship = Event(card_id=8238, title='The Obsidian Championship', keywords=[Unique], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'After you reveal cards in your Provinces at the start of your turn, if this Event is face-up in one of them, choose one of your Shugenja in play. Permanently give him Shadowlands and the ability, "<b>Maho Limited, :bow::</b> Destroy your other target Personality to search your discard pile, then deck, then Provinces for an Oni Personality, Recruit it <i>(paying all costs)</i>, and lose 3 Honor."'
The_Onyx_Championship = Event(card_id=8242, title='The Onyx Championship', keywords=[Unique], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'After you reveal cards in your Provinces at the start of your turn, if this Event is face-up in one of them, choose one of your Personalities in play. Permanently give him Imperial, Magistrate, and the ability, "<b>Battle:</b> Bow a target enemy Personality; if he is dishonorable, destroy a card without attachments in his unit."'
The_Ruby_Championship = Event(card_id=8288, title='The Ruby Championship', keywords=[Unique], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'After you reveal cards in your Provinces at the start of your turn, if this Event is face-up in one of them, choose one of your Personalities in play without abilities. Permanently give him +1F/+1C, the trait "Before the first time each turn another player\'s card effect destroys this Personality, negate the destruction", and the ability, "<b>Battle:</b> Destroy a target enemy card without attachments."'
The_Topaz_Championship = Event(card_id=8387, title='The Topaz Championship', keywords=[Unique], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'After you reveal cards in your Provinces at the start of your turn, if this Event is face-up in one of them, choose one of your Personalities in play. Permanently give him Artisan and the ability, "<b>Limited:</b> Choose a player. He gains or loses 1 Honor."'
The_Turquoise_Championship = Event(card_id=8399, title='The Turquoise Championship', keywords=[Unique], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<b>Limited:</b> Until your second turn from now begins, your Personalities have +1F while attacking a player who declared an attack against you since your last turn ended.'
Yozos_Inspiration = Event(card_id=10564, title="Yozo's Inspiration", keywords=[Unique], traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])