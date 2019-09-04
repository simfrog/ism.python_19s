dial={'ABC':2,'DEF':3,'GHI':4,'JKL':5,'MNO':6,'PQRS':7,'TUV':8,'WXYZ':9}

word=input("문자열을 입력하시오:")


for x in word:
    for item in dial.items():
        if x in item[0]:
            print(item[1],end='')