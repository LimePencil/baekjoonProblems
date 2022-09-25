import sys

input = lambda: sys.stdin.readline().rstrip()
for t in range(1,int(input())+1):
    n=int(input())
    if n==0:
        print(f"Case #{t}: INSOMNIA")
    else:
        s=set(list(str(n)))
        multiplyer=2
        while True:
            s=s.union(set(list(str(n*multiplyer))))
            if len(s)==10:
                print(f"Case #{t}: {n*multiplyer}")
                break
            multiplyer+=1