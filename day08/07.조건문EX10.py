# 통과하는 역의 수에 따라 소요시간을 출력하는 프로그램
# 역은 하나당 통과하는데 3분의 시간이 소요됩니다.
# 입력한 역의 수에 따라 소요시간을 출력하세요
# 단, 조건이 있습니다.
# 1) 음수가 입력되면 3회까지 재입력을 받습니다.
# 2) 3회를 넘어서도 여전히 음수이면 
# <잘못된 입력입니다>를 출력하세요.

# 첫번쨰 형태
count = int(input("통과하는 역의 수를 입력 >> "))
if count < 0:
    count = int(input("잘못되었습니다.\n통과하는 역의 수량 >> "))
    if count < 0:
        count = int(input("잘못되었습니다.\n통과하는 역의 수량 >> "))
        if count < 0:
            count = int(input("잘못되었습니다.\n통과하는 역의 수량 >> "))
            if count < 0:
                print("잘못된 입력입니다.")
            else:
                print("소요시간 : %d분"%(count*3))
        else:
            print("소요시간 : %d분"%(count*3))
    else:
        print("소요시간 : %d분"%(count*3))
else:
    print("소요시간 : %d분"%(count*3))


# 두 번째 형태 : 결과는 하나뿐이니, 입력만 세번 받는다.
count = int(input("통과하는 역의 수를 입력 >> "))
if count < 0:
    count = int(input("잘못되었습니다.\n통과하는 역의 수량 >> "))
if count < 0:
    count = int(input("잘못되었습니다.\n통과하는 역의 수량 >> "))
if count < 0:
    count = int(input("잘못되었습니다.\n통과하는 역의 수량 >> "))

if count < 0:
    print("잘못된 입력입니다.")
else:
    print("소요시간 : %d분"%(count*3))