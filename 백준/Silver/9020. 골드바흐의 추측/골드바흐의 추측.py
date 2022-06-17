s=list()
for j in range(2, 10001):
    for l in range(2, int(j ** 0.5) + 1):
        if j % l == 0:
            break
    else:
        s.append(j)
T=int(input())
for i in range(T):
    n=int(input())
    for k in s:
        if k > (0.5 * n):
            a = s.index(k)
            S = s[:a]
            break
    for j in reversed(S):
        if n - j in s:
            print(j, n-j)
            break
    S=s