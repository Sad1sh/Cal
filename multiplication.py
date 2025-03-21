try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    print("Result:", num1 * num2)
except ValueError:
    print("Error: Enter valid numbers.")
