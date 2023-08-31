from __future__ import annotations
import time
from pathlib import Path
import json
import html
from typing import TypedDict
import requests
from pprint import pprint

from itertools import chain


import ast
import re

ROOT_PATH = Path(__file__).parent.parent
CARD_PATH = ROOT_PATH / "cards"
GENERATOR_PATH = ROOT_PATH / "generate"
JSON_FILE = GENERATOR_PATH / "cards.json"

URL = "https://api.oracleofthevoid.com/oracle-fetch?table=l5r&cardid={number}"


class Card(TypedDict):
    """{
    "playtestname": [
        "A New Year"
    ],
    "printing": [
        {
            "flavor": [
                "<i>\"The Empress declared a great celebration to mark the victory, and the Champions of the Great Clans were honored with invitations to her court.\" - The Chronicles of Empress Iweko, Part V</i>"
            ],
            "printingid": "1",
            "number": [
                "1"
            ],
            "artnumber": [
                "9850"
            ],
            "set": [
                "Celestial Edition"
            ],
            "artist": [
                "IFS"
            ],
            "printimagehash": [
                "93/f6"
            ],
            "text": [
                "Discard zero to two cards; each other player in turn order may discard a card. Each player then draws as many cards as he discarded."
            ],
            "rarity": [
                "Rare"
            ]
        },
        {
            "printingid": "2",
            "set": [
                "Twenty Festivals"
            ],
            "keywords": [
                "Festival"
            ],
            "artist": [
                "IFS"
            ],
            "use": [
                "Story card"
            ],
            "printimagehash": [
                "aa/10"
            ],
            "title": [
                "A New Year"
            ],
            "type": [
                "Event"
            ],
            "flavor": [
                "With each new year come new challenges and celebrations, but few years see the ascension of a new Emperor. When it occurs, a series of twenty festivals is held to commemorate the occasion."
            ],
            "number": [
                "1"
            ],
            "artnumber": [
                "17400454"
            ],
            "text": [
                "Open: Discard zero to two cards; each other player in turn order may discard a card. Each player then draws as many cards as he discarded."
            ],
            "rarity": [
                "Rare"
            ]
        }
    ],
    "printingprimary": "2",
    "text": [
        "<b>Open:</b> Discard zero to two cards; each other player in turn order may discard a card. Each player then draws as many cards as he discarded."
    ],
    "formattedtitle": "A New Year",
    "cardid": 59,
    "imagehash": "38/bf",
    "legality": [
        "A Brother's Destiny (Twenty Festivals)",
        "Destroyer War (Celestial)",
        "Onyx Edition",
        "Modern"
    ],
    "deck": [
        "Dynasty"
    ],
    "keywords": [
        "Festival"
    ],
    "title": [
        "A New Year"
    ],
    "type": [
        "Event"
    ]
    }"""

    playtestname: list[str]
    printing: list[dict[str, list[str]]]
    printingprimary: str
    text: list[str]
    formattedtitle: str
    cardid: int
    imagehash: str
    legality: list[str]
    deck: list[str]
    keywords: list[str]
    title: list[str]
    type: list[str]

    clan: list[str]


CLAN_KEYWORDS = {
    "Crab": "CrabClan",
    "Crane": "CraneClan",
    "Dragon": "DragonClan",
    "Lion": "LionClan",
    "Mantis": "MantisClan",
    "Phoenix": "PhoenixClan",
    "Scorpion": "ScorpionClan",
    "Spider": "SpiderClan",
    "Unicorn": "UnicornClan",
}
FACTION_KEYWORDS = {
    "Monk": "BrotherhoodOfShinsei",
    "Shadowlands": "ShadowlandsFaction",
    "Ninja": "NinjaFaction",
    "Spirit": "SpiritFaction",
    "Naga": "NagaFaction",
    "Ratling": "RatlingFaction",
}


def get_clans(card: Card, keywords: list[str] | None) -> list[str]:
    clans = []
    existing_factions = {**CLAN_KEYWORDS, **FACTION_KEYWORDS}

    for clan in card.get("clan", []):
        clan = to_import(clan)
        clans.append(existing_factions.get(clan, clan))

    for keyword in keywords or []:
        if faction := FACTION_KEYWORDS.get(keyword):
            clans.append(faction)

    return clans


