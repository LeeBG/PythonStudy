"""
헷갈리지 않도록 값을 한 종류만 받아서 어떻게 운용하는가?
-> 리스트의 특성을 첨가하여 운용한다.
-> 리스트는 문자열 처럼 합치기와 반복하기가 가능한다.

"""

# 합치기 - 서로 다른 리스트를 하나로 합치는 용도
# -> 값을 추가하는 방식으로 이용할 수 있다.
# -> 이를 기반으로 반복문을 구성하여 이용한다.

# 1) 유한반복기반 입력
lst = []
num = 1
# 다중반복문 중 이중반복
while num <= 5: # 필요한 값의 수량을 확보
    tmp = int(input(">> ")) # 값들을 필요한 것만 걸러서 저장
    while tmp <= 0:
        tmp = int(input(">> "))
    lst += [tmp]
    num += 1
print(lst)

# 2) 무한 반복기반 입력
lst = []
num = 0
while num <= 0: # 반복문의 조건식이 참인 값을 리스트에 보관한다.
    tmp = int(input(">> "))
    if num <= 0:
        lst += [num]
print(lst) # 양수가 들어오면 바로 리스트 출력, 반복문 종료
