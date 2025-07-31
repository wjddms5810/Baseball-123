import pytest
from game import Game

@pytest.fixture
def game():
    return Game()

def test_exception_when_input_is_none(game):
    with pytest.raises(TypeError):
        game.guess(None)


def test_exception_when_input_length_is_unmatched(game):
    with pytest.raises(TypeError):
        game.guess("12")