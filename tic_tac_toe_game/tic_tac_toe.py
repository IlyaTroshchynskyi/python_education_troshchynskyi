# -*- coding: utf-8 -*-
"""
   Implements simple Tic Tac Toe game
"""


from download_logger_config import set_config_logger

logger = set_config_logger()


class TicTacToe:
    """
    Implements class for game Tic Tac Toe
    """

    def __init__(self):
        self.board = ['-', '-', '-',
                      '-', '-', '-',
                      '-', '-', '-']
        self.player_1 = ''
        self.player_2 = ''
        self.game_score = dict()
        self.counter_movements = 0
        self.winner = False

    def display_board(self):
        """
        Display game board in console and table with place of every item on the board
        """

        coordinates = ((0, 1, 2), (3, 4, 5), (6, 7, 8))
        for col_1, col_2, col_3 in coordinates:
            print('| ' + self.board[col_1] + ' | ' + self.board[col_2] + ' | ' +
                  self.board[col_3] + ' |', '**** ', '| ' + str(col_1+1) + ' | ' +
                  str(col_2+1) + ' | ' + str(col_3+1) + ' |')

    def update_players_name(self, player_1, player_2):
        """
        Update players name in constructor and initialize the game score
        """

        self.player_1 = player_1
        self.player_2 = player_2
        self.game_score[player_1] = 0
        self.game_score[player_2] = 0
        logger.info("User_1 has name %s, user_2 has name %s", self.player_1, self.player_2)

    def ask_name_players(self):
        """
        Ask players name from console input
        """

        player_1 = input("Please enter name of the first player\n")
        player_2 = input("Please enter name of the second player\n")
        self.update_players_name(player_1, player_2)

    def check_winner(self):
        """
        Check the winning combination on the board and return winner name or False
        """

        winning_coordinates = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6),
                                 (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
        for comb in winning_coordinates:
            if self.board[comb[0]] == self.board[comb[1]] == self.board[comb[2]]\
                    and self.board[comb[0]] in 'X0':
                return self.player_1 if self.board[comb[0]] == 'X' else self.player_2
        return False

    @staticmethod
    def define_continue_game():
        """
        Ask user about continue game
        """

        flag_continue_game = input("Do you want continue game? Please enter 'Y' or 'N'\n")
        return flag_continue_game.upper() == 'Y'

    def play_game(self):
        """
        Define the action during the game
        """

        self.ask_name_players()
        while not self.winner:

            if self.counter_movements % 2 == 0:
                self.make_move(self.player_1, 'X')
            else:
                self.make_move(self.player_2, '0')

            if self.counter_movements == 9:
                message = 'Nobody win'
                print(message)
                logger.info(message)
                continue_game = TicTacToe.define_continue_game()
                if continue_game:
                    self.update_variables_for_new_game()
                else:
                    break

            if self.winner:
                message = f"Current game was won by player: {self.winner}"
                print(message)
                logger.info(message)
                logger.info('The count between two players: %s', self.game_score)
                continue_game = TicTacToe.define_continue_game()
                if continue_game:
                    self.game_score[self.winner] += 1
                    self.update_variables_for_new_game()
                else:
                    break

    def make_move(self, player, move_sign):
        """
        Define action of player during the move
        """

        self.display_board()
        print(f"Player with name: '{player}' should make a move")
        choice = input("Please select an empty space between 1 and 9\n")
        try:

            self.update_game_table(int(choice), move_sign)
        except ValueError as ex:
            self.counter_movements -= 1
            print(ex)
            logger.error(ex)
        self.winner = self.check_winner()
        self.counter_movements += 1

    def update_variables_for_new_game(self):
        """
        Update variables in constructor for new game lap if user want to continue play the game
        """

        self.counter_movements = 0
        self.refresh_game_table()
        self.show_count_players()
        self.winner = False

    def show_count_players(self):
        """
        Show count in console between two players
        """

        print(f"The {self.player_1} has {self.game_score[self.player_1]}, "
              f"{self.player_2} has {self.game_score[self.player_2]}")

    def update_game_table(self, item, value):
        """
        Update game table after user choice
        """

        if item > 9 or item <= 0 or self.board[item-1] != '-':
            raise ValueError(f"You entered wrong or busy item: {item}")
        self.board[item-1] = value

    def controller(self, choice):
        """
        Define which action execute after user choice from menu
        """

        if choice == 1:
            self.play_game()
        if choice == 2:
            self.look_log()
        if choice == 3:
            self.clean_log_file()

    def refresh_game_table(self):
        """
        Refresh game table for new game lap
        """

        self.board = ['-' for _ in self.board]
        logger.info('Game table was refreshed')

    @staticmethod
    def look_log():
        """
        Print the data from the log file
        """

        with open('tic_tac_toe.log', 'r') as log:
            for line in log.readlines():
                print(line.strip())

    @staticmethod
    def clean_log_file():
        """
        Clean the log file
        """

        with open('tic_tac_toe.log', 'w'):
            pass
        logger.info("The log was cleaned")


def show_menu():
    """
    Show menu for user in console
    """

    choice = 0
    while choice != 4:
        game = TicTacToe()
        try:
            choice = int(input("Menu:\n "
                            "1-Play.\n "
                            "2-Look through the log\n "
                            "3-Clean the log of victories \n "
                            "4-Exit\n "))
        except ValueError as ex:
            print("You should choose one option")
            logger.error(ex)
            continue
        logger.info("User choose the option from menu: %s", str(choice))
        game.controller(choice)


def main():
    """
    Entry point for game
    """
    show_menu()


if __name__ == '__main__':
    main()
