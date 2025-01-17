import db
import json


class Gameboard():
    def __init__(self):
        self.player1 = ""
        self.player2 = ""
        self.board = [[0 for x in range(7)] for y in range(6)]
        self.game_result = ""
        self.current_turn = 'p1'
        self.remaining_moves = 42
        self.player1col = None

    def update_player1col(self, col):
        self.player1col = col

    def get_player1col(self):
        return self.player1col

    def newGame(self):
        self.player1 = ""
        self.player2 = ""
        self.board = [[0 for x in range(7)] for y in range(6)]
        self.game_result = ""
        self.current_turn = 'p1'
        self.remaining_moves = 42
        self.player1col = None
        db.clear()

    def updateDB(self):
        move = (
            self.current_turn,
            json.dumps(self.board),
            self.game_result,
            self.player1,
            self.player2,
            self.remaining_moves
        )
        db.add_move(move)

    def retrieveSave(self):
        save = db.getMove()
        if save is not None:
            self.current_turn = save[0]
            self.board = json.loads(save[1])
            self.game_result = save[2]
            self.player1 = save[3]
            self.player2 = save[4]
            self.remaining_moves = save[5]
        else:
            return "FAIL"

    def move(self, player, col):
        if self.game_result != "":
            return "Game Result Already Declared"
        elif self.board[0][col] != 0:
            return "Cannot Insert into a Filled Column"
        elif self.current_turn == "p1":
            return "Please Pick a Color First"
        elif self.current_turn != player:
            return "Please Wait for Opponent to Make Move"
        else:
            row = next(
                row for row in range(5, -1, -1) if self.board[row][col] == 0
            )
            self.board[row][col] = player
            self.checkWin(player)
            self.switchCurrentPlayer()
            self.remaining_moves -= 1
            if self.remaining_moves <= 0:
                self.game_result = "DRAW"
            self.updateDB()
            return None

    def switchCurrentPlayer(self):
        if self.current_turn == self.player1:
            self.current_turn = self.player2
            return
        self.current_turn = self.player1

    def checkWin(self, player):
        # horizontal
        for row in self.board:
            counter = 0
            for cell in row:
                if cell == player:
                    counter += 1
                else:
                    counter = 0
                if counter >= 4:
                    self.game_result = player
                    return
        # vertical
        for col in range(7):
            counter = 0
            for row in self.board:
                if row[col] == player:
                    counter += 1
                else:
                    counter = 0
                if counter >= 4:
                    self.game_result = player
                    return
        # diagonal
        # starting top left - bot right
        TL_BR = [(2, 0), (1, 0), (0, 0), (0, 1), (0, 2), (0, 3)]
        # starting top right - bot left
        TR_BL = [(2, 6), (1, 6), (0, 6), (0, 5), (0, 4), (0, 3)]
        for (row, col) in TL_BR:
            counter = 0
            while row < 6 and col < 7:
                # print(f"{row}, {col}")
                if self.board[row][col] == player:
                    counter += 1
                else:
                    counter = 0
                if counter >= 4:
                    self.game_result = player
                    return
                row += 1
                col += 1
        for (row, col) in TR_BL:
            counter = 0
            while row < 6 and col >= 0:
                if self.board[row][col] == player:
                    counter += 1
                else:
                    counter = 0
                if counter >= 4:
                    self.game_result = player
                    return
                row += 1
                col -= 1
        return
