heroes = ["spider man", "thor","hulk", "iron man", "captain america"]

print(len(heroes))
output = []
for i in heroes:
    output.append(i)

output.append("black panther")
print(output)
output.remove("black panther")
print(output)
output.insert(3, "black panther")
print(output)
output[1:3] = ["doctor strange"]
print(output)


