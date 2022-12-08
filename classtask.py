students_score = [
    {"name": "Ram", "score": 80},
    {"name": "Sita", "score": 100},
    {"name": "Abc", "score": 35},
    {"name": "xyz", "score": 40},
    {"name": "john", "score": 37},
    {"name": "shyam", "score": 90},
    {"name": "hari", "score": 36},
]
output = []
for score in students_score:
    a = score.get("score")
   
    if a>=40:
        output.append(score)
print(output)



output = list(filter(lambda i:i.get("score")>= 40, students_score))
print(output)



colors = ["yellow", "red", "green", "blue", "yellow", "orange", "red"]
remove = ["yellow", "red"]
color = ["yellow", "red", "green", "blue", "yellow", "orange", "red"]



output = []


    
    


