n=int(input("n을 입력하세요:"))
for a in range(1,n+1):
    for b in range(a,n+1):
        for c in range(b,n+1):
            if a+b>=c:
                print("(",a,b,c,")")
