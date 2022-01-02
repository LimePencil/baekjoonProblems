import sys

def rec(i,j,n):
    global ans
    same = True
    first = table[i][j]
    for a in range(i,i+n):
        for b in range(j,j+n):
            if first != table[a][b]:
                same = False
                break
        if not same:
            break
    if not same:
        n//=2
        print("(",end="")
        rec(i,j,n)
        rec(i,j+n,n)
        rec(i+n,j,n)
        rec(i+n,j+n,n)
        print(")",end="")

    else:
        print(table[a][b],end="")


n = int(sys.stdin.readline().rstrip("\n"))
table = []*n
ans = ""
for _ in range(n):
    s = sys.stdin.readline().rstrip("\n")
    l = []
    for i in s:
        l.append(int(i))
    table.append(l)
rec(0,0,n)
