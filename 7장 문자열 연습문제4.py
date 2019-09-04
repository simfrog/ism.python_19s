s=input("문장:")

#1
count=0
for i in range (len(s)):
    if "o" in s:
        count+=1
print("o의 개수:",count)

#2
print(s.count("o"))

