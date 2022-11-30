# 4형식 - 기본형태
def program():
    num1 = int(input("정수1입력 >> "))
    num2 = int(input("정수2입력 >> "))
    print("함 : ",num1+num2)

# 3형식 - 외부로 값이 전달됨
def get_sum():
    num1 = int(input("정수1 입력 >> "))
    num2 = int(input("정수2 입력 >> "))
    return num1+num2

# 2형식 - 자료를 외부에서 복사 받아서 이용한다.
# - 함수명은 동사로 설정하며, show, print, present 등
# - 외부에서 값을 복사받기 위해서... 매개변수(parameter)를 준비한다.

def show_sum1(num1,num2):
    # - 함수 내의 변수와 함수 외부의 변수는 항상 동명이인관계
    # - 값을 불러오는 용도가 아닌, 값을 받기 위한 용도
    print("합 : ",num1+num2)

# - 주의 : 함수 내부에 없는 변수를 쓸 경우, 파이썬이 반강제로 맞춰버린다.
#          비정상 동작이니 주의할 것
# def show_sum2():
#     print("합 : ",num1+num2)

num1 = 10

show_sum1( num1, 15 )
# show_sum2()


# # 4형식의 호출
# program() 

# # 3형식의 호출
# result1 = get_sum()
# result2 = get_sum()
# print("정수 4개의 합 :",result1+result2)

