infile=open("marry.txt","r")

wordlist=dict()

for line in infile:
    words=line.split()
    for word in words:
        if word in wordlist:
            wordlist[word]+=1
        else:
            wordlist[word]=1
for word in wordlist:
    print((word,wordlist[word]))

infile.close()