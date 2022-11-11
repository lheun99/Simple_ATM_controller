class Card:
    def __init__(self, card_number, account_number, PIN):
        self.card_number = card_number
        self.account_number = account_number
        self.PIN = PIN

    def get_init_info(self):
        print()
        print("<Your card has been issued>")
        print("------------------------------------------------------------------")
        print(f"[Card number] : {self.card_number}")
        print(f"[Linked account number]: {self.account_number}")
