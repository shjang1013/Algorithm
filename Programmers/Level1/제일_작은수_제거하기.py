# 나의 코드
def solution(arr):
    if arr != [10]:
        arr.pop(arr.index(min(arr)))
    else:
        arr = [-1]
    return arr
