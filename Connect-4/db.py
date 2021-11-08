import sqlite3
from sqlite3 import Error

'''
Initializes the Table GAME
Do not modify
'''


def init_db():
    # creates Table
    conn = None
    try:
        conn = sqlite3.connect('sqlite_db')
        conn.execute('CREATE TABLE GAME(current_turn TEXT, board TEXT,' +
                     'winner TEXT, player1 TEXT, player2 TEXT' +
                     ', remaining_moves INT)')
        print('Database Online, table created')
    except Error as e:
        print(e)

    finally:
        if conn:
            conn.close()


'''
move is a tuple (current_turn, board, winner, player1, player2,
remaining_moves)
Insert Tuple into table
'''


def add_move(move):  # will take in a tuple
    clear()
    init_db()
    conn = None
    try:
        conn = sqlite3.connect('sqlite_db')
        cur = conn.cursor()

        # cur.execute("DELETE FROM GAME")
        cur.execute("insert into GAME values (?, ?, ?, ?, ?, ?)", move)
        conn.commit()
        print("move added to db")
    except Error as e:
        print(e)

    finally:
        if conn:
            conn.close()


'''
Get the last move played
return (current_turn, board, winner, player1, player2, remaining_moves)
'''


def getMove():
    # will return tuple(current_turn, board, winner, player1, player2,
    # remaining_moves) or None if db fails
    conn = None
    try:
        conn = sqlite3.connect('sqlite_db')
        cur = conn.cursor()

        # cur.execute("DELETE FROM GAME")
        cur.execute("select * from GAME")
        result = cur.fetchall()
        # print(result)
        # print(result[0])
        return result[0]

    except Error as e:
        print(e)
        return None

    finally:
        if conn:
            conn.close()


'''
Clears the Table GAME
Do not modify
'''


def clear():
    conn = None
    try:
        conn = sqlite3.connect('sqlite_db')
        conn.execute("DROP TABLE GAME")
        print('Database Cleared')
    except Error as e:
        print(e)

    finally:
        if conn:
            conn.close()
