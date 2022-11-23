"""
이름 나이 키를 입력받아서 정렬하여 출력하기
"""
info = [
    input("이름 입력 >> "),
    int(input("나이 입력 >> ")),
    float(input("키 입력 >> "))
]

# 리스트는 순서에 목숨을 거는 경향이 생긴다.
# - 같은 종류의 순서가 별 상관없는 값들이라면 편하게 이용 가능
# - 다른 종류 / 순서가 필요한 값들이 오면 난장판이 된다.
while len(info[0]) < 2 or len(info[0]) > 3 :
    info[0] = input("이름을 다시 입력하세요 >> ")
while info[1] < 0 or info[1] > 120:
    info[1] = input("나이를 다시 입력하세요 >> ")
while info[2] < 10 or info[2] > 300:
    info[2] = input("키를 다시 입력하세요 ")

# 탭을 이용하여 신속하게 정렬가능
print("이름 \t: %s"%(info[0]))
print("이름 \t: %s세"%(info[1]))
print("이름 \t: %scm"%(info[2]))
