# Calculator Using Python

def addition(a,b):
    result=a+b
    print(result)

def substraction(a,b):
    result=a-b
    print(result)

def multipication(a,b):
    result=a*b
    print(result)

def division(a,b):
    result=a/b
    print(result)


a=int(input("Enter a number: "))
b=int(input("Enter a number: "))
op=(input("Enter a Operator: "))

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

