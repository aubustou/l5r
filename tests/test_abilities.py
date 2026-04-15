"""Tests for Ability cost payment and target gathering."""

from __future__ import annotations

from l5r_auto.abilities import RecruitAction, _pay_gold
from l5r_auto.cards.personalities.common import Personality
from l5r_auto.cards.strategies.common import Strategy
from l5r_auto.clans import CrabClan, CraneClan
from l5r_auto.legality import TwentyFestivalsEdition
from l5r_auto.locations import PlayArea, ProvinceLocation
from tests.conftest import _CHEAP_PERS, _HOLDING, _HOLDING2, _PERSONALITY

# Unique personality card used across Unique-related tests
_UNIQUE_PERS = Personality(
    card_id=90091,
    title="Unique Test Hero",
    force=2,
    chi=2,
    personal_honor=0,
    gold_cost=3,
    honor_requirement=None,
    clan=[CrabClan],
    keywords=[],  # keywords set in tests that need Unique
    legality=[TwentyFestivalsEdition],
)

# Out-of-clan personality (CraneClan, player is CrabClan)
_OOC_PERS = Personality(
    card_id=90092,
    title="Out-of-Clan Samurai",
    force=2,
    chi=2,
    personal_honor=0,
    gold_cost=3,
    honor_requirement=None,
    clan=[CraneClan],
    legality=[TwentyFestivalsEdition],
)

# Expensive strategy for "not gathered when expensive" test
_EXPENSIVE_STRAT = Strategy(
    card_id=90093,
    title="Pricey Strategy",
    gold_cost=5,
    focus_value=3,
    legality=[TwentyFestivalsEdition],
)


class TestPayGold:
    def test_pay_gold_success_bows_entity(self, mock_game, mock_player):
        holding = _HOLDING(game=mock_game, owner=mock_player)
        holding.location = PlayArea
        holding.face_down = False
        mock_player.entities = [holding]

        result = _pay_gold(mock_game, mock_player, gold_cost=2)

        assert result is True
        assert holding.bowed is True

    def test_pay_gold_insufficient_returns_false(self, mock_game, mock_player):
        mock_player.entities = []  # no gold producers

        result = _pay_gold(mock_game, mock_player, gold_cost=2)

        assert result is False

    def test_pay_gold_bows_minimum_needed(self, mock_game, mock_player):
        """With a 3gp and a 2gp holding, paying 2 gold should bow only the 2gp one."""
        h3 = _HOLDING(game=mock_game, owner=mock_player)  # 3 gold production
        h3.location = PlayArea
        h3.face_down = False

        h2 = _HOLDING2(game=mock_game, owner=mock_player)  # 2 gold production
        h2.location = PlayArea
        h2.face_down = False

        mock_player.entities = [h3, h2]

        result = _pay_gold(mock_game, mock_player, gold_cost=2)

        assert result is True
        assert h2.bowed is True
        assert h3.bowed is False  # not needed


class TestRecruitActionPayCost:
    def test_pay_cost_success(self, mock_game, mock_player):
        holding = _HOLDING(game=mock_game, owner=mock_player)
        holding.location = PlayArea
        holding.face_down = False
        mock_player.entities = [holding]

        personality = _CHEAP_PERS(game=mock_game, owner=mock_player)
        # gold_cost=3, holding produces 3 → should succeed

        action = RecruitAction()
        result = action.pay_cost(mock_game, personality)

        assert result is True
        assert holding.bowed is True

    def test_pay_cost_insufficient_gold(self, mock_game, mock_player):
        mock_player.entities = []  # no gold producers

        personality = _PERSONALITY(game=mock_game, owner=mock_player)
        # gold_cost=5, no gold → should fail

        action = RecruitAction()
        result = action.pay_cost(mock_game, personality)

        assert result is False

    def test_pay_cost_out_of_clan_adds_two(self, mock_game, mock_player):
        """Out-of-clan personality costs 2 more gold."""
        holding = _HOLDING(game=mock_game, owner=mock_player)
        holding.location = PlayArea
        holding.face_down = False
        mock_player.entities = [holding]
        mock_player.clan = CrabClan  # player is Crab

        # OOC personality costs 3 normally, +2 = 5 effective; holding produces 3 → fail
        ooc = _OOC_PERS(game=mock_game, owner=mock_player)
        action = RecruitAction()
        result = action.pay_cost(mock_game, ooc)

        assert result is False  # 3 gold produced < 5 effective cost


