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
            if course in first_lecturer.lecturer_grade:
                first_lecturer.lecturer_grade[course] += grade
            else:
                first_lecturer.lecturer_grade[course] = [grade]
        else:
            return 'Ошибка'


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
        self.lecturer_grade = {}

    def __str__(self):
        res = f'Имя: {self.name.title()}\n' \
              f'Фамилия: {self.surname.title()}\n' \
              f'Средняя оценка за лекции: {average_rating_lesson(lecturer_list)}'
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


first_reviewer = Reviewer('edward', 'norton')
second_reviewer = Reviewer('John', 'Stump')

first_lecturer = Lecturer('Tim', 'smith')
second_lecturer = Lecturer('Liza', 'Simpson')

best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
new_student = Student('Nally', 'Zwan', 'female')
new_student.courses_in_progress += ['Java']
new_student.courses_in_progress += ['Git']

first_lecturer.courses_attached += ['Java']
first_lecturer.courses_attached += ['Python']
second_lecturer.courses_attached += ['Java']
second_lecturer.courses_attached += ['Python']


first_reviewer.courses_attached += ['Python']
first_reviewer.courses_attached += ['Java']
second_reviewer.courses_attached += ['Git']

first_reviewer.rate_hw(best_student, 'Python', 10)
first_reviewer.rate_hw(best_student, 'Python', 10)
first_reviewer.rate_hw(best_student, 'Python', 10)
first_reviewer.rate_hw(best_student, 'Python', 10)
first_reviewer.rate_hw(new_student, 'Java', 5)
first_reviewer.rate_hw(new_student, 'Java', 9)
first_reviewer.rate_hw(new_student, 'Git', 8)
second_reviewer.rate_hw(new_student, 'Git', 9)

best_student.lecture_rate(first_lecturer, 'Python', 5)
new_student.lecture_rate(first_lecturer, 'Java', 6)
new_student.lecture_rate(second_lecturer, 'Git', 10)


# print(best_student.grades)
# print(first_reviewer.courses_attached)
# print(first_lecturer.courses_attached)
# print(first_lecturer.lecturer_grade)
# print(first_reviewer.__str__())





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
        for key, value in x.lecturer_grade.items():
            if courses in key:
                sum_course_grade += sum(value) / len(value)
                iterator += 1
    return round(sum_course_grade / iterator, 2)

print(average_rating_lesson(lecturer_list, 'Python'))