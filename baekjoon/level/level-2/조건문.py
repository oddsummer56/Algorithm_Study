# 1번 1330

# a, b = map(int, input().split())

# if a>b :
#     print(">")
# elif a<b:
#     print("<")
# else:
#     print("==")

# 2번 9498

# a = int(input())

# if 90<=a<=100:
#     print("A")
# elif 80<=a<=89:
#     print("B")
# elif 70<=a<=79:
#     print("C")
# elif 60<=a<=69:
#     print("D")
# else:
#     print("F")
    

# 3번 2753

"""
&와 | 연산자는 파이썬에서 비트 연산자. 즉, 두 숫자의 이진 표현을 비교하여 각 비트에 대해 AND 혹은 OR 연산을 수행.
논리 연산을 수행할 때는 AND 혹은 OR 키워드를 사용해야 함.
"""
# year = int(input())

### solution 1

# if year%4==0 and (year%100!=0 or year%400==0):
#     print(1)
# else:
#     print(0)

### solution 2

# if year%4==0:
#     if year%100!=0: 
#         print("1")
#     elif year%400==0:
#         print("1")
#     else:
#         print("0")
# else:
#     print("0")


# 4번 14681

# x=int(input())
# y=int(input())

# if x>=0 and y>0:
#     print(1)
# elif x<0 and y>0:
#     print(2)
# elif x<0 and y<0:
#     print(3)
# else:
#     print(4)

# 5번 2884

# h, m = map(int, input().split())


### solution 1

# if m>=45:
#         print(f"{h} {m-45}")
# else:
#     if h==0:
#           print(f"{h+23} {m+15}")
#     else:
#          print(f"{h-1} {m+15}")


### solution 2

# total = h*60 + m-45

"""
00:00 ~ 00:44 에 대한 예외처리
"""

# if total<0:
#     total += 24*60

# h = total // 60 
# m = total % 60

# print(h, m)

# 6번 2525

"""
24:00 초과에 대한 예외처리
"""

# h, m = map(int, input().split())
# c = int(input())
# total = h*60 + m + c

# if total>=1440:
#     total -= 24*60

# h = total // 60 
# m = total % 60

# print(h, m)

# 7번 2480

""" 
수정필요
"""
a, b, c = map(int, input().split())

if a==b==c:
    total = 10000+a*1000
    print(total)
elif a==b:
    total = 1000+a*100
    print(total)
elif a==c:
    total = 1000+a*100
    print(total)
elif b==c:
    total = 1000+b*100
    print(total)
else:
    total = max(a, b, c)*100
    print(total)