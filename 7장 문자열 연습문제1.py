birth=input('생년월일:')
if int(birth[0:4])>2019:
    print('올바른 생년월일이 아닙니다.')
if int(birth[4:6])>12:
    print('올바른 생년월일이 아닙니다.')
if int(birth[6:8])>31:
    print('올바른 생년월일이 아닙니다.')