# 당첨 가능한 최고 순위와 최저 순위를 차례대로 배열에 담아서 return
def solution(lottos, win_nums):
    answer = []
    # 당첨 번호에 따른 순위
    rank = {0: 6, 1: 6, 2: 5, 3: 4, 4: 3, 5: 2, 6: 1}
    # 알아볼 수 없는 번호
    zero = 0

    # 0의 개수 세기
    for lotto in lottos:
        if lotto == 0:
            zero += 1

    lottos = set(lottos)
    win_nums = set(win_nums)

    # lottos와 win_nums의 교집합
    same = len(lottos.intersection(win_nums))

    # 최고 순위, 최저 순위 
    answer.append(rank[same+zero])
    answer.append(rank[same])

    return answer