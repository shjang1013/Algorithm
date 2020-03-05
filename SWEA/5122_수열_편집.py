# 문제
# SWEA 5122 - [파이썬 S/W 문제해결 기본 7일차] Linked List - 수열 편집

# 나의 코드
T = int(input())

for tc in range(T):
    # N: 수열의 길이, M: 추가 횟수, L: 출력할 인덱스 번호
    N, M, L = map(int, input().split())
    
    List = list(map(int, input().split()))
    
    for _ in range(M):
        temp = list(input().split())
        
        i = int(temp[1])
        
        # insert
        if temp[0] == 'I':
            List[i:i] = [int(temp[2])] # 리스트 중간에 삽입할 경우 
        # delete
        elif temp[0] == 'D':
            List.pop(i)
        # change
        else:
            List[i] = int(temp[2])

    if len(List) <= L:
        print("#%d %d" %(tc+1, -1))
    else:
        print("#%d %d" %(tc+1, List[L]))
