import sys
N = int(sys.stdin.readline()) #26
N_1 = N #26
i=0
while True:
    if N<10:
        N=int(str(N)*2)
        i+=1
    else:
        a=int(str(N)[0])+int(str(N)[1]) 
        N=int(str(N)[1]+str(a)[-1]) 
        i+=1
    if N == N_1:
        break
print(i)