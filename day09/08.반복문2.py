"""
유한반복 : 반복횟수가 정해지는 반복문
- 접근방식 : 규칙성을 기반으로 한다.

1단계 : 나오게 할 내용을 작성한다.
2단계 : 같은 모양이 나오도록 분해한다.
3단계 : 변수와 복합 대입 연산으로 다시 한 번 모양을 통일한다.
4단계 : 반복되는 내용을 찾아서 while로 포장한다.
5단계 : 상수값을 건드리면 어떤 동작이 발생하는 지를 파악한다.
"""
# 1) 규칙성이 명백하게 존재하는 것
# 1,2,3,4,5단계 모두 완료
limit = int(input("출력할 범위 >> "))
num = 1
while num <= limit:
    print(num,end=" ") # end : print의 줄바꿈을 바꾸는 옵션
    num+=1
print()

# 2) 규칙성이 없는 것이 있다. - 엄청 간단하다.
# 1부터 1씩 증가하는 숫자로 보통 준비한다.
# +@ : 일정 횟수만큼 반복하는 유한반복문을 아예 외워서 쓰기도 한다.
num = 1
while num <= 3:
    print("Hello",end=" ") # 5 print(num) - 5 
    num += 1
