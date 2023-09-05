from __future__ import annotations

from copy import copy
from dataclasses import field, make_dataclass
from typing import Type

from l5r_auto.utils import dataclass_ as dataclass

from .clans import NagaFaction, NinjaFaction, SpiritFaction


@dataclass
class Keyword:
    name: str = field(init=False)

    def __post_init__(self):
        self.name = self.__class__.__name__


def SoulOf(title: str) -> Type[Keyword]:
    klass = copy(Keyword)
    klass.name = f"Soul of {title}"

    return klass


@dataclass
class Baraunghar(Keyword):
    pass


@dataclass
class Bushi(Keyword):
    pass


@dataclass
class Explorer(Keyword):
    pass


@dataclass
class Port(Keyword):
    pass


@dataclass
class Samurai(Keyword):
    pass


# Boldface keywords
@dataclass
class Armor(Keyword):
    """A keyword found on some Items. A Personality cannot attach more than one Armor."""


@dataclass
class Cavalry(Keyword):
    """The Cavalry keyword is relevant to the following player ability which all players have:
    Absent Engage: Target your unbowed Personality in a Cavalry unit at any location.
    Move it to the current battlefield.
    Note that a “Cavalry unit” is one in which the Personality and all Followers, if any, have
    the Cavalry keyword (see Unit keywords)."""


@dataclass
class Conqueror(Keyword):
    """Cards in a Conqueror Personality’s unit do not bow prior to returning home after a
    battle’s resolution.
    """


@dataclass
class Courage(Keyword):
    """All players have the following ability relevant to the Courage keyword.
    Repeatable Courage Interrupt: Discard a Courage card from your hand to give one
    of the action’s Fear effects either +2 or-2 strength.
    """


@dataclass
class Destined(Keyword):
    """After a player’s card with the Destined keyword enters play, he or she draws a Fate
    card.
    """


@dataclass
class Duelist(Keyword):
    """If a Personality in a duel has the Duelist keyword then, if scores are tied in the duel’s
    resolution, and the other Personality is not a Duelist, the Duelist wins.
    """


@dataclass
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


@dataclass
class Fortication(Keyword):
    """When brought into play, Holdings with the Fortication keyword are attached to the
    Province they entered play from, or to any of their player’s Provinces if they were not
    brought in from a Province. Such Holding cards are kept under the card in the
    Province (if any), in the same way an attachment is kept under its Personality.
    Fortications are Recruited as normal, and enter play bowed. They are destroyed if
    the Province is destroyed. During a battle, abilities on a Fortication can only be used
    if the Fortication is attached to the current battleeld’s Province.
    """


@dataclass
class Inexperienced(Keyword):
    pass


@dataclass
class Kensai(Keyword):
    """A Kensai Personality can attach two Weapons if neither of them is Two-handed."""


@dataclass
class Kharmic(Keyword):
    """A keyword that can appear on Dynasty or Fate cards.

    Players have the following ability relevant to Kharmic cards:
    Kharmic Repeatable Limited, : Discard a Kharmic card from your hand to draw a
    card, or discard a Kharmic card from your Province to rell the Province face-up.
    """


@dataclass
class Legacy(Keyword):
    """A keyword on Holdings that refers to the following player ability:

    Dynasty, GC*: Remove a card in your hand from the game to search your deck and
    Provinces for a Legacy Holding and Recruit it. If you fail to nd one, you lose the game.
    """


@dataclass
class Loyal(Keyword):
    """A Personality with the Loyal keyword will not be controlled by a player who does not
    share a Clan Alignment with the Personality. This restricts entering play as well as
    changing control.
    """


@dataclass
class Naval(Keyword):
    """Players have the following ability relevant to Naval cards, known as Naval Invasion:
    NAVAL INVASION #
    Engage: If you are the Attacker, you have the first opportunity to take a Battle action,
    which must come from a card in a Naval Personality’s unit. Passing that action does
    not count toward ending the action round.
    """


