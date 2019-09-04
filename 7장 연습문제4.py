numberdict=dict()

while 1:
    name=input("(입력모드)이름을 입력하시오:")
    number=input("(입력모드)번호를 입력하시오:")
    numberdict[name]=number
    if not name:
        break

callnumber=input("(검색모드)이름을 입력하세요:")
if callnumber not in numberdict:
    print("찾는이름이 없습니다.")
else: 
    print("전화번호는 %s 입니다."%numberdict.get(callnumber))