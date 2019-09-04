age=input("나이:")
check=age.isdecimal()

if check==False:
    print("정수로 다시 입력해주세요.")
else:
    print("맞습니다.")