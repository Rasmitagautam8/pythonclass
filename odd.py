a = int(input("enter a number"))
b = int(input("enter second number"))
c = int(input("enter third number"))

if a >= b and a >= c:
    print(a," is greater")
elif b >= a and a >= c:
    print(b," is greatest") 
else:
    print(c," is greatest")       
     
    