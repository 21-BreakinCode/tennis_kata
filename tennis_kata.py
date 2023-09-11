class TennisGame:
    def __init__(self, player_one, player_two):
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

        if self._is_over_deuce():
            diff = self.player_one_score - self.player_two_score
            if abs(diff) == 1:
                return self._is_adv()
            if diff == 2:
                return f'{self.player_one} wins'
            return f'{self.player_two} wins'

        if self.player_one_score != self.player_two_score:
            if self.player_one_score == 4:
                return f'{self.player_one} wins'
            if self.player_two_score == 4:
                return f'{self.player_two} wins'

            return f'{score_map[self.player_one_score]} {score_map[self.player_two_score]}'

        return f'{score_map[self.player_one_score]} all'

    def player_one_scored(self):
        self.player_one_score += 1

    def player_two_scored(self):
        self.player_two_score += 1

    def _is_over_deuce(self):
        if self.player_one_score >= 3 and self.player_two_score >= 3:
            return True

    def _is_deuce(self):
        if self._is_over_deuce():
            if self.player_one_score == self.player_two_score:
                return True
        return False

    def _is_adv(self):
        if self.player_one_score > self.player_two_score:
            return f'{self.player_one} advantage'
        return f'{self.player_two} advantage'