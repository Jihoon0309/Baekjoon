martix=[]
for _ in range(1,10):
    a=list(map(int, input().split()))
    martix.append(a)

max_num=max(map(max, martix))

for i in range(len(martix)):
    for j in range(len(martix)):
        if martix[i][j] == max_num:
            row, col= i+1, j+1
            break

print(max_num)
print(row, col)