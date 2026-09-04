# Class methods = Allow operations related to the class itself
#                 Take (cls) as the first parameter, which represents the class itself.

# Instance methods = Best for operations on instances of the class (objects)
# Static methods = Best for utility functions that do not need access to class data
# Class methods = Best for class-level data or require access to the class itself


class Student:
    count = 0
    total_gpa = 0

    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        Student.count += 1
        Student.total_gpa += gpa

    def get_info(self):
        return f"{self.name} has {self.gpa} gpa"

    @classmethod
    def count_stu(cls):
        return f"The # of Studnents: {cls.count}"

    @classmethod
    def get_avg_gpa(cls):
        if cls.count == 0:
            return 0
        else:
            return f"The average gpa of the whole class is: {cls.total_gpa / cls.count:.2f}"


student1 = Student("Strange", 9)
student2 = Student("Heart", 7.5)
students = [student1, student2]
print(Student.count_stu())
print(Student.get_avg_gpa())

for student in students:
    print(student.get_info())
