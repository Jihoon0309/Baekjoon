N,M=map(int, input().split())

word_list=[]
result=0

for _ in range(N):
    word_N=input()
    word_list.append(word_N)

for _ in range(M):
    word_M=input()
    if word_M in word_list:
        result+=1

print(result)