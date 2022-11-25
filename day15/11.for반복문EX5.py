"""
조건
1. 내가 입력한 양의 정수의 약수들을 모두 출력하세요.
2. 양의 정수가 아니면 재입력을 받습니다. 0도 포함입니다.

결과
약수를 구할 양수 입력 >> 0
약수를 구할 양수 입력 >> -15
약수를 구할 양수 입력 >> 15

15의 약수들
1, 3, 5, 15
"""

num = 0
while num <= 0:
    num = int(input("약수를 구할 양수 입력 >> "))
# 출력문
print("%d의 약수들"%(num))
for i in range(1,num+1): # 1은 모든 양의 정수의 약수
    if i == num:
        print(i)
    elif num % i == 0:
        print(i,end=", ")
    

# num = 0
# while num <= 0:
#     num = int(input("약수를 구할 양수 입력 >> "))
# # 출력문
# # 팁 : 숫자 자체에서는 규칙성이 없는 경우가 많겠지만...
# #      숫자들의 특성이 반복에 도움되는 경우가 존재한다.
# print("%d의 약수들"%(num))
# for i in range(1,num//2 + 1): # 1은 모든 양의 정수의 약수
#     if num % i == 0:
#         print(i,end=", ")
# print(num)
    
