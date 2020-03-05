# 문제
# SWEA 5110 - [파이썬 S/W 문제해결 기본 7일차] Linked List - 수열 합치기

# 나의 코드(시간초과)
T = int(input())

for tc in range(T):
    # 수열의 길이, 수열의 개수 M
    N, M = map(int, input().split())
    
    result = list(map(int, input().split()))
    
    for _ in range(N-1):
        List = list(map(int, input().split()))
        
        for i in range(len(result)):
            if result[i] > List[0]:
                result = result[:i] + List + result[i:]
                break
    
        else:
            result = result + List

    print("#%d" %(tc+1), end=' ')
    for k in result[:len(result)-11:-1]:
        print("%d" %(k), end=' ')
    print()

# 수정한 코드(참고) - 성공
T = int(input())

for tc in range(T):
    # 수열의 길이, 수열의 개수 M
    N, M = map(int, input().split())
    
    result = list(map(int, input().split()))
    
    for _ in range(N-1):
        List = list(map(int, input().split()))
        
        for i in range(len(result)):
            if result[i] > List[0]:
                result[i:i] = List  # 중간에 List만 추가
                break
    
        else:
            result = result + List

    print("#%d" %(tc+1), end=' ')
    for k in result[:len(result)-11:-1]:
        print("%d" %(k), end=' ')
    print()

# 수정한 코드(참고) - 연결 리스트 이용
def addtoFirst(data):  # 첫 노드에 데이터 삽입
    global Head
    Head = Node(data, Head)


def add(pre, data):  # pre 다음에 데이터 삽입
    if pre == None:
        print('error')
    else:
        pre.link = Node(data, pre.link)


def addtoLast(data):  # 마지막에 데이터 삽입
    global Head
    if Head == None:
        Head = Node(data, None)
    else:
        p = Head
        while p.link != None:
            p = p.link
        p.link = Node(data, None)


class Node:
    def __init__(self, item, n=None):
        self.item = item
        self.link = n


if __name__ == "__main__":
    T = int(input())
    for tc in range(T):
        # N: 수열의 길이, M: 수열의 개수
        N, M = map(int, input().split())
        
        List = list(map(int, input().split()))
        
        # 노드로 삽입
        Head = None
        addtoFirst(List[0])
        
        for item in List[1:]:
            addtoLast(item)
    
        # 다음 수열과 비교
        for _ in range(M - 1):
            temp = list(map(int, input().split()))
            
            # 노드의 맨 앞부터 돌면서 temp보다 큰 숫자 찾기
            pre = Head
            while pre.link != None:
                if pre.link.item > temp[0]:
                    break
                pre = pre.link
            
            # 수열을 노드에 삽입
            # 맨 앞에 들어가는 경우
            if pre == Head:
                addtoFirst(temp[0])
                pre = Head  # 중요
                for item in temp[1:]:
                    add(pre, item)
                    pre = pre.link
            else:
                for item in temp:
                    add(pre, item)
                    pre = pre.link  # 연결 잊지 않기

        # 수열의 맨 뒤부터 10개의 숫자 출력
        pre = Head
        result = [0] * N * M
        i = 0
        while pre.link != None:
            result[i] = pre.item
            pre = pre.link
            i += 1

        # 수열의 마지막 값
        result[i] = pre.item
        
        # 출력
        print("#{0} {1}".format(tc + 1, ' '.join(list(map(str, result[::-1][:10])))))
