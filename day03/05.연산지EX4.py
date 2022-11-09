print("--입력구간--")
fnum1 = float(input("첫 번째 실수 입력 >>"))
fnum2 = float(input("두 번째 실수 입력 >>"))
fnum3 = float(input("세 번째 실수 입력 >>"))
# 코드는 다 만들고 나서 반복되는 것은 
# 줄일 수 있으면 줄여주는 게 관리할 때 좋다.
print("--출력구간--")
sum = fnum1+fnum2+fnum3 # 합
avg = sum/3 # 평균
result = int(avg)
print("합:",sum)
print("평균:",avg)
print("정수부:",result)
print("실수부:",float(avg-result))
