
class Card:
    # 카드 발급
    def __init__(self, card_number, account_number, username, PIN):
        self.card_number = card_number
        self.account_number = account_number
        self.username = username
        self.PIN = PIN

    # 기본 카드 정보 출력
    def get_init_info(self):
        print()
        print("카드 개설이 완료되었습니다.")
        print("----------------------------------------------------")
        print(f"사용자 이름 : {self.username}")
        print(f"카드 번호 : {self.card_number}")
        print(f"연결 계좌 번호 : {self.account_number}")

    # # 카드 존재 확인
    # def check_valid_card(self, card_number):
    #     # 카드 번호 확인

    # def get_PIN(self, PIN):
    #     while self.PIN == PIN:
    #         return False
