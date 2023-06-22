import sys
input=sys.stdin.readline

N, M = map(int, input().split())

basket=[0 for i in range(N)]
for _ in range(M):
    i, j, k = map(int, input().split())
    for ball in range(i-1,j):
        basket[ball] = k

for i in basket:
    print(i, end=' ')