from __future__ import annotations
from ..common import Personality
from l5r_auto.clans import BrotherhoodOfShinsei, PhoenixClan
from l5r_auto.keywords import Cavalry, Duelist, ElementalMaster, Henshin, Inquisitor, Magistrate, Monk, Samurai, Shugenja, Unique, Void, Water, Yojimbo
from l5r_auto.legality import CelestialEdition, EmperorEdition, ModernEdition
"After Chukage enters play, search your discard pile, then hand, then deck, for a Ring of Water. Put it into play or in your hand. If this put it into play, while it remains in play, it does not count towards an Enlightenment Victory.<br><b>Water Tireless Reaction:</b> After the resolution of an action that moved your Personality, move Chukage to the Personality's location. After this moves him, straighten Chukage's unit."
Asako_Chukage = Personality(card_id=533, title='Asako Chukage', force=4, chi=5, personal_honor=3, gold_cost=10, honor_requirement=6, clan=[PhoenixClan, BrotherhoodOfShinsei], keywords=[Cavalry, Unique, ElementalMaster, Henshin, Monk, Shugenja, Water], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
'<b>Battle:</b> Target an enemy Personality: Reduce his Force to 0. Destroy a card without attachments in his unit if he is Kolat, Ninja, or Shadowlands.'
Asako_Kaitoko = Personality(card_id=549, title='Asako Kaitoko', force=4, chi=3, personal_honor=4, gold_cost=8, honor_requirement=0, clan=[PhoenixClan], keywords=[Inquisitor, Magistrate, Shugenja, Void], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
'<b>Iaijutsu Battle:</b> Target an enemy Personality or Follower: Give it -5F.'
Shiba_Sawaken = Personality(card_id=6804, title='Shiba Sawaken', force=4, chi=3, personal_honor=3, gold_cost=7, honor_requirement=6, clan=[PhoenixClan], keywords=[Duelist, Samurai, Yojimbo], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])