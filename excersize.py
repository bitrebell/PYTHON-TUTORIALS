         #FAULTY CALCULATOR

print("choose your operator +, -, *, /")
n1 = input()
print("enter the both value with an enter")
n2 = int(input())
n3 = int(input())
if n1 == "*" and n2 == 45 and n3 == 3:
    print("555")
elif n1 == "+" and n2 == 56 and n3 == 9:
    print("77")
elif n1 == "/" and n2 == 56 and n3 == 6:
    print(4)
elif n1 == "+":
    plus = n2+n3
    print(plus)
elif n1 == "-":
    minus = n2-n3
elif n1 == "*":
    multiply = n2*n3
    print(multiply)
elif n1 == "/":
    divide = n2+n3
    print(divide)
else:
    print(n1, "NOT ACCEPTABLE")

n = 18
number_of_guess=1
print("Number of guesses is limited to only 9 times")
while (number_of_guess <= 9):
    guess_number=int(input("guess the number."))
    print(9 - number_of_guess, "no. of guess left")
    if guess_number<18:
        print("you enter a less number please input greater number.")
    elif guess_number > 18:
        print("you enter a greater number please take some smaller number")
    else:
        print("you win congratulation!!!")
        print(number_of_guess, "no. of guess you took to finish")
        break
    print(9-number_of_guess, "no. of guess left")
    number_of_guess = number_of_guess + 1

                     # USER BUILT FUNCTION
# a = 9
# b = 8
# c = sum(a, b)
# print(c)
#
"""def function1(a, b):
     print("hello you are in my world", a+b)

function1(5, 7)"""
#
# def function2(a, b):
#      """This is function which help to average of two numbers"""
#      average = (a+b)/2
#      print("this is my average", average)
#      return average
# function2(7, 5)
# v = function2(6,8)
# print(v)
# print(function2.__doc__)





                    # SNAKE WATER GAME


import random
print("           ****SNAKE WATER GAME*****")
lst = ["s", "w", "g"]

chance = 10
no_of_chance = 0
computer_point = 0
human_point = 0

print("s for snake \nw for water \ng for gun \n")

while no_of_chance < chance:
    _input = input("choose your attacker:- ")
    _random = random.choice(lst)

    if _input == _random:
        print("*** better luck next time both you are right!!! ***\n")

    elif _input == "s" and _random == "g":
        computer_point = computer_point + 1
        print(f"your guess is {_input} and computer guess is {_random}\n")
        print("*** sad you gave a point to this duffer computer ***")
        print(f"computer point is {computer_point} and your point is {human_point}\n")

    elif _input == "s" and _random == "w":
        human_point = human_point + 1
        print(f"your guess is {_input} and computer guess is {_random}\n")
        print("*** it's seems good you add 1 point to your score ***")
        print(f"computer point is {computer_point} and your point is {human_point}\n")

    elif _input == "w" and _random =="g":
        human_point = human_point + 1
        print(f"your guess is {_input} and computer guess is {_random}\n")
        print("*** it's seems good you add 1 point to your score ***")
        print(f"computer point is {computer_point} and your point is {human_point}\n")

    elif _input == "w" and _random == "s":
        computer_point = computer_point + 1
        print(f"your guess is {_input} and computer guess is {_random}\n")
        print("*** sad you gave a point to this duffer computer ***")
        print(f"computer point is {computer_point} and your point is {human_point}\n")

    elif _input == "g" and _random == "w":
        computer_point = computer_point + 1
        print(f"your guess is {_input} and computer guess is {_random}\n")
        print("*** sad you gave a point to this duffer computer ***")
        print(f"computer point is {computer_point} and your point is {human_point}\n")

    elif _input == "g" and _random == "s":
        human_point = human_point + 1
        print(f"your guess is {_input} and computer guess is {_random}\n")
        print("*** it's seems good you add 1 point to your score ***")
        print(f"computer point is {computer_point} and your point is {human_point}\n")

    else:
        print("you type wrong input\n")

    no_of_chance = no_of_chance + 1
    print(f"{chance - no_of_chance} is left out of {chance}\n")

print("*** lets make party because the game is over ***")

if computer_point == human_point:
    print("both play nice congrats!!!!")

elif computer_point > human_point:
    print("*** SAD BUT YES YOU LOOSE THE GAME AND COMPUTER IS CLEARLY WINNER ***")

else:
    print("*** YES THAT'S TRUE WIN THE MATCH CONGRATULATION!!!! ***")

print(f"YOUR POINT IS {human_point} and computer point is {computer_point}")