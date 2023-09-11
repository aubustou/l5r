from __future__ import annotations

from l5r_auto.clans import DragonClan
from l5r_auto.keywords import (
    ClanChampion,
    Dragon,
    Duelist,
    Experienced,
    Loyal,
    Nonhuman,
    Samurai,
    Shugenja,
    Unique,
)
from l5r_auto.legality import ModernEdition, OnyxEdition, TwentyFestivalsEdition

from ..common import Personality

'Cannot gain Corruption tokens or Shadowlands. After Hitomi enters play, you may create and Equip to her <i>(paying all costs)</i> a +2F/4GC <b>Hand &#149; Obsidian</b> Item with the traits, "Cannot be transferred or destroyed. Hitomi has Shugenja. Has +2C while opposing a Jade card or a Personality with higher Personal Honor."<br><b>Unstoppable Engage:</b> Target one to three cards in the hand of a player with a unit at this battlefield. He or she shuffles them into their deck and draws that many cards.'
Mirumoto_Hitomi_Seven_Thunder_Experienced_2CW = Personality(
    card_id=12642,
    title="Mirumoto Hitomi, Seven Thunder",
    force=5,
    chi=4,
    personal_honor=1,
    gold_cost=10,
    honor_requirement=None,
    clan=[DragonClan],
    keywords=[Duelist, Experienced("2CW"), Loyal, Unique, Samurai],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
"Cannot gain Corruption tokens or Shadowlands. Yokuni and your Seven Thunder cards in and out of play cannot be controlled by other players and lose Loyal.<br><b>Open, :g4::</b> If it is your turn, even if Yokuni is face-up in your Province, look at the top card of your Fate deck. You may put it at the bottom. Draw a card.<br><b>Battle:</b> Melee 4 Attack."
Togashi_Yokuni_Kami_Experienced_2CW = Personality(
    card_id=12643,
    title="Togashi Yokuni, Kami",
    force=6,
    chi=6,
    personal_honor=4,
    gold_cost=15,
    honor_requirement=10,
    clan=[DragonClan],
    keywords=[
        Duelist,
        Experienced("2CW"),
        Unique,
        ClanChampion,
        Dragon,
        Nonhuman,
        Samurai,
        Shugenja,
    ],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
