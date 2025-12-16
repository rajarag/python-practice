balance = 10000 

while True:
    print("\n--- ATM MENU ---")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("Your balance is: ₹", balance)

    elif choice == "2":
        amount = float(input("Enter deposit amount: ₹"))
        if amount > 0:
            balance += amount
            print("Deposit successful!")
        else:
            print("Invalid amount")

    elif choice == "3":
        amount = float(input("Enter withdrawal amount: ₹"))
        if amount > balance:
            print("Insufficient balance")
        elif amount <= 0:
            print("Invalid amount")
        else:
            balance -= amount
            print("Please collect your cash")

    elif choice == "4":
        print("Thank you for using the ATM!")
        break

    else:
        print("Invalid choice, try again")