"""
1. 5번이 아니라 횟수를 지정하여 추가합니다.
2. (선택사항) 횟수로 0을 넣을 경우, 입력을 받는 
   정수값이 0이 아니라면 계속 추가합니다.
3. 저장된 값들은 출력하지 않고, 합만 구하여 출력합니다.
4. (선택사항) 음수합/양수합을 구하여 출력하세요
5. 선택사하은 필수가 아님

결과
횟수 >> 7
정수 >> -123
정수 >> 123
정수 >> 23
정수 >> -1231
정수 >> -12344
정수 >> 12355
정수 >> 231
값들의 합 : -966
양수 합 : 12732
음수 합 : -13698
"""
lst = []
num = 1
result = 1

# 입력구간
numOfTry = int(input("횟수 >> "))   # ex)6회
if numOfTry == 0:
    tmp = 1
    while tmp != 0:
        tmp = int(input("%d번 정수 >> "%(num)))
        lst.append(tmp)
        num +=1
elif numOfTry > 0 :
    while num <= numOfTry:
        lst.append(int(input("%d번 정수 >> "%(num))))
        num += 1
else :
    print("횟수입력으로 음수 입력")

# 입력 수집된 정보를 처리

count = 0 
plus = 0    # 양수합
minus = 0   # 음수합

while count < len(lst):
    if lst[count] < 0:
        minus += lst[count]
    else :
        plus += lst[count]
    count += 1

# 출력구간
print("값들의 합 : %d"%(plus+minus))
print("양수 합 : %d"%(plus))
print("음수 합 : %d"%(minus))



print("=======================================================")
lst = []
limit = input("횟수 >> ")
limit = int(limit[:-1])
count = 1
if limit == 0:
    num = 1
    while num != 0:
        num = int(input("%d번 정수 >> "%(count)))
        if num != 0:
            lst.append(num)
            count += 1
elif limit > 0:
    while count <= limit:
        lst.append(int(input(str(count)+"번 정수 >> ")))
        count += 1
else:
    print("입력받지 않습니다.")



print("--출력구간--")
print(lst)
result = 0
index = 0
while index < len(lst):
    result += lst[-index]
    index += 1
print("값들의 합 : ",result)
result1 = 0
result2 = 0
index = 0
while index < len(lst):
    if lst[index] > 0:
        result1 += lst[index]
    else:
        result2 += lst[index]
print("양수합:",result1)
print("음수합:",result2)