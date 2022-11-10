"""
대입연산자 : 변수의 생성 / 값의 교체 
같은 변수가 두 개 생기지 않는다. 
변수에 있던 값이 복사만 된다.
"""
value1 = 100
print(value1)
value1 = 200
print(value1)
value2 = value1 # 다른 변수에 있는 값을 복사할 수 있다.
print(value1,value2) # 변수가 복사된 것이 아니니 
value1 = 300
print(value1,value2) # value1과 value2는 서로 다른 변수이다.

"""
# 복합 대입 연산자 : 변수에 "누적" - 산술연산자와 연계됨.
- 대입도 연산자이고, 우선순위가 바닥에 있음. 오른쪽부터 먼저 됨.
"""
# value1 = 400
value1 = value1 + 100 # '=' 는 가장 마지막에 실행되는 연산자(400이 되는 과정)
print(value1)
value1 += 500 # 복합대입연산자 value1 = value1 + (500)
print(value1)

value1 /= 2 # value1 = value1 / (2)
print(value1)

value1 -= 100 - 50 # value1 = value1 - (100 - 50)
print(value1)

""" 
주의 사항 ! 
- 변수 생성용으로 못씀 : 값을 먼저 불러오기 때문에 안된다.    
"""