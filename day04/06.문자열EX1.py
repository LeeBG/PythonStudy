"""
조건
1. 자신의 이름의 성과 명을 각각 따로 입력을 받습니다.
2. 입력을 받은 값을 각각 출력합니다.
3. 이를 하나로 합쳐서 출력합니다.
4. 출력할 때마다 = 을 15개씩 출력하여 구분합니다.
"""

lastName = input("성 입력 >> ")
firstName = input("명 입력 >> ")

print("="*15)
print("입력된 성:"+lastName)
print("="*15)
print("입력된 명:"+firstName)
print("="*15)
print("성명:"+ lastName+firstName)
print("="*15)


age = int(input("나이 입력 >>"))
print("나이 : ",age,"세")
# str형변환은 문자열이 아닌 것을 문자열로 바꿔서 그 특성을 이용하게 만든다.
print("나이 : "+str(age)+"세")