# atm operations.py

from atm_except import DepositError,WithdrawError,InSuffFundError
bal = 500.00
def deposit():
    damt  = float(input("Enter the deposit amount : "))
    if (damt<=0):
        raise DepositError
    else:
        global bal
        bal = bal  + damt
        print("Ur Account xxxxxxxxxxxx123 Credited with INR : {}".format(damt))
        print("Now ur Acount Bal INR : {}".format(bal))

def withdraw():
    global bal
    wamt = float(input("Enter the withdraw amount : "))
    if (wamt<=0):
        raise WithdrawError
    elif((wamt+500)>bal):
        raise InSuffFundError
    else:
        bal=bal-wamt
        print("Ur Account xxxxxxxxxxxx123 Debited with INR : {}".format(wamt))
        print("Now ur Acount Bal INR : {}".format(bal))

def balenq():
    print("Ur account Bal INR : {}".format(bal))