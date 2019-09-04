infile=open("marry.txt","r")

wordlist=dict()

for line in infile:
    words=line.split()
    for word in words:
        if word in wordlist:
            wordlist[word]+=1
        else:
            wordlist[word]=1

infile.close()

sorted_wordlist=sorted(wordlist.items(),key=lambda kv:kv[1],reverse=True)
print(sorted_wordlist)
