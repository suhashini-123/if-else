from selectors import EpollSelector


cp=int(input("cost price"))
sp=int(input("selling price")) 
if cp>sp:
    print("loss")
elif sp>cp:
    print("profit")
else:
    print("no profit no loss")
