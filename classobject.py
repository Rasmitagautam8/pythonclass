# 1. class and object
# 2. inheritance
# 3. abstraction
# 4. polymorphism

#noun -> object
#adjective -> property, characteristics
#verb -> method, function, action
   

# class Student:
#     def __init__(self, _id, roll_no, name, gender):    #init -> initializer function
#         self._id = _id
#         self.roll_number = roll_no
#         self.name = name
#         self.gender = gender
#         self.total_attendance = 0

#     def view_attendance(self):
#         return f"Total attendence of {self.name} is {self.total_attendance}"

# s = Student(1, 1, "Ram", "Male")
# # print(s.__dict__)
# print(f"Name :{s.name}")
# print(f"Roll number:{s.roll_number}")
# print(s.view_attendance())
# s2 = Student(2, 2, "Sita", "Female")
# print(s2.view_attendance())





# ################# STUDENT RECORS######################
# students=[]
# for i in range(1, 6):
#     roll_n = input("enter roll number:")
#     name= input("enter name: ")
#     gender = input("enter gender: ")
#     s = Student(i, roll_n, name, gender)
#     students.append(s)

# for student in students:
#     print(f"Name: {student.name}")
#     print(f"Roll number: {student.roll_number}")
#     print(student.view_attendance())
#     print("_"*50)




    #staff 
    # id, name, degignation, contact

# class Staff:
#     def __init__(self, _id, designation, name, contact):    #init -> initializer function
#         self._id = _id
#         self.designations = designation
#         self.name = name
#         self.contacts = contact
#         self.contact_num = 100


#     def view_contact_num(self):
#         return f"contact number of {self.name} is {self.contact_num}"



# staffs=[]
# for i in range(1, 6):
#     designations = input("enter a designation:")
#     name= input("enter name: ")
#     contact = input("enter contact number: ")
#     s = Staff(i, designations, name, contact)
#     staffs.append(s)

# for staff in staffs:
#     print(f"Name: {staff.name}")
#     print(f"designation: {staff.designations}")
#     print(staff.view_contact_num())
#     print("_"*50)


class ProductPriceError(Exception):
    pass

class Product:
    def __init__(self, name, sku, price):
        self.name = name
        self.sku = sku
        self.__price = price
    @property                                 #getter
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        if price <= 0:
            raise ProductPriceError("Price can not be smaller than zero")
            
        self.__price = price

tshirt = Product("T-shirt", "123", 500)
# print(f"Price of tshirt : {tshirt.price}")
# tshirt.price = -1
# print(f"Price of tshirt : {tshirt.price}")
print(tshirt.__dict__)
try:
    tshirt.price = -200
except ProductPriceError as err:
    print(err)
# tshirt.price = -1
print(tshirt.__dict__)







class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return self.num1 + self.num2

    def difference(self):
        return self.num1 - self.num2
    def product(self):
         return self.num1 * self.num2


    @staticmethod
    def sqrt(num):
        return num**0.5


c = Calculator(20, 10)
print(c.add())
print(c.difference())
print(c.product())
print(Calculator.sqrt(25))
