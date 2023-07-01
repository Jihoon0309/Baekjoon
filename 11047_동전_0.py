import sys
input = sys.stdin.readline

N,K=map(int, input().split())

money_list=[]
for _ in range(N):
    money_list.append(int(input()))

result=0

for i in range(len(money_list)):
    money=money_list[-1-i]
    if K>=money:
        count=K//money
        K-=(count*money)
        result+=count
    if K==0:
        break

print(result)