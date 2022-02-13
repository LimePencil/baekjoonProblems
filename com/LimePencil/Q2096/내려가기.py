import sys

n = int(sys.stdin.readline().rstrip("\n"))
dp_max = [[0 for _ in range(3)] for _ in range(2)]
dp_min = [[0 for _ in range(3)] for _ in range(2)]

k = 1
for i in range(n):
    x,y,z = list(map(int,sys.stdin.readline().rstrip("\n").split(" ")))
    dp_max[k][0] = max(dp_max[k-1][0],dp_max[k-1][1])+ x
    dp_max[k][1] = max(dp_max[k-1][0],dp_max[k-1][1],dp_max[k-1][2])+ y
    dp_max[k][2] = max(dp_max[k-1][1],dp_max[k-1][2])+ z

    dp_min[k][0] = min(dp_min[k-1][0],dp_min[k-1][1])+ x
    dp_min[k][1] = min(dp_min[k-1][0],dp_min[k-1][1],dp_min[k-1][2])+ y
    dp_min[k][2] = min(dp_min[k-1][1],dp_min[k-1][2])+ z
    k=1-k

print(str(max(dp_max[1-k][0],dp_max[1-k][1],dp_max[1-k][2])) + " " +str(min(dp_min[1-k][0],dp_min[1-k][1],dp_min[1-k][2])))