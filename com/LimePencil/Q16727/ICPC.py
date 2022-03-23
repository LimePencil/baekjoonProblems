import sys

input = sys.stdin.readline
p1,e1 = list(map(int,input().split(" ")))
e2,p2 = list(map(int,input().split(" ")))
if p1+p2 >e1+e2:
    print("Persepolis")
elif p1+p2 <e1+e2:
    print("Esteghlal")
else:
    if p2>e1:
        print("Persepolis") 
    elif p2<e1:
        print("Esteghlal")
    else:
        print("Penalty")