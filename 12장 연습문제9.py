infile=open('data.txt','r')
outfile=open('output.txt','w')
sum=0
count=0
for line in infile:
        sum+=float(line)
        count+=1

outfile.write('합계:'+str(sum)+'\n')
outfile.write('평균:'+str(sum/count))

infile.close()
outfile.close()
