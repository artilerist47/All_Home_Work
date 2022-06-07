# Списки
questions = ["Вопрос первый\nMy name ___is Vova", "Вопрос второй\nI ___ a coder", "Вопрос третий\nI live ___ Moscow",
             "Вопрос четвёртый\nI ___ studying"]
# 4 вопрос добавлен лично от меня, для проверки правильности работоспособности
answers = ["is", "am", "in", "like"]
ball_list = ["Балл!", "Баллов!", "Балла!"]
answers_text = ["Ответ верный!", "Неправильно.", "Правильный ответ:"]
attempts_text = ["Осталось попыток:", ", попробуйте еще раз!", ]

# Переменные
youll_get = "Вы получаете"
ready = "ready"
total_questions = len(questions)  # количество вопросов
total_balls = 0  # сумма баллов
count = 0  # счётчик правильных ответов
total_attempts = 3  # количество  попыток
summ_balls = 3  # сколько баллов за ответ с первой попытки
# minus = ? сколько баллов будет сниматься за неправильный ответ (на данный момент отсутствует)


print("Привет! \nПредлагаю проверить свои знания английского!")
print("Расскажи, как тебя зовут!")
user_name = str(input("Меня зовут "))  # ввести имя пользователя
print(f"Привет, {user_name},\nНаберите {ready}, чтобы начать!")
readiness_check = str(input())

if readiness_check == ready:

    for questions_number in range(len(questions)):
        attempts = total_attempts
        balls = summ_balls
        print(questions[questions_number])
        while attempts != 0:
            user_answer = input()
            if user_answer == answers[questions_number]:
                print(answers_text[0])
                last_digit = balls % 10
                if 11 <= balls <= 19:
                    ball_text = ball_list[1]
                elif balls == 1:
                    ball_text = ball_list[0]
                elif 2 <= last_digit <= 4:
                    ball_text = ball_list[2]
                else:
                    ball_text = ball_list[1]
                print(youll_get, balls, ball_text)
                count += 1
                total_balls += balls
                break
            else:
                attempts -= 1
                if attempts == 0:
                    print(answers_text[1])
                    print(answers_text[2], answers[questions_number])
                else:
                    print(attempts_text[0], attempts, attempts_text[1])
                    balls -= 1

    print(f"Вот и все, {user_name}!")
    print(f"Вы ответили на {count} из {total_questions} вопросов верно.")

    last_digit = total_balls % 10
    if 11 <= total_balls <= 19:
        total_balls_text = ball_list[1]
    elif total_balls == 1:
        total_balls_text = ball_list[0]
    elif 2 <= last_digit <= 4:
        total_balls_text = ball_list[2]
    else:
        total_balls_text = ball_list[1]

    print(f"Вы заработали {total_balls} {total_balls_text}")
    procents = 100 / total_questions * count  # счётчик процентов
    print(f"это {round(procents, 2)} процентов")

else:
    print("Кажется, вы не хотите играть. Очень жаль")
