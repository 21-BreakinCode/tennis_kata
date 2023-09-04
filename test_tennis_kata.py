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

        self.assertEqual(result, expected_output)

    def test_player2_fifteen(self):
        expected_output = 'love fifteen'

        self.addScore('Ken', 1)
        result = self.game.get_result()

        self.assertEqual(result, expected_output)

    def test_two_players_fifteen_all(self):
        expected_output = 'fifteen all'

        self.addScore('Joe', 1)
        self.addScore('Ken', 1)
        result = self.game.get_result()

        self.assertEqual(result, expected_output)

    def test_player1_thirty(self):
        expected_output = 'thirty love'

        self.addScore('Joe', 2)
        result = self.game.get_result()

        self.assertEqual(result, expected_output)

    def test_player2_thirty(self):
        expected_output = 'love thirty'

        self.addScore('Ken', 2)
        result = self.game.get_result()

        self.assertEqual(result, expected_output)

    def test_player1_forty(self):
        expected_output = 'forty love'

        self.addScore('Joe', 3)
        result = self.game.get_result()

        self.assertEqual(result, expected_output)

    def test_player2_forty(self):
        expected_output = 'love forty'

        self.addScore('Ken', 3)
        result = self.game.get_result()

        self.assertEqual(result, expected_output)

    def test_two_players_is_deuce(self):
        expected_output = 'Deuce'

        self.addScore('Joe', 3)
        self.addScore('Ken', 3)
        result = self.game.get_result()

        self.assertEqual(result, expected_output)

    def test_player1_adv(self):
        expected_output = 'Joe Adv'

        self.addScore('Joe', 4)
        self.addScore('Ken', 3)
        result = self.game.get_result()

        self.assertEqual(result, expected_output)

    def test_player2_adv(self):
        expected_output = 'Ken Adv'

        self.addScore('Joe', 3)
        self.addScore('Ken', 4)
        result = self.game.get_result()

        self.assertEqual(result, expected_output)

    def test_player_win__before_deuce(self):
        expected_output = 'Joe Win'

        self.addScore('Joe', 4)
        self.addScore('Ken', 2)
        result = self.game.get_result()

        self.assertEqual(result, expected_output)

    def test_player_win_after_deuce(self):
        expected_output = 'Ken Win'

        self.addScore('Joe', 5)
        self.addScore('Ken', 7)
        result = self.game.get_result()

        self.assertEqual(result, expected_output)
