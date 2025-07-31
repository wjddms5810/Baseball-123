class Game:
    def guess(self, param):
        if param is None or len(param) != 3:
            raise TypeError()
