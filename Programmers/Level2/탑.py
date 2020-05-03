def solution(answer):
    signal = [0] * len(answer)
    for i in range(len(answer)-1, 0, -1):
        for j in range(i-1,-1,-1):
            if answer[i] < answer[j]:
                signal[i] = j+1
                break

    return signal
