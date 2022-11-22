# 리스트 - 변수(값)의 묶음
# - 목록을 만들어 써야 하면, 그 때 준비하여 사용한다.
# 1) 비어있는 리스트 - 필요한 것을 내부에 추가하여 사용한다.
lst1 = []      # 비어있는 리스트
num = 1

while num > 0:
    num = int(input(">> "))
    if num > 0:
        lst1.append(num)
print(lst1)
num = 1
while num <= 10:
    lst1.append(num)
    num += 1
print(lst1)

# 2) 값이 들어있는 리스트 -> 인덱싱한다.
# -> 값이 보관된 리스트의 운용에는 반복이 들어간다.
# -> 인덱스를 변수로 치환하여 운용한다.

lst2 = [10,20,30]   # 미리 값을 넣어 초기화
index = 0
while index <= 2:
    print(lst2[index],end=" ")
    index +=1 
print()

# 리스트는 문자열처럼 len을 이용해 전체 크기를 구할 수 있음
# 팁 : x와y가 정수값만 나온다면  x <= y == x < y + 1
index = 0
while index < len(lst1):
    print(lst1[index],end=" ")
    index += 1
print()