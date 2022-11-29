# 불러오는 소스파일에는 무조건 함수만 있어야 한다.

def get_sum():
    result = 0
    num = int(input("합을 구하려는 정수 입력 >> "))
    for i in range(1,num+1):
        result += i
    return result
