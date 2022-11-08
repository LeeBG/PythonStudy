"""
" 출력 " 
- 사람이 이용할 수 있도록 보여주는 것
print() : 화면에 값을 보여준다.
- 괄호안에 넣은 값을 출력
- 상수 및 변수를 가리지 않음
- 여러 개면 쉼표로 구분하여 출력함
"""

num = 123
fnum = 3.14
word = "Apple"
result = False
print(num) # num이라는 변수이름에 저장된 값을 보여줌
# 실행 ctrl + F5
print("num : ",num, "fnum : ",fnum) # 쉼표로 구분할 수 있는 수량은 무한에 가까움
print(num,fnum,word,result)
# 상수는 나오는 결과물을 적절하게 꾸며주기 위해 사용하게 된다.
print("이건",num,"이고 정수값입니다.") # 정보의 형태
print("3은 5보다 큰가요? ",result)
print(num, "+",fnum,"=",126.14)