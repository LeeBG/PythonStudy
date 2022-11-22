"""
리스트의 운용방식은 기본적으로 
반복을 통해 준비하는 숫자를 응용한다.

주의사항 : 서로 다른 '목적'을 가진 코드는 합치지 않는다.
-> 자료 - 처리 - 출력 - 정보

"""
# 자료들 입력 / 수집
lst = []
index = 0
while index < 3:
    tmp = input(">> ")
    lst.append(tmp)
    count -= 1

# 입력 / 수집된 자료들을 처리중
result = ""
index = 0
while index < len(lst):
    result += lst[index]
    index += 1

# 정보를 출력
print("결과 : ",result)