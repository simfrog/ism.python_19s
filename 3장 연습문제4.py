country=input("국가를 입력하시오:")
area=input("시를 입력하시오:")

if(country == '한국') :
    if(area=='제주시') :
         print("배송료는 10000원입니다.")
    else:
        print("배송료는 5000원입니다.")
else :
    print("배송료는 20000원입니다.")
