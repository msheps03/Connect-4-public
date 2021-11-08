import unittest
from Gameboard import Gameboard


class Test_TestGameboard(unittest.TestCase):
    # test correct moves
    def test_moveCorrect(self):
        game = Gameboard()
        game.player1 = 'red'
        game.player2 = 'yellow'
        game.current_turn = game.player1

        # red moves on col 0
        game.move(game.player1, 0)
        self.assertEqual(game.board[5][0], game.player1)

        # yellow moves on col 6
        game.move(game.player2, 6)
        self.assertEqual(game.board[5][6], game.player2)

        # red moves on col 6
        game.move(game.player1, 6)
        self.assertEqual(game.board[4][6], game.player1)

    def test_retrieveSave(self):
        game = Gameboard()
        game.player1 = 'red'
        game.player2 = 'yellow'
        game.current_turn = game.player1

        # red moves on col 0
        game.move(game.player1, 0)
        # yellow moves on col 6
        game.move(game.player2, 6)
        # red moves on col 6
        game.move(game.player1, 6)

        game2 = Gameboard()
        self.assertEqual(game2.board[5][0], 0)
        game2.retrieveSave()
        self.assertEqual(game2.board[5][0], game.player1)

    def test_newGame(self):
        game = Gameboard()
        game.player1 = 'red'
        game.player2 = 'yellow'
        game.current_turn = game.player1

        # red moves on col 0
        game.move(game.player1, 0)
        # yellow moves on col 6
        game.move(game.player2, 6)
        # red moves on col 6
        game.move(game.player1, 6)

        game.newGame()
        self.assertEqual(game.board[5][0], 0)
        self.assertEqual(game.retrieveSave(), 'FAIL')
        self.assertEqual(game.board[5][0], 0)

    # test horizontal win
    def test_WinHorizontal(self):
        game = Gameboard()
        game.player1 = 'red'
        game.player2 = 'yellow'
        game.current_turn = game.player1

        game.move(game.player1, 0)
        game.move(game.player2, 0)
        game.move(game.player1, 1)
        game.move(game.player2, 1)
        game.move(game.player1, 2)
        game.move(game.player2, 2)
        self.assertEqual(game.game_result, "")
        game.move(game.player1, 3)
        self.assertEqual(game.game_result, game.player1)

    # test vertical win
    def test_WinVertical(self):
        game = Gameboard()
        game.player1 = 'red'
        game.player2 = 'yellow'
        game.current_turn = game.player1

        game.move(game.player1, 0)
        game.move(game.player2, 1)
        game.move(game.player1, 0)
        game.move(game.player2, 1)
        game.move(game.player1, 0)
        game.move(game.player2, 1)
        self.assertEqual(game.game_result, "")
        game.move(game.player1, 0)
        self.assertEqual(game.game_result, game.player1)

    # test top left - bot right diagonal win
    def test_WinDiagonal_TLBR(self):
        game = Gameboard()
        game.player1 = 'red'
        game.player2 = 'yellow'
        game.current_turn = game.player1

        game.move(game.player1, 0)
        game.move(game.player2, 0)
        game.move(game.player1, 0)
        game.move(game.player2, 0)
        game.move(game.player1, 0)
        game.move(game.player2, 1)
        game.move(game.player1, 1)
        game.move(game.player2, 1)
        game.move(game.player1, 2)
        game.move(game.player2, 2)
        game.move(game.player1, 2)
        self.assertEqual(game.game_result, "")
        game.move(game.player2, 3)
        self.assertEqual(game.game_result, game.player2)

    # test top right - bot left diagonal win
    def test_WinDiagonal_TRBL(self):
        game = Gameboard()
        game.player1 = 'red'
        game.player2 = 'yellow'
        game.current_turn = game.player1

        game.move(game.player1, 6)
        game.move(game.player2, 6)
        game.move(game.player1, 6)
        game.move(game.player2, 6)
        game.move(game.player1, 5)
        game.move(game.player2, 3)
        game.move(game.player1, 5)
        game.move(game.player2, 5)
        game.move(game.player1, 4)
        self.assertEqual(game.game_result, "")
        game.move(game.player2, 4)
        self.assertEqual(game.game_result, game.player2)

    # test invalid move - not current player's turn
    def test_Invalid_WrongTurn(self):
        game = Gameboard()
        game.player1 = 'red'
        game.player2 = 'yellow'
        game.current_turn = game.player1

        moveFailReason = game.move(game.player1, 0)
        self.assertIsNone(moveFailReason)
        moveFailReason = game.move(game.player1, 4)
        self.assertEqual(moveFailReason, "Not your turn.")

        moveFailReason = game.move(game.player2, 0)
        self.assertIsNone(moveFailReason)
        moveFailReason = game.move(game.player2, 4)
        self.assertEqual(moveFailReason, "Not your turn.")

    # test invalid move - winner already declared
    def test_Invalid_WinnerDeclared(self):
        game = Gameboard()
        game.player1 = 'red'
        game.player2 = 'yellow'
        game.current_turn = game.player1

        game.move(game.player1, 0)
        game.move(game.player2, 1)
        game.move(game.player1, 0)
        game.move(game.player2, 1)
        game.move(game.player1, 0)
        game.move(game.player2, 1)
        game.move(game.player1, 0)
        moveFailReason = game.move(game.player2, 1)
        self.assertEqual(moveFailReason, "Game result already declared.")
        self.assertEqual(game.game_result, game.player1)
        self.assertEqual(game.board[3][1], game.player2)
        self.assertEqual(game.board[2][1], 0)

    # test invalid move - draw (tie)
    def test_Invalid_Draw(self):
        game = Gameboard()
        game.player1 = 'red'
        game.player2 = 'yellow'
        game.current_turn = game.player1

        player1_moves = [
            0, 1, 2, 0, 1, 2, 0, 1, 2,
            5, 3, 4, 3, 4, 3, 4, 6, 5, 6, 5, 6]

        player2_moves = [
            0, 1, 2, 0, 1, 2, 0, 1, 2,
            3, 4, 3, 4, 3, 4, 5, 6, 5, 6, 5, 6]

        for turn in range(21):
            game.move(game.player1, player1_moves[turn])
            game.move(game.player2, player2_moves[turn])

        self.assertEqual(game.game_result, "DRAW")
        self.assertEqual(game.remaining_moves, 0)
        moveFailReason = game.move(game.player1, 0)
        self.assertEqual(moveFailReason, "Game result already declared.")

    # test invalid move - current column is filled
    def test_Invalid_ColumnFilled(self):
        game = Gameboard()
        game.player1 = 'red'
        game.player2 = 'yellow'
        game.current_turn = game.player1

        player1_moves = [
            5, 5, 5]

        player2_moves = [
            5, 5, 5]

        for turn in range(3):
            game.move(game.player1, player1_moves[turn])
            game.move(game.player2, player2_moves[turn])

        moveFailReason = game.move(game.player1, 5)
        self.assertEqual(moveFailReason, "Cannot insert into a filled column.")
