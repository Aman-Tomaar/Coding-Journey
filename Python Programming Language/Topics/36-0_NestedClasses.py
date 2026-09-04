# Nested class = A class defined within another class
#        class Outer:
#            class Inner:
#
# Benefits: Allows you to logically group classes that are closely related
#           Encapsulates private details that aren't relevant outside of the outer class
#           Keeps the namespace clean; reduces the possibility of naming conflicts
class Company:
    class Employee:
        def __init__(self, name, position):
            self.name = name
            self.position = position

        def get_details(self):
            return f"Employee Name: {self.name}, Position: {self.position}"

    def __init__(self, c_name):
        self.c_name = c_name
        self.employee = []

    def add_employee(self, name, position):
        add_employee = self.Employee(name, position)
        self.employee.append(add_employee)

    def employees_list(self):
        return [employee.get_details() for employee in self.employee]


company = Company("Harley Devidson")
print(company.c_name)

company.add_employee("William S. Harley", "Founder")
company.add_employee("Artie Starrs", "CEO")

for x in company.employees_list():
    print(x)
