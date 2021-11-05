# -*- coding: utf-8 -*-
"""
   Implements the controller of Tic Tac Toe
"""


import tkinter as tk
import tkinter.messagebox
from tkinter import Button, DISABLED
from model import TicTacToe
from view import Main, Child

from download_logger_config import set_config_logger

logger = set_config_logger()


class Controller:
    """
       Implements the controller of Tic Tac Toe
    """

    def __init__(self):
        self.model = TicTacToe()
        self.view = Main()
        self.logger = logger
        self.start_game = None
        self.see_log = None
        self.clean_log = None
        self.close_game = None
        self.cell_0 = None
        self.cell_1 = None
        self.cell_2 = None
        self.cell_3 = None
        self.cell_4 = None
        self.cell_5 = None
        self.cell_6 = None
        self.cell_7 = None
        self.cell_8 = None
        self.counter_game = 0
        self.init_main()

    @staticmethod
    def result(boards, mark):
        """
        Check the winning combination on the board.
        """
        winning_coordinates = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6),
                                 (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
        for comb in winning_coordinates:
            if boards[comb[0]] == boards[comb[1]] == boards[comb[2]]\
                    and boards[comb[0]] == mark:
                return True
        return False

    def disable_cells(self):
        """
        Set disabled state of the cells when one of the players won the game.
        """
        for index in range(0, 9):
            cell = getattr(self, 'cell_' + str(index))
            cell.config(state=DISABLED)

    def define_sign(self, number):
        """
        Checking which button has been clicked and checking if
        the button has been already clicked or not to avoid over-writing
        """
        for index in range(0, 9):
            if number == index and number in self.model.numbers:
                self.model.numbers.remove(number)
                if self.model.player_move % 2 == 0:
                    self.model.player_mark = 'X'
                    self.model.boards[number] = self.model.player_mark
                elif self.model.player_move % 2 != 0:
                    self.model.player_mark = 'O'
                    self.model.boards[number] = self.model.player_mark
                cell = getattr(self, 'cell_'+str(index))
                cell.config(text=self.model.player_mark)
                self.model.player_move += 1
                mark = self.model.player_mark
                if self.result(self.model.boards, mark) and mark == 'X':
                    self.update_score('X')
                    self.logger.info("Player_1 wins")
                    tkinter.messagebox.showinfo("Result", "Player_1 wins")
                    self.disable_cells()
                elif self.result(self.model.boards, mark) and mark == 'O':
                    self.update_score('O')
                    self.logger.info("Player_2 wins")
                    self.disable_cells()
                    tkinter.messagebox.showinfo("Result", "Player_2 wins")
        if self.model.player_move > 8 and self.result(self.model.boards, 'X') is False and\
                self.result(self.model.boards, 'O') is False:
            tkinter.messagebox.showinfo("Result", "Match Tied")
            self.logger.info("Match Tied")
            self.disable_cells()

    def init_main(self):

        """
        Init the buttons in the view
        """
        self.start_game = tk.Button(self.view.frame_2, text="Start Game",
                                    command=lambda: self.draw_game_table())

        self.start_game.pack(side=tk.LEFT)
        self.see_log = tk.Button(self.view.frame_2, text="See Log",
                                 command=lambda: self.look_log())
        self.see_log.pack(side=tk.LEFT)

        self.clean_log = tk.Button(self.view.frame_2, text="Clean Log",
                                   command=lambda: self.model.clean_log_file())
        self.clean_log.pack(side=tk.LEFT)
        self.close_game = tk.Button(self.view.frame_2, text="Close Game",
                                    command=lambda: self.view.root.destroy())
        self.close_game.pack(side=tk.LEFT)

    def get_names_users(self):
        """
        Get the users name from the gui.
        """
        user_1 = self.view.entry_player_1.get()
        user_2 = self.view.entry_player_2.get()
        if len(user_1) == 0 or len(user_2) == 0:

            tk.messagebox.showwarning("Warning", "Please enter players name")
            self.logger.warning("Please enter players name")
            return False
        self.update_players_name(user_1, user_2)
        return True

    def update_players_name(self, player_1, player_2):
        """
        Update players name in constructor and initialize the game score
        """
        self.model.player_1 = player_1
        self.model.player_2 = player_2
        self.logger.info("User_1 has name %s, user_2 has name %s", player_1, player_2)

    def update_state_game_variables(self):
        """
        Update variables in constructor for new game if user want to continue play the game
        """
        self.model.numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        self.model.player_mark = ""
        self.model.player_move = 0
        self.model.boards = ["board"] * 9
        self.update_score_board()

    def update_score_board(self):
        """
        Insert the score of the players in gui entry.
        """
        score = ''
        for key, value in self.model.game_score.items():
            score += key + "-" + str(value) + ':'
        if self.view.score_board_entry.get():
            self.view.score_board_entry.delete(0, tkinter.END)
        self.view.score_board_entry.insert('1', score)

    def draw_game_table(self):
        """
        Draw the game table.
        """
        if not self.get_names_users():
            return
        if self.counter_game == 0:
            self.set_default_score()

        self.counter_game += 1
        self.update_state_game_variables()

        self.cell_0 = Button(self.view.frame_3, width=20, height=10,
                             command=lambda: self.define_sign(0))
        self.cell_0.grid(row=1, column=1)
        self.cell_1 = Button(self.view.frame_3, width=20, height=10,
                             command=lambda: self.define_sign(1))
        self.cell_1.grid(row=1, column=2)
        self.cell_2 = Button(self.view.frame_3, width=20, height=10,
                             command=lambda: self.define_sign(2))
        self.cell_2.grid(row=1, column=3)
        self.cell_3 = Button(self.view.frame_3, width=20, height=10,
                             command=lambda: self.define_sign(3))
        self.cell_3.grid(row=2, column=1)
        self.cell_4 = Button(self.view.frame_3, width=20, height=10,
                             command=lambda: self.define_sign(4))
        self.cell_4.grid(row=2, column=2)
        self.cell_5 = Button(self.view.frame_3, width=20, height=10,
                             command=lambda: self.define_sign(5))
        self.cell_5.grid(row=2, column=3)
        self.cell_6 = Button(self.view.frame_3, width=20, height=10,
                             command=lambda: self.define_sign(6))
        self.cell_6.grid(row=3, column=1)
        self.cell_7 = Button(self.view.frame_3, width=20, height=10,
                             command=lambda: self.define_sign(7))
        self.cell_7.grid(row=3, column=2)
        self.cell_8 = Button(self.view.frame_3, width=20, height=10,
                             command=lambda: self.define_sign(8))
        self.cell_8.grid(row=3, column=3)

    def look_log(self):
        """
        Look log in the gui.
        """
        Child(self.model.look_log())

    def update_score(self, mark):
        """
        Update score between two players.
        """
        if mark == 'X':
            self.model.game_score[self.model.player_1] += 1
        else:
            self.model.game_score[self.model.player_2] += 1

    def set_default_score(self):
        """
        Init default score
        """
        self.model.game_score[self.model.player_1] = 0
        self.model.game_score[self.model.player_2] = 0
