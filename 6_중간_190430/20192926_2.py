days=['월','화','수','목','금','토','일']
today=1
skip=int(input("경과 일수 입력:"))
next_days=days[(today+skip)%7]
print("%d일 후는 %s요일 입니다."%(skip,next_days))
