import random

class TicTacToe:
    def __init__(self):
        # Initialize a 3x3 board with empty spaces
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        # Player X always starts first
        self.player = 'X'

    def print_board(self):
        # Print the current state of the board
        for row in self.board:
            print('|'.join(row))
            print('-' * 5)
        print('\n')

    def make_move(self, row: int, col: int) -> bool:
        """
        Place the current player's mark on the board at the given row and column.
        :param row: The row index for the move (0-2)
        :param col: The column index for the move (0-2)
        :return: True if the move is valid and has been made, False otherwise
        """
        print(f'Player {self.player} making a move')
        if self.board[row][col] == ' ':
            self.board[row][col] = self.player
            return True
        return False

    def check_winner(self) -> str:
        """
        Check the current state of the board to see if there is a winner.
        :return: 'X' if Player X wins, 'O' if Player O wins, or '' if no winner yet
        """
        # Check rows, columns, and diagonals for a winner
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != ' ':
                return self.board[i][0]
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != ' ':
                return self.board[0][i]

        if self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ':
            return self.board[0][0]
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != ' ':
            return self.board[0][2]

        return ''

    def is_draw(self) -> bool:
        """
        Check if the game is a draw (i.e., the board is full and there's no winner).
        :return: True if the game is a draw, False otherwise
        """
        for row in self.board:
            if ' ' in row:
                return False
        return True

    def switch_player(self):
        # Switch turns between Player X and Player O
        self.player = 'O' if self.player == 'X' else 'X'

    def play(self):
        """
        Main game loop. Automatically alternates between players, makes moves, checks for a winner,
        and prints the game result.
        """
        while True:
            self.print_board()
            # Get the move for the current player (for example purposes, we'll just make moves manually)
            row, col = self.get_random_empty_spot()

            if self.make_move(row, col):
                winner = self.check_winner()
                if winner or self.is_draw():
                    self.print_board()
                    if winner:
                        print(f"PLAYER {winner} WINS")
                    else:
                        print("DRAW")
                    break
                else:
                    self.switch_player()
            else:
                print("Invalid move. Try again.")

    def get_random_empty_spot(self) -> tuple:
        """
        Generates a move by selecting a random empty spot on the board.
        :return: A tuple (row, col) for the selected move.
        """
        empty_spots = [(r, c) for r in range(3) for c in range(3) if self.board[r][c] == ' ']
        return random.choice(empty_spots)

# Initialize and play the game
game = TicTacToe()
game.play()
