N=int(input())
card_N=map(int, input().split())
num_dict={}
for i in card_N:
    num_dict[i]=num_dict.get(i,0)+1

result=[]
M=int(input())
card_M=map(int, input().split())
for num in card_M:
    if num in num_dict:
        result.append(num_dict[num])
    else:
        result.append(0)

print(*result)