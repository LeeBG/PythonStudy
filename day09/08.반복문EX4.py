"""
조건
1. 10부터 1까지 1씩 감소하는 정수들을 출력하세요
2. 11부터 20까지 1씩 증가하는 정수들을 출력하세요
"""

num = 10
while num >= 1:
    print("%.2d"%(num),end=" ")
    num -= 1
print()
num = 11
while num <= 20:
    print("%.2d"%(num),end=" ")
    num += 1

