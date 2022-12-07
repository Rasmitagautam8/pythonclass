
#child class "IS A" parent class



# class Person:
#     def __init__(self,name,address):
#         self.name = name
#         self.address = address


#     def profile(self):
#         print(f"Name: {self.name}")
#         print(f"Address: {self.address}")

# class Student(Person):
#     def __init__(self, name, address, roll_number):
#         super().__init__(name, address)
#         self.roll_number = roll_number

#     def profile(self):
#         super().profile()
#         print(f"Roll number: {self.roll_number}")

# class Teacher(Person):
#     def __init__(self, name, address, designation):
#         super().__init__(name, address)
#         self.designation = designation 

# s = Student("Ram", "Ktm", 1)
# s.profile()



class User:
    def __init__(self, _id, username, pwd):
        self._id = _id
        self.username = username
        self.password = pwd




class Person(User):
    def __init__(self, _id, username, pwd, name, address):
        super().__init__(_id, username, pwd)
        self.name = name
        self.address = address


    def profile(self):
        print(f"Name: {self.name}")
        print(f"Address: {self.address}")

class Staff(Person):
    def __init__(self, _id, username, pwd, name, address, designation):
        super().__init__(_id, username, pwd, name, address)
        self.designation = designation

    def profile(self):
        print(f"Username: {self.username}")
        print(f"ID: {self._id}")
        super().profile()
        print(f"Designation:{self.designation}")
        
s = Staff(1, "Ram", 23, "R", "ktm", "manager")
s.profile()