def to_ast(
    card: Card,
) -> tuple[ast.Assign | None, list[str] | None, list[str] | None, list[str] | None]:
    if not (type_to_ast := types_to_ast[card["type"][0].lower()]):
        return None, None, None, None

    class_name = to_valid_var_name(card["formattedtitle"])
    legalities = get_legalities(card.get("legality", []))

    keywords, ast_keywords = get_keywords(card.get("keywords", []))

    clans = get_clans(card, keywords)

    return (
        ast.Assign(
            targets=[
                ast.Name(
                    id=class_name,
                    ctx=ast.Store(),
                )
            ],
            value=ast.Call(
                args=[],
                func=ast.Name(
                    id=type_to_ast,
                    ctx=ast.Load(),
                ),
                keywords=[
                    ast.keyword(
                        arg="id",
                        value=ast.Constant(
                            value=card["cardid"],
                        ),
                    ),
                    ast.keyword(
                        arg="title",
                        value=ast.Constant(
                            value=card["title"][0],
                        ),
                    ),
                    ast.keyword(
                        arg="force",
                        value=ast.Constant(
                            value=int(card["force"][0]),
                        ),
                    ),
                    ast.keyword(
                        arg="chi",
                        value=ast.Constant(
                            value=int(card["chi"][0]),
                        ),
                    ),
                    ast.keyword(
                        arg="honor_requirement",
                        value=ast.Constant(
                            value=get_honor(card["honor"][0]),
                        ),
                    ),
                    ast.keyword(
                        arg="personal_honor",
                        value=ast.Constant(
                            value=int(card["ph"][0]),
                        ),
                    ),
                    ast.keyword(
                        arg="gold_cost",
                        value=ast.Constant(
                            value=int(card["cost"][0]),
                        ),
                    ),
                    ast.keyword(
                        arg="clan",
                        value=ast.List(
                            elts=[
                                ast.Name(
                                    id=clan,
                                    ctx=ast.Load(),
                                )
                                for clan in clans
                            ],
                            ctx=ast.Load(),
                        ),
                    ),
                    ast.keyword(
                        arg="keywords",
                        value=ast.List(
                            elts=ast_keywords,
                            ctx=ast.Load(),
                        ),
                    ),
                    ast.keyword(
                        arg="traits",
                        value=ast.List(
                            elts=[],
                            ctx=ast.Load(),
                        ),
                    ),
                    ast.keyword(
                        arg="abilities",
                        value=ast.List(
                            elts=[],
                            ctx=ast.Load(),
                        ),
                    ),
                    ast.keyword(
                        arg="legality",
                        value=ast.List(
                            elts=[
                                ast.Name(
                                    id=legality,
                                    ctx=ast.Load(),
                                )
                                for legality in legalities
                            ],
                            ctx=ast.Load(),
                        ),
                    ),
                ],
            ),
            lineno=0,
        ),
        legalities,
        keywords,
        clans,
    )


def to_valid_var_name(s):
    # Replace HTML entities
    s = s.replace("&#149;", "")

    # Remove all non-word characters (everything except numbers and letters)
    s = re.sub(r"[^\w\s]", "", s)

    # Replace all runs of whitespace with a single underscore
    s = re.sub(r"\s+", "_", s)

    # Make sure it starts with a letter (use a prefix if it doesn't)
    if not s[0].isalpha():
        s = "var_" + s

    return s


# function for removing <b> and </b> from text
def remove_bold(text: str) -> str:
    return text.replace("<b>", "").replace("</b>", "")


types_to_ast = {"personality": "Personality"}
legality_to_ast = {
    "A Brother's Destiny (Ivory Edition)": "IvoryEdition",
    "A Brother's Destiny (Twenty Festivals)": "TwentyFestivalsEdition",
    "Age of Conquest (Emperor)": "EmperorEdition",
    "Age of Enlightenment (Lotus)": "LotusEdition",
    "Clan Wars (Imperial)": "ImperialEdition",
    "Destroyer War (Celestial)": "CelestialEdition",
    "Four Winds (Gold)": "GoldEdition",
    "Hidden Emperor (Jade)": "JadeEdition",
    "Race for the Throne (Samurai)": "SamuraiEdition",
    "Rain of Blood (Diamond)": "DiamondEdition",
    "Modern": "ModernEdition",
    "Onyx Edition": "OnyxEdition",
}


