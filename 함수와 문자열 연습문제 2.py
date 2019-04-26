days = ['월','화','수','목','금','토','일']
today = int(input("오늘 요일을 입력하세요(월:0,화:1,수:2,목:3,금:4,토:5,일:6):"))
skips = int(input("며칠 이후의 요일을 알고 싶나요?"))
print(skips,"일 이후의 요일은 %s요일입니다." % days[(today + skips) % 7])