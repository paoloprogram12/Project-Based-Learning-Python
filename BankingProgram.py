# shows balance of user
def showBalance(balance):
    print(f"Your balance is ${balance:.2f}") # .2f adds a decimal and 2 numbers after decimal

# deposit money
def deposit():
    amount = float(input("Enter amount to be deposited: "))

    if amount < 0:
        print("Not valid.")
        return 0
    else:
        return amount

# withdraw money
def withdraw(balance):
    amount = float(input("Enter amount to withdraw: "))

    if amount > balance:
        print("Insufficient funds")
        return 0
    elif amount < 0:
        print("Amount must be greater than 0.")
        return 0
    else:
        return amount

def main():
    balance = 0
    isRunning = True

    while isRunning:
        print("Banking Program")
        print("1. Show Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            showBalance(balance)
        elif choice == "2":
            balance += deposit()
        elif choice == "3":
            balance -= withdraw(balance)
        elif choice == "4":
            isRunning = False
        else:
            print("Not valid, please try again.")

    print("Thank you, come again!")

if __name__ == "__main__":
    main()