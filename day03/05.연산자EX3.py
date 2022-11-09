# 입력은 "문자값"을 대체한다.
# - 정수값, 실수값, 논리값을 대체하지 못한다.
# - 입력받은 값은 대부분의 경우 형변환이 적용되어야한다.

print("--입력 구간--")
num1 = int(input("첫 번째 정수 입력 >>"))
num2 = int(input("두 번째 정수 입력 >>"))

print("--출력 구간--")
print(num1,"+",num2,"=", num1+num2)
print(num1,"-",num2,"=",num1-num2)
print(num1,"*",num2,"=",num1*num2)
print(num1,"/",num2,"=",num1/num2)