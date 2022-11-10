from Account import Account
from Card import Card

account_list = []
card_list = []

functions = '''
====================================================
1. Bank statement
2. Deposit
3. Withdraw
4. Terminate Account inquiry
====================================================
'''


class ATM:
    def register_account(self):
        print()
        print("<Please enter the following information to open an account>")
        print("----------------------------------------------------")

        username = input("Username : ")
        account_number = int(input("Bank account number : "))
        account_password = int(input("Bank account password : "))
        balance = int(input("Initial deposit($): "))

        account = Account(username, account_number, account_password, balance)
        account_list.append(account)
        account.get_init_info()

    def register_card(self):
        print()
        print("<Please enter the following information to issue a card>")
        print("----------------------------------------------------")

        card_number = int(input("Card number : "))

        is_valid_account = False
        is_valid_password = False
        while not is_valid_account:
            account_number = int(input("Account number to be linked : "))

            for account in account_list:
                if account.account_number == account_number:
                    while not is_valid_password:
                        account_password = int(
                            input("Account password to be linked : "))
                        if account.account_password == account_password:
                            account.related_card.append(card_number)
                            is_valid_password = True
                        else:
                            print()
                            print(
                                "**Password does not match. Please enter it again**")
                    is_valid_account = True

                else:
                    print()
                    print("**This account does not exist. Please enter it again**")
                    break

        PIN = int(input("Card PIN number to use : "))

        card = Card(card_number, account_number, PIN)
        card_list.append(card)
        card.get_init_info()

    def check_card_and_get_account(self):
        print()
        print("<Please enter the following information to inquiry your account>")
        print("----------------------------------------------------")

        is_valid_card = False
        while not is_valid_card:
            card_number = int(input("Please enter your card number : "))

            for card in card_list:
                if card.card_number == card_number:
                    is_valid_card = True
                else:
                    print()
                    print("**This card does not exist. Please enter it again**")
                    break

        is_valid_PIN = False
        while not is_valid_PIN:
            PIN = int(input("Please enter your PIN number : "))

            for card in card_list:
                if card.PIN == PIN:
                    is_valid_PIN = True
                else:
                    print()
                    print("**PIN number does not match. Please enter it again**")
                    break

        for account in account_list:
            if card_number in account.related_card:
                return account

    def get_account_function(self):
        account = self.check_card_and_get_account()

        while True:
            account.get_info()
            print("Please select the function you want from your account.", end="\n")
            print(functions)
            # 1. Transaction history
            # 2. Deposit
            # 3. Withdraw
            # 4. Terminate Account inquiry
            function_num = int(input("function number >> "))

            if function_num == 1:
                account.get_translation_history()
            if function_num == 2:
                account.deposit()
            if function_num == 3:
                account.withdraw()
            if function_num == 4:
                break
