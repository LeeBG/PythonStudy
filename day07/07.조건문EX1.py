# 주석의 실제 용도

# 판단할 값 입력, num애 정수값 저장됨
num = int(input("정수 입력 >>"))

# 7의 배수라면 num에 7증가 후 출력
# - 14, 7 등에서 작동 확인


# 원본 유지가 필요 없을 경우
if num % 7 == 0:
    num += 7

# 7의 배수가 아니라면 if를 안타고 그냥 출력
print("변수에 저장된 값 :",num)


# 원본 유지가 필요하다면
if num % 7 == 0:
    result = num + 7
if num % 7 != 0:
    result = num
# 7의 배수가 아니라면 if를 안타고 그냥 출력
print("변수에 저장된 값 :",result)