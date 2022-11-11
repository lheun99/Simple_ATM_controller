from ATM import ATM

functions = '''
==================================================================
1. Open an account
2. Card issuance
3. Account inquiry
4. Terminate ATM
==================================================================
'''
print()
print("Hello, this is Simple bank ATM :)")

atm = ATM()

while True:
    print()
    print("Please select the function you want to use.", end="\n")
    print(functions)
    # 1. Open an account
    # 2. Card issuance
    # 3. Account inquiry
    # 4. Terminate ATM
    try:
        function_num = int(input("function number >> "))
    except:
        print("**Invalid input. Please enter again.**")
        continue

    if function_num == 1:
        atm.register_account()
    if function_num == 2:
        atm.register_card()
    if function_num == 3:
        atm.get_account_function()
    if function_num == 4:
        break
