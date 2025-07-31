from game_result import GameResult

class Game:
    def __init__(self):
        self._question = ''

    def guess(self, guess_number) -> GameResult:
        self._assert_illegal_value(guess_number)
        return GameResult(True, 3, 0)

    def _is_duplicate_method(self, guess_number):
        return len(set(guess_number)) != 3

    def _assert_illegal_value(self, guess_number):
        if guess_number is None:
            raise TypeError("입력이 None 입니다.")
        if len(guess_number) != 3:
            raise TypeError("입력은 세자리 문자열이어야 합니다.")
        if not guess_number.isdigit():
            raise TypeError("모든 문자는 숫자로 구성되어야 합니다.")
        if self._is_duplicate_method(guess_number):
            raise TypeError("중복된 숫자가 존재합니다.")
