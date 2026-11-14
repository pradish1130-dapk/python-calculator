print("===== PYTHON CALCULATOR =====")

while True:
    print("\n1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Exit")

    choice = str(input("Enter your choice: ")).strip()    

    if choice == "5":
        print("Thank you!")
        break

    if choice not in ("1", "2", "3", "4"):
        print("Invalid choice!")
        continue

    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == "1":
            result = num1 + num2
        elif choice == "2":
            result = num1 - num2
        elif choice == "3":
            result = num1 * num2
        else:
            if num2 == 0:
                print("Cannot divide by zero!")
                continue
            result = num1 / num2

        print("Result:", result)

    except ValueError:
        print("Please enter valid numbers!")
