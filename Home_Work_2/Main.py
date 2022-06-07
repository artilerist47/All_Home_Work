print("Привет! Предлагаю проверить свои знания английского!")
print("Расскажи, как тебя зовут!")
user_name = str(input("Меня зовут "))  # ввести имя пользователя
print(f"Привет, {user_name}, начинаем тренировку!")


print("Вопрос первый")
print("My name ___ Vova")
answer1 = str(input()) # ответ пользователя 1
count = 0  # счётчик правильных ответов
if answer1 == str("is"):
    print("Ответ верный!")
    print("Вы получаете 10 баллов!")
    count = count + 1
else:
    print("Неправильно.")
    print("Правильный ответ: is")


print("Вопрос второй")
print("I ___ a coder")
answer2 = str(input())  # ответ пользователя 2
if answer2 == str("am"):
    print("Ответ верный!")
    print("Вы получаете 10 баллов!")
    count = count + 1
else:
    print("Неправильно.")
    print("Правильный ответ: am")


print("Вопрос третий")
print("I live ___ Moscow")
answer3 = str(input())  # ответ пользователя 3
if answer3 == str("in"):
    print("Ответ верный!")
    print("Вы получаете 10 баллов!")
    count = count + 1
else:
    print("Неправильно.")
    print("Правильный ответ: in")


print(f"Вот и все, {user_name}!")
print(f"Вы ответили на {count} вопросов из 3 верно.")
print(f"Вы заработали {count*10} баллов")
procents = 100/3*count  # счётчик процентов
print(f"это {procents} процентов")
