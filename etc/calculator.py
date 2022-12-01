"""
◆ 목표 : 계산기( Calculator ) 만들기
◆ 제한시간 : 3시간 이내로 계산기를 완성해야 함
◆ 요구조건
  1. 기능은 3가지로
    <연산> / <기록> / <종료> 이다.
  2. <연산> 으로 입력하여 진입하고는 메뉴이고
    정수 2개와 연산기호를 입력을 받아 결과를 출력한다.
  3. <기록> 은 입력을 받아 진입하는 메뉴이고
    지금까지 수행한 연산기록을 출력한다.
  4. <종료> 는 입력을 받아 진입하는 메뉴이고
    프로그램이 종료된다.
  5. 기능은 선택하거나 직접 기능명을 입력하여 진입한다.
◆제한사항
  1. 구현 불가능한 기능은 포기하고, 타협한다.
  2. 기억이 안나면 이전에 했던 내용을 확인하고 잘 모르겠으면 질문한다.
  3. 따라 적는게 아닌, 직접 창조해야 공부가 된다.

"""
import os
# 전역 리스트들
operatorList = ('+','-','*','x','/')  # 연산자 튜플(불변)
history = []                          # 기록 리스트

# 메뉴 입력
def input_menu():
  menu = input()
  if menu == "종료":
    print("계산기를 종료합니다...")
    os.system("pause")
    os._exit(1)                       # 프로그램 종료 함수
  elif menu == "기록":
    print("=======================")
    for i in history:
      print(i)
    print("=======================")
    return "기록"
  else:
    return menu

# 메뉴처리 및 계산식 검증
def validate(menu):  # 메뉴 처리 및 계산식을 검증을 하는 함수()
  lst = []           # 띄어쓰기를 제외한 식을 담을 리스트
  count = 0          # 한 연산식의 연산자 갯수 카운트
  index = 0          # 연산자가 있는 위치 인덱스 
  num1 = ""          # 계산식의 앞의 숫자를 저장할 변수
  num2 = ""          # 계산식의 뒤의 숫자를 저장할 변수
  operator = ""      # 연산자
    
  if menu == "기록":
    return
  
  else:              # 종료, 기록이 아닌 문자열 입력
    for i in menu:
      if i != " ":    # 공백 제거 후 리스트에 담아서
        lst.append(i)
    for i in lst:     # 검증 (올바른 수식인가)
      for j in operatorList:
        if i == j:
          index = lst.index(i)          # 첫번쨰 수가 음수가 아닌 경우 연산자 위치
          count +=1
          if index == 0 and i == '-':   # 첫번쨰 수가 음수일 경우 처리
            if '+' in lst[1:]:
              index = lst[1:].index('+')+1 # 첫 음수기호를 제외한 나머지에서 연산자 찾기
            elif '*' in lst[1:]:
              index = lst[1:].index('*')+1
            elif 'x' in lst[1:]:
              index = lst[1:].index('x')+1 
            elif '/' in lst[1:]:
              index = lst[1:].index('/')+1
            else:                        # -는 가장 마지막에(num2가 음수인 경우가 있음)
              index = lst[1:].index('-')+1
              
    if count > 3 or count == 0:          # 정상적인 계산식에는 연산자 최대 3개(음수 연산자 음수 형태)
      print("이해할 수 없는 연산입니다.")
      return
    
    # 문자열을 정수로 변환
    for i in range(index):
      num1 += lst[i]
    for i in range(index+1,len(lst)):
      num2 += lst[i]
  try:              # 정수로 변환할 수 없는 값(빈값포함)을 수식에 집어 넣었다면..
    num1 = int(num1)
    num2 = int(num2)
    operator = lst[index]         # 연산자(+,-,*,x,/)
    return num1,operator,num2     # 검증된 값을 튜플로 return
  except ValueError:                      
    print("이해할 수 없는 연산입니다.(숫자아님)")
    return
  
# 계산식 계산 및 기록
def calculator(value):          # 계산 및 기록을 하는 함수()
  record = ""
  result = 0
  operator = value[1]
  if operator == '+':
    result = value[0]+value[2]
    record = "%d %s %d = %d"%(value[0],value[1],value[2],result) # 기록할 내용을 서식으로 담는다.
  elif operator == '-':
    result = value[0]-value[2]
    record = "%d %s %d = %d"%(value[0],value[1],value[2],result)
  elif operator == '*' or operator == 'x':
    result = value[0]*value[2]
    record = "%d %s %d = %d"%(value[0],value[1],value[2],result)
  else:
    try:
      result = value[0]/value[2]
      record = "%d %s %d = %.2f"%(value[0],value[1],value[2],result)
    except ZeroDivisionError:
      print("이해할 수 없는 연산입니다.(0으로 나누기)")
      return
  history.append(record)
  return record

# 계산기 함수
def start_calulator() :          # 전체 로직을 총괄하는 함수
  while True:                    # 종료메뉴 선택시 까지 무한반복
    result = ""                  # 반복돌때마다 빈 결과값으로 초기화
    menu = input_menu()          # 메뉴를 문자열로 입력을 받는다.
    value = validate(menu)       # 메뉴를 처리하고 올바른 값인지 검증
    if value is not None:        # 검증된 유효한 값이라면..
      result = calculator(value) # 계산 및 기록
    if result is not None:       # 예외 발생 시 출력 X
      print(result)              # 결과값 출력
    os.system("pause")
    os.system("cls")
    
# 실행
start_calulator()                # 계산기 실행