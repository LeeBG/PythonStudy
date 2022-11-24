"""
조건
1. 아래의 예시를 띄어쓰기 단위로 구분하여 문자열로 리스트에 저장합니다.
2. 리스트에 저장된 것을 결과와 동일하게 for 반복문을 이용하여 출력하세요

        "apple pie so delicious !!!"

"""

word = "apple pie so delicious !!!"
# lst = word.split() 
# split 메서드의 구조
lst = []
word += " "
while True:
    index = word.find(" ")
    if index != -1:
        lst.append(word[:index])
        word = word[index+1:]
    else:
        lst.append(word)
        break
print(word,lst)

word = "apple pie so delicious !!!"
lst = []
word += " "
while word != "":
    index = word.find(" ")
    lst.append(word[:index])
    word = word[index+1:]
print(word,lst)

# split의 for 구현
word = "apple pie so delicous !!!"
lst = []
tmp = ""
word += " "
for ch in  word:
    if ch != " ":
        tmp += ch
    else:
        lst.append(tmp)
        tmp = ""
print(word,lst)