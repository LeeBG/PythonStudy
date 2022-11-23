"""
    딕셔너리에 이름, 나이, 취미를 입력을 하고 받아 저장하고
    자료가 보관된 딕셔너리를 그대로 출력하세요
"""
key_list = ["이름","나이","취미"]
info1 = {}
index = 0

msglist = ["성명 >> ", "연세 >> ", "취미활동 >> "]
while index < len(key_list):
    if key_list[index] != "나이":
        info1[key_list[index]] = input(key_list[index]+" 입력 >> ")
    else:
        info1[key_list[index]] = int(input(key_list[index]+" 입력 >> "))
    index += 1

# # 후처리
# info1["나이"] = int(info1["나이"])

print("개인정보")
print(info1)

####
info = {}
lst = ["이름","나이","취미"]
msglist = ["성명 >> ", "연세 >> ", "취미활동 >> "]
index = 0
while index < len(lst):
    info[lst[index]] = input(msglist[index])
    if index == 1:
        info[lst[index]] = int(info[lst[index]])
    index += 1
print("개인정보")
print(info)
