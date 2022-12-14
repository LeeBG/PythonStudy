"""
함수의 실제 사용방식
import 명령어를 이용해, 함수가 들어있는 소스파일을 불러와서 합친다.

주의사항 
- 함수가 들어있는 소스파일에는 함수만 있어야 한다.
- 코드는 사용하려는 소스파일 내에 작성된 함수보다
  위에 배치한다. (import->함수->코드)
"""
# 다른 함수 불러오기 : 함수가 작성되어 저장된 소스파일을 불러옴
# - 이 소스파일을 모듈(Module)이라고 부른다.
import TEST # TEST.py 모듈을 불러옴

# 불러온 함수의 사용 : 소스파일명.함수명()
value1 = TEST.get_sum()
value2 = TEST.get_sum()
print("결과:",value1+value2)