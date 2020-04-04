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
    >>> game = TicTacToe(board)
    >>> game.number_of_x()
    >>> game.is_valid
    False

    Players take turns making moves.
    >>> board = ["XOX", " X ", "   "]
    >>> game = TicTacToe(board)
    >>> game.number_of_x()
    >>> game.is_valid
    False

    >>> board = ["XXX", "   ", "OOO"]
    >>> game = TicTacToe(board)
    >>> game.number_of_x()
    >>> game.is_valid
    False

    >>> board = ["XOX", "O O", "XOX"]
    >>> game = TicTacToe(board)
    >>> game.number_of_x()
    >>> game.is_valid
    True
    '''

    def __init__(self, board):
        self.is_valid = True
        self.count_dict = self.get_dict(board)

    def get_dict(self, board):
        turn_count = {}
        for row in board:
            for col in row:
                turn_count[col] = turn_count.get(col, 0) + 1
        return turn_count
        
    def number_of_x(self):
        if not (self.count_dict.get('X', 0) - self.count_dict.get('O', 0) >= 0 and self.count_dict.get('X', 0) - self.count_dict.get('O', 0) <= 1):
            self.is_valid = False

    def win(self):
        pass

if __name__ == '__main__':
    import doctest
    if doctest.testmod(verbose=True).failed == 0:
        print('all tests passed')