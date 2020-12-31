import random
number=random.randint(0000,9999)
ns=str(number)
guess=int(input("사용자의 복권번호를 입력하세요:"))
gs=str(guess)
right=0

for i in range(4):
        if ns[i]==gs[i]:
            right+=1
if right==4:
    print("당첨금액은 100만원입니다.")
elif right>=2:
    print("당첨금액은 50만원입니다.")
else:
    print("당첨금액은 0원입니다.")
