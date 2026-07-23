def calculate(num1, num2, operation):
    if operation == "+":
        print("Addition:", num1 + num2)

    elif operation == "-":
        print("Subtraction:", num1 - num2)

    elif operation == "*":
        print("Multiplication:", num1 * num2)

    elif operation == "/":
        if num2 != 0:
            print("Division:", num1 / num2)
        else:
            print("Error: Division by zero is not allowed.")

    else:
        print("Invalid operation!")

# Function calls using keyword arguments
calculate(num1=10, num2=5, operation="+")
calculate(operation="-", num2=4, num1=20)
calculate(num2=6, operation="*", num1=7)
calculate(operation="/", num1=15, num2=3)