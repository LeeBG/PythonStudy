"""
다중 반복문 - 반복문 내부에 반복문이 중첩되어 들어있는 제어문
-> 기본적으로 시계와 같은 논리로 작동한다.

"""
for num3 in range(1,4):# 3차원 반복문
    print(num3+20)
    for num2 in range(1,5): # 2차원 반복문
        print(num2 + 10, end = " ")
        for num1 in range(1,6): # 단일 반복문
            print(num1, end=" ")
        print()
# 3차원 : 가로 세로 높이가 존재하기 된다.


# 다중 반복문은 서로 연계되는 구조이고, 안쪽의 반복문이 다 끝나야
# 바깥의 1회차가 끝난다.
for num3 in range(1,4):# 3차원 반복문
    for num2 in range(1,5): # 2차원 반복문
        for num1 in range(1,6): # 단일 반복문
            print("%d시간 %d분 %d초"%(num3,num2,num1))
        print()