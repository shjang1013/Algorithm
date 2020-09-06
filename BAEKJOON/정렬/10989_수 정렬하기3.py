# PyPy3로 채점하면 메모리 초과, Python3로 채점하면 통과
# 계수 정렬
import sys

N = int(sys.stdin.readline())

count = [0] * 10001

for i in range(N):
    count[int(sys.stdin.readline())] += 1

for i in range(len(count)):
    if count[i] != 0:
        for j in range(count[i]):
            print(i)


1. 2751_수 정렬하기 시간 및 메모리
# PyPy3 메모리 : 211060KB, 시간 : 860ms
# Python3 메모리 : 82224KB, 시간 : 1368ms
# PyPy3는 시간적으로 유리하지만, 메모리는 Python3에 비해 많이 차지한다.
# 이유는? PyPy에서는 print가 sys.stdout.write에 비해 꽤 많은 메모리를 사용, Python에서는 차이 없음
