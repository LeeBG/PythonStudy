"""
반복문 응용 : 메뉴 만들기
- 가장 대표적인 이중 반복
- 메뉴는 선택에 의해서 구현이 된다.
- 이 때 조건식은 비교하기 보다는 무조건 작동하도록 구성하지 않고
  상수값 True를 넣는다.
- 전체코드를 무조건 실행하는 무한 반복문 
- 선택을 필요한 값만 통과시키는 무한 반복문
- = 메뉴가 된다.
"""

# 무한 반복문 안에 무한 반복문이 menu의 정체이다.
while True: # 이 때는 break문이 꼭 들어가 줘야 한다.
    menu = 0
    while menu < 1 or menu > 3:
        menu = int(input("1. 선택1 / 2. 선택2 / 3. 종료 >> "))
        if menu < 1 or menu > 3:
            print("잘못된 선택입니다.")
    if menu == 1:
        print("선택1 !! ")
    elif menu == 2:
        print("선택2 !! ")
    else: # 3인 경우
        print("프로그램 종료 ") 
        break

# 조건식이 True일 경우, while을 두 번 쓰지 않아도 성립하도록 만들 수 있다.
while True: # 이 때는 break문이 꼭 들어가 줘야 한다.
    menu = int(input("1. 선택1 / 2. 선택2 / 3. 종료 >> "))
    if menu < 1 or menu > 3:
        print("잘못된 선택입니다.")
        continue    # 주 목적은 반복을 처음부터 재시작
        # 메뉴같이 조건문 및 코드가 많이 돌아가는 반복문에서
        # while을 한 번 더 준비할 필요없이 쓸 수 있게 해줌
    if menu == 1:
        print("선택1 !! ")
    elif menu == 2:
        print("선택2 !! ")
    else: # 3인 경우
        print("프로그램 종료 ") 
        break