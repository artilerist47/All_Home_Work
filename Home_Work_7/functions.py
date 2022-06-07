import json


def load_students():
    """
    получает данные студента из файла
    :return:
    """
    with open("students.json") as file:
        data = json.load(file)
    return data


def load_professions():
    """
    получает данные профессии из файла
    :return:
    """
    with open("professions.json") as file:
        data = json.load(file)
    return data


def get_student_by_pk(pk):
    for data_student in students_data:
        if data_student["pk"] == pk:
            print(data_student)
            return data_student
    else:
        print("У нас нет такого студента")
        quit()


def get_profession_by_title(title):
    for data_professions in professions_data:
        if data_professions['title'] == title:
            return data_professions
    else:
        print("У нас нет такой специальности")
        quit()


def check_fitness(student, profession):
    result = {}
    result_skills_know = student.intersection(profession)
    result_skills_don_know = profession.difference(student)
    suitability = len(result_skills_know)/len(profession)*100
    result["has"] = list(result_skills_know)
    result["lacks"] = list(result_skills_don_know)
    skill_know = ', '.join(result["has"])
    skill_don_know = ', '.join(result["lacks"])
    result["fit_percent"] = int(suitability)
    print(f"Пригодность {int(suitability)} %")
    print(f"Студент '{student_name}' знает: {skill_know}")
    print(f"Студент '{student_name}' не знает: {skill_don_know}")


"""
начало основного тела программы
"""
print("Приветствую. Сегодня мы попробуем подобрать студентам должности.")


students_data = load_students()
professions_data = load_professions()


user_input_student_pk = input("Введите номер студента -> ")
if user_input_student_pk.isdigit():
    pk = int(user_input_student_pk)
    data_student = get_student_by_pk(pk)
else:
    print("Введённые данные не корректны")
    quit()


student_name = data_student["full_name"]
student_skill = ', '.join(data_student['skills'])
desired_skills = ', '.join(data_student['learns'])


print("Студент:", student_name)
print("Знает:", student_skill)
print("Хочет изучить: ", desired_skills)


user_input_student_title = input(f"Выберите специальность для оценки студента: {student_name} -> ").title()
title = user_input_student_title
data_professions = get_profession_by_title(title)


student = set(data_student["skills"])
profession = set(data_professions["skills"])


check_fitness(student, profession)

