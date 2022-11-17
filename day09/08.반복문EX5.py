"""
조건
1. 1부터 40까지의 정수 중 5의 배수만 출력하세요.
2. 1부터 40까지의 정수 중 6의 배수만 출력하세요.

결과

5 10 15 20 25 30 35 40 
6 12 18 24 30 36

"""

num = 0
while num <= 40:
    num += 1
    if num % 5 == 0:
        print(num,end=" ")

print()
num = 0
while num <= 40:
    num += 1
    if num % 6 == 0:
        print(num,end=" ")
        
