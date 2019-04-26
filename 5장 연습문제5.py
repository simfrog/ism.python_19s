#get_filtered
def get_filtered(data,filter):
    result=""
    for i in data:
        if i not in filter:
            result += i
    return result

x=input("문장을 입력하세요:")
y="$#?!_-.'"

result=get_filtered(x,y)
print(result)

