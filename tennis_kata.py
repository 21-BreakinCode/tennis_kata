class Player:
    def __init__(self, name) -> None:
        self.name = name
        self.score = 0

    def add_score(self):
        self.score += 1
        print(f'{self.name} score: {self.score}')


class TennisGame:
    def __init__(self, player1: Player, player2: Player) -> None:
        self.player1 = player1.name
        self.player2 = player2.name
        self.player1_score = player1.score
        self.player2_score = player2.score

    def get_result(self):
        lookUpMap = {
            0: 'love',
            1: 'fifteen',
            2: 'thirty',
            3: 'forty'
        }

        if self._is_deuce():
            return "Deuce"

        if self.player1_score != self.player2_score:
            if self.player1_score >= 3 and self.player2_score >= 3:
                # After deuce
                diff = self.player1_score - self.player2_score
                if diff == 1:
                    return f'{self.player1} Adv'
                elif diff == -1:
                    return f'{self.player2} Adv'
                elif diff == 2:
                    return f'{self.player1} Win'
                elif diff == -2:
                    return f'{self.player2} Win'

            # Before deuce
            if self.player1_score == 4:
                return f'{self.player1} Win'
            elif self.player2_score == 4:
                return f'{self.player2} Win'
            return f'{lookUpMap[self.player1_score]} {lookUpMap[self.player2_score]}'

        return f'{lookUpMap[self.player1_score]} all'

    def _is_deuce(self):
        if self.player1_score == self.player2_score and self.player1_score >= 3:
            return True
        return False
