import sys
input=sys.stdin.readline

N, M =map(int, input().split())

basket=[i+1 for i in range(N)]


for _ in range(M):
        i, j =map(int, input().split())
        
        basket_reverse=[]
        for num in range(j,i-1,-1):
            basket_reverse.append(basket[num-1])
        
        n=0
        for num in range(i-1,j):
            basket[num]=basket_reverse[0+n]
            n+=1

print(basket)



