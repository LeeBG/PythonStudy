"""
딕셔너리 : 실제로 사전과 같이 단어와 뜻이 있다면
딕셔너리라는 객체에서는 Key(키)와 Value(값)가 있다.
목적자체는 리스트처럼 여러 종류의 값들을 하나로 묶어서 쓰게 해준다.
# 딕셔너리 : 값들의 별개 명칭을 부여해서 관리하는 객체
※ 형태
dic = { "A" : 1, "B" : 2 } # 키는 문자열로 넣는것이 좋다.
dic = {}
리스트의 인덱싱 슬라이싱에 대한 고려가 필요 없다.
"""
key_list = ["이름",'나이']
info1 = {}

# 딕셔너리는 해당 키에 값이 없으면 만들어서 저장한다.
# - 딕셔너리는 중복을 허용하지 않는 구조가 된다.
index = 0
while index < len(key_list):
    # 값의 종류를 달리 하고 싶을 경우 내부의 if를 구성하거나
    # 외부에서 후처리를 한다.
    if key_list[index] == "나이":
        tmp = int(input(key_list[index]+" 입력 >> "))
    else:
        tmp = input(key_list[index]+" 입력 >> ")
    info1[key_list[index]] = tmp
    index += 1
    
# 또는 외부에서 후처리
info1["나이"] = int(info1["나이"])

index = 0
while index < len(key_list):
    print(info1[key_list[index]])
    index += 1

