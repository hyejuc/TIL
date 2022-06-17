import sys

N=list(map(str,sys.stdin.readline().strip()))
print(''.join(reversed(sorted(N))))