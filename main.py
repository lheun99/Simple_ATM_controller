from ATM import ATM

functions = '''
1. 계좌 개설 
2. 카드 발급
3. 계좌 조회
'''
print("안녕하세요. OO은행 입니다 :)")
print("사용하실 기능을 선택해주세요!", end="\n")
print(functions)

function_num = int(input("사용 기능 번호 >> "))

if function_num == 1:
    ATM.register_account()
if function_num == 2:
    ATM.register_card()
if function_num == 2:
    ATM.check_account()
