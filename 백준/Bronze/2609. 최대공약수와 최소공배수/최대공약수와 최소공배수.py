import sys

n=list(map(int,sys.stdin.readline().split()))
y=[]
for i in range(1, min(n) + 1):
    if n[0] % i == 0 and n[1] % i == 0:
        y.append(i)
print(max(y))
i = 1
while True:
    if (max(n) * i) % min(n) == 0:
        print(max(n) * i)
        break
    i += 1
