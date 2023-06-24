N=int(input())

name_dic={}

for _ in range(N):
    name, record= input().split()

    if record=='enter':
        name_dic[name]='enter'
    else:
        del name_dic[name]
    
result=sorted(name_dic, reverse=True)
for i in result:
    print(i)
