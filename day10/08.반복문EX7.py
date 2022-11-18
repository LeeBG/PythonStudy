"""
조건
1. 1부터 9사이의 정수를 입력을 받아 1부터 해당 정수까지의 합을 구하는 코드입니다.
2. 조건을 만족하지 않는 값은 재입력을 받습니다.
결과
1 ~ 9 중 하나를 입력 >> 8
결과 : 36

1 ~ 9 중 하나를 입력 >> 0
재입력하세요.
1 ~ 9 중 하나를 입력 >> 15
재입력하세요.
"""
num = int(input("1 ~ 9 중 하나를 입력 >> "))

while 1 > num or num > 9:
    num = int(input("재입력하세요\n1 ~ 9 중 하나를 입력 >> "))

# 유한반복 - 값을 온존시킬지에 따라 별개 변수를 준비한다.
# 1) 온존 시킨다.
result = 0
value = 1
while value <= num :
    result += value
    value += 1
print("결과 : %d"%(result))

#2) 온존시키지 않는다.
result = 0
while 1 <= num <= 9 :
    result += num
    num -= 1
print("결과 : %d"%(result))




# 유한 반복 주기
count = 3
num = 0
while count >= 1:
    print("입력기회가 %d번 남았습니다."%(count))
    num  = int(input("1 ~ 9 중 하나를 입력 >> "))
    if num < 1 or num >9:
        count -= 1
        if count >= 1:
            print("재입력하세요")
    else:
        break   # 보조 제어문 : 반복을 강종시킨다.
                # - 무조건 조건문과 연계시켜서 사용한다.
if count >= 1 :
    print('원하는 동작을 수행합니다.')
else:
    print("입력횟수를 전부 소진했습니다.")
# 유한반복이 "범용성이 좋다" ?????? 는 무슨 의미인가??? 
# 유한반복을 유한반복으로 바꾼다.
