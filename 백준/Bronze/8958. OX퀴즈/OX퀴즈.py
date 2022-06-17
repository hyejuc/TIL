import sys

n=int(sys.stdin.readline())
score=0
N=0
for i in range(n):
    a=list(str(sys.stdin.readline()))
    for j in range(len(a)):
        if a[j]=='O':
            N+=1
            score+=1*N
            j+=1
        else:
            N=0
            j+=1
    print(score)
    score=0
    i+=1