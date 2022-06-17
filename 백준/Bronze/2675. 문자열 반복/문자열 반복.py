import sys

T=int(sys.stdin.readline())
for i in range(T):
    R, S = sys.stdin.readline().split()
    R=int(R)
    S=list(S)
    a=str()
    for j in range(len(S)):
        a+=S[j]*R
        j+=1
    print(a)
    i+=1