"""
반복문 응용 문제 - 메뉴 구현
# 조건 
# "시작" 을 입력하면 "끝" 이 출력되고
# "끝" 을 입력하면 "시작" 이 출력됩니다.
# "기록" 을 입력하면 현재 메뉴의 반복한 횟수를 출력합니다. 
# "종료" 를 입력하면 메뉴가 종료됩니다.
"""
count = 0  # 반복한 횟수

while True:
    count += 1
    menu = input("시작 / 끝 / 기록 / 종료 중 입력 >> ")
    if menu == "시작":
        print("끝")
    elif menu == "끝":
        print("시작")
    elif menu == "기록":
        print("반복 횟수 : %d회"%(count))
    elif menu == "종료":
        print("종료합니다.")
        break
    else:
        print("잘못된 메뉴를 입력했습니다.")   
########################################################
count = 0
menu_list = ["시작","끝","기록","종료"]
while True:
    count += 1
    menu = input("시작 / 끝 / 기록 / 종료 >> ")

    if menu not in menu_list:
        print("잘못된 입력...")
        continue
    if menu == "종료":
        print("종료")
        break
    if menu == "시작":
        print("끝")
    elif menu == "끝":
        print("시작")
    elif menu == "기록":
        print("반복 횟수 : ",count)
    
print("프로그램이 종료되었습니다.")