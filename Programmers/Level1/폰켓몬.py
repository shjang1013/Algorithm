# 가장 많은 종류의 폰켓몬을 선택하는 방법이 여러 가지인 경우에도, 선택할 수 있는 폰켓몬 종류 개수의 최댓값 하나만 return
def solution(nums):
    answer = 0
    N = len(nums)
    # 같은 종류의 폰켓몬 지우기
    nums = list(set(nums))

    # 연구실에 있는 총 N마리의 폰켓몬 중에서 N/2마리 가져가기
    if N//2 >= len(nums):
        answer = len(nums)
    else:
        answer = N // 2

    return answer