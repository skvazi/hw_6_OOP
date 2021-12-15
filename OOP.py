class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

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

    def average_grade(self):
        for key in self.lecturer_grade.keys():
            return key


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super(Reviewer, self).__init__(name, surname)
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name.title()}\n' \
              f'Фамилия: {self.surname.title()}'
        return res


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.finished_courses += ['Java script']

new_student = Student('Nally', 'Zwan', 'female')
new_student.courses_in_progress += ['Java']
new_student.courses_in_progress += ['Git']
new_student.finished_courses += ['Java script']

first_reviewer = Reviewer('edward', 'norton')
first_reviewer.courses_attached += ['Python']
first_reviewer.courses_attached += ['Java']
first_reviewer.rate_hw(best_student, 'Python', 10)
first_reviewer.rate_hw(best_student, 'Python', 10)
first_reviewer.rate_hw(best_student, 'Python', 10)
first_reviewer.rate_hw(best_student, 'Python', 10)
first_reviewer.rate_hw(new_student, 'Java', 5)
first_reviewer.rate_hw(new_student, 'Java', 9)
first_reviewer.rate_hw(new_student, 'Git', 8)

second_reviewer = Reviewer('John', 'Stump')
second_reviewer.courses_attached += ['Git']
second_reviewer.rate_hw(new_student, 'Git', 9)

first_lecturer = Lecturer('Tim', 'smith')
first_lecturer.courses_attached += ['Java']
first_lecturer.courses_attached += ['Python']

second_lecturer = Lecturer('Liza', 'Simpson')
second_lecturer.courses_attached += ['Git']
second_lecturer.courses_attached += ['Python']

best_student.lecture_rate(first_lecturer, 'Python', 10)

new_student.lecture_rate(first_lecturer, 'Java', 6)
new_student.lecture_rate(second_lecturer, 'Git', 10)
new_student.lecture_rate(second_lecturer, 'Python', 7)


# print(best_student.grades)
# print(first_reviewer.courses_attached)
# print(first_lecturer.courses_attached)
# print(first_lecturer.lecturer_grade)

# № 3. Полиморфизм и магические методы

# print(first_reviewer.__str__(),'\n')
# print(second_reviewer.__str__())
# print(first_lecturer.__str__())


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

# print(average_rating_lesson(lecturer_list, 'Python'))
# print(average_rating_hw(student_list, 'Java'))
# print(average_rating_hw(student_list, 'Git'))

# print(second_lecturer.__str__())

# Подсчет средней оценки за курсы по дз и за леции:
# print(f'Средняя оценка студентов за курс GIT: {average_rating_hw(student_list, "GIT")}')
# print(f'Средняя оценка студентов за курс Python: {average_rating_hw(student_list, "Python")}')
# print(f'Средняя оценка лекторов за курс Python: {average_rating_lesson(lecturer_list, "Python")}')
print(f'Средняя оценка лекторов за курс GIT: {average_rating_lesson(lecturer_list, "GIT")}')