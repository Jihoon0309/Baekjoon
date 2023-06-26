N=int(input())

result=0
name_set=set()
for i in range(N):
    name=input()
    if name=='ENTER':
        if name_set:
            result+=len(name_set)
            name_set=set()
    else:
        name_set.add(name)
result+=len(name_set)
print(result)