word=input("word:")

#1
rword=""
for i in range (len(word)):
    rword+=word[-(i+1)]
if word==rword:
    print("회문 입니다.")
else:
    print("회문이 아닙니다.")

#2
rword="".join(reversed(word))
if word==rword:
    print("회문 입니다.")
else:
    print("회문이 아닙니다.")

