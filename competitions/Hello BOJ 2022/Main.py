from random import randint
import sys
 
t = int(sys.stdin.readline().rstrip("\n"))
for _ in range(t):
    A,B,C = list(map(int,sys.stdin.readline().rstrip("\n").split(" ")))
    # a = randint(10**8,10**9-1)
    # b = randint(10**8,10**9-1)
    # c = randint(10**8,10**9-1)
    a,b,c = sorted((A,B,C),reverse=True)
    maximum = max(a,b,c)
    s = sum([a,b,c])
    exceed = s//2 > 8*2*(10**8)
    if s%2 == 1 or 2*maximum >s or exceed:
        print("-1")
        continue
    l = [1,1,0,0,0,0]
    temp = (a+b-c)//2
    temp2 = s//2-(a+b-c)//2
    if (a+b-c)//2>=s//2-(a+b-c)//2:
        w= (a+b-c)//2
        w-=max(0,((a+b-c)//2)-(8*10**8-1)) 
    else:
        w= s//2-(a+b-c)//2
        w-=max(0,(s//2-a+b-c)//2-(8*10**8-1)) 
    h = s//2-w
    if w+h !=a:
        l[2] = 1+w
        l[3] = a-w+1
        l[4] = w-(a+b)+1
        l[5] = h+1
    else:
        l[2] = 1+w
        l[3] = 1+h
        l[4] = w-b+1
        l[5] = 1+h
    x1 = abs(l[2]-l[0])+abs(l[3]-l[1]) == a
    x2 = abs(l[4]-l[2])+abs(l[5]-l[3]) == b 
    x3 = abs(l[4]-l[0])+abs(l[5]-l[1]) == c
    deb = b-(abs(l[4]-l[2])+abs(l[5]-l[3]))
    if not (x1 and x2 and x3 and l[0] <= 8*10**8 and l[1] <= 8*10**8 and l[2] <= 8*10**8 and l[3] <= 8*10**8 and l[4] <= 8*10**8 and l[5] <= 8*10**8):
        print("-1")
    else:
        if (a,b,c) == (A,B,C):
            print(" ".join(map(str,l)))
        elif (a,b,c) == (A,C,B):
            l[2],l[3],l[4],l[5] = l[4],l[5],l[2],l[3]
            print(" ".join(map(str,l)))
        elif (a,b,c) == (B,A,C):
            l[0],l[1],l[2],l[3] = l[2],l[3],l[0],l[1]
            print(" ".join(map(str,l)))
        elif (a,b,c) == (B,C,A):
            l[0],l[1],l[2],l[3] = l[2],l[3],l[0],l[1]
            l[0],l[1],l[4],l[5] = l[4],l[5],l[0],l[1]
            print(" ".join(map(str,l)))
        elif (a,b,c) == (C,B,A):
            l[0],l[1],l[4],l[5] = l[4],l[5],l[0],l[1]
            print(" ".join(map(str,l)))
        elif (a,b,c) == (C,A,B):
            l[0],l[1],l[2],l[3] = l[2],l[3],l[0],l[1]
            l[2],l[3],l[4],l[5] = l[4],l[5],l[2],l[3]
            print(" ".join(map(str,l)))
        
    
