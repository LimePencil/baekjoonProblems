import sys

sys.setrecursionlimit(10**4)
n =  int(sys.stdin.readline())
count = 0


def backtracking(l,v,length):
    if length > n: 
        global count
        count +=1
        return
    for i in range(1,n+1):
        if v[i-1] == False and check_possible(i,length,l):
            v_c = v[:]
            l_c = l[:]
            l_c.append(i)
            v_c[i-1] = True
            backtracking(l_c,v_c,length+1)

def check_possible(a,b,ls):
    for y,x in enumerate(ls,1):
        if abs(a-x) == abs(b-y):
            return False
    return True


for i in range(1,n+1):
    vi = [False]*n
    vi[i-1] = True
    backtracking([i],vi,2)

sys.stdout.write(str(count))