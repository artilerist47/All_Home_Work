print(
    "Приветствую.\n"
    "Сегодня мы попробуем потренироваться в разгадывании анаграмм.\n"
    "Но для начала"
)

user_name = input("Введите ваше имя -> ")

separator_length = 35

with open("history.txt", "a", encoding="utf-8") as file:
    """
    Вводим в файл имя игрока
    """
    file.write(f"{user_name} - ")


def get_words():
    """
    Читаем слова из файла и заносим из в список для дальнейшей работы с ними
    """
    words = []
    with open('words.txt', "rt", encoding="utf-8") as f:
        for text in f:
            words.append(text.rstrip('\n'))
        return words


def get_statatistic():
    """
    Читаем историю для статистики
    """
    balls = []
    with open('history.txt', "rt") as f:
        for text in f:
            player, ball = text.strip().split(" -" + " ")
            balls.append(int(ball))
    return balls


def reset_list():
    """
    Обнуляем историю игры
    """
    new_answers_choice = ""
    with open("answers.txt", "w", encoding="utf-8") as file:
        file.write(f"{new_answers_choice}")


user_balls = 0  # стартовое количество баллов
words = get_words()
reset_list()  # обнуляем список ответов для занесения новых
for word in words:
    balls = len(word)
    import random
    text = random.sample(word, len(word))
    result = ''.join(text)

    user_answer = input(f"Как по вашему мнению расшифровывается слово {result} -> ")

    if user_answer.lower() == word.lower():
        print(f"Верно.\nВы получаете {balls} баллов!")
        user_balls += balls
        with open("answers.txt", "a", encoding="utf-8") as file:
            """
            Вводим в файл ответы
            """
            file.write(f"{user_answer.title()} - ответ дан верно\n")
    else:
        print(f"Увы но неверно! Потому что верный ответ – {word.title()}")
        with open("answers.txt", "a", encoding="utf-8") as file:
            """
            Вводим в файл ответы
            """
            file.write(f"{user_answer.title()} - неверно, верный ответ - {word.title()}\n")

with open("history.txt", "a", encoding="utf-8") as f:
    """
    Вводим кто играл и сколько очков заработал в файл
    """
    f.write(f"{user_balls}\n")


with open("history.txt") as f:
    game_count = 0
    for data in f:
        data.strip().split(" -" + " ")
        game_count += 1


max_balls = get_statatistic()
print(f"Вы заработали: {user_balls} баллов")
print(f"\nвсего игры сыгранно: {game_count}")
print(f"максимальный рекорд: {max(max_balls)} баллов")
print("-" * separator_length)


"""
 просим пользователя выбрать что делать/смотреть
 """
while True:
    print("Выберите действие:")
    response = input("1 - Посмотреть более детальную информацию своих ответов\n"
                     "2 - Посмотреть топ игроков\n"
                     "3 - Посмотреть список участников\n"
                     "стоп/stop - Закончить\n"
                     "-> ")
    print("-" * separator_length)

    if response == "1":
        file = open("answers.txt", "r", encoding="utf-8")
        informations = file.read()
        print(informations.rstrip("\n"))
        print("-" * separator_length)
        file.close()

    elif response == "2":
        with open('history.txt', "rt", encoding="utf-8") as f:
            for top_statistic in f:
                name, top_balls = top_statistic.rstrip("\n").split(" - ")
                if int(top_balls) == max(max_balls):
                    print(f"Пользователь '{name}' заработал {max(max_balls)} балов, и занимает первое место")
        print("-" * separator_length)

    elif response == "3":
        file = open("history.txt", "r", encoding="utf-8")
        informations = file.read()
        print(informations.rstrip("\n"))
        print("-" * separator_length)
        file.close()

    elif response == "стоп" or response == "stop":
        break

