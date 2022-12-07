#for <variable> in <iterable object>:
#code to execute 

#range(start, stop, step)
#range(10) -> start=0, stop=9, step=1
#range(1,10) -> start=1, stop=9, step=1
#range(1, 10, 2) -> start=1, stop=9, step=1



#print(sum(range(3, 101, 3)))

result = 0
for i in range(1,100):
    if i%3 == 0 or i%5 == 0:
        result += i
print(result)
