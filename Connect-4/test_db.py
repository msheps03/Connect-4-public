import unittest
import db


class Test_Testdb(unittest.TestCase):
    def test_db(self):
        move = (
            'test_current_turn',
            'test_board',
            'test_winner',
            'test_player1',
            'test_player2',
            1
        )
        db.add_move(move)
        gotMove = db.getMove()
        self.assertEqual(gotMove, move)

        move2 = (
            'test2_current_turn',
            'test2_board',
            'test2_winner',
            'test2_player1',
            'test2_player2',
            2
        )
        db.add_move(move2)
        gotMove2 = db.getMove()
        self.assertEqual(gotMove2, move2)