class TestRecruitActionGather:
    def test_gather_skips_entity_not_in_province(self, mock_game, mock_player):
        entity = _PERSONALITY(game=mock_game, owner=mock_player)
        entity.location = PlayArea  # not ProvinceLocation
        entity.face_down = False
        mock_game.entities = [entity]

        action = RecruitAction()
        targets = list(action.gather_legal_target_entities(mock_game, mock_player))

        assert entity not in targets

    def test_gather_skips_face_down_in_province(self, mock_game, mock_player):
        entity = _PERSONALITY(game=mock_game, owner=mock_player)
        entity.location = ProvinceLocation
        entity.face_down = True  # face down
        mock_game.entities = [entity]

        action = RecruitAction()
        targets = list(action.gather_legal_target_entities(mock_game, mock_player))

        assert entity not in targets

    def test_gather_yields_face_up_in_province(self, mock_game, mock_player):
        entity = _PERSONALITY(game=mock_game, owner=mock_player)
        entity.location = ProvinceLocation
        entity.face_down = False
        mock_game.entities = [entity]

        action = RecruitAction()
        targets = list(action.gather_legal_target_entities(mock_game, mock_player))

        assert entity in targets

    def test_gather_skips_unique_already_in_play(self, mock_game, mock_player):
        from l5r_auto.keywords import Unique

        unique_card = Personality(
            card_id=90094,
            title="One-of-a-Kind",
            force=2,
            chi=2,
            personal_honor=0,
            gold_cost=4,
            honor_requirement=None,
            clan=[CrabClan],
            keywords=[Unique],
            legality=[TwentyFestivalsEdition],
        )

        in_play = unique_card(game=mock_game, owner=mock_player)
        in_play.location = PlayArea
        in_play.face_down = False

        in_province = unique_card(game=mock_game, owner=mock_player)
        in_province.location = ProvinceLocation
        in_province.face_down = False

        mock_game.entities = [in_play, in_province]

        action = RecruitAction()
        targets = list(action.gather_legal_target_entities(mock_game, mock_player))

        assert in_province not in targets

    def test_gather_allows_unique_not_yet_in_play(self, mock_game, mock_player):
        from l5r_auto.keywords import Unique

        unique_card = Personality(
            card_id=90095,
            title="Potential Unique",
            force=2,
            chi=2,
            personal_honor=0,
            gold_cost=4,
            honor_requirement=None,
            clan=[CrabClan],
            keywords=[Unique],
            legality=[TwentyFestivalsEdition],
        )

        in_province = unique_card(game=mock_game, owner=mock_player)
        in_province.location = ProvinceLocation
        in_province.face_down = False

        # No matching title in play
        mock_game.entities = [in_province]

        action = RecruitAction()
        targets = list(action.gather_legal_target_entities(mock_game, mock_player))

        assert in_province in targets


class TestPlayStrategyAbility:
    def test_strategy_gathered_when_affordable(
        self, mock_game, mock_player, strategy_entity
    ):
        from l5r_auto.abilities import PlayStrategyAbility

        # strategy_entity has gold_cost=0, always affordable
        mock_player.entities = []  # no gold needed

        ability = PlayStrategyAbility()
        targets = list(ability.gather_legal_target_entities(mock_game, mock_player))

        assert strategy_entity in targets

    def test_strategy_not_gathered_when_too_expensive(self, mock_game, mock_player):
        from l5r_auto.abilities import PlayStrategyAbility

        expensive = _EXPENSIVE_STRAT(game=mock_game, owner=mock_player)
        expensive.location = __import__("l5r_auto.locations", fromlist=["Hand"]).Hand
        expensive.face_down = False
        mock_player.hand = [expensive]
        mock_player.entities = []  # no gold producers

        ability = PlayStrategyAbility()
        targets = list(ability.gather_legal_target_entities(mock_game, mock_player))

        assert expensive not in targets
