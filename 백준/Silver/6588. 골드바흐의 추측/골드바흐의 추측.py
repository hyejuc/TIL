import sys

s=[False,False]+[True]*(1000000-1)
for i in range(2,int(1000000**0.5)+1):
    if s[i]:
        for j in range(2*i,1000000+1,i):
            s[j]=False
while True:
    n=int(sys.stdin.readline())
    if not n:
        break
    if n==0:
        break
    for i in range(3,n):
        if s[i] and s[n-i]:
            print(n,'=',i,'+',n-i)
            break
    else:
        print("Goldbach's conjecture is worng.")