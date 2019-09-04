word = input("word:")

#1
rword=""
for i in range (len(word)):
    rword+=word[-(i+1)]
print(rword)

#2
rword="".join(reversed(word))
print(rword)

