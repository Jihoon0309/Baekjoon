import sys
input=sys.stdin.readline

N, K = map(int, input().split())
list_num=[]
list_result=[]


for i in range(1,N+1):
    list_num.append(i)
    

while len(list_result)!=N:
    for i in range(K):
        if i!=K-1:
            pop=list_num.pop(0)
            list_num.append(pop)
        else:
            pop=list_num.pop(0)
    list_result.append(pop)

print('<', end='')
print(', '.join(map(str,list_result)), end='')
print('>')