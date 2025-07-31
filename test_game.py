import pytest

from game import Game
from game_result import GameResult


@pytest.fixture
def game():
    return Game()


def assert_illegal_argument(game, guess_number):
    with pytest.raises(TypeError):
        game.guess(guess_number)


@pytest.mark.parametrize('invalide_input', [None, "12", "1234", "12s", "121"])
def test_exception_when_invalid_input(game, invalide_input):
    assert_illegal_argument(game, None)
    assert_illegal_argument(game, "12")
    assert_illegal_argument(game, "1234")
    assert_illegal_argument(game, "12s")
    assert_illegal_argument(game, "121")


def assert_matched_number(result, solved, strikers, balls):
    assert result is not None
    assert result.solved == solved
    assert result.strikes == strikers
    assert result.balls == balls


def test_return_solved_result_if_matched_number(game):
    game.question = '123'
    assert_matched_number(game.guess('123'), True, 3, 0)


def test_return_solved_result_if_unmatched_number(game):
    game.question = '123'
    assert_matched_number(game.guess('456'), False, 0, 0)
