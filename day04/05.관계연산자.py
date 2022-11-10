"""
# 관계연산자: 우선순위가 산술보다 낮고, 대입보다 높음
# - 크기 비교는 정수와 실수만 가능하다.
# - ★문자는 순서 비교가 된다.
    -> 1. 순서(최우선순위)
    -> 2. 길이(일부일치 시)
"""
value1 = int(input("정수1 입력 >> "))
value2 = int(input("정수2 입력 >> "))

print(value1, ">" , value2,":", value1 >  value2)
print(value1, "<" , value2,":", value1 <  value2)
print(value1, ">=", value2,":", value1 >= value2)
print(value1, "<=", value2,":", value1 <= value2)
print(value1, "==", value2,":", value1 == value2)
print(value1, "!=", value2,":", value1 != value2)

# 예시) 컴퓨터 살 때
# - RAM 16GB이고, 화면 15인치 대 노트북을 산다. 
ram = 16
display = 15.6
find_ram = int(input("램 입력 >>"))
find_display = int(input("화면 크기 입력 >>"))
print(ram == find_ram) # 내가 찾고 있는 램이 맞는지 확인
print(find_display <= display < find_display+1)
