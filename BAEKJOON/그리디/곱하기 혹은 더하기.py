# 첫째 줄에 만들어질 수 있는 가장 큰 수를 출력하기

S = list(map(int, input()))

# 가장 큰 수를 만들기 위해서는 '+', 'x'만 사용
for i in range(len(S)-1):
    if S[i] <= 1 or S[i+1] <= 1:
        S[i+1] += S[i]
    else:
        S[i+1] *= S[i]

print(S[-1])