def get_legalities(legalities: list[str]) -> list[str]:
    found_legalities = []
    for legality in set(legalities):
        found_legalities.append(
            legality_to_ast[legality],
        )
    return found_legalities


def get_honor(honor: str) -> int | None:
    return int(honor) if honor != "-" else None


def to_import(name: str) -> str:
    return "".join(word.capitalize().replace("'", "") for word in name.split(" "))


KEYWORDS_TO_REMOVE = {
    "Crab Clan",
    "Crane Clan",
    "Dragon Clan",
    "Lion Clan",
    "Mantis Clan",
    "Phoenix Clan",
    "Scorpion Clan",
    "Spider Clan",
    "Unicorn Clan",
}


def get_keywords(keywords: list[str]) -> tuple[list[str], list[ast.AST]]:
    formatted_keywords: list[str] = []
    ast_keywords: list[ast.AST] = []
    ast_: ast.AST
    for keyword in keywords:
        keyword = remove_bold(keyword)
        if keyword in KEYWORDS_TO_REMOVE:
            continue

        if "Soul of" in keyword:
            soul_name = keyword.replace("Soul of ", "")
            keyword = "SoulOf"
            ast_ = ast.Call(
                args=[
                    ast.Constant(
                        value=soul_name,
                    )
                ],
                func=ast.Name(
                    id=keyword,
                    ctx=ast.Load(),
                ),
                keywords=[],
            )
        elif "Experienced" in keyword:
            if " " not in keyword:
                # Assume 1 experience
                experience = "1"
            else:
                experience = keyword.replace("Experienced ", "")
            keyword = "Experienced"
            ast_ = ast.Call(
                args=[
                    ast.Constant(
                        value=experience,
                    )
                ],
                func=ast.Name(
                    id=keyword,
                    ctx=ast.Load(),
                ),
                keywords=[],
            )
        else:
            keyword = to_import(keyword)
            ast_ = ast.Name(
                id=keyword,
                ctx=ast.Load(),
            )
        ast_keywords.append(ast_)
        formatted_keywords.append(keyword)

    return formatted_keywords, ast_keywords


def main():
    if JSON_FILE.exists():
        cards = json.load(open(JSON_FILE))
    else:
        cards = []

    # start_number = len(cards)
    # for number in range(start_number, start_number + 300):
    #     response = requests.get(URL.format(number=number))
    #     if response.status_code == 200:
    #         card = response.json()
    #         cards.append(card)

    #         json.dump(cards, open(Path(__file__).parent / "cards.json", "w"), indent=4)
    #         print(f"Added card {card['cardid']}")
    #     elif response.status_code == 404:
    #         print(f"Card {number} not found")
    #         break
    #     time.sleep(0.1)

    # print("Done")

    cards_by_type: dict[str, list[Card]] = {}

    for card in cards:
        formatted_legalities = []
        for legality in card.get("legality", []):
            formatted_legalities.append(legality.replace("&nbsp;", " "))
        card["legality"] = formatted_legalities

        # check legality contains twenty festival
        if "A Brother's Destiny (Twenty Festivals)" not in card.get("legality", []):
            continue

        card_type = card["type"][0].lower()

        cards_by_type.setdefault(plural(card_type), []).append(card)

    for type_, cards_ in cards_by_type.items():
        save_path = CARD_PATH / type_
        save_path.mkdir(exist_ok=True, parents=True)

        json.dump(cards_, open(save_path / f"{type_}.json", "w"), indent=4)

    get_personalities(cards_by_type["personalities"])


def plural(s: str) -> str:
    return s[:-1] + "ies" if s.endswith("y") else s + "s"


