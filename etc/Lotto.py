# 로또 자동 번호 뽑기
import random
import time
# 로또만들기
startTime = time.time() # 실행시간 측정하기

a = list(range(1,46)) #중복체크를 위한 리스트
b = list()
while(len(b)<6):
    num = random.randint(1,45) # 랜덤
    if num in a:#중복체크
        a.remove(num)
        b.append(num)
b.sort()
print(b)
print("실행시간은",time.time()-startTime,"초입니다.")
