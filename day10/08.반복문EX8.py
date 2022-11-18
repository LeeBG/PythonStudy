"""
조건
1. 임의의 정수를 입력을 받아 0부터 해당 정수까지의 합을 구하는 코드입니다.
2. 양의 정수이면 양수 합, 음의 정수이면 음수합 입니다.

결과
정수 입력 >> 10
결과 : 55

정수 입력 >> -5
결과 : -15
# 반복은 "방향"이 생긴다. 증가/감소를 의미한다.
# 방향이 다르면 합칠 수 없다.
# 범위가 달라도 합칠 수 없다
"""
num = int(input("정수 입력 >> "))
result = 0                      # num을 0을 입력하면 0을 출력한다. 0으로 초기화
while num < 0:
    result += num
    num += 1
while num > 0:
    result += num
    num -= 1
print("결과 : %d"%(result))


# 이쁘게 만들기
limit = -num if num < 0 else num
# ※ 조건연산자 : 값만 선택해주는 연산자

while limit > 0:
    result += limit
    limit -= 1
    if num < 0:
        result *= -1
print("결과 :",result)