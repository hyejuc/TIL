import sys

T=int(sys.stdin.readline())
for i in range(T):
    H, W, N = map(int, sys.stdin.readline().split())
    h=N%H
    d = (N // H) + 1
    if N%H==0:
        h=H
        d=N//H
    if d<10:
        print(f'{h}0{d}')
    else:
        print(f'{h}{d}')