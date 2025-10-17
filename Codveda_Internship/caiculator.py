"""
Description:
This program defines a basic calculator that performs addition,
subtraction, multiplication, and division.

It uses a class-based (OOP) approach to organize arithmetic
operations as methods of a Calculator class.

Program Flow:
1. Welcomes the user.
2. Repeats calculations using a while loop.
3. Prompts for the first number, operator, and second number.
4. Performs the calculation and displays the result.
5. Allows the user to exit the program by typing 'exit'.
6. Handles invalid inputs and division by zero gracefully.
"""

# Define the Calculator class
class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return self.num1 + self.num2

    def subtract(self):
        return self.num1 - self.num2

    def multiply(self):
        return self.num1 * self.num2

    def divide(self):
        if self.num2 == 0:
            return "Error: Division by zero is not allowed."
        return self.num1 / self.num2


# --- Main program execution ---
print("Welcome to the Simple Calculator")
print("---------------------------------")

while True:
    try:
        num1 = input("\nEnter first number (or type 'exit' to quit): ")
        if num1.lower() == 'exit':
            print("Exiting the calculator. Goodbye.")
            break
        num1 = float(num1)

        operator = input("Enter operator (+, -, *, /): ")
        if operator.lower() == 'exit':
            print("Exiting the calculator. Goodbye.")
            break

        num2 = input("Enter second number (or type 'exit' to quit): ")
        if num2.lower() == 'exit':
            print("Exiting the calculator. Goodbye.")
            break
        num2 = float(num2)

        calc = Calculator(num1, num2)

        if operator == '+':
            print(f"Result: {calc.add()}")
        elif operator == '-':
            print(f"Result: {calc.subtract()}")
        elif operator == '*':
            print(f"Result: {calc.multiply()}")
        elif operator == '/':
            print(f"Result: {calc.divide()}")
        else:
            print("Invalid operator entered.")

    except ValueError:
        print("Error: Please enter valid numbers only.")