@dataclass
class Reserve(Keyword):
    """The following player abilities are relevant to the Reserve keyword:
    Absent Repeatable Battle, : If he would be opposed, Recruit your target Reserve
    Personality (into the current battleeld).
    Repeatable Battle, : If it would be opposed, Equip a Reserve attachment to your
    target Personality (at the current battleeld)."""


@dataclass
class Resilient(Keyword):
    """The Resilient keyword means that, once per game per card, the card is not destroyed
    by the rulebook effects of battle resolution; that is, if its side loses or it ties. Its
    attached cards are still destroyed normally.
    A card that loses and then gains Resilient is still bound by the “once per game per
    card” restriction."""


@dataclass
class Tactician(Keyword):
    """All Tactician Personalities have the following ability, known as “Tactical Advantage”.
    This ability is not printed on the Tactician and cannot be removed or copied from him
    or her.
    TACTICAL ADVANTAGE #
    Battle: Discard a card to give this Personality a Force bonus equal to the Focus Value
    of the discarded card.
    """


@dataclass
class Weapon(Keyword):
    """A Personality can have only one Weapon Item attached. Exception: Kensai."""


@dataclass
class Unique(Keyword):
    """A player will not bring into play or take control of a Unique card if he or she already
    controls a Unique card with the same title (but see Experienced for exceptions). If a
    player takes control of a unit with a copy of a Unique attachment he or she already
    controls, discard the new attachment.
    The Unique keyword also restricts deck construction.
    """


# Elements


@dataclass
class Air(Keyword):
    pass


@dataclass
class Earth(Keyword):
    pass


@dataclass
class Fire(Keyword):
    pass


@dataclass
class Void(Keyword):
    pass


@dataclass
class Water(Keyword):
    pass


# Minor clans and factions


@dataclass
class BatClan(Keyword):
    pass


@dataclass
class DragonflyClan(Keyword):
    pass


@dataclass
class Naga(Keyword, NagaFaction):
    pass


@dataclass
class Ninja(Keyword, NinjaFaction):
    pass


@dataclass
class Spirit(Keyword, SpiritFaction):
    pass


# Other keywords
@dataclass
class Actor(Keyword):
    pass


@dataclass
class Alchemist(Keyword):
    pass


@dataclass
class Ancestor(Keyword):
    pass


@dataclass
class Artisan(Keyword):
    pass


@dataclass
class Ashigaru(Keyword):
    pass


@dataclass
class Assassin(Keyword):
    pass


@dataclass
class BattleMaiden(Keyword):
    pass


@dataclass
class Beastmaster(Keyword):
    pass


@dataclass
class Berserker(Keyword):
    pass


@dataclass
class BitterLies(Keyword):
    pass


@dataclass
class BlessedByBenten(Keyword):
    pass


@dataclass
class Bloodspeaker(Keyword):
    pass


@dataclass
class BogHag(Keyword):
    pass


@dataclass
class BountyHunter(Keyword):
    pass


@dataclass
class Braggart(Keyword):
    pass


@dataclass
class Bully(Keyword):
    pass


@dataclass
class Chieftain(Keyword):
    pass


@dataclass
class ChildOfProphecy(Keyword):
    pass


@dataclass
class ClanChampion(Keyword):
    pass


@dataclass
class Commander(Keyword):
    pass


@dataclass
class Constrictor(Keyword):
    pass


@dataclass
class Courtier(Keyword):
    pass


@dataclass
class Cursed(Keyword):
    pass


@dataclass
class Daimyo(Keyword):
    pass


@dataclass
class DeathPriest(Keyword):
    pass


@dataclass
class Deathseeker(Keyword):
    pass


@dataclass
class Dog(Keyword):
    pass


@dataclass
class Dragon(Keyword):
    pass


@dataclass
class DragonChild(Keyword):
    pass


@dataclass
class Drunkard(Keyword):
    pass


@dataclass
class ElementalMaster(Keyword):
    pass


