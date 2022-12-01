"""
사용방법
0. 내가 하려는 것에 필요한 모든 모듈을 판별해야 한다.
1. 파이썬 공식 홈페이지로 간다 
2. 상단의 PyPI에서 필요한 모듈을 검색한다
3. 설치 명령어를 복사해서 명령 프롬프트에 입력한다.
ex) matplotlib가 필요하다
pip install matplotlib를 관리자 권한으로 실행된 명령프롬프트(CMD)에
입력하여 설치를 진행한다.
4. 기다리면 설치가 완료된다.
"""
# # 선그리기
# import matplotlib.pyplot as p 
# # as는 matplotlib.pyplot의 명칭을  'p'로 줄여서 사용
# p.plot([1,3,9,7,8]) # Y값들의 집합을 직선으로
# p.ylabel("Y-axis")
# p.xlabel("X-axis")
# p.show() # 내가 올바르게 처리되었다면 이 값들로 그래프를 그려준다.

import matplotlib.pyplot as plt
import numpy as np               #numpy는 수학 관련 함수 

x = np.linspace(0, 2 * np.pi, 200)
y = np.sin(x)

fig, ax = plt.subplots()
ax.plot(x, y)
plt.show()