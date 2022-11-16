# 조건문 : 선택
# - 전제조건을 작성하고, 그 조건이 맞다는 가정하에 코드를 작성한다.

num1 = input("숫자 입력 >> ")
# 멤버십 연산자 : 좌측이 우측에 있는지 여부를 체크한다.

# if+else 문 : 둘 중 하나를 무조건 선택하도록 해주는 조합
if "." in num1:
    num1 = float(num1)
else:
    num1 = int(num1)

print("입력받은 값 : ", num1)

# if만 사용하기 : 되면 좋고, 안돼도 별 상관없음.
if num1 >= 100 :
    num1 %= 100
print("처리된 결과 :",num1)

# elif : 조건문의 선택지를 늘려준다. 걸러내는 방식으로 작성.
if num1 % 5 == 0:
    print("5의 배수입니다.")
elif num1 % 3 == 0:
    print("3의 배수입니다.")
elif num1 % 2 == 0:
    print("2의 배수입니다.")
else:
    print("5,3,2의 배수가 이닙니다.")
