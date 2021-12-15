class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.average_rating = 0

    def lecture_rate(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += grade
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'
        sum = 0
        len = 0
        for key in lecturer.grades.keys():
            for grad in list(lecturer.grades[key]):
                sum = sum + grad
                len += 1
        lecturer.average_grade = round(sum / len, 2)

    def __lt__(self, other):
        if not isinstance(other, Student):
            print("Нельзя сравнить")
            return
        return self.average_rating < other.average_rating

    def __str__(self):
        res = f"Имя: {self.name}\n" \
              f"Фамилия: {self.surname}\n" \
              f"Средняя оценка за домашние задания: {self.average_rating}\n" \
              f"Курсы в процессе изучения: {self.courses_in_progress}\n" \
              f"Завершенные курсы: {self.finished_courses}"
        return res


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super(Lecturer, self).__init__(name, surname)
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.grades = {}
        self.average_grade = 0

    def __str__(self):
        res = f'Имя: {self.name.title()}\n' \
              f'Фамилия: {self.surname.title()}\n' \
              f'Средняя оценка за лекции: {(self.average_grade)}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print("Нельзя сравнить")
            return
        return self.average_grade < other.average_grade


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super(Reviewer, self).__init__(name, surname)
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if isinstance(student,
                      Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
        sum = 0
        len = 0
        for key in student.grades.keys():
            for grad in list(student.grades[key]):
                sum = sum + grad
                len += 1
        student.average_rating = round(sum / len, 2)

    def __str__(self):
        res = f'Имя: {self.name.title()}\n' \
              f'Фамилия: {self.surname.title()}'
        return res


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.finished_courses += ['Java script']

new_student = Student('Nally', 'Zwan', 'female')
new_student.courses_in_progress += ['Java']
new_student.finished_courses += ['Git']

first_reviewer = Reviewer('edward', 'norton')
first_reviewer.courses_attached += ['Python']
first_reviewer.courses_attached += ['Java']
first_reviewer.rate_hw(best_student, 'Python', 10)
first_reviewer.rate_hw(best_student, 'Python', 10)
first_reviewer.rate_hw(best_student, 'Python', 10)
first_reviewer.rate_hw(best_student, 'Python', 10)
first_reviewer.rate_hw(new_student, 'Java', 5)
first_reviewer.rate_hw(new_student, 'Java', 9)
first_reviewer.rate_hw(new_student, 'Java', 8)

second_reviewer = Reviewer('John', 'Stump')
second_reviewer.courses_attached += ['Java']
second_reviewer.rate_hw(new_student, 'Java', 9)

first_lecturer = Lecturer('Tim', 'smith')
first_lecturer.courses_attached += ['Java']
first_lecturer.courses_attached += ['Python']

second_lecturer = Lecturer('Liza', 'Simpson')
second_lecturer.courses_attached += ['Java']
second_lecturer.courses_attached += ['Python']

best_student.lecture_rate(first_lecturer, 'Python', 10)

new_student.lecture_rate(first_lecturer, 'Java', 6)
new_student.lecture_rate(second_lecturer, 'Java', 10)
new_student.lecture_rate(second_lecturer, 'Python', 7)

# № 3. Полиморфизм и магические методы
print(first_reviewer.__str__(),'\n')
print(second_reviewer.__str__(),'\n')
print(first_lecturer.__str__(),'\n')
print(second_lecturer.__str__(),'\n')
print(best_student.__str__(),'\n')
print(new_student.__str__(),'\n')
print(first_lecturer.__lt__(second_lecturer))
print(best_student.__lt__(new_student))


# Задание 4.Полевые испытания

student_list = [best_student, new_student]
lecturer_list = [first_lecturer, second_lecturer]


def average_rating_hw(students, courses):
    sum_course_grade = 0
    iterator = 0
    for student in students:
        for key, value in student.grades.items():
            if courses in key:
                sum_course_grade += sum(value) / len(value)
                iterator += 1
    return round(sum_course_grade / iterator, 2)


def average_rating_lesson(lecturers, courses):
    sum_course_grade = 0
    iterator = 0
    for x in lecturers:
        for key, value in x.grades.items():
            if courses in key:
                sum_course_grade += sum(value) / len(value)
                iterator += 1
    return round(sum_course_grade / iterator, 2)


# Подсчет средней оценки за курсы по дз и за лекции:


print(f'Средняя оценка студентов за курс Java: {average_rating_hw(student_list, "Java")}')
print(f'Средняя оценка студентов за курс Python: {average_rating_hw(student_list, "Python")}')
print(f'Средняя оценка лекторов за курс Python: {average_rating_lesson(lecturer_list, "Python")}')
print(f'Средняя оценка лекторов за курс Java: {average_rating_lesson(lecturer_list, "Java")}')

# Сравнение лекторов по средней оценке за лекции и студентов по средней оценке за домашние задания:
print(f"{best_student < new_student}")
print(f"{second_lecturer < first_lecturer}")