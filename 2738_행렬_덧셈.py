N, M = map(int, input().split())

A=[]
B=[]
result=[]

for _ in range(N):
    matrix_1 = A.append(list(map (int, input().split())))

for _ in range(N):
    matrix_2 = B.append(list(map (int, input().split())))

for i,j in zip(A,B):
    result_sum=[]
    for x,y in zip(i,j):
        result_sum.append(x+y)
    result.append(result_sum)

for i in result:
    for j in i:
        print(j, end=' ')
    print()