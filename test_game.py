import pytest

from game import Game


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
