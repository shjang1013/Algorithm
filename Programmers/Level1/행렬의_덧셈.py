# 나의 풀이
def solution(arr1, arr2):
    for i in range(len(arr1)):
        for j in range(len(arr1[0])):
            arr1[i][j] += arr2[i][j]

    return arr1

# zip을 이용한 풀이
def solution(arr1, arr2):
    answer = [[c + d for c, d in zip(a, b)] for a, b in zip(arr1, arr2)]
    return answer

# list(zip([1,2,3], [4,5,6]))
# [(1,4), (2,5), (3,6)]
