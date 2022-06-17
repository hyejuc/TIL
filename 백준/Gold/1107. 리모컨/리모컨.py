import sys

N=int(sys.stdin.readline())
M=int(sys.stdin.readline())
ans = abs(N - 100)
if M==0:
    print(min(len(str(N)), ans))
else:
    b = sorted(list(map(int, sys.stdin.readline().split())))
    for i in range(1000000):
        for j in range(len(str(i))):
            if int(str(i)[j]) in b:
                break
        else:
            ans = min(ans, abs(N - i) + len(str(i)))
    print(ans)