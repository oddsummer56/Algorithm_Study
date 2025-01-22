"""
두 자연수 A와 B가 주어진다. 이때, A+B, A-B, A*B, A/B(몫), A%B(나머지)를 출력하는 프로그램을 작성하시오. 

예제 입력 
7 3

예제 출력
10
4
21
2
1

map() 함수는 여러 개의 데이터를 받아서 각각의 요소에 함수를 적용한 결과를 반환하는 내장 함수
"""

a, b = map(int, input().split())
print(a+b)
print(a-b)
print(a*b)
print(a//b)
print(a%b)