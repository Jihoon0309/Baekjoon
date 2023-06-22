N=int(input())

dot=3
for i in range(N-1):
    dot+=dot-1

print(dot*dot)