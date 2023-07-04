import sys
from collections import deque

input = sys.stdin.readline

N, M =map(int, input().split())
select_list=deque(list(map(int, input().split())))
num_list=deque()
count=0

for i in range(1,N+1):
    num_list.append(i)

while len(select_list)!=0:
    if num_list[0]!=select_list[0]:
        if (len(num_list)-num_list.index(select_list[0]))> \
            (num_list.index(select_list[0])-0):
            popleft=num_list.popleft()
            num_list.append(popleft)
            count+=1
        else:
            pop=num_list.pop()
            num_list.appendleft(pop)
            count+=1
    else:
        num_list.popleft()
        select_list.popleft()
print(count)
