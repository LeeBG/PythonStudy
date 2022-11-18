"""
유한 반복문은 언제나 규칙성이다.
- 규칙성이 없을 경우, 많은 경우 1씩 증가/감소한다.
"""
num = 10
while num >= 10:
    print("%.2d"%(num),end=" ")
    num += 1
print()

num = 1
while num <= 10:
    # 나오는 숫자를 겸사겸사 이용한다.
    print(num + 10, end = " ")
    num += 1
print()

# 반복횟수를 중점으로 준비한 반복문
count = 10
num = 11
while count >= 1:
    print(num, end=" ")
    num += 1
    count -= 1
print()