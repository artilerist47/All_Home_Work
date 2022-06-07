from player_single import Player
from utils import load_random_word
import random


def main_single():
    user_name = input("Введите своё имя -->> ")
    player = Player(user_name)

    with open("history.txt", "a", encoding="utf-8") as file:
        file.write(f"Пользователь: {user_name} -> ")

    print("привет", player.user_name)
    print("Приятной игры")

    word_questions = load_random_word()

    for text in word_questions:
        print("-" * separator_length)
        print("Слово", text.word)
        print(f"Из этого слова можно составит {len(text.subwords)} других слов, найдите их")
        while len(text.subwords) > 0:
            user_answer = input("-->").lower()
            player.user_answer = user_answer
            text.user_answer = user_answer
            if user_answer in stop_game:
                with open("history.txt", "a", encoding="utf-8") as f:
                    f.write(f"Количество самостоятельно найденных слов: {player.len_player_words()} "
                            f"| Найденные слова при помощи подсказки: {player.len_player_help_words()}\n\n")
                quit(f"Очень жаль, но это ваш выбор.\n"
                     f"Количество найденных вами слов составляет: {player.len_player_words()}")
            elif text.word_in_subwords():
                print("Да, такое слово есть")
                player.append_user_words()
                text.subwords.remove(user_answer)
            elif player.check_used_words() or player.check_help_words():
                print("Такое слово уже было")
            elif user_answer == "help":
                random_help_word = random.choice(text.subwords)
                print(random_help_word)
                player.help_words.append(random_help_word)
                text.subwords.remove(random_help_word)
            elif user_answer == "next word":
                break
            else:
                print("Такого слова нет")
    with open("history.txt", "a", encoding="utf-8") as f:
        f.write(f"Количество самостоятельно найденных слов: {player.len_player_words()} "
                f"| Найденные слова при помощи подсказки: {player.len_player_help_words()}\n\n")
    print("-" * separator_length)
    print(
        f"Игра закончилась, вы хорошо подумали над каждым словом\n"
        f"Количество самостоятельно найденных слов составляет: {player.len_player_words()}"
    )
    quit()


print(
    "Привет. сегодня мы будем находить слова в слове.\n"
    "Запустите игру командой запуск/старт/start/run или можете выйти из неё командой stop/стоп/quit.\n"
    "Наберите rules/informations/информация/правила, что бы узнать правила\n"
)


stop_game = ["stop", "стоп", "quit"]
start_game = ["запуск", "старт", "start", "run"]
rules = ["rules", "правила", "информация", "informations"]
separator_length = 35


while True:
    start_user_game = input("--> ").lower()
    if start_user_game in start_game:
        main_single()
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
            print(informations.rstrip("\n"))
            print("-" * separator_length)
            file.close()
        except:
            print("статистики пока нет")
    else:
        print("Введённое слово не корректно")
        continue
