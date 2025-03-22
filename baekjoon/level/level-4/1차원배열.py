import sys
input = sys.stdin.readline

# # 10807

# a = int(input())
# number = list(map(int, input().split()))
# n = int(input())
# print(number.count(n))

# # 10871

# N, X = map(int, input().split())
# lists = list(map(int, input().split()))
# # for i in range(len(lists)):
# #     if lists[i] < X:
# #         print(lists[i], end=" ")

# for i in lists:
#     if i < X:
#         print(i, end=" ")

# # 10818

# a = int(input())
# lists = list(map(int, input().split()))
# print(min(lists), end=" ")
# print(max(lists))

# # 2562

# lists=[]
# for i in range(9):
#     b = int(input())
#     lists.append(b)
    
# max=max(lists)
# num=lists.index(max)
# print(max)
# print(num+1)

# # 10810
# input = sys.stdin.readline
# a, b = map(int, input().split())
# arr = [0 for _ in range(a)]    
# #num1, num2, num3 = map(int, input().split())

# for _ in range(b):
#     num1, num2, num3 = map(int, input().split())
#     for i in range(num1-1, num2):
#         arr[i]=num3

# for i in range(a):
#     print(arr[i], end=" ")


# # 10813
# input = sys.stdin.readline
# a, b = map(int, input().split())
# arr = list(range(1, a+1))

# for i in range(b):
#     num1, num2 = map(int, input().split())
#     arr[num1-1], arr[num2-1] = arr[num2-1], arr[num1-1]

# # for x in arr:
# #     print(x, end=" ")

# print(*arr)

# # 5597
# arr = list(range(1, 31))

# for i in range(28):
#     num = int(input())
#     arr.remove(num)

# print(min(arr))
# print(max(arr))

# # 3052
# list=[]
# for i in range(10):
#     num = int(input())
#     val = num%42 
#     list.append(val)

# result = set(list)
# print(len(result))

################# 1517 #################

# n = int(input())
# array = list(map(int, input().split()))
# swap_count = 0

# def merge_sort(array):
#     global swap_count
#     if len(array) < 2:
#         return array

#     mid = len(array) // 2
#     low_arr = merge_sort(array[:mid])
#     high_arr = merge_sort(array[mid:])

#     merged_arr = []
#     l = h = 0

#     while l < len(low_arr) and h < len(high_arr):
#         if low_arr[l] <= high_arr[h]:
#             merged_arr.append(low_arr[l])
#             l += 1
#         else:
#             merged_arr.append(high_arr[h])
#             swap_count += len(low_arr) - l  # Swap 발생 횟수 추가
#             h += 1

#     merged_arr += low_arr[l:]
#     merged_arr += high_arr[h:]
#     return merged_arr

# merge_sort(array)
# print(swap_count)

# # 10811
"""
a[ start : end : step ]
step이 양수일 때: 오른쪽으로 step만큼 이동하면서 가져옴.
step이 음수일 때: 왼쪽으로 step만큼 이동하면서 가져옴.

a.reverse() # 리스트를 뒤집고, return 값 없음음
list(reversed(a)) # 뒤집어진 리스트의 값을 return 해줌
"""

# n, m = map(int, input().split())
# arr = list(range(1, n+1))

# for i in range(m):
#     a, b = map(int, input().split())
#     arr[a-1:b] = arr[a-1:b][::-1]

# print(*arr)

# 1546
"""
max(arr)
sum(arr)
"""
a = int(input())
score = list(map(int, input().split()))
sum = sum(score)
max = max(score)
result = (sum/max*100)/a
print(result)