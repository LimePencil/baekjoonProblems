import sys

def print_star(x,y,o):
    if o == 3:
        star[x][y] = "*"
        star[x+1][y-1] = "*"
        star[x+1][y+1] = "*"
        for i in range(-2,3):
            star[x+2][i+y] = "*"
    else:
        print_star(x,y,o//2)
        print_star(x+o//2,y+o//2,o//2)
        print_star(x+o//2,y-o//2,o//2)

n = int(sys.stdin.readline().rstrip("\n"))

star =[[" " for _ in range(2*n)]for _ in range(n)]

print_star(0,n-1,n)
for i in range(n):
    print("".join(star[i]))
