# -*- coding: utf-8 -*-
"""
   Implements simple view for Tic Tac Toe game.
"""

import tkinter as tk
from tkinter import Label, Entry


class Main(tk.Frame):
    """
    Implement main frame.
    """

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Tic tac toe")
        self.root.geometry('665x650+300+200')
        self.root.resizable(False, False)
        self.frame_1 = None
        self.frame_2 = None
        self.frame_3 = None
        self.player_1 = None
        self.entry_player_1 = None
        self.player_2 = None
        self.entry_player_2 = None
        self.score_board_label = None
        self.score_board_entry = None

        super().__init__(self.root)
        self.init_main()

    def run_loop(self):
        """
        Run the main loop of the main window.
        """
        self.root.mainloop()

    def init_main(self):
        """
        Init the frames and fields for view.
        """

        self.frame_1 = tk.Frame(self.root, height=75, bg="#d7d8e0", bd=2)
        self.frame_1.pack(fill=tk.X)

        self.frame_2 = tk.Frame(self.root, height=75, bg="white", bd=2)
        self.frame_2.pack(fill=tk.X)

        self.frame_3 = tk.Frame(self.root, height=500, bg="#d7d8e0")
        self.frame_3.pack(fill=tk.X)

        self.player_1 = Label(self.frame_1, text="Player_1", bg="green")
        self.entry_player_1 = Entry(self.frame_1, bg="#BDFFC4", bd=3)
        self.player_1.pack(side=tk.LEFT)
        self.entry_player_1.pack(side=tk.LEFT)

        self.player_2 = Label(self.frame_1, text="Player_2", bg="green")
        self.entry_player_2 = Entry(self.frame_1, bg="#BDFFC4", bd=3)
        self.player_2.pack(side=tk.LEFT)
        self.entry_player_2.pack(side=tk.LEFT)

        self.score_board_label = Label(self.frame_1, text="Score Board ", bg="green")
        self.score_board_entry = Entry(self.frame_1, bg="#BDFFC4", bd=3)
        self.score_board_label.pack(side=tk.TOP)
        self.score_board_entry.pack(side=tk.RIGHT)


class Child(tk.Toplevel):
    """
    Implement child window in order to look log information.
    """
    def __init__(self, log_information):
        super().__init__()
        self.init_child(log_information)

    def init_child(self, log_information):
        """
        Set up config for child window.
        """
        self.title("Log file")
        self.geometry('400x220+400+300')
        self.resizable(True, True)

        text_box = tk.Text(self)
        text_box.insert('1.0', log_information)
        text_box.pack()
