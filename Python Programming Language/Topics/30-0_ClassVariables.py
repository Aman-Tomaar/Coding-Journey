# Class Variables = Shared among all instances of a class
#                   Defined outside of a constructor
#                   Allow you to share data among all objects created from that class


class Student:

    batch = 2024
    num_students = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.num_students += 1  # self is like we replace it as the variable name such as student1, student2 , student3
        # but to access a class veriable we would have to use the name of class


student1 = Student("Strange", 19)
student2 = Student("Lazer", 30)
student3 = Student("Heart", 99)


print(
    f"The total number of Students in the batch {Student.batch} is: {Student.num_students}"
)
print(
    f"Name: {student1.name} \nAge:{student1.age}\n{student1.batch}\n\n"
)  # We can use batch from either one of them student 1, 2 or 3
print(f"Name: {student2.name} \nAge:{student2.age}\n{student2.batch}\n\n")
print(
    f"Name: {student3.name} \nAge:{student3.age}\n{Student.batch}\n\n"
)  # and we can use it from the Class name too and its preffered to use it from class name
