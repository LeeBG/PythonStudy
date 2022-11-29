"""
함수 내부에서 값을 여러개 복사되도록 할 수 없나??
"""
def test1():
    num1 = int(input("정수1 입력 >>"))
    num2 = int(input("정수2 입력 >>"))
    return num1
    return num2 # 얘가 작동을 안함 return은 함수가 종료되기 떄문

# 해결책 1 : 딕셔너리 사용
# - 이 값들에 각각 이름을 붙여서 구별해서 써야할 때
def solve1():
    num1 = int(input("정수1 입력 >>"))
    num2 = int(input("정수2 입력 >>"))
    result = {"num1":num1,"num2":num2}
    return result

# 해결책 2 : 리스트
# - 값들만 필요할 때 유용함
def solve2():
    num1 = int(input("정수1 입력 >>"))
    num2 = int(input("정수2 입력 >>"))
    return [num1,num2] # 리턴 다음에은 상수값도 올 수 있다.

# 해결책 3 : 쉼표로 구분해서 리턴하기
# - 파이썬에서 값이 오른 자리에 쉼표를 쓰면 자동으로
#   튜플 자료구조를 하나 생성해서 하나로 묶는 문법이 존재한다.
# - 순서를 바꿀 수 없고, 반드시 정해진 순서로만 나오게 됨
#   참고 : 튜플은 반복으로 못만듬
#   - 리스트를 형변환(tuple()) 시키거나, 직접 만들어야 한다.
def solve3():
    num1 = int(input("정수1 입력 >>"))
    num2 = int(input("정수2 입력 >>"))
    return num1,num2

result0 = test1()
result1 = solve1()
result2 = solve2()
result3 = solve3() # (num1,num2) # 값을 못바꾸는 리스트 = "튜플"이다. 

print(result0)
print(result1)
print(result2)
print(result3) # (num1,num2) # 값을 못바꾸는 리스트 = "튜플"이다. 

