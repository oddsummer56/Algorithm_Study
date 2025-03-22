# # 25083
"""
\n	문자열 안에서 줄을 바꿀 때 사용
\t	문자열 사이에 탭 간격을 줄 때 사용
\\	문자 \를 그대로 표현할 때 사용
\'	작은따옴표(')를 그대로 표현할 때 사용
\"	큰따옴표(")를 그대로 표현할 때 사용

"""
# print("         ,r\'\"7")
# print("r`-_   ,\'  ,/")
# print(" \. \". L_r\'")
# print("   `~\\/")
# print("      |")
# print("      |")

# # 3003
# a, b, c, d, e, f = list(map(int, input().split()))
# print(1-a, 1-b, 2-c, 2-d, 2-e, 8-f)

# # 2444

# num = int(input())

# for i in range(1, num+1):
#     print((num-i)*" "+"*"*(2*i-1))

# for i in range(num-1, 0, -1):
#     print((num-i)*" "+"*"*(2*i-1))

# # 10988

# word = input()
# flip_word = word[::-1]

# if word == flip_word:
#     print("1")
# else:
#     print("0")

###############################################################

# # 1157

# word = input().upper()
# word_list = list(set(word))

# cnt = []
# for i in word_list:
#   count = word.count
#   cnt.append(count(i))

# if cnt.count(max(cnt)) > 1:
#   print("?")

# else:
#   print(word_list[(cnt.index(max(cnt)))])


# # 2941

# aph = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
# word = input()

# for i in aph:
#     word = word.replace(i, "0")

# print(len(word))
  
# # 1316

# N = int(input())
# cnt = N

# for i in range(N):
#     word = input()
#     for j in range(0, len(word)-1):
#         if word[j] == word[j+1]:
#             pass
#         elif word[j] in word[j+1:]:
#             cnt -= 1
#             break

# print(cnt)
    
# 25206

# score = {'A+': 4.5, 'A0': 4.0, 'B+': 3.5, 'B0': 3.0, 'C+': 2.5, 'C0': 2.0, 'D+': 1.5, 'D0': 1.0,'P': 0.0, 'F': 0.0}


# for i in range(20):
#     tot_score, tot_grade = 0, 0
#     lec, score, grade = map(str, input().split())
#     if grade == 'F' or 'P':
#         pass
#     else:
#         tot_score += tot_score
#         tot_grade += int(score)*int(score[grade])

#     print(tot_grade, tot_score)
# print(tot_grade/tot_score)

rating = ['A+', 'A0', 'B+', 'B0', 'C+', 'C0', 'D+', 'D0', 'F']
grade = [4.5, 4.0, 3.5, 3.0, 2.5, 2.0, 1.5, 1.0, 0]

total = 0	# 학점 총합을 담을 변수
result = 0	# (학점 * 과목평점) 총합을 담을 변수
for _ in range(20) :
    s, p, g = input().split()
    p = float(p)
    if g != 'P' :	# 등급이 P인 과목은 계산 안함
        total += p
        result += p * grade[rating.index(g)]

print('%.6f' % (result / total))
