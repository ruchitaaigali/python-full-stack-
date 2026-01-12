num=float(input("enter the number"))
if num>0:
    print("number is positive")
else:
    print("number is negative")




num=int(input("enter the number"))
if num%2==0:
    print("even")
else:
    print("odd")



a=float(input("enter the numbers"))
b=float(input("enter the numbers"))
c=float(input("enter the numbers"))
if a>=b and a>=c:
    largest=a
elif b>=a and b>=c:
    largest=b
else:
    largest=c
    print("the largest number is {largest}")
      
