from __future__ import annotations
import time
from pathlib import Path
import json
import html
from typing import TypedDict
import requests
from pprint import pprint

JSON_FILE = Path(__file__).parent / "cards.json"

URL = "https://api.oracleofthevoid.com/oracle-fetch?table=l5r&cardid={number}"

if JSON_FILE.exists():
    cards = json.load(open(JSON_FILE))
else:
    cards = []

start_number = len(cards)
for number in range(start_number, start_number + 300):
    response = requests.get(URL.format(number=number))
    if response.status_code == 200:
        card = response.json()
        cards.append(card)

        json.dump(cards, open(Path(__file__).parent / "cards.json", "w"), indent=4)
        print(f"Added card {card['cardid']}")
    elif response.status_code == 404:
        print(f"Card {number} not found")
        break
    time.sleep(0.1)

print("Done")


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
    plural = card_type[:-1] + "ies" if card_type.endswith("y") else card_type + "s"

    cards_by_type.setdefault(plural, []).append(card)


card_path = Path(__file__).parent.parent / "cards"

for type_, cards_ in cards_by_type.items():
    save_path = card_path / type_
    save_path.mkdir(exist_ok=True, parents=True)

    json.dump(cards_, open(save_path / f"{type_}.json", "w"), indent=4)

import ast
import re


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
    "A Brother's Destiny (Ivory Edition)": "Ivory",
    "A Brother's Destiny (Twenty Festivals)": "TwentyFestivals",
    "Age of Conquest (Emperor)": "Emperor",
    "Age of Enlightenment (Lotus)": "Lotus",
    "Clan Wars (Imperial)": "Imperial",
    "Destroyer War (Celestial)": "Celestial",
    "Four Winds (Gold)": "Gold",
    "Hidden Emperor (Jade)": "Jade",
    "Race for the Throne (Samurai)": "Samurai",
    "Rain of Blood (Diamond)": "Diamond",
    "Modern": "Modern",
    "Onyx Edition": "Onyx",
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


def to_ast(
    card: Card,
) -> tuple[ast.Assign | None, list[str] | None, list[str] | None, list[str] | None]:
    if not (type_to_ast := types_to_ast[card["type"][0].lower()]):
        return None, None, None, None

    class_name = to_valid_var_name(card["formattedtitle"])
    legalities = get_legalities(card.get("legality", []))
    clans = card.get("clan", [])
    keywords = [remove_bold(x) for x in card.get("keywords", [])]

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
                            elts=[
                                ast.Name(
                                    id=x,
                                    ctx=ast.Load(),
                                )
                                for x in keywords
                            ],
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


personalities = sorted(
    cards_by_type["personalities"], key=lambda card: card["formattedtitle"]
)
assigns_by_clan: dict[str, list[ast.Assign]] = {}
import_clans: set[str] = set()
import_keywords: set[str] = set()
import_legalities: set[str] = set()

for personality in personalities:
    ast_, legalities, keywords, clans = to_ast(personality)
    if ast_ is None:
        continue

    assigns_by_clan.setdefault(personality["clan"][0], []).append(ast_)
    if clans:
        import_clans.update(clans)
    if keywords:
        import_keywords.update(keywords)
    if legalities:
        import_legalities.update(legalities)


for clan, assigns in assigns_by_clan.items():
    if (module_path := card_path / "personalities" / f"{clan.lower()}.py").exists():
        module_ast = ast.parse(module_path.read_text())
    else:
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
    module_ast.body.extend(assigns)

    module_ast = ast.fix_missing_locations(module_ast)

    module_path.write_text(ast.unparse(module_ast))


ast_ = {
    "ast_type": "Assign",
    "targets": [
        {
            "ctx": {"ast_type": "Store"},
            "id": "ShinjoXushen",
        }
    ],
    "value": {
        "args": [],
        "ast_type": "Call",
        "func": {
            "ast_type": "Name",
            "ctx": {"ast_type": "Load"},
            "id": "Personality",
        },
        "keywords": [
            {
                "arg": "id",
                "ast_type": "keyword",
                "value": {"ast_type": "Constant", "value": 6925},
            },
            {
                "arg": "title",
                "ast_type": "keyword",
                "value": {"ast_type": "Constant", "value": "Shinjo Xushen"},
            },
            {
                "arg": "force",
                "ast_type": "keyword",
                "value": {"ast_type": "Constant", "value": 3},
            },
            {
                "arg": "chi",
                "ast_type": "keyword",
                "value": {"ast_type": "Constant", "value": 3},
            },
            {
                "arg": "honor_requirement",
                "ast_type": "keyword",
                "value": {"ast_type": "Constant", "value": None},
            },
            {
                "arg": "personal_honor",
                "ast_type": "keyword",
                "value": {"ast_type": "Constant", "value": 1},
            },
            {
                "arg": "gold_cost",
                "ast_type": "keyword",
                "value": {"ast_type": "Constant", "value": 8},
            },
            {
                "arg": "clan",
                "ast_type": "keyword",
                "value": {
                    "ast_type": "List",
                    "ctx": {"ast_type": "Load"},
                    "elts": [
                        {
                            "ast_type": "Name",
                            "ctx": {"ast_type": "Load"},
                            "id": "Unicorn",
                        }
                    ],
                },
            },
            {
                "arg": "keywords",
                "ast_type": "keyword",
                "value": {
                    "ast_type": "List",
                    "ctx": {"ast_type": "Load"},
                    "elts": [
                        {
                            "ast_type": "Name",
                            "ctx": {"ast_type": "Load"},
                            "id": "Cavalry",
                        },
                        {
                            "ast_type": "Name",
                            "ctx": {"ast_type": "Load"},
                            "id": "Baraunghar",
                        },
                        {
                            "ast_type": "Name",
                            "ctx": {"ast_type": "Load"},
                            "id": "Bushi",
                        },
                    ],
                },
            },
            {
                "arg": "traits",
                "ast_type": "keyword",
                "value": {
                    "ast_type": "List",
                    "ctx": {"ast_type": "Load"},
                    "elts": [],
                },
            },
            {
                "arg": "abilities",
                "ast_type": "keyword",
                "value": {
                    "ast_type": "List",
                    "ctx": {"ast_type": "Load"},
                    "elts": [],
                },
            },
            {
                "arg": "legality",
                "ast_type": "keyword",
                "value": {
                    "ast_type": "List",
                    "ctx": {"ast_type": "Load"},
                    "elts": [
                        {
                            "ast_type": "Name",
                            "ctx": {"ast_type": "Load"},
                            "id": "Diamond",
                        }
                    ],
                },
            },
        ],
    },
}
