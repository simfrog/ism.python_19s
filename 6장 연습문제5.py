score=[]
sum=0
for i in range(5):
    number=int(input("점수를 입력하세요:"))
    sum+=number
    score.append(number)

ave=sum/5
person=0
for i in range(len(score)):
    if score[i]>= ave:
        person+=1

print("평균=",ave)
print("평균 이상의 학생수=",person)


