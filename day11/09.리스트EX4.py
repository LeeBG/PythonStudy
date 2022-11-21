"""
조건
1. 앞에서 입력을 받아 생성되는 리스트를 이용합니다.
2. 리스트에 보관된 값을 인덱싱으로 가져와 순서가 뒤집힌 새로운 리스트를
생성하고 추가합니다.
3. 두 리스트를 합쳐 새로운 리스트를 생성합니다.
4. 새로운 리스트의 첫 번째와 마지막을 인덱싱하여 출력합니다.
"""

lst = []
count = 1
while count <= 3:
    # 포맷팅(서식)은 print가 아닌, 문자열의 기능이다.

    # lst += [input("%d >> "%(count))]
    # -> 연산자를 써도 되지만, 가독성을 위해서 메서드로 바꾼다. 
    lst.append(input("%d >> "%(count)))
    count +=1
print(lst)

# +@ : 문자열에는, 한번에 리스트로 만들어주는 메서드가 하나 존재함.
# split() : 띄어쓰기를 기준으로 문자열을 쪼개준다. 그리고 최종적으로 리스트로 묶음
values = (input("3개 입력 >> ").split())
print(values)

# 순서를 뒤집는 리스트
count2 = 2
print("순서를 뒤집은 새로운 리스트")
lst2 = []
while count2 >= 0:
    lst2.append(lst[count2])
    count2-=1
print(lst2)
print("합친 리스트의 첫번째와 마지막 인덱싱")
print((lst2+lst)[0],",",(lst2+lst)[-1])