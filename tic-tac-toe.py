class TicTacToe:
    '''
    A Tic-Tac-Toe board is given as a string array board. 
    Return True if and only if it is possible to reach this board position during the course of a valid tic-tac-toe game.

    The board is a 3 x 3 array, and consists of characters " ", "X", and "O".  
    The " " character represents an empty square.

    Here are the rules of Tic-Tac-Toe:

    Players take turns placing characters into empty squares (" ").
    The first player always places "X" characters, while the second player always places "O" characters.
    "X" and "O" characters are always placed into empty squares, never filled ones.
    The game ends when there are 3 of the same (non-empty) character filling any row, column, or diagonal.
    The game also ends if all squares are non-empty.
    No more moves can be played if the game is over.

    The first player always plays "X".

    >>> board = ["O  ", "   ", "   "]
    >>> game = TicTacToe()
    >>> game.validTicTacToe(board)
    False

    Players take turns making moves.
    >>> board = ["XOX", " X ", "   "]
    >>> game.validTicTacToe(board)
    False

    >>> board = ["XXX", "   ", "OOO"]
    >>> game.validTicTacToe(board)
    False

    >>> board = ["XOX", "O O", "XOX"]
    >>> game.validTicTacToe(board)
    True

    >>> board = ["XXX","OOX","OOX"]
    >>> game.validTicTacToe(board)
    True

    >>> board = ["XXX","XOO","OO "]
    >>> game.validTicTacToe(board)
    False

    >>> board = ["OXX","XOX","OXO"]
    >>> game.validTicTacToe(board)
    False
    '''

    def count_dict(self, board):
        mark_dict = {}
        for row in board:
            for col in row:
                if col == 'X' or col == 'O':
                    mark_dict[col] = mark_dict.get(col, 0) + 1
        return mark_dict

    def winner_dict(self, board):
        winners_dict = {}
        if board[0][0] == board[0][1] == board[0][2] != ' ':
            winners_dict[board[0][0]] = winners_dict.get(board[0][0], 0) + 1
        if board[1][0] == board[1][1] == board[1][2] != ' ':
            winners_dict[board[1][0]] = winners_dict.get(board[1][0], 0) + 1
        if board[2][0] == board[2][1] == board[2][2] != ' ':
            winners_dict[board[2][0]] = winners_dict.get(board[2][0], 0) + 1

        if board[0][0] == board[1][1] == board[2][2] != ' ':
            winners_dict[board[0][0]] = winners_dict.get(board[0][0], 0) + 1
        if board[0][2] == board[1][1] == board[2][0] != ' ':
            winners_dict[board[0][2]] = winners_dict.get(board[0][2], 0) + 1

        if board[0][0] == board[1][0] == board[2][0] != ' ':
            winners_dict[board[0][0]] = winners_dict.get(board[0][0], 0) + 1
        if board[0][1] == board[1][1] == board[2][1] != ' ':
            winners_dict[board[0][1]] = winners_dict.get(board[0][1], 0) + 1
        if board[0][2] == board[1][2] == board[2][2] != ' ':
            winners_dict[board[0][2]] = winners_dict.get(board[0][2], 0) + 1

        return winners_dict

    def validTicTacToe(self, board):
        winners_dict = self.winner_dict(board)
        count_dict = self.count_dict(board)

        if len(winners_dict) > 1:
            return False
        elif 'O' in winners_dict and count_dict['O'] != count_dict.get('X', 0):
            return False
        elif not (count_dict.get('X', 0) - count_dict.get('O', 0) >= 0 and count_dict.get('X', 0) - count_dict.get('O', 0) <= 1):
            return False
        elif 'X' in winners_dict and 'X' in count_dict and count_dict['X'] - count_dict.get('O', 0) != 1:
            return False
        else:
            return True
        

if __name__ == '__main__':
    import doctest
    if doctest.testmod(verbose=True).failed == 0:
        print('all tests passed')