# Python-Assignment
try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    op = input("Enter operation (+, -, *, /): ")

    if op == '+':
        print("Result:", num1 + num2)
    elif op == '-':
        print("Result:", num1 - num2)
    elif op == '*':
        print("Result:", num1 * num2)
    elif op == '/':
        if num2 == 0:
            print("Error: Division by zero!")
        else:
            print("Result:", num1 / num2)
    else:
        print("Invalid operation!")

except ValueError:
    print("Invalid number input!")
