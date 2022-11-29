"""
조건 
1. 정수 하나를 입력을 받아 1부터 해당 정수까지
    1씩 증가하는 정수들의 합을 구합니다.
2. 구한 합을 외부에 복사하는 함수를 정의하세요.
3. 함수에서 결과를 출력하지 않습니다.
4. 함수명은 get_sum으로 합니다.
결과
합을 구하려는 정수 입력 >> 15
함수에서 구한 합 : 120
"""
def get_sum():
    result = 0
    num = int(input("합을 구하려는 정수 입력 >> "))
    for i in range(1,num+1):
        result += i
    return result

# 함수 호출
result = get_sum()
print("함수에서 구한 합 :",result)