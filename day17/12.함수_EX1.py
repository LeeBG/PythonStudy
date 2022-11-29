"""
조건
1. 2개의 정수를 입력을 받아 합/차/곱/몫을 출력하는 함수를 정의하세요.
2. 몫을 구할 때 연산이 되지 않는 경우의 수는 <연산불가>라고 출력합니다.
3. 함수명은 calculator로 합니다.
결과 (10과 3을 입력한 경우)
정수1 입력 >> 10
정수2 입력 >> 3
합 : 13
차 : 7
곱 : 30
몫 : 3
"""
def calculator():
    a = int(input("정수1 입력 >> "))
    b = int(input("정수2 입력 >> "))

    # 나누기의 주의사항 : 0으로 절대 나눌 수 없음
    # 몫연산의 주의사항 : 파이썬에서는 소수점의 내림처리. 
    if b == 0:
        print("연산불가")
    else:
        print("합 : %2d"%(a+b)) 
        print("차 : %2d"%(a-b))
        print("곱 : %2d"%(a*b))
        result = int(a/b)
        print("몫 :",result) # 처리
        # result = a // b
        # # 음수 몫에 대한 처리를 해줘야 한다.(소수의 내림)
        # # 나눗값 float에 대한 int() 형 변환을 해도 내림처리가 가능하다.
        # if result >=0:
        #     print("몫 :",result)
        # else:
        #     if a % b != 0:
        #         result += 1
        #     print("몫 :",result)
# 함수 호출하기
calculator()