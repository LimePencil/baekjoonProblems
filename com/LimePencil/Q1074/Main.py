import sys

def recursive(i,j,ord):
    global r,c, ans
    if ord == 1:
        if i == r and j == c:
            pass
        elif i+1 == r and j ==c:
            ans +=2
        elif i == r and j+1 ==c:
            ans +=1
        elif i+1 ==r and j+1 ==c:
            ans +=3
        return
    if i<= r <i+2**(ord-1) and j<=c <j+2**(ord-1): # top left
        recursive(i,j,ord-1)
    elif i<=r <i+2**(ord-1) and j+2**(ord-1)<=c <j+2**ord: # top right
        ans += 2**(2*(ord-1))
        recursive(i,j+2**(ord-1),ord-1)
    elif i+2**(ord-1)<=r <i+2**ord and j<=c <j+2**(ord-1): # bottom left
        ans += 2*2**(2*(ord-1))
        recursive(i+2**(ord -1),j,ord-1)
    elif i+2**(ord-1)<=r <i+2**ord and j+2**(ord-1)<=c <j+2**ord: # bottom right
        ans += 3*2**(2*(ord-1))
        recursive(i+2**(ord -1),j+2**(ord-1),ord-1)

n,r,c = list(map(int,sys.stdin.readline().rstrip("\n").split(" ")))
ans = 0
recursive(0,0,n)
print(ans)