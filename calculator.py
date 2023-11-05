def add(x,y):
    return x+y
def substract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    if y==0:
        return("Error! Division by 0 not possible")
    return x/y
try:
    num1=float(input("Enter the first number\t:"))
    num2=float(input("Enter the second number\t:"))
    operation=(input("Enter Operation(+,-,*,/):\t"))
    if operation == '+':
        result=add(num1,num2)
    elif operation == '-':
        result=substract(num1,num2)
    elif operation == '*':
        result=multiply(num1,num2)
    elif operation == '/':
        result=divide(num1,num2)
    else:
        result="Invalid operation entered"
    print("Result:",result)
except ValueError:
    print("Invalid input. Please enter valid numbers")
except Exception as e:
    print("An error occured:",str(e))