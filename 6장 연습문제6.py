import random

list=[0,0,0,0,0,0]
for i in range(600):
    number=random.randint(1, 6)
    for j in range(6):
        if number==j+1:
            list[j]=list[j]+1

for k in range(6):
    print("주사위가 %d인 경우는 %d번"%(k+1,list[k]))





