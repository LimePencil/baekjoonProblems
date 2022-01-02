import sys
# extended euclidean algorithm
# chinese remainder theorem
def EEA(a,b):
    s1,s2,t1,t2 = 1, 0, 0, 1
    while b:
        q = a//b
        a,b = b,a-q*b
        s1,s2 = s2,s1-q*s2
        t1,t2 = t2,t1-q*t2
    return a,s1,t1

t= int(sys.stdin.readline().rstrip("\n"))
for _ in range(t):
    n,m,x,y = list(map(int,sys.stdin.readline().rstrip("\n").split(" ")))
    if m>n:
        x,y = y,x
        n,m = m,n
    g,a,b = EEA(n,m)
    lcm = n*m//g
    d = x-y
    if d%g !=0:
        print("-1")
    else:
        K=x-d//g*a*n
        print((K-1)%lcm+1)