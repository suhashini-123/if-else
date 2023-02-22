a=int(input("enter the 1st side of a triangle"))
b=int(input("enter the 2 nd side of a triangle"))
c=int(input("enter the 3 rd side of a triangle"))
if a==b and b==c and c==a:
    print("equilateral triangle")
elif a==b or b==c or c==a:
    print("isosceless triangle")
else:
    print("scalane triangle")