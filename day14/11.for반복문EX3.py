"""
조건
1. 리스트에 정수값을 입력을 받아 저장합니다.
2. 0이 입력되면 종료하고, 그 외에는 리스트에 저장합니다.
3. 리스트에 저장된 값을 출력합니다.
4. 리스트에 저장된 값들의 합을 구하여 출력합니다.
"""
tmp = 1
count = 1
lst = []
print("--입력구간--") # 입력은 while로 받는 것이 깔끔하다.
while tmp != 0:
    tmp = int(input("%d번 정수 >> "%(count)))
    if tmp != 0:    # 0을 리스트에 담으면 안되기 때문!!
        lst.append(tmp)
    count += 1 
    
# 목적이 다른것들은 합치지 않는다.
sum = 0
for num in lst:
    sum += num

print("--출력구간--")
print("리스트에 저장된 값들")
for num in lst:
    print(num,end=" ")
    # sum += num
print("\n저장된 값들의 합 : %d"%(sum))

for num in range(46):
    print(num)