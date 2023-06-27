from collections import deque

T=int(input())

for i in range(T):
    N, M = map(int, input().split())

    list_num=deque(map(int, input().split()))
    order=0

    while True:
        max_num=max(list_num)
        if M==0 and list_num[0]==max_num:
            order+=1
            break
        elif M!=0 and list_num[0]!=max_num:
            M-=1
            pop=list_num.popleft()
            list_num.append(pop)

        elif M==0 and list_num[0]!=max_num:
            M=len(list_num)-1
            pop=list_num.popleft()
            list_num.append(pop)

        elif M!=0 and list_num[0]==max_num:
            pop=list_num.popleft()
            M-=1
            order+=1
    print(order)
