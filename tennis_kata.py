class TennisGame:
    def __init__(self, player_one, player_two) -> None:
        self.player_one = player_one
        self.player_two = player_two
        self.player_one_score = 0
        self.player_two_score = 0

    def get_score(self):
        score_map = {
            0: 'love',
            1: 'fifteen',
            2: 'thirty',
            3: 'forty'
        }

        if self._is_deuce():
            return 'deuce'

        if self.player_one_score == self.player_two_score:
            return f'{score_map[self.player_one_score]} all'

        if self._after_deuce():
            return self._after_deuce_result()

        if self.player_one_score == 4:
            return f'{self.player_one} win'
        if self.player_two_score == 4:
            return f'{self.player_two} win'

        return f'{score_map[self.player_one_score]} {score_map[self.player_two_score]}'

    def player_one_scored(self):
        self.player_one_score += 1

    def player_two_scored(self):
        self.player_two_score += 1

    def _is_deuce(self):
        if self.player_one_score >= 3 and self.player_two_score >= 3:
            if self.player_one_score == self.player_two_score:
                return True
        return False

    def _after_deuce(self):
        if self.player_one_score >= 3 and self.player_two_score >= 3:
            return True
        return False

    def _after_deuce_result(self):
        diff = self.player_one_score - self.player_two_score
        if diff == 1:
            return f'{self.player_one} adv'
        if diff == -1:
            return f'{self.player_two} adv'
        if diff == 2:
            return f'{self.player_one} win'
        if diff == -2:
            return f'{self.player_two} win'
        return 'deuce'
