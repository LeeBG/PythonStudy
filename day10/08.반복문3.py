"""
반복문 값의 누적 / 누적값 활용

무한반복 - (자료)입력
★ 유한반복 - (자료)처리
유한반복 - (정보)입력
"""
# 반복을 이용한 연산 -> 일정한 규칙성이 존재해야한다.
# - 만들기 위한 과정은 똑같음
result = 0
num = 1
while num <= 10:
    result += num
    num += 1

print(result) # 1+2+3+4+5+6+7+8+9+10

# 누적을 숫자만이 아니라, 문자열로 할 수 있다.
result = ""     # Empty String / 깡통문자열(비어있는 문자열)
num = 1
while num <= 10:
    result += str(num)
    num +=1
print(result)

result = ""     # Empty String / 깡통문자열(비어있는 문자열)
num = 1
while num <= 10:
    result += "="
    num +=1
print(result,"="*10)