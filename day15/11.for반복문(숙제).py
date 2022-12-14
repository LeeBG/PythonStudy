"""
숙제
# 1. for 반복문을 이용하여 구구단 중 6단을 출력하세요.

# 2. 지정한 횟수만큼 Hello를 출력합니다.
#    문자열 곱셈이 아닌 for반복문을 이용해서 진행하세요.

# 3. 내가 입력한 정수가 소수인지 아닌지 여부를 판별하세요.
#    소수는 2이상의 양의 정수 중 약수가 2개뿐인 수입니다.
#    for반복문을 이용합니다.
"""
# 1. 구구단 6단
for i in range(1,10):
    print("6 x %d = %2d"%(i,(6*i)))
print()

# 2. 지정한 횟수 만큼 Hello 출력 
num = input("횟수 입력 >> ") # EX) 3회
num = int(num[:-1])
for i in range(num):
    print("Hello", end=" ")
print()


# 3. 내가 입력한 정수가 소수인지 아닌지 여부를 판별
count = 0

tmp = int(input("소수 판별할 2 이상의 정수를 입력하세요 >> "))
for i in range(1,tmp+1):
    if tmp % i == 0:
        count += 1

if count == 2:
    print("%d는 소수입니다."%(tmp))
else:
    print("%d는 소수가 아닙니다."%(tmp))