import sys
from datetime import date, timedelta

input = sys.stdin.readline
for _ in range(int(input())):
    y,m=map(int,input().split())
    t=date(y,m,1)-timedelta(days=1)
    print(t.year,t.month,t.day)