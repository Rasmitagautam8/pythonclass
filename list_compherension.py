#a = []
#for i in range(2, 20, 2):
  #  a.append(i)
#print(a)

#a = [i for i in range(2, 20, 2)]
#print(a)

#emails = ["1@gmail.com", "2@gmail.com", "3@yahoo.com", "4@gmail.com", "5@look.com", "6@yahoo.com"]

#a = [i for i in emails if i.endswith("@gmail.com")]
#print(a)

main = []
even = []
odd = []
duplicate = []

for i in range(15):

    x = int(input("enter the number:"))
    if x in main:
        duplicate.append(x)
    else:
        
    
   
        if  x % 2 == 0:
            even.append(x)
        else:
            odd.append(x)
    main.append(x)
        
print(f"main list: {main}")
print(f"even list:{even}")
print(f"odd list:{odd}")
print(f"duplicte list:{duplicate}")


