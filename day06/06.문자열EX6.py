"""
조건
1. 아래의 문자열을 인덱싱하여 결과처럼 출력하세요
2. 출력되는 문자열은 하나의 값이다.
3. 쉼표로 구분되지 않는다.

word = "WLE\n!ORDH"

결과 
HELLO
WORLD!
"""
word = "WLE\n!ORDH"
print(word[-1]+word[2]+word[1]+word[1]+word[-4]+word[3:4]+word[0]+word[-4]+word[-3]+word[1]+word[-2]+word[-5])

# 확인(문제와 상관없음)
print(len(word))
for i in range(len(word)):
    print("["+word[i]+"]",end=" ")
# 주의사항: 이스케이프는 통째로 한개의 인덱스로 취급한다는 것!!
