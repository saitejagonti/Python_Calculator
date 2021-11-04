# Calculator Using Python

def addition(a,b):
    result=a+b
    print(f'The Addition of {a} and {b} is {result}')

def substraction(a,b):
    result=a-b
    print(f'The Substraction of {a} and {b} is {result}')

def multipication(a,b):
    result=a*b
    print(f'The Multipication of {a} and {b} is {result}')

def division(a,b):
    result=a/b
    print(f'The Division of {a} and {b} is {result}')

n =(input("Please Enter Your Name: "))
print(f'Hi {n}, Select the Numbers and Operator for Calculation')
a=int(input("Enter a First number: "))
b=int(input("Enter a  Second number: "))
op=(input("Now Select the Operator: "))

if op=="+":
    addition(a,b)

elif op=="-":
    substraction(a,b)

elif op=="*":
    multipication(a,b)

elif op=="/":
    division(a,b)

else:
    print("Invalid Operator")

