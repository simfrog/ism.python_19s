table=[[' ' for x in range(5)]for y in range(5)]

while True:
    for r in range(5):
        print("---------------------")
        print("|  "+table[r][0]+"|  "+table[r][1]+"|  "+table[r][2]+"|  "+table[r][3]+"|  "+table[r][4]+"|")
        if r==4:
            print("---------------------")

    for d in range(3):
        d=input("난로의 위치를 입력하세요:")
        table.append(d[0],d[2])

    for i in range(9):
        print(d[int(d-2)],d[]





