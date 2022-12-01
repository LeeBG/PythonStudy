"""
# 내장 모듈 - 파이썬을 설치할 때 같이 달려오는 것
# 엄청 많기 때문에 파이썬 레퍼런스를 통해 확인할 수 있다.
# 검색요령 python 문서(documentation) 모듈명 

# 모듈 불러오기
# 주의사항) 직접 정의한 함수보다 위에 작성. 최상단에 작성해야 함
"""

import random # 난수와 관련된 함수가 들어있는 모듈
import time # 시간과 관련된 함수가 들어있는 함수
import os # 운영체제와 상호작용하는 함수가 들어있는 모듈

# randint(A,B) : A이상 B이하의 임의의 정수값 하나를 반환한다.
#                사용할 때 마다 다른 값이 나온다.
lotto = []
for num in range(6):
    lotto.append(random.randint(1, 45))
print(*lotto)

# choice(목록) : 목록중에서 하나를 골라서 반환한다.
lst = ["A","B","C","D"]
result1 = random.choice(lst)
word = "abcd"
result2 = random.choice(word)  # 문자열도 가능
# dic = {'A':1,'B':2,'C':3}     # 딕셔너리는 호환이 안되서 불가능
# result3 = random.choice(dic)
print(result1,result2)

lst = ['+','+']
print(lst.index("+"))

# time() : 1970년 1월 1일 0시 0분 0초 기준 현재까지의 누적시간초를 반환하는 함수
# - 각종 소요시간 측정에 활용할 수 있다.
start = time.time()
end = time.time()
print("%.15f"%(start))
print("%.15f"%(end))

start = time.time()
result1 = 0
num1 = 1
while num1 <= 500000:
    result1 += num1
    num1 += 1
end = time.time()
print("%.2f"%(end-start))

start = time.time()
result2 = 0
num2 = 1
for i in range(1,500001):
    result2 += i
end = time.time()
print("%.2f"%(end-start))

# - 원래 반든 코드에서 개선을 했을 경우, 내부에서 측정을 해봐야 알 수 있다.

print(time.ctime())

# 지금 우리가 보고 있는 결과창 명령프롬프트 or 터미널
# system() : 터미널 명령어를 대신 입력하는 명령어
# - 시스템 관련 지식이 어느정도 있어야 활용이 가능하다.
os.system("pause")  # 터미널 자체를 일시정지 시키는 명령어
os.system("cls")    # 터미널에 출력된 내용을 모드 치워주는 명령어

num = 0
while num <= 0:
    num = int(input("0보다 큰 양수를 입력 >> "))
    if num <= 0:
        print("0이하를 입력하지 마시오.")
        os.system("pause") # 사용자에게 출력하는 메시지를 확인하게 할 시간확보
        os.system("cls")   # + 불필요한 출력내용을 제거한다.
print(num)