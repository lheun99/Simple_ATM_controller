from Account import Account
from Card import Card

account_list = []
card_list = []

functions = '''
====================================================
1. 거래 내역 조회 
2. 입금
3. 출금
4. 계좌 거래 종료
====================================================
'''


class ATM:
    def register_account(self):
        print()
        print("<계좌 개설을 위해 아래의 정보를 입력해주세요>")
        print("----------------------------------------------------")
        account_number = int(input("계좌 번호 : "))
        username = input("사용자 이름 : ")
        balance = int(input("초기 입금 금액 : "))

        account = Account(account_number, username, balance)
        account_list.append(account)
        account.get_init_info()

    def register_card(self):
        print()
        print("<카드 발급을 위해 아래의 정보를 입력해주세요>")
        print("----------------------------------------------------")
        card_number = int(input("카드 번호 : "))

        is_valid_account = False
        while not is_valid_account:
            account_number = int(input("연결할 계좌 번호 : "))

            for account in account_list:
                if account.account_number == account_number:
                    account.related_card.append(card_number)
                    is_valid_account = True
                else:
                    print()
                    print("**존재하지 않는 계좌입니다. 다시 입력해주세요**")
                    break

        username = input("사용자 이름 : ")
        PIN = int(input("사용할 PIN 번호 : "))

        card = Card(card_number, account_number, username, PIN)
        card_list.append(card)
        card.get_init_info()

    def check_card_pin(self):
        print()
        print("<계좌 조회을 위해 아래의 정보를 입력해주세요>")
        print("----------------------------------------------------")
        is_valid_card = False
        while not is_valid_card:
            card_number = int(input("카드 번호를 입력해주세요 : "))

            for card in card_list:
                if card.card_number == card_number:
                    is_valid_card = True
                else:
                    print()
                    print("**존재하지 않는 카드입니다. 다시 입력해주세요**")
                    break

        is_valid_PIN = False
        while not is_valid_PIN:
            PIN = int(input("PIN 번호를 입력해주세요 : "))

            for card in card_list:
                if card.PIN == PIN:
                    is_valid_PIN = True
                else:
                    print()
                    print("**PIN 번호가 일치하지 않습니다. 다시 입력해주세요**")
                    break

        for account in account_list:
            if card_number in account.related_card:
                return account

    def get_account(self):
        account = self.check_card_pin()

        while True:
            account.get_info()
            print("해당 계좌에서 원하시는 기능을 선택해 주세요!", end="\n")
            print(functions)
            # 1. 거래 내역 조회
            # 2. 입금
            # 3. 출금
            # 4. 계좌 거래 종료
            function_num = int(input("사용 기능 번호 >> "))

            if function_num == 1:
                account.get_translation_history()
            if function_num == 2:
                account.deposit()
            if function_num == 3:
                account.withdraw()
            if function_num == 4:
                break
