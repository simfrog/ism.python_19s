#while
n = int(input("n="))
i=1
fact = 1

while (i<=n) :
    fact = fact*i
    i+=1
print(fact)

#for
n=int(input("n="))
fact=1

for i in range (1,n,1) :
    fact = fact*i
print(fact)
