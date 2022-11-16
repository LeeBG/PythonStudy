# 통과하는 역의 수에 따라 소요시간을 출력하는 프로그램
# 역은 하나당 통과하는데 3분의 시간이 소요됩니다.
# 입력한 역의 수에 따라 소요시간을 출력하세요
# 단, 조건이 있습니다.
# 1) 음수가 입력되면 3회까지 재입력을 받습니다.
# 2) 3회를 넘어서도 여전히 음수이면 
# <잘못된 입력입니다>를 출력하세요.

error_count = 0
num = int(input("통과하는 역의 수를 입력하세요 >> "))
if num < 0 and error_count == 0:
    num = int(input("통과하는 역의 수를 입력하세요 >> "))
    print(num)
    error_count += 1
if num < 0 and error_count == 1:
    num = int(input("통과하는 역의 수를 입력하세요 >> "))
    print(num)
    error_count += 1
if num < 0 and error_count == 2:
    num = int(input("통과하는 역의 수를 입력하세요 >> "))
    error_count += 1
elif num < 0 and error_count == 3:
    print("잘못된 입력입니다.")
else:
    pass_station = num * 3
    print("소요된 시간은 총 %s 분 입니다."%(pass_station))



