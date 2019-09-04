import random
rows=5
cols=5
bingo=[]

#2차원 리스트를 생성한다.
for row in range(rows):
        bingo+=[[0]*cols]

#2차원 리스트의 각 요소에 값을 저장한다.
for r in range(5):
    for c in range(5):
        bingo[r][c]=(r*5+c+1)

#빙고판을 만든다.
def bingoboard():
    for r in range(5):
        if r==0 or r==1:
            for c in range (5):
                print(bingo[r][c],"  ",end='')
        else:
            for c in range(5):
                print(bingo[r][c], " ", end='')
        print()

while True:
    bingoboard()

#'x'로 바꾸고자 하는 번호를 입력한다. 이때 입력한 번호가 25를 넘으면 다시 입력한다.
    number=int(input("번호를 선택하세요:"))
    if number>25:
        print("다시 입력해주세요.")

#사용자가 입력한 번호를 검사한다. 이때 입력한 번호에 이미 'x'나'o'가 있으면 다시 입력한다.
    for r in range(5):
        for c in range(5):
            if number==(r*5+c+1):
                if bingo[r][c]=='x' or bingo[r][c]=='o':
                    print("다시 입력해주세요.")
                    break
                bingo[r][c]='x'
#랜덤 함수를 이용하여 컴퓨터가 놓을 위치를 결정한다. .
                done=False
                for r in range(5):
                    for c in range(5):
                        if bingo[r][c]!='x' and bingo[r][c]!='o'and not done:
                            cr = random.randint(0, 4)
                            cc = random.randint(0, 4)
                            if bingo[cr][cc]!='x' and bingo[cr][cc]!='o' and not done:
                                bingo[cr][cc]='o'
                                done=True
                                break
    result=""
#빙고를 검사한다.
    for r in range(5):
        if bingo[r][0]==bingo[r][1]==bingo[r][2]==bingo[r][3]==bingo[r][4]:
            if bingo[r][0]=='x':
                result='win'
            else:
                result='loose'
        elif bingo[0][r]==bingo[1][r]==bingo[2][r]==bingo[3][r]==bingo[4][r]:
            if bingo[0][r]=='x':
                result='win'
            else:
                result='loose'
    if bingo[0][0]==bingo[1][1]==bingo[2][2]==bingo[3][3]==bingo[4][4]:
        if bingo[0][0]=='x':
            result='win'
        else:
            result='loose'
    elif bingo[0][4]==bingo[1][3]==bingo[2][2]==bingo[3][1]==bingo[4][0]:
        if bingo[0][4]=='x':
            result='win'
        else:
            result='loose'

#승패를 결정한다.
    if result=='win':
        bingoboard()
        print("빙고! 사용자가 이겼습니다.")
        break
    elif result=='loose':
        bingoboard()
        print("빙고! 컴퓨터가 이겼습니다.")
        break