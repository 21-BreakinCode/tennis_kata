# 14:05  --> 14:45
import unittest

from tennis_kata import TennisGame


class TestTennisGame(unittest.TestCase):
    def setUp(self):
        player_one = 'Joe'
        player_two = 'Bob'
        self.game = TennisGame(player_one, player_two)

    def test_score_0_0(self):
        expected_result = 'love all'

        result = self.game.get_score()

        self.assertEqual(result, expected_result)

    def test_score_1_0(self):
        expected_result = 'fifteen love'

        self.game.player_one_scored()
        result = self.game.get_score()

        self.assertEqual(result, expected_result)

    def test_score_2_0(self):
        expected_result = 'thirty love'

        self.game.player_one_scored()
        self.game.player_one_scored()
        result = self.game.get_score()

        self.assertEqual(result, expected_result)

    def test_score_3_0(self):
        expected_result = 'forty love'

        self.game.player_one_scored()
        self.game.player_one_scored()
        self.game.player_one_scored()
        result = self.game.get_score()

        self.assertEqual(result, expected_result)

    def test_score_0_1(self):
        expected_result = 'love fifteen'

        self.game.player_two_scored()
        result = self.game.get_score()

        self.assertEqual(result, expected_result)

    def test_score_0_2(self):
        expected_result = 'love thirty'

        self.game.player_two_scored()
        self.game.player_two_scored()
        result = self.game.get_score()

        self.assertEqual(result, expected_result)

    def test_score_0_3(self):
        expected_result = 'love forty'

        self.game.player_two_scored()
        self.game.player_two_scored()
        self.game.player_two_scored()
        result = self.game.get_score()

        self.assertEqual(result, expected_result)

    def test_score_1_1(self):
        expected_result = 'fifteen all'

        self.game.player_one_scored()
        self.game.player_two_scored()
        result = self.game.get_score()

        self.assertEqual(result, expected_result)

    def test_score_2_2(self):
        expected_result = 'thirty all'

        self.game.player_one_scored()
        self.game.player_two_scored()
        self.game.player_one_scored()
        self.game.player_two_scored()
        result = self.game.get_score()

        self.assertEqual(result, expected_result)

    def test_score_is_deuce(self):
        expected_result = 'deuce'

        self.game.player_one_scored()
        self.game.player_two_scored()
        self.game.player_one_scored()
        self.game.player_two_scored()
        self.game.player_one_scored()
        self.game.player_two_scored()
        result = self.game.get_score()

        self.assertEqual(result, expected_result)

    def test_score_player_one_advantage(self):
        expected_result = 'Joe advantage'

        self.game.player_one_scored()
        self.game.player_two_scored()
        self.game.player_one_scored()
        self.game.player_two_scored()
        self.game.player_one_scored()
        self.game.player_two_scored()
        self.game.player_one_scored()
        result = self.game.get_score()

        self.assertEqual(result, expected_result)

    def test_score_player_two_advantage(self):
        expected_result = 'Bob advantage'

        self.game.player_one_scored()
        self.game.player_two_scored()
        self.game.player_one_scored()
        self.game.player_two_scored()
        self.game.player_one_scored()
        self.game.player_two_scored()
        self.game.player_two_scored()
        result = self.game.get_score()

        self.assertEqual(result, expected_result)

    def test_score_player_one_win_before_deuce(self):
        expected_result = 'Joe wins'

        self.game.player_one_scored()
        self.game.player_one_scored()
        self.game.player_one_scored()
        self.game.player_one_scored()
        result = self.game.get_score()

        self.assertEqual(result, expected_result)

    def test_score_player_two_win_before_deuce(self):
        expected_result = 'Bob wins'

        self.game.player_two_scored()
        self.game.player_two_scored()
        self.game.player_two_scored()
        self.game.player_two_scored()
        result = self.game.get_score()

        self.assertEqual(result, expected_result)

    def test_score_player_one_win_after_deuce(self):
        expected_result = 'Joe wins'

        self.game.player_one_scored()
        self.game.player_two_scored()
        self.game.player_one_scored()
        self.game.player_two_scored()
        self.game.player_one_scored()
        self.game.player_two_scored()
        self.game.player_one_scored()
        self.game.player_two_scored()
        self.game.player_one_scored()
        self.game.player_one_scored()
        result = self.game.get_score()

        self.assertEqual(result, expected_result)

    def test_score_player_two_win_after_deuce(self):
        expected_result = 'Bob wins'

        self.game.player_one_scored()
        self.game.player_two_scored()

        self.game.player_one_scored()
        self.game.player_two_scored()

        self.game.player_one_scored()
        self.game.player_two_scored()

        self.game.player_one_scored()
        self.game.player_two_scored()

        self.game.player_one_scored()
        self.game.player_two_scored()

        self.game.player_two_scored()
        self.game.player_two_scored()
        result = self.game.get_score()

        self.assertEqual(result, expected_result)
