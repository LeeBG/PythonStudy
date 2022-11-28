# 다중반복문은 크게 2가지 이유로 준비한다.
# 1) 반복문끼리 서로 일부만 바뀌면서 연동된다.

# # 이런 숫자가 나오게 하고 싶다. (별 의미 없다.)
# print(11,12,13,14)
# print(21,22,23,24)
# print(31,32,33,34)

num = 0

for value in range(10,31,10):
    for num in range(value + 1, value + 5):
        print(num,end=" ")
    print()

# 2) 객체를 제대로 쓰기 위해서 내부에 객체들이 존재할 수 있다.
# 2차원 리스트 : 리스트 내부에 리스트가 있음

lst2d = [
#   x 0  1  2   # y 
    [10,20,30], # 0
    [11,21,31], # 1
    [12,22,32]  # 2
]
# 사용방식 : y부터 인덱싱후 x인덱싱, y와x가 교차되는 것을 가져온다.
print(lst2d[2][0])
# 값만 쓴다 -> for문 
for lst1d in lst2d:
    for value in lst1d:
        print(value, end= " ")
print()

# 인덱싱으로 교체도 가능하다.
for y in range(3):
    for x in range(3):
        print(lst2d[y][x],end=" ")
    print()

# 인덱싱으로 교체도 가능하다.
for x in range(3):
    for y in range(3):
        print(lst2d[y][x],end=" ")
    print()
