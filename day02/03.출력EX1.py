"""
조건
1. 자신의 이름과 나이 취미를 상수로 출력하세요.
2. 자신의 이름과 나이, 취미를 변수에 저장하고 저장된 값을 이용하여 출력하세요.
3. 저장된 값은 부등호기호 안쪽에 출력합니다.

"""

name = "홍길동"
age = 27
hobby = "코딩"

# 상수출력
print("<홍길동> <",27,"> <코딩>")
# 변수에는 핵심이 되는 것을 저장한다.
# -> 변수에 저장했다. 
# -> "연동"을 시키는 것이 주 목적이다.
# -> 범용성이 있어야 한다.
# -> 나중에 어떤 용도로 쓰이나?
# print를 이용하면 무조건 출력된다.

# 변수출력
print("<",name,"> <",age,"> <",hobby,">")
print()

print("이름 :",name)
print("나이 :",age)
print("취미 :",hobby)
print("당신의 이름은",name,"이며, 나이는",age,"세이고, 취미는 ",hobby,"입니다.")

