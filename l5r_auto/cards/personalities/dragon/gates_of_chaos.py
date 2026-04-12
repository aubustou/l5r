from __future__ import annotations
from ..common import Personality
from l5r_auto.clans import BrotherhoodOfShinsei, DragonClan
from l5r_auto.keywords import Alchemist, Conqueror, Destined, Duelist, Earth, Experienced, Fallen, Fire, Kensai, Magistrate, Monk, Samurai, Shugenja, Tattooed, TopazChampion, Unique
from l5r_auto.legality import EmperorEdition, IvoryEdition, ModernEdition, OnyxEdition, TwentyFestivalsEdition
'<b>Open:</b> Give a target Personality -2F, or -3F if he is dishonorable.'
Kitsuki_Nakai_Experienced = Personality(card_id=10629, title='Kitsuki Nakai', force=1, chi=4, personal_honor=3, gold_cost=6, honor_requirement=8, clan=[DragonClan], keywords=[Duelist, Unique, Experienced('1'), Magistrate, Samurai, TopazChampion], traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
'<i>(Draw a card after your Destined card enters play.)</i><br>After Bojan enters play, lose 1 Honor.'
Mirumoto_Bojan = Personality(card_id=10630, title='Mirumoto Bojan', force=3, chi=2, personal_honor=0, gold_cost=5, honor_requirement=None, clan=[DragonClan], keywords=[Destined, Fallen, Samurai], traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
'<b>Battle, :gstar::</b> Equip a target non-Unique Weapon in your discard pile to Katagi.'
Mirumoto_Katagi_Experienced = Personality(card_id=10631, title='Mirumoto Katagi', force=4, chi=4, personal_honor=3, gold_cost=8, honor_requirement=7, clan=[DragonClan], keywords=[Kensai, Unique, Experienced('1'), Samurai], traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
Mirumoto_Omero = Personality(card_id=10632, title='Mirumoto Omero', force=2, chi=3, personal_honor=2, gold_cost=5, honor_requirement=4, clan=[DragonClan], keywords=[Conqueror, Kensai, Samurai], traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
'<i>(Shugenja may attach and cast Spells.)</i><br><b>Earth Battle:</b> Bow a target enemy card without attachments.'
Tamori_Jinai = Personality(card_id=10633, title='Tamori Jinai', force=3, chi=4, personal_honor=3, gold_cost=8, honor_requirement=4, clan=[DragonClan], keywords=[Alchemist, Earth, Shugenja], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, EmperorEdition, OnyxEdition, ModernEdition])
'Invest :g3:: Give Noritada two +1F <b>Fire </b>tokens. <i>(After this card enters play, you may also pay the Invest cost to get the effect, once.)</i>'
Togashi_Noritada = Personality(card_id=10634, title='Togashi Noritada', force=2, chi=3, personal_honor=2, gold_cost=4, honor_requirement=4, clan=[DragonClan, BrotherhoodOfShinsei], keywords=[Fire, Monk, Tattooed], traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])