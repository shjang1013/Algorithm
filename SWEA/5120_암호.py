# 문제
# SWEA 5120 - [파이썬 S/W 문제해결 기본 7일차] Linked List - 암호

# 나의 코드
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
        N, M, K = map(int, input().split())
        List = list(map(int, input().split()))
        
        Head = None
        addtoFirst(List[0])
        
        for item in List[1:]:
            addtoLast(item)
    
        pre = Head
        
        for _ in range(K):
            # 지정 위치부터 M번째 칸을 추가, 여기에 앞칸의 숫자와 뒤로 밀려난 칸의 숫자를 더해 넣음, 추가된 칸이 새로운 지정 위치 
            for _ in range(M-1):
                if pre.link == None:
                    pre.link = Head
                pre = pre.link
            
            if pre.link == None:
                pre.link = Head
            add(pre, pre.item + pre.link.item)
            pre = pre.link

        pre = Head
        result = [0]*(N+K)
    
        for i in range(N+K):
            result[i] = pre.item
            pre = pre.link
        
        # 출력
        if len(result) >= 10:
            print("#{0} {1}".format(tc + 1, ' '.join(list(map(str, result[::-1][:10])))))
        
        else:
            print("#{0} {1}".format(tc + 1, ' '.join(list(map(str, result[::-1])))))
