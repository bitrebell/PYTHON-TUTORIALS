print("choose your operator +, -, *, /")
n1 = input()
print("enter the both value with an enter")
n2 = int(input())
n3 = int(input())

if n1 == "*" and n2 == 45 and n3== 3:
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
