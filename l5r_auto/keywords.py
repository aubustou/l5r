from __future__ import annotations

from copy import copy
from dataclasses import dataclass, field, make_dataclass
from typing import Type

from .clans import NagaFaction, NinjaFaction, SpiritFaction


@dataclass(repr=False, kw_only=True)
class Keyword:
    name: str = field(init=False)

    def __post_init__(self):
        self.name = self.__class__.__name__


def SoulOf(title: str) -> Type[Keyword]:
    klass = copy(Keyword)
    klass.name = f"Soul of {title}"

    return klass


@dataclass(repr=False, kw_only=True)
class Baraunghar(Keyword):
    pass


@dataclass(repr=False, kw_only=True)
class Bushi(Keyword):
    pass


@dataclass(repr=False, kw_only=True)
class Explorer(Keyword):
    pass


@dataclass(repr=False, kw_only=True)
class Port(Keyword):
    pass


@dataclass(repr=False, kw_only=True)
class Samurai(Keyword):
    pass


# Boldface keywords
@dataclass(repr=False, kw_only=True)
class Armor(Keyword):
    """A keyword found on some Items. A Personality cannot attach more than one Armor."""


@dataclass(repr=False, kw_only=True)
class Cavalry(Keyword):
    """The Cavalry keyword is relevant to the following player ability which all players have:
    Absent Engage: Target your unbowed Personality in a Cavalry unit at any location.
    Move it to the current battlefield.
    Note that a “Cavalry unit” is one in which the Personality and all Followers, if any, have
    the Cavalry keyword (see Unit keywords)."""


@dataclass(repr=False, kw_only=True)
class Conqueror(Keyword):
    """Cards in a Conqueror Personality’s unit do not bow prior to returning home after a
    battle’s resolution.
    """


@dataclass(repr=False, kw_only=True)
class Courage(Keyword):
    """All players have the following ability relevant to the Courage keyword.
    Repeatable Courage Interrupt: Discard a Courage card from your hand to give one
    of the action’s Fear effects either +2 or-2 strength.
    """


@dataclass(repr=False, kw_only=True)
class Destined(Keyword):
    """After a player’s card with the Destined keyword enters play, he or she draws a Fate
    card.
    """


@dataclass(repr=False, kw_only=True)
class Duelist(Keyword):
    """If a Personality in a duel has the Duelist keyword then, if scores are tied in the duel’s
    resolution, and the other Personality is not a Duelist, the Duelist wins.
    """


@dataclass(repr=False, kw_only=True)
class Expendable(Keyword):
    """After a card with the Expendable keyword is destroyed, the player who controlled it
    draws a card. “Expendable” status is checked just before being destroyed.
    """


def Experienced(level: str) -> Type[Keyword]:
    """Some Personality cards have the Experienced keyword, which is sometimes followed
    by a number representing the Personality’s experience level. A Personality with
    Experienced and no number has experience level of one. A Personality without
    Experienced has experience level zero.
    Any number of single Personalities with the same title but dierent experience levels
    may be included in a deck.
    During the Dynasty Phase, a player may bring an Experienced Personality into play
    normally, or may overlay him onto one of his or her Personalities in play with the
    same title but lower experience level. When overlaying, a player does not need to
    meet Honor Requirements or pay costs, but does need to meet other requirements
    and restrictions, including Loyal.
    An overlaying card replaces its less experienced version without entering play, and the
    less experienced card is removed from the game without leaving play. On overlaying,
    the new card keeps all states, ongoing eects, attachments, and tokens of the old
    card, and is considered to be the same card. Overlaying is not Recruiting.
    Experienced cards that are not Personalities follow the Experienced deck construction
    rules, but do not overlay.
    Some cards released in the Coils of Madness expansion have the “Experienced CoM”
    keyword. These may overlay a non-Experienced version as usual, but may not be
    overlaid by a higher level version.
    """
    klass = make_dataclass(
        f"Experienced{level.replace(' ', '')}",
        [
            ("name", str, field(default=f"Experienced {level}")),
            ("level", str, field(default=level)),
        ],
        bases=(Keyword,),
    )

    return klass


