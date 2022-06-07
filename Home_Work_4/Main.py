difficulty_level = {
    "лёгкий": {
        "family":"семья",
        "hand": "рука",
        "people":"люди",
        "evening": "вечер",
        "minute":"минута",
    },
    "средний": {
        "believe":"верить",
        "feel": "чувствовать",
        "make":"делать",
        "open": "открывать",
        "think":"думать",
    },
    "тяжёлый": {
        "rural":"деревенский",
        "fortune": "удача",
        "exercise":"упражнение",
        "suggest": "предлагать",
        "except":"кроме",
    }
}


levels = {
   0: "Нулевой",
   1: "Так себе",
   2: "Можно лучше",
   3: "Норм",
   4: "Хорошо",
   5: "Отлично",
}


answers = {}
words = {}


print("Выберите уровень сложности")
print(", ".join(difficulty_level).title())
user_selected_difficulty_level = input().lower()
separator_length = 20
print(f"Ваш выбор: {user_selected_difficulty_level.title()}")
words = difficulty_level[user_selected_difficulty_level]


print(f"В данном уровне сложности, {len(words)} вопросов")
print("-" * separator_length)
for question_keys, question_values in words.items():
    print(f"Слово: {question_keys}, начинается на: {question_values[0].title()}, количество букв: {len(question_values)}\n")
    user_answer = input("Слово переводится как: ").lower()
    if user_answer == question_values:
        print(f"Верно, {question_keys.title()} это {question_values.title()}")
        answers[user_answer.title()] = True
        print("-" * separator_length)
    else:
        print(f"Неверно, {question_keys.title()} это {question_values.title()}")
        answers[user_answer.title()] = False
        print("-" * separator_length)


level_correct_answers = 0
print("правильно написанные слова:")
for answers_key, answers_values in answers.items():
    if answers_values == True:
        print(answers_key)
        level_correct_answers += 1
print("-----------------------------------------")
print("неверно написанные слова:")
for answers_key, answers_values in answers.items():
    if answers_values == False:
        print(answers_key)

print("-----------------------------------------")
print(f"ваш ранг: {levels[level_correct_answers]}")