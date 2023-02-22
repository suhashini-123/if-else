a=int(input("enter the no.of units"))
if a<=50:
    amount=a*0.50
    surcharge=amount*20/100
    print("total",amount+surcharge)
elif a<=100:
    amount=25+(a-50)*0.75
    surcharge=amount*20/100
    print("total",amount+surcharge)
elif a<=150:
    amount=75+(a-100)*1.20
    surcharge=amount*20
    print("total",amount+surcharge)
else:
    a>=250
    amount=300+(a-250)*
    