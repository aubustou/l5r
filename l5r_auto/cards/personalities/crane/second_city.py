from __future__ import annotations
from ..common import Personality
from l5r_auto.clans import CraneClan
from l5r_auto.keywords import Air, Artisan, BountyHunter, Courtier, Duelist, Experienced, Imperial, IronCrane, Magistrate, Samurai, Scout, Sculptor, Shugenja, Unique
from l5r_auto.legality import CelestialEdition, EmperorEdition, IvoryEdition, ModernEdition, TwentyFestivalsEdition
'<b>Open:</b> Target your Temple Holding: Straighten it.<br><b>Battle:</b> Even if Munefusa is not at the current battlefield, target an attacking Personality: Move him home. If he moved, gain 1 Honor.'
Asahina_Munefusa = Personality(card_id=505, title='Asahina Munefusa', force=2, chi=5, personal_honor=4, gold_cost=10, honor_requirement=6, clan=[CraneClan], keywords=[Air, Shugenja], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
"After the resolution of your Recon action: Give Ebizo +1F.<br><b>Battle:</b> Ranged Attack with strength equal to Ebizo's Force."
Daidoji_Ebizo = Personality(card_id=1629, title='Daidoji Ebizo', force=4, chi=4, personal_honor=2, gold_cost=9, honor_requirement=4, clan=[CraneClan], keywords=[BountyHunter, IronCrane, Samurai, Scout], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
"<b>Recon Reaction:</b> After engaging at Yuki's battlefield, if all your Personalities there are Scouts: You have Reconnaissance there. You have the first opportunity in this battle to take a Battle action or pass."
Daidoji_Yuki_Experienced = Personality(card_id=1696, title='Daidoji Yuki', force=4, chi=3, personal_honor=2, gold_cost=8, honor_requirement=0, clan=[CraneClan], keywords=[Unique, Experienced('1'), IronCrane, Samurai, Scout], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
'Dainagon may Lobby as an Open action.'
Doji_Dainagon = Personality(card_id=2070, title='Doji Dainagon', force=1, chi=3, personal_honor=3, gold_cost=5, honor_requirement=6, clan=[CraneClan], keywords=[Courtier, Imperial], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, EmperorEdition, CelestialEdition, ModernEdition])
'<b>Political Battle:</b> Target an enemy Personality: Bow him. If he is dishonorable, choose a player who gains or loses 2 Honor.'
Doji_Yoshitada = Personality(card_id=2179, title='Doji Yoshitada', force=3, chi=4, personal_honor=3, gold_cost=7, honor_requirement=6, clan=[CraneClan], keywords=[Duelist, Magistrate, Samurai], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
'<b>Reaction:</b> After a duel ends that your Personality won, bow Maratai: She sculpts a statue to honor the winner. Gain 2 Honor. Take the Imperial Favor.'
Kakita_Maratai = Personality(card_id=4197, title='Kakita Maratai', force=2, chi=4, personal_honor=4, gold_cost=8, honor_requirement=8, clan=[CraneClan], keywords=[Artisan, Sculptor], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])