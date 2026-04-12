from __future__ import annotations
from ..common import Stronghold
from l5r_auto.clans import DragonClan
from l5r_auto.keywords import Dojo
from l5r_auto.legality import CelestialEdition, EmperorEdition, ModernEdition
"After another player's Dynasty Phase begins, if he controls any Personalities and he assigned none of them to an attacking army this turn: Gain 2 Honor.<br><b>Reaction:</b> Even if this card is bowed, after engaging at a battlefield at one of your provinces: The Attacker targets and bows one of his Personalities there."
Dragons_Breath_Castle = Stronghold(card_id=2219, title="Dragon's Breath Castle", gold_production='4', starting_family_honor=5, province_strength=7, clan=[DragonClan], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
'Equipping Weapons is a <b>Battle/Open</b> action for you.<br><b>Battle/Open, :gstar::</b> Choose your performing Kensai and Equip a target Weapon in your discard pile to him.'
Foothills_Keep = Stronghold(card_id=2626, title='Foothills Keep', gold_production='4', starting_family_honor=5, province_strength=7, clan=[DragonClan], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<b>Reaction:</b> After the resolution of a Kiho Battle action you took: Take an additional Battle action.'
Pillars_of_Virtue = Stronghold(card_id=5957, title='Pillars of Virtue', gold_production='4', starting_family_honor=5, province_strength=7, clan=[DragonClan], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
"<b>Iaijutsu Tireless Open:</b> Choose your performing unbowed Personality. He challenges another player's target Personality. He may refuse; if he does, dishonor him and gain 1 Honor. Bow the duel's loser."
Watchful_Eye_Dojo = Stronghold(card_id=9246, title='Watchful Eye Dojo', gold_production='4', starting_family_honor=5, province_strength=7, clan=[DragonClan], keywords=[Dojo], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])