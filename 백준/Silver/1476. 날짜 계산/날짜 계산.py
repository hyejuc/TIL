import sys

E,S,M=map(int,sys.stdin.readline().split())
ans=1
if E==1 and S==1 and M==1:
    print(ans)
else:
    while True:
        if E == 1:
            E = 15
        else:
            E -= 1
        if S == 1:
            S = 28
        else:
            S -= 1
        if M == 1:
            M = 19
        else:
            M -= 1
        ans += 1
        if E == 1 and S == 1 and M == 1:
            break
    print(ans)