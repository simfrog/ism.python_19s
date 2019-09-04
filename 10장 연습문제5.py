import random

list=[]

for i in range(100):
    r=random.randint(0,100)
    list.append(-r)

print(sorted(list, key=abs))

