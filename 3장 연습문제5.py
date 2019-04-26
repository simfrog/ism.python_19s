from random import randint

answer = randint(1, 99)
ans = str(answer)
guess = input("복권번호를 입력하세요:")

if(ans==guess):
    print("100만원 당첨되셨습니다.")
elif((ans[0]==guess[0])or(ans[1]==guess[1])) :
    print("50만원 당첨되셨습니다.")
else:
    print("당첨되지 않으셨습니다.")
