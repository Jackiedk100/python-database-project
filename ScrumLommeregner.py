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

def discount(a, b):
    return a * (1-b/100)

def vat(a, b):
    return a * (1+b/100)

def percentage(a, b):
    return a * (b/100)

def get_number(prompt):
    while True:
        try:
            number = float(input(prompt))
            return number
        except ValueError:
            print("Invalid input. Please enter a valid number")



while True:
    print("\n\n[1] Basic calculator\n[2] Advanced calculator\n[3] Exit?\n\n")
    mode = input("Choose option: ")
    if mode not in ("1", "2", "3"):
        print("Invalid choice. Please enter a number between 1 and 3.")
    else:
        if mode == "1":
            print("Hello User! I am a basic calculator. I can perform the following operations:")
            print("[1] Addition")
            print("[2] Subtraction")
            print("[3] Multiplication")
            print("[4] Division")

            operation = input("\nPlease select an operation by entering the corresponding number (1-4): ")
            if operation not in ("1", "2", "3", "4"):
                print("Invalid choice. Please enter a number between 1 and 4.")
            else:
                while True:
                    try:
                        num1 = float(input("Enter the first number: "))
                        break
                    except ValueError:
                        print("Invalid input. Please enter a valid number")
                while True:
                    try:
                        num2 = float(input("Enter the second number: "))
                        break
                    except ValueError:
                        print("Invalid input. Please enter a valid number")
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

        if mode == "2":
            print("Hello User! I am an advanced calculator. I can perform the following operations:")
            print("[1] Pythagoras")
            print("[2] Average")
            print("[3] Discount")
            print("[4] VAT")
            print("[5] Percentage of a number")
            print("[6] Percentage increase/decrease of two numbers")
            operation = input("\nPlease select an operation by entering the corresponding number (1-6): ")
            if operation not in ("1", "2", "3", "4", "5", "6"):
                print("Invalid choice. Please enter a number between 1 and 6.")
            else:
                if operation == "1":
                    a = get_number("Enter the value for side a: ")
                    b = get_number("Enter the value for side b: ")
                    result = pythagoras(a, b)
                    print(f"The result of Pythagoras with sides {a} and {b} is: {result}")

                elif operation == "2":
                    print("Type each number you want, followed by ENTER to find the average number")
                    print("Type c to calculate the average")
                    numbers = []
                    while True:
                        userinput = input("Please enter a number or c to calculate the average: ")
                        if userinput == "c":
                            if len(numbers) == 0:
                                print("You haven't entered any numbers yet.")
                            else:
                                result = average(numbers)
                                print(f"The average of {numbers} is: {result}")
                                break
                        else:
                            try:
                                numbers.append(float(userinput))
                                print(numbers)
                            except ValueError:
                                print("Invalid input. Please enter a number or c to calculate the average")

                elif operation == "3":
                    a = get_number("Enter price of the merchandise: ")
                    b = get_number("Enter discount percentage: ")
                    result = discount(a, b)
                    print(f"The result of merchandise costing: {a} and a discount of {b}% it will cost: {result}")

                elif operation == "4":
                    a = get_number("Enter price of the merchandise: ")
                    b = get_number("Enter VAT percentage: ")
                    result = vat(a, b)
                    print(f"The result of merchandise costing: {a} and VAT of {b}% the total cost is: {result}")
                    
                elif operation == "5":
                    a = get_number("Enter the number you wish to find a percentage of: ")
                    b = get_number("Enter the percentage you wish to find: ")
                    result = percentage(a, b)
                    print(f"{b}% of {a} is {result}")
                elif operation == "6":
                    a = get_number("Enter the original number: ")
                    b = get_number("Enter the new number: ")
                    if a == 0:
                        print("Error: The original number cannot be zero for percentage increase/decrease calculation.")
                    else:
                        percentage_change = ((b - a) / a) * 100
                        print(f"The percentage change from {a} to {b} is: {percentage_change}%")
        if mode == "3":
            break

