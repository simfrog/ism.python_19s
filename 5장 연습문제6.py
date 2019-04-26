#bin_to_dec
def bin_to_dec(a):
    n=3
    result=0
    for i in range (len(a)):
        result += int(a[i])*2**n
        n-=1
    return result

a = input("2진수:")
result = bin_to_dec(a)

print("10진수:%d"%result)