@dataclass(repr=False, kw_only=True)
class Fortication(Keyword):
    """When brought into play, Holdings with the Fortication keyword are attached to the
    Province they entered play from, or to any of their player’s Provinces if they were not
    brought in from a Province. Such Holding cards are kept under the card in the
    Province (if any), in the same way an attachment is kept under its Personality.
    Fortications are Recruited as normal, and enter play bowed. They are destroyed if
    the Province is destroyed. During a battle, abilities on a Fortication can only be used
    if the Fortication is attached to the current battleeld’s Province.
    """


@dataclass(repr=False, kw_only=True)
class Inexperienced(Keyword):
    pass


@dataclass(repr=False, kw_only=True)
class Kensai(Keyword):
    """A Kensai Personality can attach two Weapons if neither of them is Two-handed."""


@dataclass(repr=False, kw_only=True)
class Kharmic(Keyword):
    """A keyword that can appear on Dynasty or Fate cards.

    Players have the following ability relevant to Kharmic cards:
    Kharmic Repeatable Limited, : Discard a Kharmic card from your hand to draw a
    card, or discard a Kharmic card from your Province to rell the Province face-up.
    """


@dataclass(repr=False, kw_only=True)
class Legacy(Keyword):
    """A keyword on Holdings that refers to the following player ability:

    Dynasty, GC*: Remove a card in your hand from the game to search your deck and
    Provinces for a Legacy Holding and Recruit it. If you fail to nd one, you lose the game.
    """


@dataclass(repr=False, kw_only=True)
class Loyal(Keyword):
    """A Personality with the Loyal keyword will not be controlled by a player who does not
    share a Clan Alignment with the Personality. This restricts entering play as well as
    changing control.
    """


@dataclass(repr=False, kw_only=True)
class Naval(Keyword):
    """Players have the following ability relevant to Naval cards, known as Naval Invasion:
    NAVAL INVASION #
    Engage: If you are the Attacker, you have the first opportunity to take a Battle action,
    which must come from a card in a Naval Personality’s unit. Passing that action does
    not count toward ending the action round.
    """


@dataclass(repr=False, kw_only=True)
class Reserve(Keyword):
    """The following player abilities are relevant to the Reserve keyword:
    Absent Repeatable Battle, : If he would be opposed, Recruit your target Reserve
    Personality (into the current battleeld).
    Repeatable Battle, : If it would be opposed, Equip a Reserve attachment to your
    target Personality (at the current battleeld)."""


@dataclass(repr=False, kw_only=True)
class Resilient(Keyword):
    """The Resilient keyword means that, once per game per card, the card is not destroyed
    by the rulebook effects of battle resolution; that is, if its side loses or it ties. Its
    attached cards are still destroyed normally.
    A card that loses and then gains Resilient is still bound by the “once per game per
    card” restriction."""


@dataclass(repr=False, kw_only=True)
class Tactician(Keyword):
    """All Tactician Personalities have the following ability, known as “Tactical Advantage”.
    This ability is not printed on the Tactician and cannot be removed or copied from him
    or her.
    TACTICAL ADVANTAGE #
    Battle: Discard a card to give this Personality a Force bonus equal to the Focus Value
    of the discarded card.
    """


@dataclass(repr=False, kw_only=True)
class Weapon(Keyword):
    """A Personality can have only one Weapon Item attached. Exception: Kensai."""


@dataclass(repr=False, kw_only=True)
class Unique(Keyword):
    """A player will not bring into play or take control of a Unique card if he or she already
    controls a Unique card with the same title (but see Experienced for exceptions). If a
    player takes control of a unit with a copy of a Unique attachment he or she already
    controls, discard the new attachment.
    The Unique keyword also restricts deck construction.
    """


# Elements


@dataclass(repr=False, kw_only=True)
class Air(Keyword):
    pass


