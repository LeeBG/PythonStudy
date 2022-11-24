"""
객체 : 현실에 존재하는 것(가상/실제 모두)을 프로그래밍 언어로
       그 내부에서 쓸 수 있도록 적절하게 구현한 것
클래스 : 객체의 설계동

# 우리가 배운 개념은 리스트와 딕셔너리가 있다. 
# 딕셔너리 : 보관되는 것들의 고유명사(key)를 붙여서 관리한다.
# 변수명은 값들을 대표하는 이름, dic1,dic2,dic3 으로 만드는 것이 일반적이다.
"""
item1 = {}
item1["name"],item1["price"],item1["quan"] = "캬라멜마키야또",3000,2

##         상품명                     가격        수량
# item1 = {"name":"캬라멜마끼아또", "price":3000, "quan":2}
print(
    "%s %d원 %d개 총액 : %d"%(
    item1["name"],item1["price"],item1["quan"],item1["price"]*item1["quan"]
        )
    )

    
# 반복으로 운용할 때는 리스트로 목로글 만들어서 리스트에 대한 인덱싱으로
# 반복을 구현한다.
lst = ["name","price","quan"]
index = 0
while index < len(lst):
    print(item1[ lst[index] ] ,end = " ")
    index += 1
print()