from __future__ import annotations

from l5r_auto.clans import BrotherhoodOfShinsei, DragonClan
from l5r_auto.keywords import (
    Commander,
    Courtier,
    Destined,
    Duelist,
    Earth,
    Experienced,
    Magistrate,
    Monk,
    Resilient,
    Samurai,
    Shugenja,
    Tattooed,
)
from l5r_auto.legality import ModernEdition, OnyxEdition, TwentyFestivalsEdition

from ..common import Personality

"<i>(Draw a card after you Recruit a Destined card.)</i> <br><b>Interrupt:</b> After the action destroys a dishonorable Personality, gain 1 Honor.<br><b>Engage:</b> Dishonor a target enemy Personality with lower Chi."
Kitsuki_Goshi = Personality(
    card_id=12452,
    title="Kitsuki Goshi",
    force=3,
    chi=3,
    personal_honor=3,
    gold_cost=7,
    honor_requirement=5,
    clan=[DragonClan],
    keywords=[Destined, Courtier, Magistrate],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
"<i>(Once per game per card, a Resilient card does not die in battle resolution.)</i> <br><b>Political Interrupt, :bow::</b> If you took an Honor Interrupt to the action, return the Honor card you discarded for it to your hand. You may not take Honor actions this turn."
Kitsuki_Goto = Personality(
    card_id=12453,
    title="Kitsuki Goto",
    force=0,
    chi=3,
    personal_honor=3,
    gold_cost=4,
    honor_requirement=5,
    clan=[DragonClan],
    keywords=[Resilient, Courtier, Magistrate],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
"<i>(Duelists win tied duels versus non-Duelists.)</i><br><b>Battle:</b> If Konoe is opposed, look at the top three cards of your Fate deck. You may discard a card to put one of them into your hand; if it is Iaijutsu, you may take an additional action to play it. Put the other cards back in any order."
Mirumoto_Konoe = Personality(
    card_id=12454,
    title="Mirumoto Konoe",
    force=3,
    chi=3,
    personal_honor=1,
    gold_cost=5,
    honor_requirement=3,
    clan=[DragonClan],
    keywords=[Duelist, Samurai],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
'After Sannin enters play, permanently give them one of the following abilities <i>(and its elemental keyword)</i> not already on your Sannin in play: "<b>Void Dynasty, :bow::</b> Recruit a Sannin from your discard pile or Dynasty deck."; "<b>Fire Battle, :bow::</b> Melee 3 Attack."; or "<b>Air Battle:</b> Straighten a target Sannin."'
Sannin = Personality(
    card_id=12455,
    title="Sannin",
    force=3,
    chi=3,
    personal_honor=1,
    gold_cost=6,
    honor_requirement=3,
    clan=[DragonClan, BrotherhoodOfShinsei],
    keywords=[Monk, Tattooed],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
"Invest :g2:, or :g0: if you have <b>Courtesy</b>: Search your deck for The Mountainborn or Bound Spirit, show it, and put it in your hand. <i>(Courtesy does not take effect if you went first.)</i><br><b>Earth Battle, :bow::</b> Melee 3 Attack. You may bow one of Daiishu's Followers to straighten him."
Tamori_Daiishu_Experienced = Personality(
    card_id=12456,
    title="Tamori Daiishu",
    force=3,
    chi=4,
    personal_honor=2,
    gold_cost=8,
    honor_requirement=2,
    clan=[DragonClan],
    keywords=[Commander, Earth, Experienced("1"), Shugenja],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
"<i>(Draw a card after you Recruit a Destined card. Once per game per card, a Resilient card does not die in battle resolution.)</i><br>Gaitsuru's Earth attachments have <b>Resilient</b>."
Tamori_Gaitsuru = Personality(
    card_id=12457,
    title="Tamori Gaitsuru",
    force=2,
    chi=3,
    personal_honor=1,
    gold_cost=5,
    honor_requirement=2,
    clan=[DragonClan],
    keywords=[Destined, Resilient, Commander, Earth, Shugenja],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
