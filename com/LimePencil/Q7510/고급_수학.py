import sys

input = sys.stdin.readline
for t in range(int(input())):
    a,b,c= sorted(list(map(int,input().split())))
    
    print("Scenario #{}:".format(t+1))
    print("yes" if a**2+b**2==c**2 else "no")
    print()