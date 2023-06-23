N=int(input())

result=0

for i in range(1,N+1):
    result=sum([int(j) for j in str(i)])+i
    if result==N:
        print(i)
        break
    if i==N:
        print(0)