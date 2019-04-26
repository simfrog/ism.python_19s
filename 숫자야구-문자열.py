number = "4123"
#총 5번 반복한다. 5번 반복하면 '게임을 종료합니다.'를 출력한다.
for count in range(5):
    ball = 0
    strike =0
    i = 0
    # 숫자 4개를 입력한다.
    guess = input("숫자를 입력하세요 : ")
    # guess의 i번째와 number의 j번째가 맞는지 안 맞는지 4번 반복하여 확인한다.
    for i in range(4): # i와 j를 4번반복하여
        for j in range(4):
            if guess[i] == number[j]:
                # i와 j가 같으면 즉, 자릿수와 숫자가 같으면 strike가 1씩 올라간다.
                if i==j:
                    strike+=1
                # 자릿수는 같지 않으나 숫자가 같으면 ball이 1씩 올라간다.
                else:
                    ball+=1
    # 다 맞췄으므로 break를 통해 반복문을 빠져나온다.
    if strike == 4:
        print("4스트라이크입니다. 정답입니다.")
        break
    # ball과strike가 둘 다 0이면 '아웃입니다.'를 출력한다.
    if ball == 0 and strike == 0:
        print("아웃입니다.")
    else :
        #ball이 0이면 스트라이크 개수만 출력한다.
        if ball == 0:
            print("%d스트라이크입니다." % strike)
        # strike가 0이면 볼 개수만 출력한다.
        if strike == 0:
             print("%d볼입니다."%ball)
        #둘 다 0이 아니면 스트라이크 개수와 볼 개수 둘 다 출력한다.
        if ball != 0 and strike != 0:
            print("%d스트라이크 %d볼입니다."%(strike, ball))
print("게임을 종료합니다.")