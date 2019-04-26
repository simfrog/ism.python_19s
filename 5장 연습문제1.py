def get_sum(x,y):
    for i in range (x+1,y+1):
        x += i
    return x

sum=get_sum(2, 5)
print(sum)