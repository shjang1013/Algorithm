# 첫째 줄에 Hamming Distance의 합이 가장 작은 DNA를 출력하고, 둘째 줄에는 Hamming Distance의 합을 출력하기
N, M = map(int, input().split())

# N개의 DNA
List = []

# Hamming Distance의 합
sum = 0

# Hamming Distance의 합이 가장 작은 문자열
s = ""

for i in range(N):
    List.append(input())

for i in range(M):
    DNA = [['A', 0], ['T', 0], ['G', 0], ['C', 0]]
    for j in range(N):
        for k in range(len(DNA)):
            if List[j][i] == DNA[k][0]:
                DNA[k][1] += 1

    DNA.sort(key=lambda x:(-x[1],x[0]))
    s += DNA[0][0]
    sum += (N-DNA[0][1])

print(s)
print(sum)
