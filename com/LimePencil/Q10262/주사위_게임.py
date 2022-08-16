import sys

def seq_sum(n):
    return n*(n+1)//2

input = sys.stdin.readline
a1,b1,a2,b2 = list(map(int,input().split()))
c1,d1,c2,d2 = list(map(int,input().split()))
g=(seq_sum(b1)-seq_sum(a1-1))/(b1-a1+1)+(seq_sum(b2)-seq_sum(a2-1))/(b2-a2+1)
e=(seq_sum(d1)-seq_sum(c1-1))/(d1-c1+1)+(seq_sum(d2)-seq_sum(c2-1))/(d2-c2+1)
if e==g:
    print("Tie")
elif e>g:
    print("Emma")
else:
    print("Gunnar")