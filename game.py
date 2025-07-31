from game_result import GameResult


class Game:
    def __init__(self):
        self._question = ''

    @property
    def question(self):
        raise AttributeError("읽을 수 없는 속성")

    @question.setter
    def question(self, value):
        self._question = value

    def _count_strike_and_ball(self, quess_number):
        strike_cnt = 0
        ball_cnt = 0
        for i in range(0, 3):
            if quess_number[i] == self._question[i]:
                strike_cnt += 1
            elif quess_number[i] in self._question[i]:
                ball_cnt += 1
        return strike_cnt, ball_cnt

    def guess(self, guess_number) -> GameResult | None:
        self._assert_illegal_value(guess_number)
        if guess_number == self._question:
            return GameResult(True, 3, 0)
        strike_cnt, ball_cnt = self._count_strike_and_ball(guess_number)
        return GameResult(False, strike_cnt, ball_cnt)

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
