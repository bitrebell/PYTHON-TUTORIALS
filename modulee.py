import math
import random
random_number = random.randint(0, 24)
# print(random_number)
rand = random.random() *100
# print(rand)
list = ["Star plus", "DD1", "Aaj Tak", "CodeWithHarry"]
maje = random.choice(list)
print(maje)

                # F string

me = str(input("type your name\n"))
b = int(input("type the number\n"))
# a = "this is %s %s"[me, b]
# a = "this is your {1} {0}"
# c = a.format(me, b)
#print(c)
a = f"this is {me} {b} {math.cos(65)}"
print(a)
