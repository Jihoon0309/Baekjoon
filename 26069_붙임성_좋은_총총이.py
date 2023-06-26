N=int(input())

dance=set()
for i in range(N):
    A, B = input().split()

    if (A == 'ChongChong') or (B == 'ChongChong'):
        dance.add(A)
        dance.add(B)

    if 'ChongChong' in dance and ((A in dance) or (B in dance)):
        dance.add(A)
        dance.add(B)

print(len(dance))
