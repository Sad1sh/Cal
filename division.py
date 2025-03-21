try:
    num1 = float(input("Enter numerator: "))
    num2 = float(input("Enter denominator: "))
    
    result = num1 / num2
    print(f"Result: {result}")
    
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except ValueError:
    print("Error: Please enter valid numerical values.")
