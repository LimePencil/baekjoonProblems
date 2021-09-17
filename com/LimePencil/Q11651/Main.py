import sys

n = int(sys.stdin.readline())
coor = []
for i in range(n):
    coordinate  = list(map(int,sys.stdin.readline().strip('\n').split(" ")))
    coor.append(coordinate)
coor.sort(key = lambda x:(x[1],x[0]))
ans = ""
for x,y in coor:
    ans += str(x) + " " + str(y) + '\n'
sys.stdout.write(ans)