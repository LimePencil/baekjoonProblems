import sys

input = sys.stdin.readline
cnt=1
while True:
    a,b,c= list(map(int,input().split()))
    if a==0 and b==0 and c==0:
        break
    print("Triangle #{}".format(cnt))
    cnt+=1
    if a==-1:
        if b>=c:
            print("Impossible.")
        else:
            print("a = {:.3f}".format((c**2-b**2)**0.5))
    elif b==-1:
        if a>=c:
            print("Impossible.")
        else:
            print("b = {:.3f}".format((c**2-a**2)**0.5))
    else:
        print("c = {:.3f}".format((a**2+b**2)**0.5))
    print()