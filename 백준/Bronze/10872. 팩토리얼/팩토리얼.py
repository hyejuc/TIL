def Nfactorial(N):
    f=1
    if N>0:
        f=N*Nfactorial(N-1)
    return f
N=int(input())
print(Nfactorial(N))