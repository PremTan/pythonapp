# atm_case_demo.py

from atm_menu import menu
from atm_except import DepositError,WithdrawError,InSuffFundError
from atm_operations import withdraw,deposit,balenq
import sys

while(True):
    menu()
    try:
        ch = int(input("Enter ur choice : "))
        match(ch):
            case 1:
                try:
                    deposit()
                except ValueError:
                    print("Dont enter Alnums,strs and special symbols")
                except DepositError:
                    print("Dont try to deposit -ve and 0 amount")
            case 2:
                try:
                    withdraw()
                except ValueError:
                    print("Dont enter Alnums,strs and special symbols")
                except WithdrawError:
                    print("Dont try to withdraw -ve or 0 amount")
                except InSuffFundError:
                    print("This Atm can withdraw only above 500 cash")
                    print("Ur ac dont have sufficient balance")
            case 3:
                balenq()
            case 4:
                print("Thnx for using this ATM----Visit Again")
                sys.exit()
            case _:
                print("Ur selection of operation is wrong --- try again")
    except ValueError:
        print("Dont enter Alnums,strs and special symbols for choice : ")
