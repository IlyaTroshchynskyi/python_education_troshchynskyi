# -*- coding: utf-8 -*-
"""
   Implements simple Tic Tac Toe game
"""


class TicTacToe:

    """
    Implements class for game Tic Tac Toe
    """

    def __init__(self):

        self.player_1 = ''
        self.player_2 = ''
        self.game_score = dict()
        self.winner = False
        self.numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        self.player_mark = ""
        self.player_move = 0
        self.boards = ["board"] * 9

    @staticmethod
    def look_log():
        """
        Read the data from the log file
        """

        with open('tic_tac_toe.log', 'r') as log:
            lines = log.readlines()
            return lines

    @staticmethod
    def clean_log_file():
        """
        Clean the log file
        """
        with open('tic_tac_toe.log', 'w'):
            pass
