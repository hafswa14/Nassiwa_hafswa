while True:
    try:
        x = int(input("Enter the first number: "))
        y = int(input("Enter the second number: "))
        result = x / y  
    except ValueError:
        print("Invalid input,please enter whole numbers only.")
    except ZeroDivisionError:
        print("Cannot divide by zero, please enter a non-zero second number.")
    else:
        print("Result:", result)
        break