def check_keywords(keywords: list[str] | dict[str, list[str]]) -> None:
    from l5r_auto import keywords as keywords_module

    if isinstance(keywords, dict):
        keywords = list(chain.from_iterable(keywords.values()))

    for keyword in sorted(set(keywords)):
        if not hasattr(keywords_module, keyword):
            print(
                f"""@dataclass(kw_only=True)
class {keyword}(Keyword):
    pass
"""
            )


def clean_edition(edition: str) -> str:
    edition = edition.replace(":", "_").replace("&ndash;", "_")
    return to_snakecase(edition)


def to_snakecase(s: str) -> str:
    return s.replace(" ", "_").replace("'", "")


def get_module(type_folder, clan_folder, edition) -> Path:
    if clan_folder:
        return (
            CARD_PATH
            / type_folder
            / clan_folder.lower()
            / f'{edition.replace(":", "_").lower()}.py'
        )
    else:
        return CARD_PATH / type_folder / f'{edition.replace(":", "_").lower()}.py'


def get_personalities(cards: list[Card]) -> None:
    personalities = sorted(cards, key=lambda card: card["formattedtitle"])
    assigns_by_clan: dict[str, dict[str, list[ast.Assign]]] = {}
    import_clans: dict[str, dict[str, set[str]]] = {}
    import_keywords: dict[str, dict[str, set[str]]] = {}
    import_legalities: dict[str, dict[str, set[str]]] = {}

    for personality in personalities:
        ast_, legalities, keywords, clans = to_ast(personality)
        if ast_ is None:
            continue

        clan = personality["clan"][0]
        edition = clean_edition(personality["printing"][0]["set"][0])

        assigns_by_clan.setdefault(clan, {}).setdefault(edition, []).append(ast_)
        if clans:
            import_clans.setdefault(clan, {}).setdefault(edition, set()).update(clans)
        if keywords:
            import_keywords.setdefault(clan, {}).setdefault(edition, set()).update(
                keywords
            )
        if legalities:
            import_legalities.setdefault(clan, {}).setdefault(edition, set()).update(
                legalities
            )

    for clan, editions in assigns_by_clan.items():
        for edition, assigns in editions.items():
            if (module_path := get_module("personalities", clan, edition)).exists():
                module_ast = ast.parse(module_path.read_text())
            else:
                module_path.parent.mkdir(exist_ok=True, parents=True)
                module_ast = ast.Module(
                    body=[
                        ast.ImportFrom(
                            module="__future__",
                            names=[ast.alias(name="annotations", asname=None)],
                            level=0,
                        ),
                        ast.ImportFrom(
                            module="dataclasses",
                            names=[ast.alias(name="dataclass", asname=None)],
                            level=0,
                        ),
                        ast.ImportFrom(
                            module="l5r_auto.card",
                            names=[
                                ast.alias(name="Ability", asname=None),
                                ast.alias(name="Trait", asname=None),
                            ],
                            level=0,
                        ),
                        ast.ImportFrom(
                            module="l5r_auto.cards.personalities.common",
                            names=[ast.alias(name="Personality", asname=None)],
                            level=0,
                        ),
                    ],
                    type_ignores=[],
                )
            if clans := import_clans.get(clan, {}).get(edition, []):
                module_ast.body.append(
                    ast.ImportFrom(
                        module="l5r_auto.clans",
                        names=[
                            ast.alias(name=clan, asname=None) for clan in sorted(clans)
                        ],
                        level=0,
                    )
                )
            if keywords := import_keywords.get(clan, {}).get(edition, []):
                module_ast.body.append(
                    ast.ImportFrom(
                        module="l5r_auto.keywords",
                        names=[
                            ast.alias(name=keyword, asname=None)
                            for keyword in sorted(keywords)
                        ],
                        level=0,
                    )
                )
            if legalities := import_legalities.get(clan, {}).get(edition, []):
                module_ast.body.append(
                    ast.ImportFrom(
                        module="l5r_auto.legality",
                        names=[
                            ast.alias(name=legality, asname=None)
                            for legality in sorted(legalities)
                        ],
                        level=0,
                    )
                )

            module_ast.body.extend(assigns)

            module_ast = ast.fix_missing_locations(module_ast)

            module_path.write_text(ast.unparse(module_ast))

        print(f"Saved {clan} personalities")


if __name__ == "__main__":
    main()