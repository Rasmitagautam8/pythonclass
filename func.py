#def sum(num1, num2):
    #total = num1 + num2
    #return total
#total_sum = sum(10 , 15)
#print(total_sum)


def profile(name, address, contact):
    print(f"Name: {name}")
    print(f"address: {address}")
    print(f"Contact: {contact}")
profile("Ram", "Ktm", "098876")      # positional argument
print("----------------------------------------------------")
profile("Ram", "098876", "Ktm") 
print("----------------------------------------------------")
print("----------------------------------------------------")
profile(name="Ram", address="ktm", contact="098876")
print("----------------------------------------------------")
profile(name="Ram", contact="098876", address="ktm",)      #keyword argument