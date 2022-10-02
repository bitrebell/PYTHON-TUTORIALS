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

    def __init__(self, aname, asallery, arole):
        self.name = aname
        self.salary = asallery
        self.role = arole

    def printdetails(self):
        return f"Name is {self.name}. Salaary is {self.salary} and role is {self.role}"

harry = Employee("Harry john", 6754, "Instructor" )
aadil = Employee("aadil shiekh", 6578, "CEO")

# n1 = input("enter employee name\n")

# harry.name = "Harry john"
# harry.salary = "6754"
# harry.role = "Instructor"
#
# aadil.name = "Aadil shiekh"
# aadil.salary = "7873"
# aadil.role = "CEO"

print(aadil.printdetails())

