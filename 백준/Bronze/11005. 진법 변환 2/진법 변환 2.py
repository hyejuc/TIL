import sys

N,B=map(int,sys.stdin.readline().split())
res=''
while N:
    if B<10:
        res+=str(N%B)
    else:
        if N%B<10:
            res += str(N % B)
        else:
            res+=chr(int(N%B)+55)
    N//=B
print(res[::-1])