@dataclass(repr=False, kw_only=True)
class Earth(Keyword):
    pass


@dataclass(repr=False, kw_only=True)
class Fire(Keyword):
    pass


@dataclass(repr=False, kw_only=True)
class Void(Keyword):
    pass


@dataclass(repr=False, kw_only=True)
class Water(Keyword):
    pass


# Minor clans and factions


@dataclass(repr=False, kw_only=True)
class BatClan(Keyword):
    pass


@dataclass(repr=False, kw_only=True)
class DragonflyClan(Keyword):
    pass


@dataclass(repr=False, kw_only=True)
class Naga(Keyword, NagaFaction):
    pass


@dataclass(repr=False, kw_only=True)
class Ninja(Keyword, NinjaFaction):
    pass


@dataclass(repr=False, kw_only=True)
class Spirit(Keyword, SpiritFaction):
    pass


# Other keywords
@dataclass(repr=False, kw_only=True)
class Actor(Keyword):
    pass


@dataclass(repr=False, kw_only=True)
class Alchemist(Keyword):
    pass


@dataclass(repr=False, kw_only=True)
class Ancestor(Keyword):
    pass


@dataclass(repr=False, kw_only=True)
class Artisan(Keyword):
    pass


@dataclass(repr=False, kw_only=True)
class Ashigaru(Keyword):
    pass


@dataclass(repr=False, kw_only=True)
class Assassin(Keyword):
    pass


@dataclass(repr=False, kw_only=True)
class BattleMaiden(Keyword):
    pass


@dataclass(repr=False, kw_only=True)
class Beastmaster(Keyword):
    pass


@dataclass(repr=False, kw_only=True)
class Berserker(Keyword):
    pass


@dataclass(repr=False, kw_only=True)
class BitterLies(Keyword):
    pass


@dataclass(repr=False, kw_only=True)
class BlessedByBenten(Keyword):
    pass


@dataclass(repr=False, kw_only=True)
class Bloodspeaker(Keyword):
    pass


@dataclass(repr=False, kw_only=True)
class BogHag(Keyword):
    pass


@dataclass(repr=False, kw_only=True)
class BountyHunter(Keyword):
    pass


@dataclass(repr=False, kw_only=True)
class Braggart(Keyword):
    pass


@dataclass(repr=False, kw_only=True)
class Bully(Keyword):
    pass


@dataclass(repr=False, kw_only=True)
class Chieftain(Keyword):
    pass


@dataclass(repr=False, kw_only=True)
class ChildOfProphecy(Keyword):
    pass


@dataclass(repr=False, kw_only=True)
class ClanChampion(Keyword):
    pass


@dataclass(repr=False, kw_only=True)
class Commander(Keyword):
    pass


@dataclass(repr=False, kw_only=True)
class Constrictor(Keyword):
    pass


@dataclass(repr=False, kw_only=True)
class Courtier(Keyword):
    pass


@dataclass(repr=False, kw_only=True)
class Cursed(Keyword):
    pass


@dataclass(repr=False, kw_only=True)
class Daimyo(Keyword):
    pass


@dataclass(repr=False, kw_only=True)
class DeathPriest(Keyword):
    pass


@dataclass(repr=False, kw_only=True)
class Deathseeker(Keyword):
    pass


@dataclass(repr=False, kw_only=True)
class Dog(Keyword):
    pass


@dataclass(repr=False, kw_only=True)
class Dragon(Keyword):
    pass


@dataclass(repr=False, kw_only=True)
class DragonChild(Keyword):
    pass


@dataclass(repr=False, kw_only=True)
class Drunkard(Keyword):
    pass


@dataclass(repr=False, kw_only=True)
class ElementalMaster(Keyword):
    pass


@dataclass(repr=False, kw_only=True)
class Empress(Keyword):
    pass


@dataclass(repr=False, kw_only=True)
class Engineer(Keyword):
    pass


@dataclass(repr=False, kw_only=True)
class Fallen(Keyword):
    pass


