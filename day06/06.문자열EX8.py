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

mms = "WEB발신\n[신한]06/07 18:33 998XX 1,000,000,000 출금"

print("은행 : "+mms[mms.find("[")+1:mms.find("]")]+" 은행")
print("날짜 : "+mms[mms.find("]")+1:mms.find("/")]+"월 "
+mms[mms.find("/")+1:mms.find(" ")]+"일")
mms = mms[mms.find(" ")+1:]
mms = mms[mms.find(" ")+1:]
print("계좌 : "+mms[:mms.find(" ")])
mms = mms[mms.find(" ")+1:]
print("금액 : "+mms[:mms.find(" ")] + "원")
print("종류 : "+mms[mms.find(" ")+1:])
