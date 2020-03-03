# 문제
# SWEA 5108 - [파이썬 S/W 문제해결 기본 7일차] Linked List - 숫자 추가

# 나의 코드
T = int(input())

for tc in range(T):
    # 수열의 길이 N, 추가 횟수 M, 출력할 인덱스 번호 L
    N, M, L = map(int, input().split())
    List = list(map(int, input().split()))
    
    # M개의 숫자를 지정된 위치에 추가 
    for _ in range(M):
        index, data = map(int, input().split())
        List.insert(index, data)

    print("#%d %d" %(tc+1, List[L]))
