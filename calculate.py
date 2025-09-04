def main():
   x = int(input("Please enter the first number: ", ))
   op = input("Please enter the operation you want :")
   y = int(input("Please enter the second number: ", ))
   
   result= operation(x, y , op)
   print("The answer is:", result)

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y
    
def operation(x, y, op):
    if op == '*':
        return multiply(x, y)
    elif op == '/':
        return divide(x, y)
    elif op == '+':
        return add(x, y)
    elif op == '-':
        return subtract(x, y)
    else:
        print("Invalid operation")

main()