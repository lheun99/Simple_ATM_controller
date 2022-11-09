from Account import Account
from Card import Card

account_list = []
card_list = []


class ATM:
    def register_account():
        print()
        print("계좌 개설을 위해 아래의 정보를 입력해주세요!")
        print("----------------------------------------------------")
        account_number = input("계좌 번호 : ")
        username = input("사용자 이름 : ")
        balance = int(input("초기 입금 금액 : "))

        account = Account(account_number, username, balance)
        account_list.append(account)
        account.get_init_info()

    def register_card():
        print()
        print("카드 발급을 위해 아래의 정보를 입력해주세요!")
        print("----------------------------------------------------")
        card_number = input("카드 번호 : ")
        account_number = input("연결 계좌 번호 : ")
        username = input("사용자 이름 : ")
        PIN = int(input("사용할 PIN 번호 : "))

        card = Card(card_number, account_number, username, PIN)
        card_list.append(card)
        card.get_init_info()

    def check_account():
        print()
        is_valid_card = False
        while not is_valid_card:
            card_number = input("카드 번호를 입력해주세요! >> ")

            for card in card_list:
                if card.card_number == card_number:
                    is_valid_card = True
                else:
                    print("존재하지 않는 카드입니다. 다시 입력해주세요.")
                    break

        is_valid_PIN = False
        while not is_valid_PIN:
            PIN = int(input("PIN 번호를 입력해주세요! >> "))

            for card in card_list:
                if card.PIN == PIN:
                    is_valid_PIN = True
                else:
                    print("PIN 번호가 일치하지 않습니다. 다시 입력해주세요.")
                    break
