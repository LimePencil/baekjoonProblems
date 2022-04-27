import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n=int(input())
    l=[]
    for i in range(1,n):
        for j in range(i+1,n):
            if i+j==n:
                l.append("{} {}".format(i,j))
    print("Pairs for {}: {}".format(n,", ".join(l)))