"""
조건
1. 리스트를 이용하여 딕셔너리의 키 목록을 생성합니다.
   키 목록은 이름,나이,취미,꿈 입니다.
2. 생성된 리스트를 이용하여 딕셔너리에 값을 저장합니다.
3. 딕셔너리에 저장된 값은 아래와 같이 출력합니다.
결과
--입력구간--
이름 >> 홍길동
나이 >> 23세
취미 >> 영화시청
꿈 >> 개발자
--출력구간--
이름     : 홍길동
나이     : 23세
취미     : 영화시청
꿈       : 개발자
"""
dic = {}
lst = ["이름","나이","취미","꿈"]
index = 0
print("--입력구간--")
while index < len(lst):
    dic[lst[index]] = input(lst[index]+" >> ")
    index += 1

index = 0
print("--출력구간--")
while index < len(lst):
    print("%s \t : %s"%(lst[index],dic[lst[index]]))
    index += 1

"""
변수 명명법
1) _를 이용하는 방식 - _가 띄어쓰기를 대체한다.
ex) my_info = {}

2) 카멜표기법 - 일정 규칙에 따라 값의 종류를 구별하는 방법
- 다른 단어가 들어갈 때 다음 단어의 첫 문자를 대문자로 치환한다.
- 변수인 경우 소문자로 시작 / 상수처럼 쓰는 경우 대문자만 사용 등
- 낙타의 등의 형태에서 비롯된 표기법이다.
ex) myInfo = {}
"""
print("----- 또 다른 방법 -----")
myInfo = {}
items = ["이름","나이","취미","꿈"]
index = 0
while index < len(items):
    myInfo = [items[index]] = input(items[index]+" >> ")
    index += 1
index = 0
while index < len(items):
    print(items[index] + "\t:", myInfo[items[index]])
    index += 1
