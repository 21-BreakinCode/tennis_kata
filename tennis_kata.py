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

    def get_result(self):
        lookUpMap = {
            0: 'love',
            1: 'fifteen',
            2: 'thirty',
            3: 'forty'
        }

        if self._is_deuce():
            return "Deuce"

        # if self.player1.score != self.player2.score:
        if self.player1.score != self.player2.score:
            if self.player1.score >= 3 and self.player2.score >= 3:
                # After deuce
                diff = self.player1.score - self.player2.score
                if diff == 1:
                    return f'{self.player1.name} Adv'
                elif diff == -1:
                    return f'{self.player2.name} Adv'
                elif diff == 2:
                    return f'{self.player1.name} Win'
                elif diff == -2:
                    return f'{self.player2.name} Win'

            # Before deuce
            if self.player1.score == 4:
                return f'{self.player1.name} Win'
            elif self.player2.score == 4:
                return f'{self.player2.name} Win'
            return f'{lookUpMap[self.player1.score]} {lookUpMap[self.player2.score]}'

        return f'{lookUpMap[self.player1.score]} all'

    def _is_deuce(self):
        if self.player1.score == self.player2.score and self.player1.score >= 3:
            return True
        return False
