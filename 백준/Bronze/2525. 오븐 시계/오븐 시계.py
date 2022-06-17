A,B=map(int,input().split())
C=int(input())
if A+C//60+(B+C%60)//60>=24:
    if B+C%60>=60:
        print(A+C//60+(B+C%60)//60-24,B+C%60-60)
    else:
        print(A+C//60+(B+C%60)//60-24,B+C%60)
else:
    if B+C%60>=60:
        print(A+C//60+(B+C%60)//60,B+C%60-60)
    else:
        print(A+C//60+(B+C%60)//60,B+C%60)