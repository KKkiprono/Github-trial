def deposit():
    balance = 1000

    amount = float(input("Enter deposit amount: "))

    if amount > 0:
        balance += amount
        print(f"Deposit successful!")
        print(f"New balance: KES {balance}")
    else:
        print("Invalid deposit amount")


deposit()