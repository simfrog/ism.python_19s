#사용자로부터 4자리의 정수를 받아서 자리수의 합을 계산하는 프로그램을 작성하여 보자. 예를 들어서 사용자가 1234를 입력하였다면 1+2+3+4를 계산하면 된다.  힌트: 나머지 연산자와 정수 나눗셈 연산자 (//)를 활용.

n = int(input("number="))
n1 = int(n//1000)
n2 = int(n%1000//100)
n3 = int(n%100//10)
n4 = int(n%10//1)

s = int(n1+n2+n3+n4)

print(s)