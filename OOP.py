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


first_reviewer = Reviewer('edward', 'norton')
first_lecturer = Lecturer('Tim', 'smith')
best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
new_student = Student('Nally', 'Zwan', 'female')
new_student.courses_in_progress += ['Java']

# cool_mentor = Mentor('Some', 'Buddy')
# cool_mentor.courses_attached += ['Python']

first_lecturer.courses_attached += ['Java']
first_lecturer.courses_attached += ['Python']
first_reviewer.courses_attached += ['Python']
first_reviewer.courses_attached += ['Java']

first_reviewer.rate_hw(best_student, 'Python', 10)
first_reviewer.rate_hw(best_student, 'Python', 10)
first_reviewer.rate_hw(best_student, 'Python', 10)
first_reviewer.rate_hw(best_student, 'Python', 10)
first_reviewer.rate_hw(new_student, 'Java', 5)
first_reviewer.rate_hw(new_student, 'Java', 9)

best_student.lecture_rate(first_lecturer, 'Python', 5)
new_student.lecture_rate(first_lecturer, 'Java', 6)

print(best_student.grades)
print(first_reviewer.courses_attached)
print(first_lecturer.courses_attached)
print(first_lecturer.lecturer_grade)