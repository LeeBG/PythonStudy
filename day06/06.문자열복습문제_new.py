"""
1. 점수 3개를 입력받습니다.
각각의 점수값은 실수입니다.

2. 입력한 값이 아래와 같이나오도록 서식을 이용하세요
ex) 97.145 / 98.1 / 99.23456을 입력했을 경우
첫번째 점수 : 97.1
두번째 점수 : 98.10
세번째 점수 : 99.235
"""
fnum1,fnum2,fnum3 = map(float,input().split()) # 입력받기
sum = fnum1+fnum2+fnum3
avg = sum/3
form = "%s번째 점수 : "
print(form % ("첫") +"%.1f"%(fnum1))
print(form % ("두") +"%.2f"%(fnum2))
print(form % ("세") +"%.3f"%(fnum3))

print("평균 : %.4f"%(avg))


