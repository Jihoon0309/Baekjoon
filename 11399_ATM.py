import sys
input = sys.stdin.readline

N=int(input())

people=list(map(int, input().split()))

time=0
time_list=[]
people.sort()

for i in range(len(people)):
    time+=people[i]
    time_list.append(time)

print(sum(time_list))