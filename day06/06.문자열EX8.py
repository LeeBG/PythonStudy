"""
아래의 문자열에서 결과에 필요한 것들만 슬라이싱하여
출력하세요
mms = "WEB발신\n[KB]06/07 18:33 998XX 10,000 출금"
결과
은행 : KB 은행
날짜 : 06월 07일
계좌 : 998XX
금액 : 10,000
종류 : 출금
"""

"""
# 풀이
mms = "WEB발신\n[KB]06/07 18:33 998XX 1,000,000,000 입금"

index = mms.find("[")
mms = mms[index+1:]
index = mms.find("]")
bank = mms[:index]

mms = mms[index+1:]
index = mms.find("/")
month = mms[:index]

mms = mms[index+1:]
index = mms.find(" ")
day = mms[:index]

mms = mms[index+7:]
index = mms.find(" ")
account = mms[:index]

mms = mms[index+1:] 
index = mms.find(" ")   # 필요한 부분을 찾고
money = mms[:index]     # 금액정보를 분리

what = mms[index+1:]

print(bank)
print(month,day)
print(account)
print(money)
print(what)

"""

print("은행 : "+mms[mms.find("[")+1:mms.find("]")]+" 은행")
print("날짜 : "+mms[mms.find("]")+1:mms.find("/")]+"월 "
+mms[mms.find("/")+1:mms.find(" ")]+"일")
mms = mms[mms.find(" ")+1:]
mms = mms[mms.find(" ")+1:]
print("계좌 : "+mms[:mms.find(" ")])
mms = mms[mms.find(" ")+1:]
print("금액 : "+mms[:mms.find(" ")] + "원")
print("종류 : "+mms[mms.find(" ")+1:])
