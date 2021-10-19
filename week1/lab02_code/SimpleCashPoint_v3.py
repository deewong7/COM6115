
def cashpoint(truepin, balance):
    # print("   <CASHPOINT FUNCTION: not yet defined>")
    print("Welcome to the ATM.")
    pin = input("Please enter your pin number: ")
    print()

    check_PIN(pin, truepin)

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
        return withdraw(balance)

    elif choice == 3:
        mobile_top_up()
        return "mobile-service"


def check_PIN(pin, truepin):
    if pin != truepin:
        print("Sorry, you pin code is wrong.")
        return "PIN-error"
        exit()


def withdraw(balance):
    daily_limit = 1000
    amount = float(input("Please enter the amount you want to withdraw: "))
    
    if amount > daily_limit:
        print("Sorry, the amount has exceeded the limit.")
        return ("withdraw-request-rejected-over-1000", amount)

    if amount <= balance:
        balance -= amount
        print("Withdraw successfully.\nNow your balance is", balance)
        return ("withdrawal-request", amount)
    else:
        print("Sorry, you are not that rich.")
        exit(0)

def mobile_top_up():
    print("Sorry, service is currently unavailable.")
    return "mobile-top-up"
    amount = input("Please enter the amount you would like to top up your phone: ")
    pass