@dataclass
class Empress(Keyword):
    pass


@dataclass
class Engineer(Keyword):
    pass


@dataclass
class Fallen(Keyword):
    pass


@dataclass
class Geisha(Keyword):
    pass


@dataclass
class Goblin(Keyword):
    pass


@dataclass
class Goryo(Keyword):
    pass


@dataclass
class Governor(Keyword):
    pass


@dataclass
class Guard(Keyword):
    pass


@dataclass
class Hatamoto(Keyword):
    pass


@dataclass
class Heir(Keyword):
    pass


@dataclass
class Hero(Keyword):
    pass


@dataclass
class HiddenGuard(Keyword):
    pass


@dataclass
class Hunter(Keyword):
    pass


@dataclass
class Imperial(Keyword):
    pass


@dataclass
class Infiltrator(Keyword):
    pass


@dataclass
class Inquisitor(Keyword):
    pass


@dataclass
class Intimidator(Keyword):
    pass


@dataclass
class IronCrane(Keyword):
    pass


@dataclass
class Ishiken(Keyword):
    pass


@dataclass
class Jade(Keyword):
    pass


@dataclass
class Jester(Keyword):
    pass


@dataclass
class Junshin(Keyword):
    pass


@dataclass
class Kami(Keyword):
    pass


@dataclass
class Kenku(Keyword):
    pass


@dataclass
class Kitsune(Keyword):
    pass


@dataclass
class Kolat(Keyword):
    pass


@dataclass
class Kuroiban(Keyword):
    pass


@dataclass
class LadyOfTheSun(Keyword):
    pass


@dataclass
class LordOfBlades(Keyword):
    pass


@dataclass
class LoveLetter(Keyword):
    pass


@dataclass
class Magistrate(Keyword):
    pass


@dataclass
class MaiMaster(Keyword):
    pass


@dataclass
class Martyr(Keyword):
    pass


@dataclass
class MasterCoin(Keyword):
    pass


@dataclass
class Mastermind(Keyword):
    pass


@dataclass
class Mercenary(Keyword):
    pass


@dataclass
class Merchant(Keyword):
    pass


@dataclass
class Monk(Keyword):
    pass


@dataclass
class Mountaineer(Keyword):
    pass


@dataclass
class Musician(Keyword):
    pass


@dataclass
class Ningyo(Keyword):
    pass


@dataclass
class Nonhuman(Keyword):
    pass


@dataclass
class Ogre(Keyword):
    pass


@dataclass
class OneTribe(Keyword):
    pass


@dataclass
class Oni(Keyword):
    pass


@dataclass
class Orator(Keyword):
    pass


@dataclass
class OrderOfTheSpider(Keyword):
    pass


@dataclass
class OrderOfVenom(Keyword):
    pass


@dataclass
class Orochi(Keyword):
    pass


@dataclass
class Paragon(Keyword):
    pass


@dataclass
class Pirate(Keyword):
    pass


@dataclass
class Poet(Keyword):
    pass


@dataclass
class PoisonMaster(Keyword):
    pass


@dataclass
class Prophetess(Keyword):
    pass


@dataclass
class Ratling(Keyword):
    pass


@dataclass
class RitualMaster(Keyword):
    pass


@dataclass
class Ronin(Keyword):
    pass


@dataclass
class SakeAddict(Keyword):
    pass


@dataclass
class Savior(Keyword):
    pass


@dataclass
class Scavenger(Keyword):
    pass


@dataclass
class Scholar(Keyword):
    pass


@dataclass
class ScionOfFlame(Keyword):
    pass


@dataclass
class ScionOfStone(Keyword):
    pass


@dataclass
class ScionOfTheSea(Keyword):
    pass


@dataclass
class ScionOfTheVoid(Keyword):
    pass


@dataclass
class ScionOfTheWind(Keyword):
    pass


@dataclass
class ScourgeOfDarkness(Keyword):
    pass


