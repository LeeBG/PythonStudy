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
# 딕셔너리 : 값들의 별개 명칭을 부여해서 관리하는 객체
info1 = {"name" : "홍길동", "age" : 23}
print(info1["name"],info1["age"])

# 순서에 신경쓰지 않고 오로지 키값에 의존하는 형태
# - 변수명을 바꿔서 넣어준 것이기 때문에 순서가 존재하지 않음
info2 = {"age" : 35 , "name" : "고길동"}
print(info2["name"],info2["age"])

# - 딕셔너리는 순서를 보는게 의미가 없음.
#   필요한 내용물이 키와 매칭되어 들어있는지만 체크하면 된다.
print(info1, info2)

# 딕셔너리도 쓰는 과정에서는 반드시 반복이 필요하다.
# - 리스트로 임의로 반복시킬 목록을 만든다

key_list = ["name",'age']
index = 0
while index < len(key_list):
    print(info1[key_list[index]],info2[key_list[index]])
    index += 1

