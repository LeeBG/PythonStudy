"""
조건
1. 앞에서 생성한 딕셔너리를 그대로 이용합니다.
2. 자신의 목표를 생성된 딕셔너리에 추가합니다.
3. 그 외 임의의 키를 입력을 받아 임의의 값으로
딕셔너리에 2번 추가합니다.
4. 딕셔너리에 보관된 자료를 결과처럼 출력합니다.
결과
이름 : 홍길동
나이 : 23세
취미 : 코딩
목표 : 저축해서 은거하기
임의의 키1 - 임의의 값1
임의의 키2 - 임의의 값2
"""

key_list = ["이름","나이","취미"]
info1 = {}
index = 0

print("-- 입력구간 -- ")
while index < len(key_list):
    if key_list[index] != "나이":
        info1[key_list[index]] = input(key_list[index]+" 입력 >> ")
    else:
        info1[key_list[index]] = int(input(key_list[index]+" 입력 >> "))
    index += 1
    
# # 후처리
# info1["나이"] = int(info1["나이"])

# 여기까지가 1번 문제 가져온거

# 2번 시작
info1["목표"] = input("목표는 >> ")
key_list.append("목표")
key = input("임의의 키1 입력 >>")
key_list.append(key)
key2 = input("임의의 키2 입력 >>")
key_list.append(key2)
# 임의의 값 입력
info1[key] = input("임의의 값1 입력 >> ")
info1[key2] = input("임의의 값2 입력 >> ")

print("-- 출력 구간 --")
print("%s : %s"%(key_list[0],info1[key_list[0]]))
print("%s : %s세"%(key_list[1],info1[key_list[1]]))
print("%s : %s"%(key_list[2],info1[key_list[2]]))
print("%s : %s"%(key_list[3],info1[key_list[3]]))
print("%s - %s"%(key_list[4],info1[key_list[4]]))
print("%s - %s"%(key_list[5],info1[key_list[5]]))

print("다른 방식")
print("====================================================")
info = {}
info["이름"] = input("이름 입력 >> ")
info["나이"] = int(input("나이 입력 >> "))
info["취미"] = input("취미 입력 >> ")
info["목표"] = input("목표 입력 >> ")

key1 = input("항목명1 >> ")
value1 = input("입력값1 >>")
info[key1] = value1

key2 = input("항목명2 >> ")
value2 = input("입력값2 >>")
info[key2] = value2


print("개인정보")
print("이름 : ",info["이름"])
print("나이 : %d세"%(info["이름"]))
print("취미 : ",info["취미"])
print("목표 : ",info["목표"])
print("%s - %s"%(key1,info[key1]))
print("%s - %s"%(key2,info[key2]))

# 리스트 - 인덱스 기반, 같은 종류의 값 저장용
# 인덱싱, 슬라이싱이 가능하다

# 딕셔너리 - 이름(KEY)기반, 다른 종류의 값 저장에 주로 씀
# 인덱싱만 됨, 슬라이싱 불가능