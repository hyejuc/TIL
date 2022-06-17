import sys

C=int(sys.stdin.readline())
count=0
for i in range(C):
    a=list(map(int,sys.stdin.readline().split()))
    N=a[0]
    del a[0]
    m=sum(a)/len(a)
    for j in range(N):
        if a[j]>m:
            count+=1
    X=(count/N)*100
    print(f'{X:.3f}%')
    count=0