@dataclass(repr=False, kw_only=True)
class Geisha(Keyword):
    pass


@dataclass(repr=False, kw_only=True)
class Goblin(Keyword):
    pass


@dataclass(repr=False, kw_only=True)
class Goryo(Keyword):
    pass


@dataclass(repr=False, kw_only=True)
class Governor(Keyword):
    pass


@dataclass(repr=False, kw_only=True)
class Guard(Keyword):
    pass


@dataclass(repr=False, kw_only=True)
class Hatamoto(Keyword):
    pass


@dataclass(repr=False, kw_only=True)
class Heir(Keyword):
    pass


@dataclass(repr=False, kw_only=True)
class Hero(Keyword):
    pass


@dataclass(repr=False, kw_only=True)
class HiddenGuard(Keyword):
    pass


@dataclass(repr=False, kw_only=True)
class Hunter(Keyword):
    pass


@dataclass(repr=False, kw_only=True)
class Imperial(Keyword):
    pass


@dataclass(repr=False, kw_only=True)
class Infiltrator(Keyword):
    pass


@dataclass(repr=False, kw_only=True)
class Inquisitor(Keyword):
    pass


@dataclass(repr=False, kw_only=True)
class Intimidator(Keyword):
    pass


@dataclass(repr=False, kw_only=True)
class IronCrane(Keyword):
    pass


@dataclass(repr=False, kw_only=True)
class Ishiken(Keyword):
    pass


@dataclass(repr=False, kw_only=True)
class Jade(Keyword):
    pass


@dataclass(repr=False, kw_only=True)
class Jester(Keyword):
    pass


@dataclass(repr=False, kw_only=True)
class Junshin(Keyword):
    pass


@dataclass(repr=False, kw_only=True)
class Kami(Keyword):
    pass


@dataclass(repr=False, kw_only=True)
class Kenku(Keyword):
    pass


@dataclass(repr=False, kw_only=True)
class Kitsune(Keyword):
    pass


@dataclass(repr=False, kw_only=True)
class Kolat(Keyword):
    pass


@dataclass(repr=False, kw_only=True)
class Kuroiban(Keyword):
    pass


@dataclass(repr=False, kw_only=True)
class LadyOfTheSun(Keyword):
    pass


@dataclass(repr=False, kw_only=True)
class LordOfBlades(Keyword):
    pass


@dataclass(repr=False, kw_only=True)
class LoveLetter(Keyword):
    pass


@dataclass(repr=False, kw_only=True)
class Magistrate(Keyword):
    pass


@dataclass(repr=False, kw_only=True)
class MaiMaster(Keyword):
    pass


@dataclass(repr=False, kw_only=True)
class Martyr(Keyword):
    pass


@dataclass(repr=False, kw_only=True)
class MasterCoin(Keyword):
    pass


@dataclass(repr=False, kw_only=True)
class Mastermind(Keyword):
    pass


@dataclass(repr=False, kw_only=True)
class Mercenary(Keyword):
    pass


@dataclass(repr=False, kw_only=True)
class Merchant(Keyword):
    pass


@dataclass(repr=False, kw_only=True)
class Monk(Keyword):
    pass


@dataclass(repr=False, kw_only=True)
class Mountaineer(Keyword):
    pass


@dataclass(repr=False, kw_only=True)
class Musician(Keyword):
    pass


@dataclass(repr=False, kw_only=True)
class Ningyo(Keyword):
    pass


@dataclass(repr=False, kw_only=True)
class Nonhuman(Keyword):
    pass


@dataclass(repr=False, kw_only=True)
class Ogre(Keyword):
    pass


@dataclass(repr=False, kw_only=True)
class OneTribe(Keyword):
    pass


@dataclass(repr=False, kw_only=True)
class Oni(Keyword):
    pass


@dataclass(repr=False, kw_only=True)
class Orator(Keyword):
    pass


@dataclass(repr=False, kw_only=True)
class OrderOfTheSpider(Keyword):
    pass


