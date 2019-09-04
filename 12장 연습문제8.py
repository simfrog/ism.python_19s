import pickle

sum=0
n=0

infile=open("data.txt","r")

for line in infile:
    sum+=float(line)
    n+=1

average=sum/n
sa={"sum:":sum,"average:":average}

pickle.dump(sa,open("output.txt","wb"))
myout=pickle.load(open("output.txt","rb"))
print(myout)
'''
infile=open('data.txt','r')
outfile=open('output.txt','w')
sum=0
count=0
for line in infile:
    for word in line.split():
        sum+=float(word)
        count+=1

outfile.write('합계:'+str(sum)+'\n')
outfile.write('평균:'+str(sum/count))

infile.close()
outfile.close()
'''