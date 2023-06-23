from fractions import Fraction

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Cannot divide by zero"

def calculate_percentage(number, percentage):
    return (number * percentage) / 100

def convert_to_fraction(number):
    return Fraction(number).limit_denominator()

def main():
    while True:
        print("\nCalculator Menu:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Percentage")
        print("6. Convert to Fraction")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")

        if choice == '7':
            print("Exiting the calculator...")
            break

        if choice in ['1', '2', '3', '4']:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))

            if choice == '1':
                result = add(num1, num2)
                operator = "+"
            elif choice == '2':
                result = subtract(num1, num2)
                operator = "-"
            elif choice == '3':
                result = multiply(num1, num2)
                operator = "*"
            else:
                result = divide(num1, num2)
                operator = "/"

            print(f"{num1} {operator} {num2} = {result}")

        elif choice == '5':
            number = float(input("Enter the number: "))
            percentage = float(input("Enter the percentage: "))
            result = calculate_percentage(number, percentage)
            print(f"{percentage}% of {number} = {result}")

        elif choice == '6':
            number = float(input("Enter the number: "))
            fraction = convert_to_fraction(number)
            print(f"The fraction of {number} = {fraction}")

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
