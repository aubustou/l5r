from __future__ import annotations

from l5r_auto.clans import BrotherhoodOfShinsei, DragonClan
from l5r_auto.keywords import (
    Air,
    Cavalry,
    Commander,
    Conqueror,
    Courtier,
    Duelist,
    Earth,
    Expendable,
    Experienced,
    Imperial,
    Magistrate,
    Monk,
    Mountaineer,
    Samurai,
    Shugenja,
    SoulOf,
    Tattooed,
    Unique,
    Void,
)
from l5r_auto.legality import ModernEdition, OnyxEdition, TwentyFestivalsEdition

from ..common import Personality

"<i>(Draw a card after your Expendable card dies.)</i><br>Courtesy: Einosuke has Destined. <i>(Courtesy traits do not take effect if you went first. Draw a card after you Recruit a Destined card.)</i>"
Kitsuki_Einosuke = Personality(
    card_id=12103,
    title="Kitsuki Einosuke",
    force=3,
    chi=2,
    personal_honor=3,
    gold_cost=6,
    honor_requirement=5,
    clan=[DragonClan],
    keywords=[Expendable, Courtier, Magistrate],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
"<b>Battle:</b> Move home a target Human Personality with the lowest Personal Honor at this battlefield <i>(you choose in case of a tie)</i>."
Kitsuki_Goichi = Personality(
    card_id=12104,
    title="Kitsuki Goichi",
    force=3,
    chi=4,
    personal_honor=3,
    gold_cost=7,
    honor_requirement=5,
    clan=[DragonClan],
    keywords=[Magistrate, Samurai, SoulOf("Kitsuki Berii")],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
"<i>(Shugenja may attach and cast Spells.)</i><br><b>Air Tireless Open:</b> If Masamitsu has cast an Air Spell this turn, straighten him. <i>(Tireless actions may be taken even while bowed.)</i>"
Kitsuki_Masamitsu = Personality(
    card_id=12105,
    title="Kitsuki Masamitsu",
    force=2,
    chi=3,
    personal_honor=3,
    gold_cost=6,
    honor_requirement=5,
    clan=[DragonClan],
    keywords=[Air, Courtier, Magistrate, Shugenja],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
"<b>Tireless Battle:</b> Target your Ring. You may bow it to straighten Akifumi or you may bow Akifumi to straighten it. <i>(Tireless actions may be taken even while bowed.)</i>"
Mirumoto_Akifumi = Personality(
    card_id=12106,
    title="Mirumoto Akifumi",
    force=3,
    chi=3,
    personal_honor=3,
    gold_cost=5,
    honor_requirement=2,
    clan=[DragonClan],
    keywords=[Samurai, Void],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
Mirumoto_Eisuke = Personality(
    card_id=12107,
    title="Mirumoto Eisuke",
    force=2,
    chi=4,
    personal_honor=3,
    gold_cost=5,
    honor_requirement=None,
    clan=[DragonClan],
    keywords=[Samurai, SoulOf("Mirumoto Daini")],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
"<b>Iaijutsu Battle, :bow::</b> Move home a target enemy defending Personality with equal or lower Chi. Straighten Rikiya if he won a duel this turn."
Mirumoto_Rikiya = Personality(
    card_id=12108,
    title="Mirumoto Rikiya",
    force=3,
    chi=3,
    personal_honor=2,
    gold_cost=6,
    honor_requirement=4,
    clan=[DragonClan],
    keywords=[Duelist, Samurai, SoulOf("Mirumoto Washizuka")],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
"<b>Iaijutsu Battle:</b> Challenge a target enemy Personality. If the target is honorable, his controller may dishonor him and move him home to refuse the duel. Destroy the loser."
Mirumoto_Tsuda_Emerald_Champion_Experienced = Personality(
    card_id=12109,
    title="Mirumoto Tsuda, Emerald Champion",
    force=3,
    chi=5,
    personal_honor=3,
    gold_cost=10,
    honor_requirement=8,
    clan=[DragonClan],
    keywords=[
        Cavalry,
        Duelist,
        Unique,
        Experienced("1"),
        Imperial,
        Magistrate,
        Samurai,
    ],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
"Seiken's Nonhuman Followers have <b>Cavalry</b>.<br><b>Earth Battle:</b> Fear equal to the Focus Value of Seiken's target Follower or Spell."
Tamori_Seiken_Experienced = Personality(
    card_id=12110,
    title="Tamori Seiken",
    force=3,
    chi=3,
    personal_honor=3,
    gold_cost=7,
    honor_requirement=7,
    clan=[DragonClan],
    keywords=[
        Cavalry,
        Unique,
        Commander,
        Earth,
        Experienced("1"),
        Mountaineer,
        Shugenja,
    ],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
"<i>(Shugenja may attach and cast Spells.)</i><br><b>Earth Battle:</b> Give a target enemy Follower or Personality -2F."
Tamori_Shoko = Personality(
    card_id=12111,
    title="Tamori Shoko",
    force=2,
    chi=3,
    personal_honor=2,
    gold_cost=5,
    honor_requirement=4,
    clan=[DragonClan],
    keywords=[Commander, Earth, Shugenja],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
"<i>(A Conqueror's unit doesn't bow after battle. Shugenja may attach and cast Spells.)</i>"
Tamori_Tsunemi = Personality(
    card_id=12112,
    title="Tamori Tsunemi",
    force=3,
    chi=2,
    personal_honor=2,
    gold_cost=6,
    honor_requirement=0,
    clan=[DragonClan],
    keywords=[Conqueror, Commander, Earth, Shugenja],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
'Taiki has the element keywords of any Rings you control. While you control a Ring of Air, he has <b>Cavalry</b>; Ring of Earth, he has +2F/+1C; Ring of Fire, he has, "<b>Battle:</b> Melee 2 Attack."; Ring of Water, he has <b>Conqueror</b>; Ring of Void, he has <b><b>Destined &#149; Expendable</b></b>.'
Togashi_Taiki = Personality(
    card_id=12113,
    title="Togashi Taiki",
    force=2,
    chi=2,
    personal_honor=1,
    gold_cost=6,
    honor_requirement=0,
    clan=[DragonClan, BrotherhoodOfShinsei],
    keywords=[Monk, Tattooed],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
