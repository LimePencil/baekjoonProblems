import sys

input = lambda: sys.stdin.readline().rstrip()


def perm(n,w_used,b_used,s,a):
    global greatest
    if w_used == n and b_used == n:
        greatest=max(greatest,a)
        return
    if w_used < n:
        perm(n, w_used+1, b_used, s+"w",(a+b)%100000)
    if b_used < w_used:
        perm(n, w_used, b_used + 1, s+"b",(a*c)%100000)


n,a,b,c=list(map(int,input().split()))
greatest=0
perm(n, 0, 0, "",a)
print(greatest)