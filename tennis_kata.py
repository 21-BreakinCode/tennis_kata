class Player:
    def __init__(self, name) -> None:
        self.name = name
        self.score = 0

    def add_score(self):
        self.score += 1


class TennisGame:
    def __init__(self, player1: Player, player2: Player) -> None:
        self.player1 = player1
        self.player2 = player2
        self.lookUpMap = {
            0: 'love',
            1: 'fifteen',
            2: 'thirty',
            3: 'forty'
        }

    def get_result(self):
        if self._is_deuce():
            return "Deuce"

        if self.player1.score != self.player2.score:
            if self.player1.score >= 3 and self.player2.score >= 3:
                return self._get_result_after_deuce()

            return self._get_result_before_deuce()
        return f'{self.lookUpMap[self.player1.score]} all'

    def _is_deuce(self):
        if self.player1.score == self.player2.score and self.player1.score >= 3:
            return True
        return False

    def _get_result_after_deuce(self):
        diffMap = {
            1: 'Adv',
            2: 'Win'
        }
        diff = self.player1.score - self.player2.score
        if diff > 0:
            return f'{self.player1.name} {diffMap[abs(diff)]}'
        return f'{self.player2.name} {diffMap[abs(diff)]}'

    def _get_result_before_deuce(self):
        if self.player1.score == self.player2.score:
            return f'{self.lookUpMap[self.player1.score]} all'

        if self.player1.score == 4:
            return f'{self.player1.name} Win'
        elif self.player2.score == 4:
            return f'{self.player2.name} Win'

        return f'{self.lookUpMap[self.player1.score]} {self.lookUpMap[self.player2.score]}'
