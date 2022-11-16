"""
조건
1. 2개의 정수를 입력을 받아 첫번째를 두번쨰로 나눕니다.
2. 첫번째가 두번째의 배수로 식별되었으면 몫연산이며
   그 외에는 소수점 한자리까지 출력합니다.
3. 예외인 경우의 수가 존재합니다. 이를 찾아내어 <연산불가>라고 합니다.

결과
결과 : 4.5      // 18과 4를 입력할 경우
결과 : 2        // 8과 4를 입력할 경우
결과 : 연산불가 // 8과 ???을 입력할 경우(0을 나누는 경우도 불가능)
"""

# 파이썬의 예외처리 예습
# 도움 받은 사이트 : https://dojang.io/mod/page/view.php?id=2398
try:
    num1 = int(input("정수 입력 >> "))
    num2 = int(input("정수 입력 >> "))
    # 서식
    word = "결과 : %s"

    if num2 == 0:
        result = "연산불가"
    elif (num1 % num2) == 0:
        result = num1 // num2
    else:
        result = num1/num2  
except ValueError:
    result = "연산불가"

# 출력
print("결과 : %s"%(result))