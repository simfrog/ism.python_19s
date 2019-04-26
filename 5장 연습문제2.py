#inc
def inc(n):
    global count
    count += 1
    return count

count = 0
n = int(input("관람객 인원:"))

for i in range(n):
    count = inc(n)
print(count)