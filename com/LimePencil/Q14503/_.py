import sys

n,m =list(map(int,sys.stdin.readline().rstrip("\n").split(" ")))
r,c,d = list(map(int,sys.stdin.readline().rstrip("\n").split(" ")))
arr = []
cleaned = 0
directions = [(-1,0),(0,-1),(1,0),(0,1)]
if d==3:
    d= 1
elif d==1:
    d=3
for _ in range(n):
    arr.append(list(map(int,sys.stdin.readline().rstrip("\n").split(" "))))
while True:
    if arr[r][c] == 0:
        cleaned +=1
        arr[r][c] = 2
    left = arr[r+directions[(d+1)%4][0]][c+directions[(d+1)%4][1]]
    right = arr[r+directions[(d+3)%4][0]][c+directions[(d+3)%4][1]]
    back = arr[r+directions[(d+2)%4][0]][c+directions[(d+2)%4][1]]
    front = arr[r+directions[d][0]][c+directions[d][1]]
    if left != 0 and right != 0 and back != 0 and front !=0:
        if back == 1:
            break
        else:
            r -= directions[d][0]
            c -= directions[d][1]
    elif left == 0:
        d = (d+1)%4
        r += directions[d][0]
        c += directions[d][1]
    elif left != 0:
        d = (d+1)%4
print(cleaned)


