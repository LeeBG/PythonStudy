"""
조건
1. 1부터 10까지의 정수를 반복으로 출력하세요.
2. 1부터 100사이의 11의 배수를 반복으로 출력하세요
2. 100부터 1사이의 8의 배수를 반복으로 출력하세요
"""
for i in range(1,11):
    print(i,end=" ")
print()
for i in range(11,100,11):
    print(i,end=" ")
print()
for i in range(100,1,-1):
    if i % 8 == 0:
        print(i,end=" ")
print()

# 첫번쨰 문제가 여기에 섞여들어감 -> 불필요한 연산과정
# + 변수가 추가로 준비됐음 -> 한번만 쓴다면 불필요함
value = 96
for num in range(12):
    print(value,end=" ")
    value -= 8
print()

for num in range(96, 7, -8):
    print(num, end= " ")
print(num)