"""
주차 요금 계산기
주차 시간에 따라 요금을 부과하는 프로그램입니다.
30분 이하의 주차시간은 무료입니다.
30분 초과 60분 이하의 주차시간은 기본요금 5000원 입니다.
60분 초과시 10분 단위로 500원씩 부가됩니다.
61분이면 5500원 70분도 5500원 71분은 6000원
"""

parking_time = int(input("주차한 시간을 입력하세요 >> "))

if parking_time <= 30:
    fee = 0
elif parking_time <= 60:
    fee = 5000
elif parking_time % 10 == 0:
    fee = 5000 + 500*((parking_time-60)//10)
else:
    fee = 5000 + 500 * ((parking_time-60)//10+1)

print("주차요금은 총 %d원입니다."%(fee))