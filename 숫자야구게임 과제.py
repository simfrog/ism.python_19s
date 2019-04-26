number = "4123"

for count in range(5):
    ball = 0
    strike =0
    i = 0
    guess = input("숫자를 입력하세요 : ")
    for a in number:
        if (a==guess[0])or(a==guess[1])or(a==guess[2])or(a==guess[3]):
            ball+=1
        if number[i] == guess[i] :
            strike += 1
        i += 1
    ball = ball - strike

    if strike == 4:
        print("4스트라이크입니다. 정답입니다.")
        break
    if ball == 0 and strike == 0:
        print("아웃입니다.")
    else :
        if ball == 0:
            print("%d스트라이크입니다." % strike)
        if strike == 0:
             print("%d볼입니다."%ball)
        if ball != 0 and strike != 0:
            print("%d스트라이크 %d볼입니다."%(strike, ball))
print("게임을 종료합니다.")