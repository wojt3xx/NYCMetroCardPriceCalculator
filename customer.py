import metro_card


class Customer:
    money = 30
    pin_code = 1234

    def __init__(self):
        self.ticket_amount = None

    def card_login():
        enter_pin = input("Please enter your PIN code to proceed: ")
        if int(enter_pin) == Customer.pin_code:
            print("PIN correct. Proceeding with payment..")
        else:
            print("Incorrect PIN!")
            exit()


    def purchase_tickets():
        total_payment = 0
        ticket_amount = input("How many tickets you want to buy?: ")
        ticket_location = input("To what location you want to go?: ")
        payment_method = input("Will you pay by card or cash?(card/cash): ")
        lower_tickets = ticket_location.lower()
        lower_payment = payment_method.lower()
        metro_card.MetroCard.locations.items()

        # check the location
        if lower_tickets == 'london':

            # check if user is buying with card
            if lower_payment == 'card':
                Customer.card_login()
                ticket_fee = metro_card.MetroCard.card_fee + metro_card.MetroCard.locations.get(ticket_location)
                total_payment = ticket_fee * int(ticket_amount)

                # check if user has enough funds
                if total_payment > Customer.money:
                    amount_missing = Customer.money - total_payment
                    print(f"You don't have enough money to buy {ticket_amount}. You are missing £{abs(amount_missing)}")
                    customer_choice = input("Do you want to try again?(yes/no): ")
                    lower_choice = customer_choice.lower()

                    # check customer choice if he wants to continue or not
                    if lower_choice == 'yes':
                        Customer.purchase_tickets()
                    else:
                        print("Goodbye and hope to see you again soon!")
                        exit()
                else:
                    metro_card.MetroCard.tickets_available -= int(ticket_amount)
                    total_payment = metro_card.MetroCard.card_fee + metro_card.MetroCard.locations.get(
                        ticket_location) * int(ticket_amount)
                    money_left = Customer.money - total_payment
                    print(
                        f"You have bought {ticket_amount} tickets to {ticket_location.capitalize()}. Total payment is £{total_payment}. You have total of £{money_left} left.")
            elif lower_payment == 'cash':
                ticket_fee = metro_card.MetroCard.locations.get(ticket_location)
                total_payment = ticket_fee * int(ticket_amount)

                # check if user has enough funds
                if total_payment > Customer.money:
                    amount_missing = Customer.money - total_payment
                    print(f"You don't have enough money to buy {ticket_amount}. You are missing £{abs(amount_missing)}")
                    customer_choice = input("Do you want to try again?(yes/no): ")
                    lower_choice = customer_choice.lower()

                    # check customer choice if he wants to continue or not
                    if lower_choice == 'yes':
                        Customer.purchase_tickets()
                    else:
                        print("Goodbye and hope to see you again soon!")
                        exit()
                else:
                    metro_card.MetroCard.tickets_available -= int(ticket_amount)
                    total_payment = metro_card.MetroCard.card_fee + metro_card.MetroCard.locations.get(
                        ticket_location) * int(ticket_amount)
                    money_left = Customer.money - total_payment
                    print(
                        f"You have bought {ticket_amount} tickets to {ticket_location.capitalize()}. Total payment is £{total_payment}. You have total of £{money_left} left.")
            else:
                print("Wrong input! Please, try again!")
                exit()

        elif lower_tickets == 'peterborough':

            # check if user is buying with card
            if lower_payment == 'card':
                Customer.card_login()
                ticket_fee = metro_card.MetroCard.card_fee + metro_card.MetroCard.locations.get(ticket_location)
                total_payment = ticket_fee * int(ticket_amount)

                # check if user has enough funds
                if total_payment > Customer.money:
                    amount_missing = Customer.money - total_payment
                    print(f"You don't have enough money to buy {ticket_amount}. You are missing £{abs(amount_missing)}")
                    customer_choice = input("Do you want to try again?(yes/no): ")
                    lower_choice = customer_choice.lower()

                    # check customer choice if he wants to continue or not
                    if lower_choice == 'yes':
                        Customer.purchase_tickets()
                    else:
                        print("Goodbye and hope to see you again soon!")
                        exit()
                else:
                    metro_card.MetroCard.tickets_available -= int(ticket_amount)
                    total_payment = metro_card.MetroCard.card_fee + metro_card.MetroCard.locations.get(
                        ticket_location) * int(ticket_amount)
                    money_left = Customer.money - total_payment
                    print(
                        f"You have bought {ticket_amount} tickets to {ticket_location.capitalize()}. Total payment is £{total_payment}. You have total of £{money_left} left.")
            elif lower_payment == 'cash':
                ticket_fee = metro_card.MetroCard.locations.get(ticket_location)
                total_payment = ticket_fee * int(ticket_amount)

                # check if user has enough funds
                if total_payment > Customer.money:
                    amount_missing = Customer.money - total_payment
                    print(f"You don't have enough money to buy {ticket_amount}. You are missing £{abs(amount_missing)}")
                    customer_choice = input("Do you want to try again?(yes/no): ")
                    lower_choice = customer_choice.lower()

                    # check customer choice if he wants to continue or not
                    if lower_choice == 'yes':
                        Customer.purchase_tickets()
                    else:
                        print("Goodbye and hope to see you again soon!")
                        exit()
                else:
                    metro_card.MetroCard.tickets_available -= int(ticket_amount)
                    total_payment = metro_card.MetroCard.card_fee + metro_card.MetroCard.locations.get(
                        ticket_location) * int(ticket_amount)
                    money_left = Customer.money - total_payment
                    print(
                        f"You have bought {ticket_amount} tickets to {ticket_location.capitalize()}. Total payment is £{total_payment}. You have total of £{money_left} left.")
            else:
                print("Wrong input! Please, try again!")
                exit()

        elif lower_tickets == 'manchester':

            # check if user is buying with card
            if lower_payment == 'card':
                Customer.card_login()
                ticket_fee = metro_card.MetroCard.card_fee + metro_card.MetroCard.locations.get(ticket_location)
                total_payment = ticket_fee * int(ticket_amount)

                # check if user has enough funds
                if total_payment > Customer.money:
                    amount_missing = Customer.money - total_payment
                    print(f"You don't have enough money to buy {ticket_amount}. You are missing £{abs(amount_missing)}")
                    customer_choice = input("Do you want to try again?(yes/no): ")
                    lower_choice = customer_choice.lower()

                    # check customer choice if he wants to continue or not
                    if lower_choice == 'yes':
                        Customer.purchase_tickets()
                    else:
                        print("Goodbye and hope to see you again soon!")
                        exit()
                else:
                    metro_card.MetroCard.tickets_available -= int(ticket_amount)
                    total_payment = metro_card.MetroCard.card_fee + metro_card.MetroCard.locations.get(
                        ticket_location) * int(ticket_amount)
                    money_left = Customer.money - total_payment
                    print(
                        f"You have bought {ticket_amount} tickets to {ticket_location.capitalize()}. Total payment is £{total_payment}. You have total of £{money_left} left.")
            elif lower_payment == 'cash':
                ticket_fee = metro_card.MetroCard.locations.get(ticket_location)
                total_payment = ticket_fee * int(ticket_amount)

                # check if user has enough funds
                if total_payment > Customer.money:
                    amount_missing = Customer.money - total_payment
                    print(f"You don't have enough money to buy {ticket_amount}. You are missing £{abs(amount_missing)}")
                    customer_choice = input("Do you want to try again?(yes/no): ")
                    lower_choice = customer_choice.lower()

                    # check customer choice if he wants to continue or not
                    if lower_choice == 'yes':
                        Customer.purchase_tickets()
                    else:
                        print("Goodbye and hope to see you again soon!")
                        exit()
                else:
                    metro_card.MetroCard.tickets_available -= int(ticket_amount)
                    total_payment = metro_card.MetroCard.card_fee + metro_card.MetroCard.locations.get(
                        ticket_location) * int(ticket_amount)
                    money_left = Customer.money - total_payment
                    print(
                        f"You have bought {ticket_amount} tickets to {ticket_location.capitalize()}. Total payment is £{total_payment}. You have total of £{money_left} left.")
            else:
                print("Wrong input! Please, try again!")
                exit()

        # exits if answer equals False
        else:
            print("Wrong location, please try again!")
            exit()
