"""
슬라이싱할 때 편리한 규칙이 2가지 있습니다.
1) 처음부터 갈 경우, 0을 안붙여도 됨 address[0:3] ==  address[:3]
2) 끝까지 갈 경우, 끝을 적지 않아도 됨

"""

address = "부산시 수영구 수영로 310번길"

print("시 : "+address[:3]) # 처음부터 3 전 까지
print("구 : "+address[4:7])
print("도로 : "+address[8:]) # 8부터 끝까지
print("도로 : "+address[-9:17]) # ==

# 실제 주소값 처리방식
# - 메서드 : 특정 종류의 값에 종속된 전용함수
# find(문자값) : 지정한 문자값의 정방향 인덱스를 구해주고...
# 없으면 -1이 반환된다.

address = "부산광역시 부산진구 서면로 123번길"

index = address.find(" ") # 띄어쓰기를 찾아서 
part1 = address[:index] # 그 앞까지 복사하고 
address = address[index+1:] # 불필요한 부분은 잘라낸다.

index = address.find(" ")
part2 = address[:index]
address = address[index+1:]

print(part1,part2,address)
