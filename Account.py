from datetime import datetime
now = datetime.now()


class Account:
    # 계좌 개설
    def __init__(self, account_number, username, balance):
        self.account_number = account_number
        self.username = username
        self.balance = balance
        self.related_card = []
        self.transaction_history = [(now.strftime(
            '%Y-%m-%d %H:%M:%S'), f"(입금) : {balance}원")]

    # 초기 계좌 정보 출력
    def get_init_info(self):
        print()
        print("<계좌 개설이 완료되었습니다>")
        print("----------------------------------------------------")
        print(f"[계좌 번호] : {self.account_number}")
        print(f"[사용자 이름] : {self.username}")
        print(f"[계좌 잔액] : {self.balance}원")
        print()

    # 기본 계좌 정보 출력
    def get_info(self):
        print()
        print("----------------------------------------------------")
        print(f"[{self.username}]님의 계좌 입니다.")
        print(f"[계좌 잔액] : {self.balance}원")
        print("----------------------------------------------------")
        print()

    # 거래 내역 조회 시 계좌 정보 출력
    def get_translation_history(self):
        print()
        print(f"[{self.username}]님의 계좌 입니다.")
        print(f"[계좌 잔액] : {self.balance}원")
        print("====================================================")
        print(f"[계좌 거래 내역]")
        for date, history in self.transaction_history:
            print("----------------------------------------------------")
            print(f"[{date}] {history}")
        print("====================================================")

    # 입금

    def deposit(self):
        print()
        print("<입금하실 금액을 입력해주세요>")
        print(f"[현재 잔액] : {self.balance}원")
        print("----------------------------------------------------")
        deposit_amount = int(input("입금 금액 : "))
        self.balance += deposit_amount
        self.transaction_history.append((now.strftime(
            '%Y-%m-%d %H:%M:%S'), f"(입금) : {deposit_amount}원"))
        print("====================================================")

    # 출금

    def withdraw(self):
        print()
        print("<출금하실 금액을 입력해주세요>")
        print(f"[현재 잔액] : {self.balance}원")
        print("----------------------------------------------------")
        withdraw_amount = int(input("출금 금액 : "))
        balance = self.balance
        if balance - withdraw_amount < 0:
            print("**잔액이 부족해 출금이 불가능 합니다**")
        else:
            self.balance -= withdraw_amount
        self.transaction_history.append((now.strftime(
            '%Y-%m-%d %H:%M:%S'), f"(출금) : {withdraw_amount}원"))
        print("====================================================")
