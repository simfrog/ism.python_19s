import csv

f = open('amazon_reviews_us_Mobile_Electronics_v1_00.tsv','r',encoding='utf-8')
dataline = csv.reader(f,delimiter='\t')
data=list(dataline)
data=data[1:]

down_3 = dict()
up_4 = dict()

for line in range(10):
    print(data[line],'\n')
    d=data[line]
    review = d[13]
    if d[7] == '1' or d[7] == '2' or d[7] == '3':
        for word in review.split():
            if word in down_3:
                down_3[word]+=1
            else:
                down_3[word]=1

    if d[7] == '4' or d[7] == '5':
        for word in review.split():
            if word in up_4:
                up_4[word]+=1
            else:
                up_4[word]=1

print(len(down_3))
print(len(up_4))
print()

sorted_down_3=sorted(down_3.items(),key=lambda dt:dt[1],reverse=True)
sorted_up_4=sorted(up_4.items(),key=lambda dt:dt[1],reverse=True)
sorted_down_3=sorted_down_3[28:160]
sorted_up_4=sorted_up_4[50:101]

print('별점 3이하')
for i in sorted_down_3:
    print(i)
print()
print('별점 4이상')
for j in sorted_up_4:
    print(j)

f.close()