@dataclass(repr=False, kw_only=True)
class OrderOfVenom(Keyword):
    pass


@dataclass(repr=False, kw_only=True)
class Orochi(Keyword):
    pass


@dataclass(repr=False, kw_only=True)
class Paragon(Keyword):
    pass


@dataclass(repr=False, kw_only=True)
class Pirate(Keyword):
    pass


@dataclass(repr=False, kw_only=True)
class Poet(Keyword):
    pass


@dataclass(repr=False, kw_only=True)
class PoisonMaster(Keyword):
    pass


@dataclass(repr=False, kw_only=True)
class Prophetess(Keyword):
    pass


@dataclass(repr=False, kw_only=True)
class Ratling(Keyword):
    pass


@dataclass(repr=False, kw_only=True)
class RitualMaster(Keyword):
    pass


@dataclass(repr=False, kw_only=True)
class Ronin(Keyword):
    pass


@dataclass(repr=False, kw_only=True)
class SakeAddict(Keyword):
    pass


@dataclass(repr=False, kw_only=True)
class Savior(Keyword):
    pass


@dataclass(repr=False, kw_only=True)
class Scavenger(Keyword):
    pass


@dataclass(repr=False, kw_only=True)
class Scholar(Keyword):
    pass


@dataclass(repr=False, kw_only=True)
class ScionOfFlame(Keyword):
    pass


@dataclass(repr=False, kw_only=True)
class ScionOfStone(Keyword):
    pass


@dataclass(repr=False, kw_only=True)
class ScionOfTheSea(Keyword):
    pass


@dataclass(repr=False, kw_only=True)
class ScionOfTheVoid(Keyword):
    pass


@dataclass(repr=False, kw_only=True)
class ScionOfTheWind(Keyword):
    pass


@dataclass(repr=False, kw_only=True)
class ScourgeOfDarkness(Keyword):
    pass


@dataclass(repr=False, kw_only=True)
class Scout(Keyword):
    pass


@dataclass(repr=False, kw_only=True)
class Seductress(Keyword):
    pass


@dataclass(repr=False, kw_only=True)
class Shadowlands(Keyword):
    pass


@dataclass(repr=False, kw_only=True)
class ShibasSoul(Keyword):
    pass


@dataclass(repr=False, kw_only=True)
class ShojusSoul(Keyword):
    pass


@dataclass(repr=False, kw_only=True)
class Shugenja(Keyword):
    pass


@dataclass(repr=False, kw_only=True)
class Siege(Keyword):
    pass


@dataclass(repr=False, kw_only=True)
class SilkenSect(Keyword):
    pass


@dataclass(repr=False, kw_only=True)
class Sinner(Keyword):
    pass


@dataclass(repr=False, kw_only=True)
class Smith(Keyword):
    pass


@dataclass(repr=False, kw_only=True)
class Sociopath(Keyword):
    pass


@dataclass(repr=False, kw_only=True)
class SodanSenzo(Keyword):
    pass


@dataclass(repr=False, kw_only=True)
class Spy(Keyword):
    pass


@dataclass(repr=False, kw_only=True)
class StableMaster(Keyword):
    pass


@dataclass(repr=False, kw_only=True)
class StormRider(Keyword):
    pass


@dataclass(repr=False, kw_only=True)
class Storyteller(Keyword):
    pass


@dataclass(repr=False, kw_only=True)
class Tattooed(Keyword):
    pass


@dataclass(repr=False, kw_only=True)
class TheBlindPhoenix(Keyword):
    pass


@dataclass(repr=False, kw_only=True)
class TheGrowingStorm(Keyword):
    pass


@dataclass(repr=False, kw_only=True)
class TheInfiniteEye(Keyword):
    pass


@dataclass(repr=False, kw_only=True)
class TheLaughingDragon(Keyword):
    pass


@dataclass(repr=False, kw_only=True)
class TheLittleBear(Keyword):
    pass


@dataclass(repr=False, kw_only=True)
class TheLivingGoddess(Keyword):
    pass


