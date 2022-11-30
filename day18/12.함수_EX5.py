"""
합을 구하는 make_sum_from 함수를 정의합니다.
1) 이 함수는 리스트를 전달받아, 그 내부의 값들의 합을 구합니다.
2) 합은 외부에서 쓸 수 있도록 return되어야 합니다.
3) 만약 비어있는 깡통 리스트가 전달되면 합은 0이 나옵니다.
"""

def make_sum_from(lst):
    result = 0
    if len(lst) == 0:
        result = 0
    else:
        for index in lst:
            result += int(index)
    return result

lst1 = [1,2,3,4,5]
lst2 = [-1,-2,-3,-4]
lst3 = []

result1 = make_sum_from(lst1)
result2 = make_sum_from(lst2)
result3 = make_sum_from(lst3)

print(result1,result2,result3) # 15, -10, 0