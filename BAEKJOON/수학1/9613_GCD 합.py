# 모든 쌍의 최대공약수의 합을 출력하기
from itertools import combinations
from math import gcd
import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    sum = 0
    
    case = list(map(int, input().split()))
    
    array = list(combinations(case[1:], 2))
    
    for i in array:
        sum += gcd(i[0], i[1])
    
    print(sum)

