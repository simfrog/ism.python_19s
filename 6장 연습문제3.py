customer=[]
for i in range(5):
    name=input("고객이름:")
    customer.append(name)

customer.sort()
print(customer)
'''
def reverseList(x):
    reverse=[]
    for i in range(5):
        reverse.append(x[-i])
    return reverse

print(reverseList(customer))'''

customer.reverse()
print(customer)


