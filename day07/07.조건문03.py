"""
조건문은, 필요하면 조건문의 종속문으로 작성 가능하다.
"""
num1 = int(input("정수1 입력 >>"))
num2 = int(input("정수2 입력 >>"))
# 조건문은, 필요하시면 조건문의 종속문으로 작성 가능하다.
# -> 경우의 수를 건져올리는 방식으로 작성한다.
if num1 >= num2 :
    if num1 > num2: # num1 >= num2 and num1 > num2
        print("첫번쨰가 더 큽니다.")
    else: # num1 >= num2 and num1 == num2
        print("서로 같습니다.")
else :
    print("두번째가 더 큽니다.")

# 이럴 떄 사용한다.
if num2 > num1 :
    print("두번째가 더 큽니다.")
else:
    if num1 > num2:
        print("첫번째가 더 큽니다.")
    else:
        print("서로 같습니다.")


# elif : else내부에 if조건문이 있을 때 이를 줄여쓰기 위한 예약어
if num2 > num1 :
    print("두번째가 더 큽니다.")
elif num1 > num2:
    print("첫번째가 더 큽니다.")
else:
    print("서로 같습니다.")