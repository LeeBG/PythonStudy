"""
1. 5번이 아니라 횟수를 지정하여 추가합니다.
2. (선택사항) 횟수로 0을 넣을 경우, 입력을 받는 
   정수값이 0이 아니라면 계속 추가합니다.
3. 저장된 값들은 출력하지 않고, 합만 구하여 출력합니다.
4. (선택사항) 음수합/양수합을 구하여 출력하세요
5. 선택사하은 필수가 아님

결과
"""
lst = []
num = 1
result = 1

# 입력구간
numOfTry = int(input("횟수 >> "))
tmp = int(input("%d번 정수 >> "%(num)))

if numOfTry == 0:
    while lst[num-1] != 0:
        lst.append(tmp)
        num += 1
elif numOfTry > 0 :
    while num <= numOfTry:
        lst.append(tmp)
        num += 1
else :
    print("횟수입력으로 음수 입력")

count = 0
plus = 0
minus = 0
# 입력 수집된 정보를 처리
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