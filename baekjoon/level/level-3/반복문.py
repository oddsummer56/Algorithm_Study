# # 2739

# a = int(input())

# for i in range (1, 10):
#     result =  a * i
#     print(a, "*", i, "=", result)

# # 10950

# a = int(input())
# result = []

# for i in range(a):
#     num1, num2 = map(int, input().split())
#     result = num1 + num2
#     print(result)

# # 8393

# a = int(input())
# sum = 0

# for i in range(1, a+1):
#     sum+=i

# print(sum)

# # 25304

# tot_price = int(input())
# a = int(input())
# tot = 0
# for i in range(a):
#     price, quantity = map(int, input().split())
#     each_price = price * quantity
#     tot +=each_price

# if tot_price == tot:
#     print("Yes")
# else:
#     print("No")

# # 25314

# # n = int(input())
# # num = n//4
# # sen="long "*num

# # print(sen+"int")

# print(int(input())//4*"long "+"int")

# # 15552

# # num = int(input())
# # for i in range(num):
# #     a, b = map(int, input().split())
# #     print(a+b)

# import sys

# # num = int(sys.stdin.readline())

# # for i in range(num):
# #     a, b = map(int, sys.stdin.readline().split())
# #     print(a+b)

# num = int(input())

# for i in range(num):
#     a = sys.stdin.readline()
# print(a)

# # 11021

# import sys

# input = sys.stdin.readline

# a = int(input())

# for i in range(1, a+1):
#     num1, num2 = map(int, input().split())
#     print(f"Case #{i}: {num1+num2}")

# # 11022

# import sys

# input = sys.stdin.readline

# a = int(input())

# for i in range(1, a+1):
#     num1, num2 = map(int, input().split())
#     print(f"Case #{i}: {num1} + {num2} = {num1+num2}")

# # 2438

# import sys
# input = sys.stdin.readline
# a=int(input())

# for i in range(1, a+1):
#     print("*"*i)

# 2439

# ### solution 1

# import sys
# input = sys.stdin.readline
# a=int(input())

# for i in range(1, a+1):
#     print(" "*(a-i)+"*"*i)

# ### solution 2

# import sys
# input = sys.stdin.readline
# a = int(input())

# for i in range(1, a+1):
#     x = " ".rjust(i, "*")
#     print(x)

# ~~~미완성~~~

# 10952

"""
런타임 에러(TypeError)
"""

# import sys
# input = sys.stdin.readline

# while 1:
#     a, b = map(int, input().split())
#     if a+b != 0:
#         print(a+b)
#     else:
#         break

import sys
input = sys.stdin.readline

while 1:
    try: 
        a, b = map(int, input().split())
        if a+b == 0:
            break
        else:
            print(a+b)
    except Exception:
        break
    
