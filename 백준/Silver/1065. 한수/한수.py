import sys

N=int(sys.stdin.readline())
def hansu_num(N):
    if N<100:
        return N
    else:
        n=99
        for i in range(100,N+1):
            I=list(str(i))
            if int(I[0])-int(I[1])==int(I[1])-int(I[2]):
                n+=1
            i+=1
        return n
print(hansu_num(N))