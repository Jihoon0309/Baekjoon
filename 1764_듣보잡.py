N, M=map(int, input().split())

name_dict={}
result=[]
for _ in range(N):
    name_N=input()
    name_dict[name_N]=None


for i in range(M):
    name_M=input()

    if name_M in name_dict.keys():
        result.append(name_M)

result.sort()
print(len(result))

for i in result:
    print(i)