T=int(input())

Q, D, N, P = 25, 10, 5, 1

for _ in range(T):
    C=int(input())
    Q_num=C//Q
    C%=Q
    D_num=C//D
    C%=D
    N_num=C//N
    C%=N
    P_num=C//P
    print(int(Q_num), int(D_num), int(N_num), int(P_num))