import sys

N=int(sys.stdin.readline())
res=''
if N==0:
    print(0)
else:
    while N:
        if N % (-2):
            res += '1'
            N = N // -2 + 1
        else:
            res += '0'
            N //= -2
    print(res[::-1])