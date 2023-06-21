import sys
input=sys.stdin.readline

list_N=list(map(int, input().split()))
list_result=[1,1,2,2,2,8]

for i,j in zip(list_N,list_result):
    print(j-i, end=' ')