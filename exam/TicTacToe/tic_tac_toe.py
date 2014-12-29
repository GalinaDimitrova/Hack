import random


class TicTacToe:
    winning_lines = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],

        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],

        [0, 4, 8],
        [2, 4, 6],
    ]

    def __init__(self):
        self.board = [None] * 9

    def is_over(self):
        if None not in [elem for elem in self.board]:
            return True
        elif self.winner() is not None:
            return True
        else:
            return False

    def winner(self):
        for player in ('X', 'O'):
            positions = self.player_possible_moves(player)
            for line in self.winning_lines:
                win = True
                for pos in line:
                    if pos not in positions:
                        win = False
                if win:
                    return player
        return None

    def player_possible_moves(self, player):
        """squares that belong to a player"""
        player_squares = []
        for pos, element in enumerate(self.board):
            if element == player:
                player_squares.append(pos)
        return player_squares

    def valid_move(self, pos):
        return (pos in range(9)) and (self.board[pos] is None)

    def make_move(self, pos, player):
        self.board[pos] = player

    def available_moves(self):
        avail_moves = []
        for pos, symbol in enumerate(self.board):
            if symbol is None:
                avail_moves.append(pos)
        return avail_moves

    def alphabeta(self, node, player, alpha, beta):
        if node.is_over():
            if self.winner() == 'X':
                return -1
            elif self.winner() == 'O':
                return 1
            elif self.is_over() is True and self.winner() is None:  # tied
                return 0

        for move in node.available_moves():
            node.make_move(move, player)
            val = self.alphabeta(node, get_enemy(player), alpha, beta)
            node.make_move(move, None)  # zanulqva napraveniq hod
            if player == 'O':
                if val > alpha:
                    alpha = val
                if alpha >= beta:
                    return beta
            else:
                if val < beta:
                    beta = val
                if beta <= alpha:
                    return alpha
        if player == 'O':
            return alpha
        else:
            return beta


def determine(board, player):
    alpha = -2
    choices = []
    for move in board.available_moves():
        board.make_move(move, player)
        val = board.alphabeta(board, get_enemy(player), -2, 2)
        board.make_move(move, None)  # zanulqva napraveni hod
        if val > alpha:
            alpha = val
            choices = [move]
        elif val == alpha:
            choices.append(move)
    return random.choice(choices)


def get_enemy(player):
    if player == 'X':
        return 'O'
    return 'X'
