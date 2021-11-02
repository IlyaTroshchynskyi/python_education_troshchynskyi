# -*- coding: utf-8 -*-
"""
   Implements simple Tic Tac Toe game with minimax algorithm
"""


from download_logger_config import set_config_logger

logger = set_config_logger()


class TicTacToe:
    """
    Implements class for game Tic Tac Toe
    """

    def __init__(self):
        self.board = [0, 1, 2,
                      3, 4, 5,
                      6, 7, 8]
        self.player_1 = ''
        self.player_2 = ''
        self.game_score = dict()
        self.counter_movements = 0
        self.winner = False
        self.counter_game_party = 0

    def update_counter_game_party(self):
        """
        Update counter for game party between computer and player
        """
        self.counter_game_party += 1

    def minimax(self, new_board, player):

        """
        Implementation of minimax algorithms.
        """

        avail_spots = self.get_empty_indices(new_board)
        if self.check_winner(new_board, 'O'):
            return {"score": -10}

        if self.check_winner(new_board, 'X'):
            return {"score": 10}

        if len(avail_spots) == 0:
            return {"score": 0}

        moves = []

        for index, _ in enumerate(avail_spots):
            move = {}
            move['index'] = new_board[avail_spots[index]]
            new_board[avail_spots[index]] = player

            if player == 'X':
                result = self.minimax(new_board, 'O')
                move["score"] = result["score"]
            else:
                result = self.minimax(new_board, 'X')
                move["score"] = result["score"]

            new_board[avail_spots[index]] = move["index"]
            moves.append(move)

        best_move = 0
        if player == 'X':
            best_score = -10000
            for index, _ in enumerate(moves):
                if moves[index]["score"] > best_score:
                    best_score = moves[index]["score"]
                    best_move = index
        else:
            best_score = 10000
            for index, _ in enumerate(moves):
                if moves[index]["score"] < best_score:
                    best_score = moves[index]["score"]
                    best_move = index

        return moves[best_move]

    @staticmethod
    def get_empty_indices(board):
        """
        Returns the available spots on the board
        """
        return list(filter(lambda cell: cell not in ('O', 'X'), board))

    def display_board(self):
        """
        Display game board in console and table with place of every item on the board
        """

        coordinates = ((0, 1, 2), (3, 4, 5), (6, 7, 8))
        for col_1, col_2, col_3 in coordinates:
            print('| ' + str(self.board[col_1]) + ' | ' + str(self.board[col_2]) + ' | ' +
                  str(self.board[col_3]) + ' |')

    def update_players_name(self, player_2):
        """
        Update players name in constructor and initialize the game score
        """

        self.player_1 = 'Comp_minimax'
        self.player_2 = player_2
        self.game_score[self.player_1] = 0
        self.game_score[player_2] = 0
        logger.info("User_1 has name %s, User_2 has name %s", self.player_1, self.player_2)

    def ask_name_player(self):
        """
        Ask player name from console input
        """
        player_2 = input("Please enter name of the second player\n")
        self.update_players_name(player_2)

    def check_winner(self, board, player):
        """
        Check the winning combination on the board and return winner name or False
        """

        winning_coordinates = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6),
                                 (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
        for comb in winning_coordinates:
            if board[comb[0]] == board[comb[1]] == board[comb[2]]\
                    and str(board[comb[0]]) == player:
                return self.player_1 if player == 'X' else self.player_2
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

        self.ask_name_player()
        while not self.winner:

            if (self.counter_movements + self.counter_game_party) % 2 == 0:
                self.comp_move('X')
            else:
                self.make_move(self.player_2, 'O')

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
                self.display_board()
                self.game_score[self.winner] += 1
                message = f"Current game was won by player: {self.winner}"
                print(message)
                logger.info(message)
                logger.info('The count between two players: %s', self.game_score)

                continue_game = TicTacToe.define_continue_game()
                if continue_game:
                    self.update_variables_for_new_game()
                else:
                    break

    def comp_move(self, move_sign):
        """
        Define action of minimax algorithms.
        """

        best_spot = self.minimax(self.board.copy(), move_sign)['index']

        try:
            self.update_game_table(int(best_spot), move_sign)
        except ValueError as ex:
            self.counter_movements -= 1
            print(ex)
            logger.error(ex)
        self.winner = self.check_winner(self.board, move_sign)
        self.counter_movements += 1

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
        self.winner = self.check_winner(self.board, move_sign)
        self.counter_movements += 1

    def update_variables_for_new_game(self):
        """
        Update variables in constructor for new game lap if user want to continue play the game
        """

        self.counter_movements = 0
        self.update_counter_game_party()
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

        if item > 8 or item < 0 or self.board[item] not in (0, 1, 2, 3, 4, 5, 6, 7, 8):
            raise ValueError(f"You entered wrong or busy item: {item}")
        self.board[item] = value

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

        self.board = list(range(9))
        logger.info('Game table was refreshed')

    @staticmethod
    def look_log():
        """
        Print the data from the log file
        """

        with open('../tic_tac_toe.log', 'r') as log:
            for line in log.readlines():
                print(line.strip())

    @staticmethod
    def clean_log_file():
        """
        Clean the log file
        """

        with open('../tic_tac_toe.log', 'w'):
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
