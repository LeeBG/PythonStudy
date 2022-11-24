"""
조건
1. while 반복문을 이용하여 리스트에 1부터 10까지의 정수를 보관합니다.
2. 보관된 값들을 for 반복을 이용하여 출력하세요
결과
반복으로 만들어진 리스트
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
반복으로 출력된 값들
1 2 3 4 5 6 7 8 9 10
"""

# 대부분의 경우 입력받을 때는 좀 더 유연한 while을 사용한다.
lst = []
count = 0
while count < 10:
    count += 1
    lst.append(count)

print('반복으로 만들어진 리스트')
print(lst)

print('반복으로 출력된 값들')
for i in lst:
    print(i,end=" ")
print()