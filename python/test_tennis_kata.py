import unittest

from tennis_kata import TennisGame

class TestTennisGame(unittest.TestCase):
    def setUp(self):
        player_one = 'Joe'
        player_two = 'Bob'
        self.game = TennisGame(player_one, player_two)

    def add_player_one_score(self, count):
        for _ in range(count):
            self.game.player_one_scored()

    def add_player_two_score(self, count):
        for _ in range(count):
            self.game.player_two_scored()

    def test_score_0_0(self):
        expected_result = 'love all'

        result = self.game.get_score()

        self.assertEqual(expected_result, result)

    def test_score_1_0(self):
        expected_result = 'fifteen love'

        self.add_player_one_score(1)
        result = self.game.get_score()

        self.assertEqual(expected_result, result)

    def test_score_2_0(self):
        expected_result = 'thirty love'

        self.add_player_one_score(2)
        result = self.game.get_score()

        self.assertEqual(expected_result, result)

    def test_score_3_0(self):
        expected_result = 'forty love'

        self.add_player_one_score(3)
        result = self.game.get_score()

        self.assertEqual(expected_result, result)

    def test_score_0_1(self):
        expected_result = 'love fifteen'

        self.add_player_two_score(1)
        result = self.game.get_score()

        self.assertEqual(expected_result, result)

    def test_score_0_2(self):
        expected_result = 'love thirty'

        self.add_player_two_score(2)
        result = self.game.get_score()

        self.assertEqual(expected_result, result)

    def test_score_0_3(self):
        expected_result = 'love forty'

        self.add_player_two_score(3)
        result = self.game.get_score()

        self.assertEqual(expected_result, result)

    def test_score_is_deuce(self):
        excepted_result = 'deuce'

        self.add_player_one_score(3)
        self.add_player_two_score(3)
        result = self.game.get_score()

        self.assertEqual(excepted_result, result)

    def test_score_player_one_adv(self):
        excepted_result = 'Joe adv'

        self.add_player_one_score(3)
        self.add_player_two_score(3)

        self.add_player_one_score(1)
        result = self.game.get_score()

        self.assertEqual(excepted_result, result)

    def test_score_player_two_adv(self):
        excepted_result = 'Bob adv'

        self.add_player_one_score(3)
        self.add_player_two_score(3)

        self.add_player_two_score(1)
        result = self.game.get_score()

        self.assertEqual(excepted_result, result)

    def test_score_player_one_win_before_deuce(self):
        excepted_result = 'Joe win'

        self.add_player_one_score(4)

        result = self.game.get_score()

        self.assertEqual(excepted_result, result)

    def test_score_player_two_win_before_deuce(self):
        excepted_result = 'Bob win'

        self.add_player_two_score(4)
        result = self.game.get_score()

        self.assertEqual(excepted_result, result)

    def test_score_player_one_win_after_deuce(self):
        excepted_result = 'Joe win'

        self.add_player_one_score(3)
        self.add_player_two_score(3)

        self.add_player_one_score(2)

        result = self.game.get_score()

        self.assertEqual(excepted_result, result)

    def test_score_player_two_win_after_deuce(self):
        excepted_result = 'Bob win'

        self.add_player_one_score(3)
        self.add_player_two_score(3)

        self.add_player_two_score(2)

        result = self.game.get_score()

        self.assertEqual(excepted_result, result)
