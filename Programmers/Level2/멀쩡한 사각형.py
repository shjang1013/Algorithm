# 참고하여 풀은 코드
import math

def solution(w,h):
    # w, h의 최대공약수를 이용하여 푸는 방법
    # 정사각형의 개수 - 정사각형을 사용할 수 없는 개수
    return w*h - (w+h-math.gcd(w,h))
