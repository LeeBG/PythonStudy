"""
조건
1. 실수값 3.141516171819를 저장한 fnum을 준비합니다.
2. 문자열 ABCDEFG를 저장한 word를 준비합니다.
3. 정수값 456을 저장한 num를 준비합니다.
4. 결과처럼 출력합니다.

-- 결과 --
3.141516
3.1415
3.14
AB ABC ABCD
045600456000456

서식문자들의 서식은, 전부 공유한다.
"""
fnum = 3.141516171819
word = "ABCDEFG"
num = 456

print("%.6f"%(fnum))
print("%.4f"%(fnum))
print("%.2f"%(fnum))
print("%.2s %.3s %.4s"%(word,word,word))
print("%.4d%.5d%.6d"%(num,num,num))
