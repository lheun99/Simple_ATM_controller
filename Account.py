from datetime import datetime


class Account:

    def __init__(self, username, account_number, account_password, balance):
        self.username = username
        self.account_number = account_number
        self.account_password = account_password
        self.balance = balance
        self.related_card = []
        now = datetime.now()
        self.transaction_history = [(now.strftime(
            '%Y-%m-%d %H:%M:%S'), f"(Initial deposit) : ${balance}")]

    def get_init_info(self):
        print()
        print("<Your account has been opened>")
        print("------------------------------------------------------------------")
        print(f"[Account number] : {self.account_number}")
        print(f"[Username] : {self.username}")
        print(f"[Account balance] : ${self.balance}")
        print()

    def get_info(self):
        print()
        print("------------------------------------------------------------------")
        print(f"[{self.username}]'s Account")
        print(f"[Account balance] : ${self.balance}")
        print("------------------------------------------------------------------")
        print()

    # 1. Bank statement (Transaction history)
    def get_translation_history(self):
        print()
        print(f"[{self.username}]'s Account")
        print(f"[Account balance] : ${self.balance}")
        print("==================================================================")
        print(f"[Bank statement]")
        for date, history in self.transaction_history:
            print(
                "------------------------------------------------------------------")
            print(f"[{date}] {history}")
        print("==================================================================")

    # 2. Deposit
    def deposit(self):
        now = datetime.now()
        print()
        print("<Please enter the amount you want to deposit>")
        print(f"[Account balance] : ${self.balance}")
        print("------------------------------------------------------------------")
        deposit_amount = int(input("Deposit($) : "))
        self.balance += deposit_amount
        self.transaction_history.append((now.strftime(
            '%Y-%m-%d %H:%M:%S'),
            f'''(Deposit) : ${deposit_amount}
                      (Balance) : ${self.balance}'''))
        print("==================================================================")

    # 3. Withdraw
    def withdraw(self):
        now = datetime.now()
        print()
        print("<Please enter the amount you want to withdraw>")
        print(f"[Account balance] : ${self.balance}")
        print("------------------------------------------------------------------")
        withdraw_amount = int(input("Withdraw($) : "))
        balance = self.balance
        if balance - withdraw_amount < 0:
            print("**Withdrawal is not possible due to insufficient balance.**")
        else:
            self.balance -= withdraw_amount
        self.transaction_history.append((now.strftime(
            '%Y-%m-%d %H:%M:%S'),
            f'''(Withdraw) : ${withdraw_amount}
                      (Balance) : ${self.balance}'''))
        print("==================================================================")
