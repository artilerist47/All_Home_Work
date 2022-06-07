import json
import random

separator_length = 50

print("Игра начинается")


def load_question():
    while True:
        user_choice = input("Выберите на каком языке хотите играть:\nРусский/Russian/1\nАнглийский/English/2\n"
                            "Для выхода из игры используйте: Выход\Стоп\Stop\Exit\n-->> ").lower()
        english_game = ["english", "английский", "2"]
        russian_game = ["russian", "русский", "1"]
        stop_game = ["stop", "стоп", "выход", "exit"]
        list_questions = []
        if user_choice in russian_game:
            with open("tasks_russian.json", encoding="utf-8") as file:
                questions_list = json.load(file)
                random.shuffle(questions_list)
                for number, keys in enumerate(questions_list):
                    list_questions.append(
                        Question(keys['questions'], keys['difficulty'], keys['answer'], number)
                    )
                return list_questions
        elif user_choice in english_game:
            with open("tasks_english.json", encoding="utf-8") as file:
                questions_list = json.load(file)
                random.shuffle(questions_list)
                for number, keys in enumerate(questions_list):
                    list_questions.append(
                        Question(keys['questions'], keys['difficulty'], keys['answer'], number)
                    )
                return list_questions
        elif user_choice in stop_game:
            quit()
        else:
            print("В меня не запрограммировали такой язык")


class Question:
    def __init__(self, question, difficulty, right_answer, number):
        self.question = question
        self.difficulty = int(difficulty)
        self.right_answer = right_answer
        self.number = number

        self.is_asked = False
        self.user_answer = None
        self.score = self.difficulty * 10

    def get_points(self):
        return self.score

    def is_correct(self):
        return self.user_answer == self.right_answer

    def build_question(self):
        return f"Вопрос {self.number + 1}:\nСложность: {self.difficulty}/5\n{self.question}"

    def build_feedback(self):
        if self.is_correct():
            return f"Ответ верный, вы заработали {self.score} баллов\n" \
                   f"{('-' * separator_length)}"
        return f"Ответ неверный, верный ответ {self.right_answer}\n" \
               f"{('-' * separator_length)}"


def statistics(questions):
    total_score = 0
    right_answer = 0

    for user_question in questions:
        if user_question.is_correct():
            total_score += user_question.score
            right_answer += 1
    print(f"отвечено правильно на {right_answer} вопросов из {len(questions)}\n"
          f"Заработано {total_score} баллов")


if __name__ == "__main__":
    QUESTIONS = load_question()

    for question in QUESTIONS:
        print(question.build_question())
        user_answer = input("-->")

        question.user_answer = user_answer.title()
        question.is_asked = True

        print(question.build_feedback())

print("Вот и всё!")
statistics(QUESTIONS)
