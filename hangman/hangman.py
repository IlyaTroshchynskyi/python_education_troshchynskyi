import random
import os


def read_words_from_file():
    with open("set_of_words.txt", "r") as file:
        return file.readlines()


def select_word():
    words = read_words_from_file()
    return random.choice(words).strip('\n')


def check_letter_in_word(letter, selected_word):
    return letter in selected_word


def search_indices_letter(letter, selected_word):
    indices = []
    while letter in selected_word:
        index_letter = selected_word.index(letter)
        selected_word = selected_word.replace(letter, '_', 1)
        indices.append(index_letter)
    return indices


def update_game_table(game_table, letter, indices):
    for index in indices:
        game_table[index] = letter
    return game_table


def define_count_attempts(word):
    return len(word) * 2


def show_menu():
    try:
        choice = int(input("Меню:\n "
                           "1-Начать игру.\n "
                           "2-Просмотреть слова которые "
                           "учавствовали в игре в текущей сессиии\n "
                           "3-Выйти.\n "))
    except ValueError:
        choice = 0
    return choice


def read_previous_words():
    with open("previous_words.txt", 'r') as file:
        return [word.strip('\n') for word in file.readlines()]


def add_word_to_file(word):
    with open('previous_words.txt', 'a') as file:
        file.write(word+"\n")


def delete_file():
    try:
        os.remove(os.getcwd() + '/previous_words.txt')
    except FileNotFoundError as ex:
        print(ex)


def check_attempt_guess_word(selected_word, user_attempt, game_table=None):
    if isinstance(user_attempt, list):
        return ''.join(game_table) == selected_word
    return selected_word == user_attempt


def print_message(count_attempts, used_attempts, game_table):
    print(f"У вас осталось '{count_attempts}' попыток и вы уже сделали "
          f"'{used_attempts}' попыток")
    print(f"Ваше игровое поле выглядит так:\n {' '.join(game_table)}")


def play_game(selected_word, game_table):
    used_attempts = 0
    count_attempts = define_count_attempts(selected_word)
    while count_attempts >= 1:
        letter = input("Пожалуйста введите букву\n")
        if len(letter) > 1:
            if check_attempt_guess_word(selected_word, letter):
                print(f"Вы отгадали слово: '{selected_word}'")
                break
            else:
                count_attempts -= 3
                used_attempts += 3
        if check_letter_in_word(letter, selected_word):
            indices = search_indices_letter(letter, selected_word)
            game_table = update_game_table(game_table, letter, indices)
        count_attempts -= 1
        used_attempts += 1
        print_message(count_attempts, used_attempts, game_table)
        if check_attempt_guess_word(letter, selected_word, game_table):
            print(f"Вы отгадали слово: '{selected_word}'")
            break
    else:
        print(f"Вы проиграли с таким полем: {''.join(game_table)}"
              f" и вы не отгадали слово: '{selected_word}'")


def main():
    delete_file()
    choice = 0
    while choice != 3:
        choice = show_menu()
        if choice == 1:
            print('Игра началась')
            selected_word = select_word()
            game_table = ['_' for x in range(len(selected_word))]
            add_word_to_file(selected_word)
            play_game(selected_word, game_table)
        elif choice == 2:
            print(read_previous_words())


if __name__ == '__main__':
    main()
