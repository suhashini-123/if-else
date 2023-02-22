a=int(input("enter the marks for physics"))
b=int(input("enter the marks for chemistry"))
c=int(input("enter the marks for biology"))
d=int(input("enter th emarks for mathematics"))
e=int(input("enter the marks for computer science"))
total=a+b+c+d+e
per=(total/500)*100
print(per)
if per>=90:
    print("grade A")
elif per>=80:
    print("grade B")
elif per>=70:
    print("grade C")
elif per>=60:
    print("grade D")
elif per>=50:
    print("grade E")
elif per<=40:
    print("grade F")