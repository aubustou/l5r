from __future__ import annotations
from .common import Event
from l5r_auto.legality import EmperorEdition, IvoryEdition, ModernEdition, OnyxEdition, TwentyFestivalsEdition
'<b>Limited:</b> Search your hand, then your discard pile, and then your Fate deck for a card titled Blood of the Preserver. Show it. Remove it from the game to gain 2 Honor.'
Changing_the_Game = Event(card_id=10819, title='Changing the Game', traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
'<b>Engage:</b> You have the first opportunity in this battle to pass or take a Battle action, which must come from a card in a unit.'
Into_the_Wastes = Event(card_id=10820, title='Into the Wastes', traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, OnyxEdition, ModernEdition])
"<b>Limited:</b> Put this Event into play. Target your Personality. While this Event remains in play, he will not be dishonored and you will not lose Honor from other players' actions that have targeted him . After your second turn from now begins, discard this Event."
Marriage_of_the_Emerald_Champion = Event(card_id=10821, title='Marriage of the Emerald Champion', traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
'<b>Limited:</b> Starting with you, each player targets <i>(if possible)</i> and destroys a card with the printed Fallen, Fudo, or Shadowlands keyword.'
Purge_of_Fudoism = Event(card_id=10822, title='Purge of Fudoism', traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])