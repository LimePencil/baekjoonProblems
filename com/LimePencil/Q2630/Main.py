import sys

n = int(sys.stdin.readline().strip("\n"))
table = []
for _ in range(n):
    table.append(list(map(int,sys.stdin.readline().strip("\n").split(" "))))

def possible(x,y,n):
    top_left = table[x][y]
    for i in range(x,x+n):
        for j in range(y,y+n):
            if table[i][j] != top_left:
                return -1
    return 0 if top_left == 0 else 1

def div_conquer(x,y,n):
    global num_blue
    global num_white
    if n == 0:
        return
    poss = possible(x,y,n)
    if poss == -1:
        div_conquer(x,y,int(n/2))
        div_conquer(x+int(n/2),y,int(n/2))
        div_conquer(x,y+int(n/2),int(n/2))
        div_conquer(x+int(n/2),y+int(n/2),int(n/2))
    elif poss == 0:
        num_white += 1
    else:
        num_blue += 1



num_blue = 0
num_white = 0

div_conquer(0,0,n)
sys.stdout.write(str(num_white) + "\n"+ str(num_blue))
