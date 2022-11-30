
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
def show_sum(num1,num2):
    print("합 : ",num1+num2)

# 1형식 - 값을 외부에서 받아 가공해서 나온 결과물을 외부로 전달하는 함수
# - 함수명은 동사이고, make / create / clone / copy 등...
def make_sum(num1,num2):
    # 주 목적은 값을 가공(처리)하는 것
    # 내부에서 입력/출력은 없음
    return num1 + num2
    # 주의사항 - 너무 단순한 건 만드나 마나
    # +@ 오버헤드(특정작업을 실행하는데 소모하는 자원)가 함수가
    # 호출될 때마다 발생하기 때문에 너무 자잘한 건 만들어봤자 좋지 않다.
value1 = 15
value2 = 14
result = make_sum(value1,value2)
print("결과 :",result)