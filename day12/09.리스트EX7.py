# 조건(반복을 이용합니다.)
# 1. 정수값을 5번 입력을 받아 리스트에 보관합니다.
# 2. 값이 보관된 리스트를 출력합니다.
# 3. 리스트에 보관된 값들을 반복을 이용하여 출력합니다.
#     출력은 결과를 참조하세요.
lst = []
num = 1
while num <= 5:
    lst.append(int(input("%d번 정수 >>"%(num))))
    num += 1

print("-출력구간-")
print(lst)

num = 1
while num <= 5:
    print("뒤에서 %d번 :"%(num),lst[len(lst)-num])
    num += 1