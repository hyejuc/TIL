def fivo(n):
    if n<=1:
        return n
    else:
        return fivo(n-1)+fivo(n-2)
n=int(input())
print(fivo(n))