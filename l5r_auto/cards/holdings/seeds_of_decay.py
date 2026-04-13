from __future__ import annotations
from .common import Holding
from l5r_auto.keywords import Farm, Fudo, Library, Market, Ninja, Port, Ship, Temple, Unique
from l5r_auto.legality import EmperorEdition, IvoryEdition, ModernEdition, OnyxEdition, TwentyFestivalsEdition
'You have +1 maximum hand size.<br><b>:bow::</b> Produce 2 Gold.'
Farmers_Market = Holding(card_id=10033, title="Farmer's Market", gold_cost=2, keywords=[Farm, Market], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, EmperorEdition, ModernEdition])
':bow:: Produce 2 Gold, or 3 Gold if you are a Crane Clan player.<br><b>Open:</b> Target a non-Unique Holding. <i>You blockade it.</i> Bow it.'
Hachis_Revenge = Holding(card_id=10034, title="Hachi's Revenge", gold_cost=4, keywords=[Unique, Ship], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
":bow:: Produce 2 Gold.<br><b>Battle/Open:</b> Target a Personality. Negate all current Force penalties on him. Negate any cards' effects that say he may not perform actions <i>(this turn)</i>."
Incense_Mill = Holding(card_id=10035, title='Incense Mill', gold_cost=2, traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
':bow:: Produce 2 Gold.<br><b>Ninja Limited:</b> Destroy this card to create a 0F/2C/0PH <b>Ninja</b> Personality with your Clan Alignment.'
Overlooked_Palace = Holding(card_id=10036, title='Overlooked Palace', gold_cost=2, keywords=[Ninja], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
':bow:: Produce 2 Gold.<br><b>Open, :bow::</b> Straighten a target Market or Port.'
Second_City_Port = Holding(card_id=10037, title='Second City Port', gold_cost=2, keywords=[Port], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'After this Holding enters play from a Province, refill the Province face-up.'
Small_Library = Holding(card_id=10038, title='Small Library', gold_cost=4, keywords=[Library], traits=[], abilities=[], legality=[TwentyFestivalsEdition, EmperorEdition, OnyxEdition, ModernEdition])
'After this Holding enters play, lose 3 Honor.<br>This Holding will not straighten before your third turn. <br>:bow:: Produce 2 Gold and lose 1 Honor.'
Temple_to_Fudo = Holding(card_id=10039, title='Temple to Fudo', gold_cost=0, keywords=[Fudo, Temple], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])