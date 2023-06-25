N, M = map(int, input().split())


num_dict_N={key: None for key in map(int, input().split())}
num_M=list(map(int, input().split()))
overlap=0

for i in num_M:
    if i in num_dict_N.keys():
        overlap+=1

print(len(num_dict_N)+len(num_M)-overlap*2)
