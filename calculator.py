#  calculator
# this is a calculator project
num1 = eval (input("enter first num"))
num2 = eval (input("enter second num"))

operator = input("enter operator: ")

def add(num1, num2):
    result= num1+ num2
    print( result)

def subtract(num1, num2):
    result= num1- num2
    print(result)
    
def divide(num1, num2):
    result=num1/ num2
    print(result)

def multiply(num1, num2):
    result=num1 * num2
    print(result)
if operator =="+":
     add (num1, num2)
elif operator =="-":
          subtract(num1, num2)
elif operator =="/":
         divide(num1, num2)
elif operator =="X" or operator:
         multiply(num1, num2)
