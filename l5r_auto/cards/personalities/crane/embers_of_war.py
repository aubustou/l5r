from __future__ import annotations
from ..common import Personality
from l5r_auto.clans import CraneClan
from l5r_auto.keywords import Air, Artisan, Courtier, Daimyo, Duelist, Imperial, IronCrane, Loyal, Magistrate, Samurai, Scout, Sensei, Shugenja, Storyteller, Unique, Yojimbo
from l5r_auto.legality import EmperorEdition, ModernEdition
Asahina_Konomi = Personality(card_id=502, title='Asahina Konomi', force=2, chi=5, personal_honor=4, gold_cost=7, honor_requirement=2, clan=[CraneClan], keywords=[Air, Artisan, Shugenja], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<b>Reaction:</b> After your Recon action from a Strategy resolves: Draw a card.<br><b>Recon Limited:</b> Discard a card: Search your Fate deck for a non-Unique card with a Recon ability, show it, and put it in your hand.'
Daidoji_Akeha = Personality(card_id=1621, title='Daidoji Akeha', force=5, chi=3, personal_honor=3, gold_cost=8, honor_requirement=0, clan=[CraneClan], keywords=[Loyal, Unique, Daimyo, IronCrane, Samurai, Scout], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<b>Battle:</b> Target an enemy Personality: Bow zero or more different cards in his unit up to the number of Recon actions you have taken this turn.'
Daidoji_Narizane = Personality(card_id=1663, title='Daidoji Narizane', force=4, chi=3, personal_honor=2, gold_cost=7, honor_requirement=2, clan=[CraneClan], keywords=[Imperial, IronCrane, Samurai, Scout, Yojimbo], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'After Gonji enters play: Discard all your other Sensei Personalities.<br>Before you focus: Once per duel, instead of focusing that time, you may give your Crane Clan Personality in the duel +4 to his duel stat until the duel ends.'
Kakita_Gonji = Personality(card_id=4167, title='Kakita Gonji', force=2, chi=5, personal_honor=3, gold_cost=7, honor_requirement=5, clan=[CraneClan], keywords=[Duelist, Loyal, Samurai, Sensei], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
"After a Battle action targets Kae, you may discard the Imperial Favor to negate Kae's destruction, bowing, and movement from the action's effects.<br><b>Battle:</b> Move Kae home."
Kakita_Kae = Personality(card_id=4179, title='Kakita Kae', force=2, chi=4, personal_honor=3, gold_cost=7, honor_requirement=6, clan=[CraneClan], keywords=[Courtier, Storyteller], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<b>Iaijutsu Reaction:</b> After an action resolves during which Kenta won a duel, target a dishonorable enemy Personality at the current battlefield: Move him home.'
Kakita_Kenta = Personality(card_id=4189, title='Kakita Kenta', force=2, chi=3, personal_honor=3, gold_cost=6, honor_requirement=3, clan=[CraneClan], keywords=[Duelist, Magistrate, Samurai], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])