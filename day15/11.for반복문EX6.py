"""
조건
1. 리스트에 입력을 받은 실수값을 보관합니다.
2. 지정한 횟수만큼 실수값을 입력합니다.
3. 리스트에 저장된 실수를 모두 출력합니다.
4. 리스트에 저장된 실수들의 합을 출력합니다.

결과

입력 횟수 >> 3회
1번째 실수 >> -3.117
2번째 실수 >> 3.118
3번째 실수 >> 15
목록
-3.12 3.12 15.00
합 : 15.00
"""
lst = []
num = 0
# 입력 구간
# while num < 0: # 횟수는 음수가 될 수 없어서 재입력 받기(안해도 됨)
num = input("입력 횟수 >> ")
num = int(num[:-1])

for x in range(1,num+1):
    lst.append(float(input("%d번째 실수 >> "%(x))))

# 필요하면 인덱스 숫자를 ㄹ준비해서 for로도 인덱싱이 가능하다.

# 처리 구간 (합 구하기)
result = 0
for value in lst:
    result += value

# 출력 구간
print("목록")
for value in lst:
    print("%.2f"%(value),end=" ")
print()
print("합 : %.2f"%(result))

# 처리구간 (합구하기)
# result = 0
# for value in range(count):
#     result += lst[x]
# 출력구간
# print("목록")
# for value in range(count):
#     print("%.2f"%(lst[value]),end=" ")
# print("\n합 :",result)