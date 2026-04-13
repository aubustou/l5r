from __future__ import annotations
from ..common import Stronghold
from l5r_auto.clans import PhoenixClan
from l5r_auto.keywords import Temple
from l5r_auto.legality import CelestialEdition, EmperorEdition, ModernEdition
'<b>Reaction:</b> Even if this card is bowed, when paying for a Spell attaching to an opposed Personality: Produce 4 Gold.<br><b>Battle:</b> Choose your performing Shugenja: Straighten him. You may take an additional Battle action.'
Library_of_Rebirth = Stronghold(card_id=4724, title='Library of Rebirth', gold_production='4', starting_family_honor=6, province_strength=6, clan=[PhoenixClan], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<b>Battle:</b> Choose your performing unbowed Samurai: Melee 4 Attack, with +2 strength if you control a Shugenja.'
Shiro_Shiba = Stronghold(card_id=7017, title='Shiro Shiba', gold_production='4', starting_family_honor=6, province_strength=7, clan=[PhoenixClan], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
"<b>Open:</b> Even if this card is bowed, target another player's Personality: Give him -4F, which will not be negated. If he is Kolat, Ninja, or Shadowlands, you control an Inquisitor, and it is not your turn, choose a player, who gains or loses 2 Honor."
Temple_of_Purity = Stronghold(card_id=7879, title='Temple of Purity', gold_production='4', starting_family_honor=6, province_strength=6, clan=[PhoenixClan], keywords=[Temple], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
"<b>Reaction:</b> After another player's action targets your performing Henshin, target another of your Personalities. <i>The Henshin is reborn.</i> Transfer his attachments and tokens to the other Personality. The action's effects that would destroy your Henshin instead overlay him onto the Personality."
Waystation_of_the_Path = Stronghold(card_id=9267, title='Waystation of the Path', gold_production='4', starting_family_honor=6, province_strength=6, clan=[PhoenixClan], keywords=[Temple], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])