#get_max
def get_max(a,b):
    if a>b:
        return a
    else:
        return b

#get_min
def get_min(a,b):
    if a>b:
        return b
    else:
        return a

x=int(input("source:"))
y=int(input("dest:"))

max=get_max(x,y)
min=get_min(x,y)

dist=max-min
print("distance:%d"%dist)
