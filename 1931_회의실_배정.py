import sys
input = sys.stdin.readline

N=int(input())
meeting_list=[]

for _ in range(N):
    time_list = list(map(int, input().split()))
    meeting_list.append(time_list)

meeting_list.sort(key=lambda num:num[0])
meeting_list.sort(key=lambda num:num[1])

result=0
end=0

for i in range(len(meeting_list)):
    if end <= meeting_list[i][0]:
        result+=1
        end=meeting_list[i][1]

print(result)