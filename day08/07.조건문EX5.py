"""
조건
1. 정수 하나를 입력을 받아 변수에 저장합니다.
2. 입력된 정수가 음수이면 <음수>라고 출력합니다.
3. 입력된 정수가 양수이면 <양수>라고 출력합니다.
4. 입력된 정수가 0이면 <0>이라고 출력합니다.
"""
#if/else 사용시
num1 = int(input("정수 입력 >> "))

if num1 < 0:
    print("음수입니다.")
else:
    if num1 == 0 :
        print("%s 입니다."%(num1))
    else:
        print("양수입니다.")

# elif사용시
if num > 0:
    result = "양수"
elif num < 0:
    result = "음수"
else:
    result = "0"
print("%s입니다."%(result))