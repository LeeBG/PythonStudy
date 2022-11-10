"""
복습문제
# 1) 엘리베이터의 최대 하중과 
# 2) 화물의 개당 무게를 
# 3) 입력을 받아 적재 가능한 물건의 수량을 수해서 출력하세요.
#    ※무게는 KG단위이며, 값의 종류는 판단해보세요.
# 단, 수량은 무조건 정수입니다.
"""

# 수량은 무조건 정수
max_weight = float(input("엘리베이터의 최대 하중 입력>>"))
weight = float(input("화물의 개당 무게 입력 >>"))

num = int(max_weight/weight) # 소수점 이하는 버림

print("최대",max_weight,"kg의 엘리베이터에 적재할 화물 하나의 무게는",weight,"kg입니다.")
print("총 적재가능한 물건의 수량은",num1,"개입니다.")
print("총 적재량",max_weight//weight*weight,"kg")

