"""
서식 만들어 이용하기 : 큰 그림을 그려야 한다.
- 큰 그림 : 다양한 종류의 값들이 섞여서 출력이 될 때
"""
name = "홍길동"
age = 35
height = 167.8
blood = 'A'
# 문자열 내부에 서식문자를 배치하고, 이에 대응하는 값을 
# 문자열 외부에서 %연산자로 대응한다.
#print("이름은 %s이고, 나이는 %d세입니다."%(name, age))
# 수량은 자유이지만, 자동인식이 안되고, 순서를 맞춰서 대응
#print("키는 %fcm이고, 혈액형은 %c형이다."%(height, blood))

"""
%c : 문자열 값 중에서 하나만 있는 문자를 출력할 때 사용한다.
+@ 겸사겸사 정수값을 문자값으로 바꿔서 보고 싶을 때 종종 사용된다.
"""
ch1 = "!"
ch2 = "글"
print("첫번째 : %c"%(ch1))
print("첫번째 : %c"%(ch2))
# 문자를 대조하는 표를 ASCII 코드 + 확장된 목록표인 유니코드도 이용
print("%c %c / %c %c"%(65,90,97,122))
# - 주로 내부 처리용도에서 자주 보게 됨
# 이 정수값은 문자열에서 대응되는 것이 있으면 문자로 바꿔서 볼 수 있다.
print("%c"%(65) <= "B" <= "%c"%(90))

# %d : 정수값을 출력하는 용도 + 형변환이 붙어 있음
# - 문자값을 %c의 반대방향처럼 바꿔주지 않음
print("%d"%(123))
print("%d"%(3.99)) # 실수값에 대한 형변환(소수 버림 처리)
# - %d부터는 값에 대한 서식을 부여할 수 있음
count = 60
print("%4.3d초"%(count)) # 스탑워치의 화면에서 많이 보이는 서식
count-=1
print("%4.3d초"%(count)) # 직접 만들려면 엄청 번거로운 과정이지만
count-=1 
print("%4.3d초"%(count)) # 서식을 이용하면 간단하게 끝난다.
# -> 앞에서 4칸을 확보해서 우측정렬해서 3자리로 보여주되, 모자른 자릿수는 0으로 채워준다.

# %f : 소수점 자릿수 조절이 간편하게 되기 때문에 사용함
weight = 176 * 176 * 22 / 10000
print(weight)
print(int(weight * 100) / 100) # 반올림처리까지 들어가면 힘들다
print("%.2f"%(weight)) # 소수점 아래 두자리 까지 표현할 때 알아서 반올림 해준다.

# 응용1
result = float("%.2f"%(weight)) # 소수점 2자리 까지 반올림한 실수값 구하기
print(result,result*5)

# 응용2
count = int(input("반올림할 자릿수 >> "))
form = "%."+str(count)+"f"
result = float(form%(weight))
print(result,result*2)

# %s : 다 된다.
# 보여줄 글자수를 조절할 수 있다.
word = "지금부터 작성하는 내용은 마치 네이버 메인화면 마냥 따라하는 겁니다~!"
show_text = "지금부터 작성하는 내용은 마치 네이버"
print(show_text, "...")
print("%.20s ..."%(word)) # 선두부터 보여줄 글자 수를 지정할 수 있음
print("%.0f"%(result)) # 서식문자별
print("%.0s"%(result)) # 서식 적용방법이 달니 혼용하면 안됨