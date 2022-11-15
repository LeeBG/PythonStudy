num = int(input("정수 입력 >> "))
# 조건문을 쓸 때는 조건식에서는 전제조건을 설정하는 과정
# 종속문에서는 전제조건이 맞는 말일 때 할 내용을 작성
result = "%s입니다."
print(result%(num))
if num > 0 :
    word = "양수"
    print(result%(word))
if num % 2 == 0:
    word = "짝수"
    print(result%(word))
