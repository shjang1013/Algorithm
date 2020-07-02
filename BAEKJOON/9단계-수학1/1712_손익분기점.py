# 총 수입(판매비용) > 총 비용(=고정비용+가변비용)
# Cx(개수) > A + Bx
A, B, C = map(int, input().split())

print(A//(C-B)+1) if B < C else print(-1)
