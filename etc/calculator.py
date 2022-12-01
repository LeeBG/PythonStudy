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
import sys
import os

operatorList = ['+','-','*','/'] # 연산자 리스트
lst = []          # 띄어쓰기를 제외한 식을 담을 리스트

index = 0           
history = []      # 기록

# 입력받기
def input_menu():
  menu = input()
  if menu == "종료":
    return "종료"
  elif menu == "기록":
    for i in history:
      print(i)
    return "기록"
  else:
    return menu


def input_cal(menu): # 입력 검증받기
  count = 0      # 연산자가 2번 들어가는 경우 방지
  if menu != "종료" and menu != "기록":
    cal = menu
    for i in cal:
      if i != " ":
        lst.append(i)
    for i in operatorList: # 검증
      if i in lst and count <= 1:
        count += 1
        index = lst.index(i)
      else:
        print("이해할 수 없는 연산입니다.")
        return
    return lst
  elif menu == "종료":
    os.system("pause")
    sys.exit()
    
def init_value(lst): # 숫자와 연산자 분리
  firstNum = ""      # 첫 숫자
  secondNum = ""     # 뒤의 숫자

  for i in range(index):
    firstNum += lst[i]
  for i in range(index+1,len(lst)):
    secondNum += lst[i]

  firstNum = int(firstNum)
  secondNum = int(secondNum)
  operator = lst[index]

  return firstNum,operator,secondNum


def calculator(value):    # 계산 및 기록
  record = ""
  result = 0
  operator = value[1]
  if operator == '+':
    result = value[0]+value[2]
    record = "%d %s %d = %d"%(value[0],value[1],value[2],result)
  elif operator == '-':
    result = value[0]-value[2]
    record = "%d %s %d = %d"%(value[0],value[1],value[2],result)
  elif operator == '*' or operator == 'x':
    result = value[0]*value[2]
    record = "%d %s %d = %d"%(value[0],value[1],value[2],result)
  else:
    result = value[0]/value[2]
    record = "%d %s %d = %.2f"%(value[0],value[1],value[2],result)
  history.append(record)
  return record

# 기록

# 종료

def start():
  validated_value = []
  value = input_cal(input_menu())
  if value is not None:
    validated_value = list(init_value(value))
    calculator(validated_value)
start()