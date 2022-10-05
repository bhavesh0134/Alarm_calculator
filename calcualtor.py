'''this
is
a
calculator'''

def operationx(operator,first,second):
    if operator == "+":
        print(first + second)
    elif operator == "-":
        print(first - second)
    elif operator == "*":
        print(first * second)
    elif operator == "%":
        print(first % second)
    else:
        print("Invalid Input")


first_1=int(input("Enter first number:"))
second_2=int(input("Enter second number:"))
first_3=int(input("Enter first number:"))
second_5=int(input("Enter second number:"))
print("---Enter key to insert operator(+,-,*,%)------")
operatorx=input("Enter any operator:")
operationx(operatorx,first_1,second_2)
operationx(operatorx,first_3,second_5)






