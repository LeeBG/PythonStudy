"""
4형식 - 게임 내부의 미니게임
"""
def program(): # 기존의 함수
    num1 = int(input("정수1 입력 >> "))
    num2 = int(input("정수2 입력 >> "))
    result = num1 + num2
    print("합 : ",result)

"""
3형식 : 함수 내부에 있는 값을 함수 외부로 '복사' 시켜주는 함수
- 3형식부터는 함수명을 동사로 설정한다. get,input,push,put,do...등
"""
def get_Sum():
    num1 = int(input("정수1 입력 >> "))
    num2 = int(input("정수2 입력 >> "))
    result = num1 + num2
    
    # return 함수내부에 있는 값을 호출된 곳으로 
    # 복사시키면서 함수를 종료하는 예약어
    return result
    # 복사시키는 값은 주로, 내부에서 제일 가치가 높은 것을 지정

# program()

# 3형식의 호출 : 변수 = 함수명()
# - 함수에서 나오는 값을 변수에 저장해서 사용한다.
value = get_Sum()
print("합 :",value)
