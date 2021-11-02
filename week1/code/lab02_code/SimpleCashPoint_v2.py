
def cashpoint(truepin, balance):
    # print("   <CASHPOINT FUNCTION: not yet defined>")
    print("Welcome to the ATM.")
    pin = input("Please enter your pin number: ")
    print()

    if pin != truepin:
        print("Sorry, you pin code is wrong.")
        return "PIN-error"
        exit()

    menu = """
    1. Balance request.
    2. Withdrawal request.
    3. Mobile top-up.

    """

    choice = int(input("Please enter a number to proceed:\n" + menu))

    if choice == 1:
        print("Your current balance is: ", balance)
        print()
        return "balance-request"
    elif choice == 2:
        amount = float(input("Please enter the amount you want to withdraw: "))
        if amount <= balance:
            balance -= amount
            print("Withdraw successfully.\nNow your balance is", balance)
            return ("withdrawal-request", amount)
        else:
            print("Sorry, you are not that rich.")
            exit(0)
    elif choice == 3:
        print("Sorry, mobile service is currently unavailable.")
        return "mobile-service"

