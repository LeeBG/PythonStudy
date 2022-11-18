"""
조건
1. 1부터 40까지의 정수 중 5의 배수만 출력하세요.
2. 1부터 40까지의 정수 중 6의 배수만 출력하세요.

결과

5 10 15 20 25 30 35 40 
6 12 18 24 30 36

"""

num = 1
while num*5 <= 40:
    print(num*5,end=" ")
    num += 1

print()
num = 1
while num*6 <= 40:
    print(num*6,end=" ")
    num += 1
