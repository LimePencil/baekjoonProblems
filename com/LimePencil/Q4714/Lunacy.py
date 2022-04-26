import sys

input = sys.stdin.readline
while True:
    n = float(input())
    if n==-1:
        break
    print("Objects weighing {:.2f} on Earth will weigh {:.2f} on the moon.".format(n,n*0.167))