import sys

input = lambda: sys.stdin.readline().rstrip()

def good(st):
    l=len(st)
    for i in range(1,l//2+1):
        if st[l-i:]==st[l-2*i:l-i]:
            return False
    return True


def recur(i,s):
    if i==n:
        print(s)
        exit()
    for j in range(1,4):
        if good(s+str(j)):
            recur(i+1,s+str(j))

n = int(input())
recur(1,"1")