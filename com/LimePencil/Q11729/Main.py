import sys

n = int(sys.stdin.readline().strip("\n"))
ans = str(2**n-1) + "\n"
sys.stdout.write(ans)
def hanoi(plate,a,b,c):
    global ans
    if plate == 1:
        sys.stdout.write(a + " " + c + "\n")
    else:
        hanoi(plate-1,a,c,b)
        sys.stdout.write(a + " " + c + "\n")
        hanoi(plate-1,b,a,c)

hanoi(n,"1","2","3")
