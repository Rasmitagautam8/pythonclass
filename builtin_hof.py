# map, filter

# def total(a, b):
#     return a+b
#     lambda a,b:a+b   #same


# total = lambda a, b:a+b
# print(total(10, 15))

# def increment_by_one(n):
#     return n + 1

# a = [1, 2, 3, 4, 5, 6, 7, 8]
# out = map(lambda n:n+1, a)
# print(list(out))

# names = ["ram", "shyam", "hari", "sita", "gita"]

# a = map(lambda names:names.capitalize(),names)
# print(list(a))



# a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# def even(num):
#     return num % 2 == 0

# out = filter(lambda num:num % 2 == 0, a)
# print(list(out))



emails = ["1@gmail.com", "2@gmail.com", "3@yahoo.com", "4@gmail.com", "5@yahoo.com", "6@outlook.com"]

    
# def a(mail):
#    return mail.endswith("@gmail.com")

# out = filter(lambda mail:mail.endswith("@gmail.com"), emails)
# print(list(out))



a = "457d89e36"
c = "12d57d54d90"
b = list(c)


d = [17, 20, 25, 30]
e = ["17", "20", "25", "30"]

# print(sum(d))


# print(sum(map(int, e)))

w = c.split("d")
# print(w)

total = 0
for i in w:
    total = total + int(i)
# print(total)
# print(sum(map(int, w)))

total = 0
for i in a:
    if i.isnumeric():
        total = total + int(i)

print(total)



print(sum(map(int, filter(lambda x:x.isnumeric(), a))))

