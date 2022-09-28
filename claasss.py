# class student:
#     pass
#
# harry = student()
# larry = student()
#
# harry.name = "HARRY"
# harry.std = 12
# harry.section = 1
# larry.std = 10
# larry.subjects = ["physics", "cemistry"]
# print(harry.section, larry.subjects)


class Employee:
    no_of_leaves = 8

    def __init__(self):
        self.role = None
        self.salary = None
        self.name = None

    def printdetails(self):
        return f"Name is {self.name}. Salaary is {self.salary} and role is {self.role}"

harry = Employee()
aadil = Employee()

# n1 = input("enter employee name\n")

harry.name = "Harry john"
harry.salary = "6754"
harry.role = "Instructor"

aadil.name = "Aadil shiekh"
aadil.salary = "7873"
aadil.role = "CEO"

print(aadil.printdetails())

