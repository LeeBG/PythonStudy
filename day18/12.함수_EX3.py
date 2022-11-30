"""
조건
1. 두 정수의 크기를 비교하여 더 큰 값을 출력하세요.
2. 함수에서 입력을 받지 않습니다.
3. 함수명은 show_bigger()로 합니다.
결과
제일 큰 값 : 15  // show_bigger(15,4)
제일 큰 값 : 15  // show_bigger(4,15)
제일 큰 값 : 4   // show_bigger(4,4)
"""
def show_bigger(num1,num2):
    if num1 == num2:
        print("서로 같은 값 : %d"%(num1))
    elif num1 < num2:
        print("제일 큰 값 : %d"%(num2))
    else:
        print("제일 큰 값 : %d"%(num1))
num1 = int(input("비교할 정수1 입력 >>"))
num2 = int(input("비교할 정수2 입력 >>"))

show_bigger(num1, num2)
show_bigger(15, 4)
show_bigger(4, 15)
show_bigger(4, 4)
