def makeFormat(num): 
    if num % 1 == 0:
        form = "%d"
    else:
        form = "%.2f"
    return form
def calculating(value):# 연산
    olst = ["+","-","*","/"]
    for op in olst:
        index = value.find(op)
        if index != -1:
            num1 = float(value[:index])
            num2 = float(value[index+1:])
            opr = value[index]
            break
    if num1 % 1 == 0:
        num1 = int(num1)
    if num2 % 1 == 0:
        num2 = int(num2)

    if index != -1 and opr in olst:
        if opr == "+":result = num1 + num2
        elif opr == "-":result = num1 - num2
        elif opr == "*":result = num1 * num2
        else:result = num1/num2
        lst = [num1,num2,result]
        for i in range(3):
            if lst[i] % 1 == 0:
                lst[i] = int(lst[i])
        flst = []
        for num in lst:
            flst.append(makeFormat(num))
        print((flst[0]+"%c"%(opr)+flst[1]+" = "+flst[2])%(lst[0],lst[1],lst[2]))
    else:
        print("잘못된 연산 기호")    

chlst = ["1","2","3","4","5","6","7","8","9","0","+","-","*","/","."]
records = []
while True:
    flag = True
    menu = input("연산식 / 기록 / 종료 >>") 
    if menu == "종료":
        break
    elif menu == "기록":
        if records ==[]:
            print("기록 없음")
        else:
            for records in records:
                print(record)
    else:
        value = ""
        for ch in menu:
            if ch != " ":
                value += ch
        for ch in menu:
            if ch not in chlst:
                flag = False
                break
        if flag:
            record = calculating(value)
            records.append(record)
            print(record)
        else:
            print("잘못된 연산식 입니다.")
            
print("프로그램이 종료되었습니다.")