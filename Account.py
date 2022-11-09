class Account:
    # 계좌 개설
    def __init__(self, account_number, username, balance):
        self.account_number = account_number
        self.username = username
        self.balance = balance
        self.related_card = []
        self.transaction_history = {}

    # 기본 계좌 정보 출력
    def get_init_info(self):
        print()
        print("계좌 개설이 완료되었습니다.")
        print("----------------------------------------------------")
        print(f"사용자 이름 : {self.username}")
        print(f"계좌 잔액 : {self.balance}")

    # 계좌 조회 시 계좌 정보 출력
    def get_info(self):
        print()
        print(f"사용자 이름 : {self.username}")
        print("----------------------------------------------------")
        print(f"계좌 잔액 : {self.balance}")
        print(f"계좌 거래 내역")
        for history in self.transaction_history:
            print(history)
