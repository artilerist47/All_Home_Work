morse_code = {
  "0": "-----",
  "1": ".----",
  "2": "..---",
  "3": "...--",
  "4": "....-",
  "5": ".....",
  "6": "-....",
  "7": "--...",
  "8": "---..",
  "9": "----.",
  "a": ".-",
  "b": "-...",
  "c": "-.-.",
  "d": "-..",
  "e": ".",
  "f": "..-.",
  "g": "--.",
  "h": "....",
  "i": "..",
  "j": ".---",
  "k": "-.-",
  "l": ".-..",
  "m": "--",
  "n": "-.",
  "o": "---",
  "p": ".--.",
  "q": "--.-",
  "r": ".-.",
  "s": "...",
  "t": "-",
  "u": "..-",
  "v": "...-",
  "w": ".--",
  "x": "-..-",
  "y": "-.--",
  "z": "--..",
  ".": ".-.-.-",
  ",": "--..--",
  "?": "..--..",
  "!": "-.-.--",
  "-": "-....-",
  "/": "-..-.",
  "@": ".--.-.",
  "(": "-.--.",
  ")": "-.--.-"
}


encrypted_words = [
                   "code",
                   "bit",
                   "listen to music",
                   "read a book",
                   "shopping trip",
                   "movie ticket",
                   "dance",
                   "game",
                   ]
answers = []
separator_length = 35
count_answers = 0


def get_word():
    """
    получает случайное слово или фраза из списка
    """
    import random
    morse_text = random.choice(encrypted_words)
    return morse_text


def english_to_morse(message):
    """
    переводит слово с английского на морзе
    """
    morse = []  # будет содержать список переведённых слов на морзе
    for char in message:
        if char in morse_code:
            morse.append(morse_code[char])
    return " ".join(morse)


def main():
    """
    просит пользователя нажать enter
    """
    while True:
        response = input("Сегодня мы потренируемся расшифровывать морзянку.\nНажмите 'enter' что бы продолжить ")
        print("-" * separator_length)
        if response == "":
            break


def print_statistics(answers):
    """
    Получает статистику ответов
    """
    print(f"Всего задачек: {len(answers)}")
    count_answers_True = []
    count_answers_False = []
    for i in answers:
        if i == "True":
            count_answers_True.append("True")
        else:
            count_answers_False.append("False")
    print(f"Правильно отвеченные слова: {len(count_answers_True)}")
    print(f"Неверно отвеченные слова: {len(count_answers_False)}")


# Основное тело программы
main()

for i in range(0, 3):
    """
    цикл вопрос-ответ
    """
    english = get_word()
    morse = english_to_morse(english)
    print(f"Расшифруйте слово {i}: {morse}")
    user_answer = input("Ваш вариант перевода: ").title()
    new_english = []
    for i in english.lower():
        if i not in [" "]:
            new_english.append(i)
    new_user_answer = []
    for i in user_answer.lower():
        if i not in [" "]:
            new_user_answer.append(i)
    if new_user_answer == new_english:
        print(f"Верно, это: {english.title()}")
        answers.append("True")
        print("-" * separator_length)
    else:
        answers.append("False")
        print(f"Увы, но вы ошиблись\nА правильным ответом будет: {english.title()}")
        print("-" * separator_length)

print_statistics(answers)