import sys
input=sys.stdin.readline
N, M =map(int, input().split())

poketmon_name={}
poketmon_num={}

for i in range(1,N+1):
    name = input().strip()
    poketmon_name[name]=i
    poketmon_num[i]=name
    
for _ in range(M):
    result=input().strip()
    if result.isdigit()==False:
        print(poketmon_name[result])
    else:
        print(poketmon_num[int(result)])