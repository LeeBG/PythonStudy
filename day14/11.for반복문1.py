"""
for 제어문 : 유한 반복만 가능
"""

# 문자열
word = "RAMEN" # 문자갑
for ch in word: # 오른쪽의 하나씩을 왼쪽 변수에 덮어쓰기하며 저장
    print(ch, end= " ")
print()

# 리스트
lst = ["라면","돈까스","치킨"]
for food in lst:
    print(food,end=" ")
print()

# 딕셔너리 - 돌려서 나오는 키를 이용해, 값을 불러온다.
# 구조가 2중이라 사용형태가 조금 다르다.
dic = {"A":1, "B":2, "C":3}
for key in dic:
    print(key, dic[ key ])
print()
dic = {"A":1, "B":2, "C":3}