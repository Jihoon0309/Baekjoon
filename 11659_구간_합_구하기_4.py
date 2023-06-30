import sys
input = sys.stdin.readline

N, M =map(int, input().split())

num_list=list(map(int, input().split()))
sum_list=[0]
num_sum=0

for num in num_list:
    num_sum+=num
    sum_list.append(num_sum)

for _ in range(M):
    i, j = map(int, input().split())
    result=sum_list[j]-sum_list[i-1]
    print(result)