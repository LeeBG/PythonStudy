"""
2중 반복문 문제
- 구구단을 전체 출력하세요
 출력형태는 마음대로
"""

for i in range(2,10):
    print("--[",i,"]단--")
    for j in range(1,10):
        print("%d x %d = %2d"%(i,j,(i*j)))
    print()

# 참고 : 그래픽 기능을 쓰지 않는 이상 화면에 출력된 내용은 항상
#       왼쪽에서 오른쪽으로 출력하고 나서 다음줄로 이동한다.

# 참고 : while로 잡을 경우, 변수 조심할 것
print()
num2 = 1
while num2 < 10:
    num1 = 1 # 안쪽 반복문의 변수는 안쪽에 있어야 한다.
    while num1 < 10:
        print("%d x %d = %2d "%(num1,num2,num1*num2),end=" ")
        num1 += 1
    print()
    num2 += 1