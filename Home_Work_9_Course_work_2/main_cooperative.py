from player_cooperative import OneUsers, AllUsers
from utils import load_random_word
import random


def main_cooperative():
    while True:
        try:
            user_select = int(input("введите количество пользователей --> "))
            if user_select == 0:
                print("Число пользователей не может быть равно нулю")
                continue
            break
        except:
            print("Введённые данные не корректны")

    numbers_players = []
    gamers = []

    word_questions = load_random_word()

    i = 0

    for players in range(user_select):
        game_players = input(f"введите имя игрока номер {players + 1} --> ")
        numbers_players.append(OneUsers(game_players))
        gamers.append(game_players)

    all_players = AllUsers(gamers)

    print(f"Начинаем\n"
          f"Привет, {numbers_players[i].user_name}")

    for text in word_questions:
        print(f"{'-' * separator_length}\n"
              f"Слово {text.word}\n"
              f"Из этого слова можно составить {len(text.subwords)} других слов, найдите их")

        while len(text.subwords) > 0:
            user_answer = input("-->").lower()
            for player in numbers_players:
                player.user_answer = user_answer
            all_players.user_answer = user_answer
            text.user_answer = user_answer

            if user_answer in stop_game:
                with open("history.txt", "a", encoding="utf-8") as f:
                    f.write(f"Пользователи: {', '.join(gamers)} -> "
                            f"Количество самостоятельно найденных слов: {all_players.len_all_players_words()} | "
                            f"Cлова выданные подсказкой: {all_players.len_help_words_all_players()}\n")
                    for player in numbers_players:
                        f.write(f"Пользователь - {player.user_name}:\n"
                                f"{' '*4}Слов Подсказок - {player.len_help_words_one_players()}: "
                                f"{', '.join(player.help_words)}\n"
                                f"{' '*4}Свои Слова - {player.len_player_words()}: "
                                f"{', '.join(player.used_words)}\n")
                    f.write("\n")

                print("Очень жаль, но это ваш выбор")
                print(f"Количество самостоятельно найденных слов всеми игроками составляет: "
                      f"{all_players.len_all_players_words()}\n"
                      f"Количество слов выданных подсказкой составляет: "
                      f"{all_players.len_help_words_all_players()}")
                for player in numbers_players:
                    print(f"Пользователь: {player.user_name} --> "
                          f"Слов Подсказок - "
                          f"{player.len_help_words_one_players()}: "
                          f"{', '.join(player.help_words)} | "
                          f"Свои Слова - "
                          f"{player.len_player_words()}: "
                          f"{', '.join(player.used_words)}")
                quit()

            elif text.word_in_subwords():
                print("Да, такое слово есть")
                all_players.append_words_all_users()
                numbers_players[i].append_user_words()
                text.subwords.remove(user_answer)

            elif all_players.check_all_used_words() or all_players.check_all_words_help():
                print("Такое слово уже было")

            elif user_answer == "help":
                random_help_word = random.choice(text.subwords)
                print(random_help_word)
                all_players.help_words.append(random_help_word)
                numbers_players[i].help_words.append(random_help_word)
                text.subwords.remove(random_help_word)
                i += 1
                if i == user_select:
                    i -= i
                print("теперь очередь", numbers_players[i].user_name)

            elif user_answer == "next word":
                text.subwords.clear()

            else:
                print("Такого слова нет")
                i += 1
                if i == user_select:
                    i -= i
                print("теперь очередь", numbers_players[i].user_name)

    with open("history.txt", "a", encoding="utf-8") as f:
        f.write(f"Пользователи: {', '.join(gamers)} -> "
                f"Количество самостоятельно найденных слов: {all_players.len_all_players_words()} | "
                f"Cлова выданные подсказкой: {all_players.len_help_words_all_players()}\n")
        for player in numbers_players:
            f.write(f"Пользователь - {player.user_name}:\n"
                    f"{' ' * 4}Слов Подсказок - {player.len_help_words_one_players()}: "
                    f"{', '.join(player.help_words)}\n"
                    f"{' ' * 4}Свои Слова - {player.len_player_words()}: "
                    f"{', '.join(player.used_words)}\n")
        f.write("\n")

    print(f"{'-' * separator_length}\n"
          f"Игра закончилась, вы хорошо подумали над каждым словом")
    print(f"Количество самостоятельно найденных слов всеми игроками составляет: "
          f"{all_players.len_all_players_words()}\n"
          f"Количество слов выданных подсказкой составляет: "
          f"{all_players.len_help_words_all_players()}")
    for player in numbers_players:
        print(f"Пользователь: {player.user_name} --> "
              f"Слов Подсказок - "
              f"{player.len_help_words_one_players()}: "
              f"{', '.join(player.help_words)} | "
              f"Свои Слова - "
              f"{player.len_player_words()}: "
              f"{', '.join(player.used_words)}")
    quit()


print(
    "Привет. сегодня мы будем находить слова в слове.\n"
    "Запустите игру командой запуск/старт/start/run или можете выйти из неё командой stop/стоп/quit.\n"
    "Наберите rules/informations/информация/правила, что бы узнать правила\n"
)


stop_game = ["stop", "стоп", "quit", "выход"]
start_game = ["запуск", "старт", "start", "run"]
rules = ["rules", "правила", "информация", "informations"]
separator_length = 35


while True:
    start_user_game = input("--> ").lower()
    if start_user_game in start_game:
        main_cooperative()
    elif start_user_game in stop_game:
        quit("Очень жаль, но это ваш выбор. До следующей встречи")
    elif start_user_game in rules:
        file = open("rules.txt", "r", encoding="utf-8")
        informations = file.read()
        print(informations.rstrip("\n"))
    elif start_user_game == "history":
        try:
            file = open("history.txt", "r", encoding="utf-8")
            informations = file.read()
            print(informations.rstrip('\n'))
            print('-' * separator_length)
            file.close()
        except:
            print("статистики пока нет")
    else:
        print("Введённое слово не корректно")
        continue
