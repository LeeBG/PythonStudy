"""
조건
1. 비어있는 리스트를 생성합니다.
2. 생성한 리스트에 정수값을 5번 입력을 받아 추가하세요
3. 생성된 리스트를 출력하여 확인합니다.
4. 1번 인덱스에 있는 자료를 제거하고 출력합니다.
5. 제거된 리스트에서 다시 1번,2번 인덱스에 있는 자료를 제거하고
    출력합니다.
결과
5개의 정수를 입력하세요111 222 333 444 555
최초 :  [111, 222, 333, 444, 555]
제거 :  [111, 333, 444, 555]
제거 :  [111, 555]
"""
lst = []
num = 0

# split을 쓸 경우  - 수량이 만족하는지를 확인해야한다.
# lst.append(int(input(">> ")) )
# lst.append(int(input(">> ")) )
# lst.append(int(input(">> ")) )
# lst.append(int(input(">> ")) )
# lst.append(int(input(">> ")) )

# 재입력
while len(lst) != 5:
    lst = input("5개의 정수를 입력하세요").split()

# 2) 내부에 있는 값을 목적에 맞게 형변환 해야한다.
index = 0
while index < len(lst):
   lst[index] = int(lst[index])
   index += 1

print("최초 : ",lst)
lst[1:2] = []
print("제거 : ",lst)
lst[1:3] = []
print("제거 : ",lst)
