
#exception handling 
#  try:
#     #code
# except Exception: #catch specific error or exception
#     #code
# except Exception: #catch specific error or exception
#     #code
# else:
#     #code
# finally:
#     #code



# def summ(num1 , num2):
#     sum = num1 + num2
#     return sum
# total_prod = summ(2 , 3)
# print(total_prod)




# a = int(input("enter a number"))
# b = int(input("enter another number"))
# sum = a + b 
# print(sum)


try:
    a = int(input("enter a number"))
    b = int(input("enter another number"))

except ValueError:
    print("cannot convert to integer")
else:
    print(a+b)
name = input("enter name")
print(name)