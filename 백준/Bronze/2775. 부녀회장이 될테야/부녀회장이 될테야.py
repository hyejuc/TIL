T=int(input())
for i in range(T):
    k=int(input())
    n=int(input())
    f0=[x for x in range(1,n+1)]
    for a in range(1,k+1):
        for b in range(1,n):
            f0[b]+=f0[b-1]
    print(f0[-1])