@dataclass(repr=False, kw_only=True)
class TheMaskedCrab(Keyword):
    pass


@dataclass(repr=False, kw_only=True)
class TheMaskedCrane(Keyword):
    pass


@dataclass(repr=False, kw_only=True)
class TheMaskedLion(Keyword):
    pass


@dataclass(repr=False, kw_only=True)
class TheMaskedMonkey(Keyword):
    pass


@dataclass(repr=False, kw_only=True)
class TheMaskedPhoenix(Keyword):
    pass


@dataclass(repr=False, kw_only=True)
class TheMaskedTortoise(Keyword):
    pass


@dataclass(repr=False, kw_only=True)
class TheMaskedWasp(Keyword):
    pass


@dataclass(repr=False, kw_only=True)
class ThePoisonMask(Keyword):
    pass


@dataclass(repr=False, kw_only=True)
class TheShadowEmperor(Keyword):
    pass


@dataclass(repr=False, kw_only=True)
class TheSmilingBlade(Keyword):
    pass


@dataclass(repr=False, kw_only=True)
class TheSteelLion(Keyword):
    pass


@dataclass(repr=False, kw_only=True)
class Thunder(Keyword):
    pass


@dataclass(repr=False, kw_only=True)
class Undead(Keyword):
    pass


@dataclass(repr=False, kw_only=True)
class Unmaker(Keyword):
    pass


@dataclass(repr=False, kw_only=True)
class VoiceOfTheEmpress(Keyword):
    pass


@dataclass(repr=False, kw_only=True)
class WarLeader(Keyword):
    pass


@dataclass(repr=False, kw_only=True)
class WarriorOfTheBrightEye(Keyword):
    pass


@dataclass(repr=False, kw_only=True)
class WitchHunter(Keyword):
    pass


@dataclass(repr=False, kw_only=True)
class Yojimbo(Keyword):
    pass


@dataclass(repr=False, kw_only=True)
class Zealot(Keyword):
    pass


@dataclass(repr=False, kw_only=True)
class Zombie(Keyword):
    pass


# Holding keywords


@dataclass(repr=False, kw_only=True)
class Barrack(Keyword):
    pass


@dataclass(repr=False, kw_only=True)
class Barracks(Keyword):
    pass


@dataclass(repr=False, kw_only=True)
class Castle(Keyword):
    pass


@dataclass(repr=False, kw_only=True)
class Dojo(Keyword):
    pass


@dataclass(repr=False, kw_only=True)
class Farm(Keyword):
    pass


@dataclass(repr=False, kw_only=True)
class Fortification(Keyword):
    pass


@dataclass(repr=False, kw_only=True)
class Fudo(Keyword):
    pass


@dataclass(repr=False, kw_only=True)
class GeishaHouse(Keyword):
    pass


@dataclass(repr=False, kw_only=True)
class Library(Keyword):
    pass


@dataclass(repr=False, kw_only=True)
class Market(Keyword):
    pass


@dataclass(repr=False, kw_only=True)
class Mine(Keyword):
    pass


@dataclass(repr=False, kw_only=True)
class Pearl(Keyword):
    pass


@dataclass(repr=False, kw_only=True)
class PearlBed(Keyword):
    pass


@dataclass(repr=False, kw_only=True)
class Retainer(Keyword):
    pass


@dataclass(repr=False, kw_only=True)
class SakeHouse(Keyword):
    pass


@dataclass(repr=False, kw_only=True)
class Stables(Keyword):
    pass


@dataclass(repr=False, kw_only=True)
class Swamp(Keyword):
    pass


@dataclass(repr=False, kw_only=True)
class Temple(Keyword):
    pass


@dataclass(repr=False, kw_only=True)
class Village(Keyword):
    pass


@dataclass(repr=False, kw_only=True)
class Winter(Keyword):
    pass


# Event keywords


@dataclass(repr=False, kw_only=True)
class Festival(Keyword):
    pass
