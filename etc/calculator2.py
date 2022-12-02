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

# 전역선언
global history
history = []                          # 기록 리스트

# 계산 로직
def calculator(menu):
  result = 0
  menu = int(menu)
  if menu != 5:
    num1 = int(input("정수 1 입력 >> "))
    num2 = int(input("정수 2 입력 >> "))
  if menu == 1:
    result = num1 + num2
    history.append("%d + %d = %d"%(num1,num2,result)) 
  elif menu == 2:
    result = num1 - num2
    history.append("%d + %d = %d"%(num1,num2,result))
  elif menu == 3:
    result = num1 * num2
    history.append("%d + %d = %d"%(num1,num2,result))
  elif menu == 4:
    result = num1 / num2
    history.append("%d / %d = %f"%(num1,num2,result))
  elif menu == 5:
    print("===기록===")
    for i in history:
      print(i)
    print("===기록===")
    return
  return result

menu = -1
while menu != 0:
  try:  
    menu = input("0.종료 / 1.+ / 2.- / 3.* / 4./ / 5.기록 \n>>")
    if menu == '0':
      print("종료합니다.")
      os._exit(1)
    elif int(menu)<0 or int(menu)>5:
      print("다시 입력하세요")
    elif int(menu) == 5:
      calculator(menu)
    else:
      result = calculator(menu)
      if int(menu) != 4:
        print("결과 :%d"%(result))
      else:
        print("결과 :%.2f"%(result))
  except:
    print("다시입력하세요")