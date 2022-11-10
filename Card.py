
class Card:
    # 카드 발급
    def __init__(self, card_number, account_number, PIN):
        self.card_number = card_number
        self.account_number = account_number
        self.PIN = PIN

    # 기본 카드 정보 출력
    def get_init_info(self):
        print()
        print("<Your card has been issued>")
        print("----------------------------------------------------")
        print(f"[Card number] : {self.card_number}")
        print(f"[Linked account number]: {self.account_number}")
