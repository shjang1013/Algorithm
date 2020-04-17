import collections

def solution(clothes):
    clothes_list = [cloth[1] for cloth in clothes]
    result = collections.Counter(clothes_list)
    count = 1
    for i in list(result.values()):
        count *= (i + 1)
    
    return count - 1

# (의상 종류 + 1)을 모두 곱한 후 -1 => 반드시 하나는 선택
