class Student:
    number_of_students = 0
    school = 'Online School'

    def __init__(self, first_name, last_name, major):
        self.first_name = first_name
        self.last_name = last_name
        self.major = major

        Student.number_of_students += 1

    def fullname_with_major(self):
        return f'{self.first_name} {self.last_name} is a {self.major} major!'

    def fullname_major_school(self):
        return f'{self.first_name} {self.last_name} is a {self.major} major going to {self.school}'

    @classmethod
    def set_online_school(cls, new_school):
        cls.school = new_school

    @classmethod
    def split_students(cls, student_str):
        first_name, last_name, major = student_str.split('.')
        return cls(first_name, last_name, major)


student_1 = Student('Eric', 'Roby', 'Computer Science')
student_2 = Student('John', 'Miller', 'Math')
new_student = 'Adil.Yutzy.English'
student_3 = Student.split_students(new_student)
print(student_3.fullname_major_school())
