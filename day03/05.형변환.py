# 절대 잊으면 안되는 것 : 입력되는 것은 많은 경우에 문자값으로 준비된다.
# - 입력할 때 요구되는 것 : 내가 필요한 값이 맞는가??? 라는 판단
# - 입력할 때 요구되는 것 : 내가 필요한 용도로 바꾼다 라는 과정이 필요


value1 = "123" # 정수 형태의 문자값
value2 = "3.14" # 실수 형태의 문자값
value3 = 123 # 정수
value4 = 3.14 # 실수
value5 = "ABC" #문자값
value6 = True # 논리값 0은 False, 1은 True

# int : ★value1, value3. ★value4, value6 까지 가능
# value1 -> 정수값으로 쓰기 위해서
# value4 -> 소수점을 버리기 위해서
print(int(value1)+5)
print(int(value4)+5) # 정수값만 남기거 버림
print(int(value6)+5)


# float : ★value1,★value2,value3,value4,value6
# value1 -> 입력받는 키 값이 '키' 같은 거라면, 무조건 실수값이 들어오지 않는다
# value2 -> 입력받는 키 값이 '키' 같은 거라면, 무조건 정수값이 들어오지 않는다
print(float(value1),float(value2),float(value3),float(value4),float(value6))
# 결과 123.0 3.14 123.0 3.14 1.0

print(float(value1)+12,float(value2)+12)

# str : 문자열로 변환(다됨)
# - 문자열의 특성을 이용하는 것이 주 목적
# - 조립하기, 반복하기, 분리하기
print(int(value1+str(value3))+5)
# bool : 다 되지만 값을 논리값으로 바꾸는 경우는 일은 거의 없다.
# - 참인 상태이면 True, 없는 상태이면 False
print(bool(1),bool(0),bool(-1)) # 0이 아니라면 True
print(bool(" "),bool(""),bool("A")) # "" 만 False