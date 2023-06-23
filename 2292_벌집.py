N=int(input())

num=6
room=1
result=1
while N>room:
    room+=num
    num+=6
    result+=1
print(result)
