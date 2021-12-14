class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}


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


first_reviewer = Reviewer('Edward', 'Norton')
first_lecturer = Lecturer('Tim', 'Smith')
best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']

cool_mentor = Mentor('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']
first_lecturer.courses_attached += ['Python']
first_reviewer.courses_attached += ['Python']

first_reviewer.rate_hw(best_student, 'Python', 10)
first_reviewer.rate_hw(best_student, 'Python', 10)
first_reviewer.rate_hw(best_student, 'Python', 10)
first_reviewer.rate_hw(best_student, 'Python', 10)
print(best_student.grades)
print(first_reviewer.courses_attached)
print(first_lecturer.courses_attached)
