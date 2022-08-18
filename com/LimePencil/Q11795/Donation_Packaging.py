import sys

input = sys.stdin.readline
a_acc=0
b_acc=0
c_acc=0
for _ in range(int(input())):
    a,b,c=list(map(int,input().split()))
    a_acc+=a
    b_acc+=b
    c_acc+=c
    m=min(a_acc,b_acc,c_acc)
    if m>=30:
        print(m)
        a_acc-=m
        b_acc-=m
        c_acc-=m
    else:
        print("NO")