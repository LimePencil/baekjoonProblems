import sys
import datetime

input = sys.stdin.readline
n = int(input())
for i in range(n):
    h,m=list(map(int,input().split()))
    t=datetime.timedelta(hours=h,minutes=m)-datetime.timedelta(minutes=45)
    print("Case #{}:".format(i+1),t.seconds//3600,(t.seconds//60)%60)