import sys

input = sys.stdin.readline
B = list(map(int,input().split(" ")))
D = list(map(int,input().split(" ")))
J = list(map(int,input().split(" ")))
d_dist = abs(D[0]-J[0])+abs(D[1]-J[1])
b_dist = max(abs(B[0]-J[0]),abs(B[1]-J[1]))
if b_dist<d_dist:
    print("bessie")
elif b_dist>d_dist:
    print("daisy")
else:
    print("tie")