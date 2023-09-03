#question8
a=int(input("enter the side"))
b=int(input("enter the side"))
c=int(input("enter the side"))
s=(a+b+c)/2
a=s*(s-a)*(s-b)*(s-c)**0.5
print("semi perimeter",s)
print("area",a)
