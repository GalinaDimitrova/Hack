import tic


class Interface():

    empty_board = """
 0 │ 1 │ 2
───┼───┼───
 3 │ 4 │ 5
───┼───┼───
 6 │ 7 │ 8

"""

    def print_board(self):
        print(self.empty_board)

    def replace_symbol_in_board(self, pos, symbol):
        position = str(pos)
        self.empty_board = self.empty_board.replace(position, symbol)
        self.print_board()

    def check_winner(self, board):
        if board.winner() == 'X':
            print('Congratulations! You Won!!!')
        elif board.winner() == 'O':
            print('Be smarter next time!')
            print('Game Over!')
        elif board.winner() is None:
            print("It's a Draw!")
            print("You can do better!")

    def start(self, board):
        self.print_board()

        while not board.is_over():
            player = 'X'
            player_move = int(input("Your Move: "))
            if not player_move in board.available_moves():
                print('You should enter positions between 0 - 8!')
                continue
            board.make_move(player_move, player)
            self.replace_symbol_in_board(player_move, player)

            if board.is_over():
                break
            player = tic.get_enemy(player)
            computer_move = tic.determine(board, player)
            board.make_move(computer_move, player)
            print('Computers turn:')
            self.replace_symbol_in_board(computer_move, player)

        self.check_winner(board)


def main():
    board = tic.TicTacToe()
    inter_board = Interface()
    inter_board.start(board)


if __name__ == '__main__':
    main()
