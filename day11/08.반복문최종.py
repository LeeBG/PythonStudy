"""
0보다 큰 양수 하나를 입력을 받아
해당 양수의 배수를 해당 양수의 크기만큼 출력합니다.
또한 출력되는 배수들의 합도 구하여 출력하세요.
참고) 입력을 받는 값은 무조건 양수여야 합니다.
    무조건 양수가 입력되도록 재입력을 받아야 합니다.
추가) 게임을 무한 반복 하고 싶고, 반복을 종료하고 싶을 때 종료한다.

# 결과 예시
ex) 4를 입력했을 경우 -> 4 8 12 16 / 합:40
ex) 5를 입력했을 경우 -> 5 10 15 20 25 / 합:75
ex) 2를 입력했을 경우 -> 2 4 / 합:6
ex) 1를 입력했을 경우 -> 1 / 합:1
ex) 7를 입력했을 경우 -> 7 14 21 28 35 42 49 / 합:196
"""
while True: # 무한 반복
    value = 0
    while value <= 0:
        value = int(input("0보다 큰 양수를 입력하세요"))
        if value <= 0:
            value = int(input("0보다 큰 양수를 입력하세요"))

    result = 0
    num = 1
    while num <= value:
        result += num
        print(num*value,end=" ")
        num += 1
    print("합 :",result*value)
    menu = input("계속할까요? ")
    if menu == "예":
        print("다시 처음부터 시작합니다.")
    elif menu == "아니요":
        print("종료합니다.")
        break # 반복문 종료
    else:
        print("잘못 넣었으니 재시작합니다.")

# 처음 코드 
# num = 1
# count = 0
# sum = 0
# while num > 0: # 양수일때 로직 
#     num = int((input("0보다 큰 양수 입력 >> ")))
#     if num > 0:
#         print("%d를 입력했을 경우 ->"%(num),end=" ")
#         while count < num:
#             count += 1
#             print("%d"%(count*num),end=" ")
#             sum += (count*num)
#             if count == num:
#                 print("합 :",sum)
#         break
#     else:   # 음수 재입력
#         num = 1s