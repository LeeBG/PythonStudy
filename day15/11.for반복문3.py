"""
1) for 는 목록이 있어야만 돌릴 수 있다.
2) 그 목록은 while에 의해서만 만들수 있다.
3) 목록을 만들어주는 함수를 이용해 범용으로 쓴다.
"""
# num = 1
# lst = []
# while num < 11:
#     lst.append(num)
#     num += 1

# range는 list와 비슷한 무언가를 준비해주는 함수(range)
# lst = range(1,11)    
# range()는 1회성으로 쓰인다(숫자로만 쓸 수 있다.)
# -> 필요한 for제어문에 바로 작성하여 쓰는 1회용 목록

# 1. range( count ) : count회 만큼 반복 0부터 count-1까지의 숫자를 준비
# -> count <= 0 이면 반복을 하지 않는다.
for value in range(5):
    print(value, end=" ")
print()
for value in range(-5):
    print(value, end=" ")
print()
for value in range(0):
    print(value, end=" ")
print()

# 2. range(start, end+1) : start부터 end까지 1씩 더하며 반복한다.
#  총(end+1-start)회 반복 
# -> 두 수가 서로 다르면서, start가 end보다 작거나 같아야 함
for value in range(-5,-1):
    print(value, end= " ")
print()

for value in range(-1,-5):
    print(value,end=" ")
print()

for value in range(-5,-4):
    print(value,end=" ")
print()

# 3. range(p1, p2, 증감계수)
# - 반복횟수가 파악이 안됨.
# - 반복횟수보다, 특정한 규치이 존재하는 숫자 준비가 주 목적
for value in range(1,11,2): # step이 양수이면 p1이 p2보다 작아야한다.
    print(value,end=" ")
print()

for value in range(1,11,-2):# step이 음수이면 p1이 p2보다 커야한다.
    print(value,end=" ")
print()

for value in range(11,1,2): # step이 양수이면 p1이 p2보다 작아야한다.
    print(value,end=" ")
print()

for value in range(11,1,-2):# step이 음수이면 p1이 p2보다 커야한다.
    print(value,end=" ")
print()