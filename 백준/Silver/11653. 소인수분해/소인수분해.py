N=int(input())
if N==1:
    pass
else:
    for i in range(2,N+1):
        while N%i==0:
            print(i)
            N/=i