import collections
import math
import sys

N=int(sys.stdin.readline())
a=list()
for i in range(N):
    a.append(int(sys.stdin.readline()))
print(round(sum(a)/len(a)))
print(sorted(a)[math.floor(len(a)/2)])#math.floor:내림
C=collections.Counter(sorted(a)).most_common(2)
if len(a)>1:
    if C[0][1] == C[1][1]:
        print(C[1][0])
    else:
        print(C[0][0])
else:
    print(C[0][0])
print(max(a)-min(a))