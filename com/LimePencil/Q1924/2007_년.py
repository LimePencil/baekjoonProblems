import sys
import datetime

input = sys.stdin.readline
days = ["MON","TUE","WED","THU","FRI","SAT","SUN"]
m,d = list(map(int,input().split()))
a =datetime.date(2007,m,d).weekday()
print(days[a])