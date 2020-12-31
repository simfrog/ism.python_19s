import math
score=[]
total=0
at=0
while True:
    number=int(input("성적을 입력하세요(종료는 -1):"))
    if number==-1:
        break
    score.append(number)
    total+=number
    at+=number**2

ave=total/len(score)
atve=at/len(score)
a=math.sqrt(atve-ave**2)
print("평균은 %d점이고 표준편차는 %f입니다."%(ave,a))

