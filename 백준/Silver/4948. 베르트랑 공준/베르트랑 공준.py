import sys
s=list()
for i in range(2,123456*2):
    for j in range(2,int(i**0.5)+1):
        if i%j==0:
            break
    else:
        s.append(i)
while True:
    n=int(sys.stdin.readline())
    cnt=0
    if n==0:
        break
    for i in s:
        if n<i<=2*n:
            cnt+=1
    print(cnt)