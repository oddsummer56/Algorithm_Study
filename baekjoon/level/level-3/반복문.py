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

# 15552

# num = int(input())
# for i in range(num):
#     a, b = map(int, input().split())
#     print(a+b)

import sys

num = int(sys.stdin.readline())

for i in range(num):
    a, b = map(int, sys.stdin.readline().split())
    print(a+b)