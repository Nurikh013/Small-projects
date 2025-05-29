def calculator():
    print("Simple Calculator")
    print("Operations: +, -, *, /")
    
    num1 = float(input("Enter first number: "))
    op = input("Enter operation: ")
    num2 = float(input("Enter second number: "))
    
    if op == '+':
        print(f"Result: {num1 + num2}")
    elif op == '-':
        print(f"Result: {num1 - num2}")
    elif op == '*':
        print(f"Result: {num1 * num2}")
    elif op == '/':
        if num2 == 0:
            print("Error: Cannot divide by zero!")
        else:
            print(f"Result: {num1 / num2}")
    else:
        print("Invalid operation!")


calculator