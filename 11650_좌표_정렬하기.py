N=int(input())

list_all=[]
for _ in range(N):
    list_num = list(map(int, input().split()))
    list_all.append(list_num)

list_all[0].sort()

for i in list_all:
    print(*i)