import sys

def backtracking(l,length):
    if length == m:
        ls.append(l)    
        return
    for i in range(1,n+1):
        if i >= l[-1]:
            l_c = l.copy()
            l_c.append(i)
            backtracking(l_c,length+1)

n, m = list(map(int,sys.stdin.readline().strip('\n').split(" ")))
ls = []
ans = ""
for i in range(1,n+1):
    backtracking([i],1)
for x in ls:
    ans += " ".join(list(map(str,x))) + "\n"
sys.stdout.write(ans)