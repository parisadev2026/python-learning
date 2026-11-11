print("Welcome to My Calculator!")

while True:
    first = input("Enter first number (or exit): ")

    if first.lower() == "exit":
        print("Goodbye!")
        break

    try:
        num1 = float(first)
    except ValueError:
        print("Please enter a valid number!")
        continue

    operator = input("Choose (+, -, *, /): ")

    try:
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Please enter a valid number!")
        continue

    if operator == "+":
        print("Result:", num1 + num2)

    elif operator == "-":
        print("Result:", num1 - num2)

    elif operator == "*":
        print("Result:", num1 * num2)

    elif operator == "/":
        if num2 != 0:
            print("Result:", num1 / num2)
        else:
            print("Cannot divide by zero!")

    else:
        print("Invalid operator!")
