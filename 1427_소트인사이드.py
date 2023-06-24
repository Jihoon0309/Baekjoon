N=map(int, input())

list_N=list(N)

list_N.sort(reverse=True)

for i in list_N:
    print(i,end='')