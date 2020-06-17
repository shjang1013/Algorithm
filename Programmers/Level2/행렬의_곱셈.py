# 나의 코드
def solution(arr1, arr2):
    answer = []
    
    for i in range(len(arr1)):
        row = []
        for j in range(len(arr2[0])):
            temp = 0
            # len(arr1[0]) = len(arr2) : 행렬의 성질
            for k in range(len(arr1[0])):
                temp += arr1[i][k] * arr2[k][j]
            row.append(temp)
        answer.append(row)
    
    return answer

# zip을 이용하여 코드를 작성해 볼 것
