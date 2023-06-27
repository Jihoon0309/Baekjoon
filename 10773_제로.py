import sys
input=sys.stdin.readline
K=int(input())

num_list=[]
for _ in range(K):
    num=int(input())
    if num!=0:
        num_list.append(num)
    else:
        del num_list[-1]

print(sum(num_list))
