# 시간/분
def get_time():
    minute = int(input("시간/분으로 전환할 시간은 몇 분입니까?? >>"))
    hour = int(minute/60)

    # 시간 / 분으로 분리하는 알고리즘
    # 조건문을 통해 선택하여 실행되도록 만들 수 있음
    if minute < 0:
        minute = minute%60
        minute -= 60
    else:
        minute %= 60

    # 리턴
    return "%.2d시간 %.2d분"%(hour,minute)

# 함수 호출
time = get_time() # 분 단위 시간 입력
print(time)