print("Welcome to Chase bank.")
print("Have a nice day!")

def bank_transactions():
    balance = int(input("Your current balance is "))
    done = "n"
    while done == "n":
        action = input("What would you like to do? (deposit, withdraw, check balance) ")
        if action == "check balance":
            print(f"Your current balance is {balance}")
            done = input("Are you done? (y/n) ")
        elif action == "deposit":
            deposit = int(input("How much would you like to deposit? "))
            balance += deposit
            print(f"Your current balance is {balance}")
            done = input("Are you done? (y/n) ")
        elif action == "withdraw":
            withdraw = int(input("How much would you like to withdraw? "))
            balance -= withdraw
            print(f"Your current balance is {balance}")
            done = input("Are you done? (y/n) ")
        else:
            action = input("What would you like to do? (deposit, withdraw, check balance) ")
    print("Thank you!")

bank_transactions()