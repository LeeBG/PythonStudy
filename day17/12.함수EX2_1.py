"""
함수 3형식 추가 문제
1. 단어 5개를 입력을 받아 리스트에 보관하고
    이를 반환하는 함수인 get_words 를 정의하세요
    참고 - 반복을 이용하세요.
2. 실수값 하나를 입력을 받아
    원본, 정수부, 실수부를 값으로 보관한 튜플을 반환하는 함수인
    get_values를 정의하세요
    참고 - 반복없이 쉼표로만 구성하세요.
            직접 만들 경우 (A,B,C)로 묶어도 됩니다.
"""

def get_words():
    lst = ["첫","두","세","네","다섯"]
    words = []
    for i in range(5):
        words.append(input("%s번째 단어를 입력하세요 >> "%(lst[i])))
    return words
# 실행코드
words = get_words()
print("입력받은 단어들 :",end=" ")
for word in words:
    print(word,end=" ")
print()

def get_values():
    fnum = float(input("실수 입력 >> "))
    num = int(fnum)
    if fnum > 0:
        fnum2 = fnum-num
    else:
        fnum2 = (fnum-num) * -1
    return fnum,num,fnum2

result = get_values()
# print(result) # 튜플에 담긴것 확인
print("원본 : %.2f"%(result[0]))
print("정수부 : %d"%(result[1]))
print("실수부 : %.2f"%(result[2]))