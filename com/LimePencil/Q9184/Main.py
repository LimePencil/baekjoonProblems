import sys

def recur(a,b,c):
    if a<=0 or b<=0 or c<=0:
        return 1
    elif a>20 or b>20 or c>20:
        return 1048576
    elif mem[a][b][c] != None:
        return mem[a][b][c]
    elif a<b and b<c:
        mem[a][b][c] = recur(a,b,c-1) + recur(a,b-1,c-1) - recur(a,b-1,c)
        return mem[a][b][c]
    else:
        mem[a][b][c] = recur(a-1,b,c) + recur(a-1,b-1,c)+ recur(a-1,b,c-1)-recur(a-1,b-1,c-1)
        return mem[a][b][c]
read = ""
while (read := list(map(int,sys.stdin.readline().strip('\n').split(" ")))) != [-1,-1,-1]:
    a,b,c = read
    mem = [[[None for k in range(21)] for j in range(21)] for i in range(21)]
    ans = recur(a,b,c)
    sys.stdout.write("w(" + str(a) + ", "+ str(b) +", "+ str(c) +") = " + str(ans)+"\n")