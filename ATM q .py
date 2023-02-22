balance=500000
print("welcome to SBI bank")
print("insert your card")
print("select your language")
language=input("enter language")
if language=="english":
    password=int(input("enter password"))
    if password==1234:
        print("1=withdrawal")
        print("2=balance_enquiry")
        print("3=pin generation ")
        print("4=deposite")
        print("5=exit")
        transaction=int(input("enter transaction:"))
        if transaction==1:
            withdrawal=int(input("enter the withdrawal1="))
            if withdrawal<=balance:
                print("transaction successfilly","collect your withdrawal cash")
                print("remaining balance",balance-withdrawal)
            else:
                print("please enter correct amount")
        elif transaction==2:
            balance_enquiry=(input("saving/current="))
            if balance_enquiry=="saving":
                print("your balance",balance)
            else:
                print("enter correct values")
        elif transaction==3:
            pin_genaration=int(input("enter new pin"))
            if password==password:
                print("new pin generated successfully")
            else:
                print("not correct")
        elif transaction==4:
            deposite=int(input("enter the deposite money"))
            if deposite>=10:
                print("total money is",deposite+balance)
                print("money is deposited successfully")
            else:
                print("no deposite")
        elif transaction==5:
            exit=input("do you want to exit")
            if exit=="yes":
                print("thanku for visiting")
            else:
                print("choose your transaction")
        else:
            print("please enter proper value")
    else:
        print("enter correct password")    
else:
    print("language doesnt exist")

























