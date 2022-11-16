"""
조건
1. 국어/영어/수학 성적을 입력받아 평균을 구하여 출력합니다.
2. 평균이 90이상이면 A,80이상이면 B, 70이상이면 C, 60이상이면 D, 그 외 F출력
3. 과목은 하나씩 입력을 받으면 됩니다.

결과 (78,87,75 입력시)
"""
kor = int(input("국어 성적 >>"))
eng = int(input("영어 성적 >>"))
mat = int(input("수학 성적 >>"))
avg = (kor+eng+mat)/3
if avg >= 90:   grade = 'A'
elif avg >= 80: grade = 'B'
elif avg >= 70: grade = 'C'
elif avg >= 60: grade = 'D'
else:           grade = 'F'
print("평균 : %.2f점\n등급 : %c등급"%(avg,grade))

# if avg >= 60:
#     # 대문자 A(65)에 숫자 (0 ~ 3)까지를 더해서 A(65),B(66),C(67)
#     rank = int(65+(100-avg) // 10)
# else:
#     rank = 'F'

# print("평균 : %.2f점\n등급 : %c등급"%(avg,rank))
