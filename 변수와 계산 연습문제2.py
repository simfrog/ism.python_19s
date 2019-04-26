#사용자로부터 두 점의 좌표 (x1, y1)과 (x2, y2)를 입력받아서 두 점 사이의 거리를 계산하는 프로그램을 작성해보자.

x1 = int(input("x1="))
y1 = int(input("y1="))
x2 = int(input("x2="))
y2 = int(input("y2="))

dist = ((x1-x2)**2 + (y1-y2)**2)**0.5

print(dist)

