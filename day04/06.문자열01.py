"""
문자열의 합치기 : 레고블럭처럼 조립한다.
"""
value1 = input("정수부 입력 >>")
value2 = input("실수부 입력 >>")
fnum = value1 + "."+value2
print(fnum)
fnum = float(fnum)
print(fnum * 5)

# 문자열의 반복 : 밑줄긋기와 비슷한 것을 만들 수 있다.
print("="*30)
word = input("영어 단어 입력 >>")
print(word)
# len() : "길이" 속성이 존재하는 것의 길이값을 구해주는 함수
print("-" * len(word))