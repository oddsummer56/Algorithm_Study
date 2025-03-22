# # 27866

# word = input()
# a = int(input())
# print(word[a-1])

# # 2743

# print(len(input()))

# # 9086

# num = int(input())

# for i in range(num):
#     word = input()
#     print(word[0]+word[-1])

# # 11654
"""
# 문자 -> 아스키코드 출력 : ord()
# 아스키코드 -> 문자 출력 : chr()
"""
# word = input()
# print(ord(word))
# print(chr(int(word)))

# # 11720

# number = input()
# word = input()
# sum=0

# for i in word:
#     num=int(i)
#     sum += num

# print(sum)

# # 10809
"""
word = 'abcde'
x = 'a'

word.find(x)=0
word.find(x, 시작위치, 종료위치)=0

존재하지 않는 값은 -1로 리턴
반면 index()에서는 ValueError 발생생

"""

# word = input()
# list = [-1 for _ in range(26)]

# for i in word:
#     x=ord(i)-97
#     list[x]=word.index(i)
    
# print(*list)


"clean code"
# s = input()
# for i in range(97,123):
#     print(s.find(chr(i)), end=' ')

# # 2675

"""
print("Hello", end='')
print("World")

HelloWorld
"""

# num = int(input())
# for i in range(num):
#     r, word = map(str, input().split())
#     r = int(r)
#     for i in word:
#         print(i*r, end='')
#     print()

# # 1152

# sentence = input().split() 
# print(len(sentence))

# # 2908

# num1, num2 = map(str, input().split())
# num1, num2 = num1[::-1], num2[::-1]
# print(max(num1, num2))

# # 5622
# dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
# word = input()
# tot = 0
# for i in word:
#     for j in dial:
#         if i in j:
#             time = dial.index(j)+3
#             tot +=time
        
# print(tot)

# 11718

while True:
    try:
        print(input())
    except EOFError:
        break

