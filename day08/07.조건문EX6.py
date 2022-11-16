"""
조건
1. 실수 1개를 입력을 받아 저장합니다.
2. 0보다 큰 양수인 경우 5를 곱해 출력합니다.
3. 0보다 작은 음수인 경우 5로 나눠 출력합니다.
4. 0일 경우 <연산할 대상이 없습니다>라고 출력합니다.

"""
# if/else만 사용 시
fnum = float(input("실수 입력 >> "))
if fnum == 0:
        print("연산할 대상이 없습니다.")
else:
    if fnum > 0:
        result = fnum * 5
        
    else:
        result = fnum / 5
    print("연산결과 : %.1f"%(result))

# elif문 사용시
word = "연산결과 : %.1f"
if fnum > 0 :
    fnum *= 5
    print(word(fnum))
elif fnun < 0:
    fnum /= 5
    print(word(fnum))
else:
    print("연산할 대상이 없습니다.")