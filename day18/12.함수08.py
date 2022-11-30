# 매개변수를 좀 더 편하게 쓰기 위한 기술이 있음
# 1) 기본값(Default Arguments)
# - 매개변수의 값을 미리 넣어두는 문법을 말한다.
#   특정 상수값이 함수를 호출할 때 많이 사용되었으니,
#   이를 줄인다.
# - 오른쪽부터 왼쪽으로 설정해줘야 함
def test1(value1,value2 = 2):
    print(value1+value2)


test1(15) # 함수에 정의된 매개변수가 2개이지만 
          # value2는 default로 잡혀있기 때문
test1(12) # 12 + 2(default)
test1(21,9) # value2값에 다른 값을 넣었을 때 다른값으로 대체
# 21 + 9(new)

# 2) 위치기반 매개변수(Positional Arguments)
# - 값들이 몇 개 들어올 지 모를 때 사용함
# - 무조건 일반 매개변수보다 왼쪽에 와야 함.
# - 기본값이 허용되지 않는다. 
# Positional Arguments는 기본적으로 ()이라는 기본값을
def test2(*values, value1 = 111, value2 = 222):
    print(value1,value2)
    for value in values:
        print(value,end=" ")
    print()

# 결과는 튜플로 이 값들을 묶어준다.
# test2(10,20,30,40,50,60) 

test2(10,20,30,40,value2 = 199)
lst = [10,20,30,40]
test2(*lst) # 위치기반 매개변수에게 리스트를 매칭시킬 경우*을 붙인다.
test2(lst) # 안붙이면 리스트가 하나로 취급되어 보관된다.
