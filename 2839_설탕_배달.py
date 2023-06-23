N=int(input())

a=3
b=5
result=5000

for i in range(1,N//b+1):
    if (N-(b*i))%a==0:
        result_sum=i+(N-(b*i))//a
        if result>result_sum:
            result=result_sum

if result==5000 and (N%a==0):
    result=N//a

if result==5000:
    result=-1

print(result)