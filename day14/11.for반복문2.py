"""
응용 : 입력받은 것을 판별한다.
# 이제 변수에 입력받을 때 바로 형변환 하지 않고 검증을 먼저 받는다
"""
lst = ['0','1','2','3','4','5','6','7','8','9']
while True: # 비교할 대상이 없어지면, True로 설정한다.
    tmp = input("정수 입력 >> ")
    result = True
    for ch in tmp:
        if ch not in lst:
            result = False
            break
    if result:  # while의 조건식이 True이면 안끝나니
        break   # 조건문과 break조합으로 종료를 설정한다.
num = int(tmp)
print(num)