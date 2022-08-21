import sys

input = sys.stdin.readline
cnt=0
while True:
    p,s=list(map(int,input().split()))
    if p==s==0:
        break
    cnt+=1
    print(f"Hole #{cnt}")
    a=s-p
    if a==0:
        print("Par.")
    elif a==-1:
        print('Birdie.')
    elif a==-2:
        if s==1:
            print('Hole-in-one.')
        else:
            print('Eagle.')
    elif a==-3:
        print('Double eagle.')
    elif a==1:
        print('Bogey.')
    else:
        print('Double Bogey.')
    print()