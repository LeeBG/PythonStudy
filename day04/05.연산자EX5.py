"""
조건
1. <> 로 표시된 구간에 복합 대입 연산자를 추가합니다.
2. 추가하여 결과처럼 나오도록 만드세요

result = 100
<>
result += 50
<>
result /= 2
<>
 ※결과
 1: 100
 2: 150
 3: 75.0
"""
result = 100
print("1:",result)
result += 50
print("2:",result)
result /= 2
print("3:",result)
