import sys

input = sys.stdin.readline
while True:
    try:
        n,w,d,r = list(map(int,input().split()))
        num_of_coin=n*(n-1)//2
        if r!=w*num_of_coin:
            print(abs(r-w*num_of_coin)//d)
        else:
            print(n)
    except:
        break