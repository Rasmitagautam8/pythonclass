def total_sum(num1, num2):
    total = num1 + num2
    #print(f"total= {total}")

def total_sum_two(num1, num2):
    total = num1 + num2
    return total

b = total_sum(10, 15)
#print(f"b: {b}")

a = total_sum_two(10, 25)
#print(f"a: {a}")

#*args , **kwargs

#def example(*args):
    #print(args)

#example(1, 2, 3, 4, 5)

#def example2(**kwargs):
    #print(kwargs)

#example2(name = "Ram", contact = "976655", nickname = "ra")



#def example3(*args, **kwargs):
    #print(args, kwargs)

#example3(1, 2, 3, name = "Ram", contact = "76554", nickname = "Ro")

def multiple_of_num(num1, factor = 5):
    return num1 * factor
print(multiple_of_num(10))