from __future__ import annotations
from ..common import Stronghold
from l5r_auto.clans import LionClan
from l5r_auto.keywords import Dojo
from l5r_auto.legality import CelestialEdition, EmperorEdition, ModernEdition
'Your deck may include four copies each of one or two non-Unique Strategies with Battle abilities.<br><b>Reaction:</b> After your Tactical action resolves: Draw a card after the next End Phase begins.'
Eternal_Victory_Dojo = Stronghold(card_id=2388, title='Eternal Victory Dojo', gold_production='3', starting_family_honor=7, province_strength=7, clan=[LionClan], keywords=[Dojo], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'Your Ancestor Personalities have -1F while attacking.<br>Your Shugenja may use their base Battle abilities even if they are not at the current battlefield.<br>After your Ancestor Personality is destroyed during a Combat Segment: Gain 1 Honor.'
Halls_of_Memory = Stronghold(card_id=2949, title='Halls of Memory', gold_production='3', starting_family_honor=7, province_strength=7, clan=[LionClan], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'Your dishonorable Paragons do not have a maximum Personal Honor of 0 from the rulebook.<br><b>Battle:</b> Choose your performing unbowed Personality and move home a target Personality with equal or lower Personal Honor. Gain 2 Honor if you do not control him.'
Shamate_Keep = Stronghold(card_id=6691, title='Shamate Keep', gold_production='3', starting_family_honor=7, province_strength=7, clan=[LionClan], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
'<b>Recon Reaction:</b> After engaging: You have Reconnaissance at the current battlefield. Create a Terrain Strategy with the ability, "<b>Battle:</b> If this card is in play, destroy it and target a Terrain in your hand: Take an additional Battle action to play it." Put it into play there.'
The_Golden_Plains = Stronghold(card_id=8105, title='The Golden Plains', gold_production='3', starting_family_honor=7, province_strength=7, clan=[LionClan], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])