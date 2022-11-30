"""
조건
1. 짝수는 1만큼 증가, 홀수는 1만큼 감소한 값이 나옵니다.
2. 함수에서 입력 / 출력 안합니다.
3. 함수명은 change 입니다.
"""
# 홀수 짝수 판별 함수
def change(num,i):
    if num % 2 == 1:
        num -= 1
    else:
        num += 1
    return num,i+1

# 입력단
lst = []
for i in range(4):
    lst.append(int(input("정수입력 >>")))

# 출력
for i in range(4):
    num = lst[i]
    result = change(num,i)
    print("결과%d :%d"%(result[1],result[0]))
