import sys

input = sys.stdin.readline
while True:
    a,b,c,d=list(map(int,input().split()))
    if a==0 and b==0 and c==0 and d==0:
        break
    cnt=0
    while not (a==b and b==c and c==d):
        cnt+=1
        a_t=abs(a-b)
        b_t=abs(b-c)
        c_t=abs(c-d)
        d_t=abs(d-a)
        a,b,c,d=a_t,b_t,c_t,d_t
    print(cnt)