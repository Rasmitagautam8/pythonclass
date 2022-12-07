# a = {
#     "properties":{
#         "profile":{
#             "name": "ram",
#             "education":[
#                 {"college": "ABC", "year": 2018},
#                 {"college": "XYZ", "year": 2020},

#             ]
#         },
#         "followers": 10000,
#         "following": 100,
#     }
# }


# name = a.get("properties").get("profile").get("name")
# followers = a.get("properties").get("followers")
# following = a.get("properties").get("following")
# print(f"Name: {name.capitalize()}")
# print(f"Followers: {followers}")
# print(f"Following: {following}")

# educations = a.get("properties").get("profile").get("education")
# for education in educations:
#     college = education.get("college")
#     year = education.get("year")
#     print(f"Education({year}): {college.upper()}")





oil_prices = [
    {
        "oil_type": "petrol",
        "prices":[
            {"year": 2018, "price": 100},
            {"year": 2019, "price": 150},
            {"year": 2020, "price": 180},

        ]

    },
    {
        "oil_type": "diesel",
        "prices":[
            {"year": 2018, "price": 80},
            {"year": 2019, "price": 100},
            {"year": 2020, "price": 100},
        ]
    }
]


print("---------------------------------------------------")
a = (oil_prices[0])


oil_type = a.get("oil_type")

print(f"oil Type: {oil_type}")
price = a.get("prices")
total = 0
for prices in price:
    year = prices.get("year")
    price = prices.get("price")
    total = total + price
    print(f"Price({year}): {price}")
avg = round((total/3),3)
print(f"average: {avg}")
print("---------------------------------------------------")
a = (oil_prices[1])     #for oil in oil prices:
                              

oil_type = a.get("oil_type")

print(f"oil Type: {oil_type}")
price = a.get("prices")
total = 0

for prices in price:
    year = prices.get("year")
    price = prices.get("price")
    total = total + price

    print(f"Price({year}): {price}")
avg = round((total/3),3)    # avg_price = round((total / len(prices)), 2)
print(f"average: {avg}")


