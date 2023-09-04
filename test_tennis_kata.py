import unittest

from tennis_kata import TennisGame, Player

class TestTennisGame(unittest.TestCase):
    def setUp(self):
        self.Joe = Player('Joe')
        self.Ken = Player('Ken')
        self.game = TennisGame(self.Joe, self.Ken)

    def addScore(self, player, count):
        for _ in range(count):
            self.game._addScore(player)

    def test_love_all(self):
        expected_output = 'love all'

        result = self.game.get_result()

        self.assertEqual(result, expected_output)

    def test_player1_fifteen(self):
        expected_output = 'fifteen love'

        self.Joe.add_score()
        result = self.game.get_result()

        self.assertEqual(self.Joe.score, 1)
        self.assertEqual(result, expected_output)

    def test_player2_fifteen(self):
        expected_output = 'love fifteen'

        self.Ken.add_score()
        result = self.game.get_result()

        self.assertEqual(result, expected_output)

    def test_two_players_fifteen_all(self):
        expected_output = 'fifteen all'

        self.Joe.add_score()
        self.Ken.add_score()
        result = self.game.get_result()

        self.assertEqual(result, expected_output)

    def test_player1_thirty(self):
        expected_output = 'thirty love'

        self.Joe.add_score()
        self.Joe.add_score()
        result = self.game.get_result()

        self.assertEqual(result, expected_output)

    def test_player2_thirty(self):
        expected_output = 'love thirty'

        self.Ken.add_score()
        self.Ken.add_score()
        result = self.game.get_result()

        self.assertEqual(result, expected_output)

    def test_player1_forty(self):
        expected_output = 'forty love'

        self.Joe.add_score()
        self.Joe.add_score()
        self.Joe.add_score()
        result = self.game.get_result()

        self.assertEqual(result, expected_output)

    def test_player2_forty(self):
        expected_output = 'love forty'

        self.Ken.add_score()
        self.Ken.add_score()
        self.Ken.add_score()
        result = self.game.get_result()

        self.assertEqual(result, expected_output)

    def test_two_players_is_deuce(self):
        expected_output = 'Deuce'

        self.Ken.add_score()
        self.Ken.add_score()
        self.Ken.add_score()

        self.Joe.add_score()
        self.Joe.add_score()
        self.Joe.add_score()

        result = self.game.get_result()

        self.assertEqual(result, expected_output)

    def test_player1_adv(self):
        expected_output = 'Joe Adv'

        self.Ken.add_score()
        self.Ken.add_score()
        self.Ken.add_score()

        self.Joe.add_score()
        self.Joe.add_score()
        self.Joe.add_score()
        self.Joe.add_score()
        result = self.game.get_result()

        self.assertEqual(result, expected_output)

    def test_player2_adv(self):
        expected_output = 'Ken Adv'

        self.Ken.add_score()
        self.Ken.add_score()
        self.Ken.add_score()
        self.Ken.add_score()

        self.Joe.add_score()
        self.Joe.add_score()
        self.Joe.add_score()
        result = self.game.get_result()

        self.assertEqual(result, expected_output)

    def test_player_win__before_deuce(self):
        expected_output = 'Joe Win'

        self.Ken.add_score()
        self.Ken.add_score()

        self.Joe.add_score()
        self.Joe.add_score()
        self.Joe.add_score()
        self.Joe.add_score()
        result = self.game.get_result()

        self.assertEqual(result, expected_output)

    def test_player_win_after_deuce(self):
        expected_output = 'Ken Win'

        self.Ken.add_score()
        self.Ken.add_score()
        self.Ken.add_score()

        self.Joe.add_score()
        self.Joe.add_score()
        self.Joe.add_score()

        self.Ken.add_score()
        self.Joe.add_score()

        self.Ken.add_score()
        self.Joe.add_score()

        self.Ken.add_score()
        self.Ken.add_score()

        result = self.game.get_result()

        self.assertEqual(result, expected_output)
