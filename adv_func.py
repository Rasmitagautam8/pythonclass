#def outer():
    #print("I am outer function")
   # def inner():
        #print("I am inner function")
   #inner()
#outer()


# def welcome(name):
#     print(f"Welcome {name}!")

# a = welcome

# a("Ram")
# def increment(num):
#     def increase_by(factor):
#         return num + factor
#     return increase_by
# increase_by = increment(20)
# print(increase_by(20))
# print(increase_by(20))

 
# def increment(num):
#     def increase_by(factor):
#         return num + factor
#     return increase_by
# increase_by = increment(20)
# print(increase_by(20))
# print(increase_by(10))

# def welcome(name):
#     print(f"Welcome {name}")

# def bye_bye(name):
#     print(f"Bye Bye {name}")

# def greet_ram(a):     #a = welcome #higher order function 
#     a("Ram") #welcome("Ram")

# greet_ram(bye_bye)


# def decorate_function(func):
#     def wrapper():
#         print("called before")
#         func()
#         print("called after")
#     return wrapper
# @decorate_function
# def example():
#     print("i am example")
# example()
# print(example)

def smart_division(func):
    def wrapper(a, b):
        if b == 0:
            return "can not divide by zero."
        else:
            return func(a, b)
    return wrapper
@smart_division
def division(a, b):
    return a/b

print(division(10,2))
print(division(10,0))