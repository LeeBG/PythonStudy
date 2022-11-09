# 로또 자동 번호 뽑기
import random
import time
# 로또만들기
a = list(range(1,46)) #중복체크를 위한 리스트
b = list()
startTime = time.time()
while(len(b)<7):
    num = random.randrange(1,46) # 랜덤
    if num not in a:#중복체크
        continue
    else:
        a.remove(num)
        b.append(num)
b.sort()
print(b)
endTime = time.time()

print("실행시간은",endTime-startTime,"입니다.")