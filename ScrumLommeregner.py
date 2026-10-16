# Lav en liste af operationer
def addition(x, y):
    return x + y

def subtraction(x, y):
    return x - y

def multiplication(x, y):
    return x * y

def division(x, y):
    if y == 0:
        return "Error: Division by zero is not allowed."
    else:
        return x / y

def pythagoras(a, b):
    return (a ** 2 + b ** 2) ** 0.5

def average(args):
    return sum(args) / len(args)

while True:
    print("\n\n[1] Basic calculator\n[2] Advanced calculator\n[3] Exit?\n\n")
    mode = input("Choose option: ")
    if mode == "1":
        print("Hello User! I am a basic calculator. I can perform the following operations:")
        print("[1] Addition")
        print("[2] Subtraction")
        print("[3] Multiplication")
        print("[4] Division")

        operation = input("\nPlease select an operation by entering the corresponding number (1-6): ")
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        if operation == "1":
            result = addition(num1, num2)
            print(f"The result of {num1} + {num2} is: {result}")
        elif operation == "2":
            result = subtraction(num1, num2)
            print(f"The result of {num1} - {num2} is: {result}")
        elif operation == "3":
            result = multiplication(num1, num2)
            print(f"The result of {num1} * {num2} is: {result}")
        elif operation == "4":
            result = division(num1, num2)
            print(f"The result of {num1} / {num2} is: {result}")
        elif operation == "5":
            a = float(input("Enter the value for side a: "))
            b = float(input("Enter the value for side b: "))
            result = pythagoras(a, b)
            print(f"The result of Pythagoras with sides {a} and {b} is: {result}")
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")
    if mode == "2":
        print("Hello User! I am an advanced calculator. I can perform the following operations:")
        print("[1] Pythagoras")
        print("[2] Custom calculator")
        print("[3] Average")
        operation = input("\nPlease select an operation by entering the corresponding number (1-6): ")
        if operation == "1":
            a = float(input("Enter the value for side a: "))
            b = float(input("Enter the value for side b: "))
            result = pythagoras(a, b)
            print(f"The result of Pythagoras with sides {a} and {b} is: {result}")
        elif operation == "2":
            result = input("Enter your custom mathematical expression: ")
            calc = eval(result)
            print(f"{result} = {calc}")
        elif operation == "3":
            print("Type each number you want, followed by ENTER to find the average number")
            print("Type c to calculate the average")
            numbers = []
            while True:
                userinput = input("Please enter a number or c to calculate the average: ")
                if userinput == "c":
                    if len(numbers) == 0:
                        print("You haven't entered any numbers yet.")
                    else:
                        average = sum(numbers) / len(numbers)
                        print(f"The average of {numbers} is: {average}")
                        break
                else:
                    try:
                        numbers.append(float(userinput))
                        print(numbers)
                    except ValueError:
                        print("Invalid input. Please enter a number or c to calculate the average")