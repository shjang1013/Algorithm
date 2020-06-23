# 나의 코드
def DFS(computers, visited, start):
    stack = [start]
    while stack:
        node = stack.pop()
        if visited[node] == 0:
            visited[node] = 1
        for i in range(0, len(computers)):
            if computers[node][i] == 1 and visited[i] == 0:
                stack.append(i)


def solution(n, computers):
    answer = 0                              # 네트워크 개수를 저장할 변수
    visited = [0] * n                       # 방문한 노드를 체크할 리스트
    start = 0
    while 0 in visited:
        if visited[s] == 0:
            DFS(computers, visited, start)
            answer += 1
        start += 1
    return answer