@dataclass
class Scout(Keyword):
    pass


@dataclass
class Seductress(Keyword):
    pass


@dataclass
class Shadowlands(Keyword):
    pass


@dataclass
class ShibasSoul(Keyword):
    pass


@dataclass
class ShojusSoul(Keyword):
    pass


@dataclass
class Shugenja(Keyword):
    pass


@dataclass
class Siege(Keyword):
    pass


@dataclass
class SilkenSect(Keyword):
    pass


@dataclass
class Sinner(Keyword):
    pass


@dataclass
class Smith(Keyword):
    pass


@dataclass
class Sociopath(Keyword):
    pass


@dataclass
class SodanSenzo(Keyword):
    pass


@dataclass
class Spy(Keyword):
    pass


@dataclass
class StableMaster(Keyword):
    pass


@dataclass
class StormRider(Keyword):
    pass


@dataclass
class Storyteller(Keyword):
    pass


@dataclass
class Tattooed(Keyword):
    pass


@dataclass
class TheBlindPhoenix(Keyword):
    pass


@dataclass
class TheGrowingStorm(Keyword):
    pass


@dataclass
class TheInfiniteEye(Keyword):
    pass


@dataclass
class TheLaughingDragon(Keyword):
    pass


@dataclass
class TheLittleBear(Keyword):
    pass


@dataclass
class TheLivingGoddess(Keyword):
    pass


@dataclass
class TheMaskedCrab(Keyword):
    pass


@dataclass
class TheMaskedCrane(Keyword):
    pass


@dataclass
class TheMaskedLion(Keyword):
    pass


@dataclass
class TheMaskedMonkey(Keyword):
    pass


@dataclass
class TheMaskedPhoenix(Keyword):
    pass


@dataclass
class TheMaskedTortoise(Keyword):
    pass


@dataclass
class TheMaskedWasp(Keyword):
    pass


@dataclass
class ThePoisonMask(Keyword):
    pass


@dataclass
class TheShadowEmperor(Keyword):
    pass


@dataclass
class TheSmilingBlade(Keyword):
    pass


@dataclass
class TheSteelLion(Keyword):
    pass


@dataclass
class Thunder(Keyword):
    pass


@dataclass
class Undead(Keyword):
    pass


@dataclass
class Unmaker(Keyword):
    pass


@dataclass
class VoiceOfTheEmpress(Keyword):
    pass


@dataclass
class WarLeader(Keyword):
    pass


@dataclass
class WarriorOfTheBrightEye(Keyword):
    pass


@dataclass
class WitchHunter(Keyword):
    pass


@dataclass
class Yojimbo(Keyword):
    pass


@dataclass
class Zealot(Keyword):
    pass


@dataclass
class Zombie(Keyword):
    pass


# Holding keywords


@dataclass
class Barrack(Keyword):
    pass


@dataclass
class Barracks(Keyword):
    pass


@dataclass
class Castle(Keyword):
    pass


@dataclass
class Dojo(Keyword):
    pass


@dataclass
class Farm(Keyword):
    pass


@dataclass
class Fortification(Keyword):
    pass


@dataclass
class Fudo(Keyword):
    pass


@dataclass
class GeishaHouse(Keyword):
    pass


@dataclass
class Library(Keyword):
    pass


@dataclass
class Market(Keyword):
    pass


@dataclass
class Mine(Keyword):
    pass


@dataclass
class Pearl(Keyword):
    pass


@dataclass
class PearlBed(Keyword):
    pass


@dataclass
class Retainer(Keyword):
    pass


@dataclass
class SakeHouse(Keyword):
    pass


@dataclass
class Stables(Keyword):
    pass


@dataclass
class Swamp(Keyword):
    pass


@dataclass
class Temple(Keyword):
    pass


@dataclass
class Village(Keyword):
    pass


@dataclass
class Winter(Keyword):
    pass


# Event keywords


@dataclass
class Festival(Keyword):
    pass
