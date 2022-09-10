import sys

input = sys.stdin.readline
n = int(input())
t=n//100*60+n%100
print(f"{n} in Ottawa")
print(f"{(((t-180)//60)%24)*100+(t-180)%60} in Victoria")
print(f"{(((t-120)//60)%24)*100+(t-120)%60} in Edmonton")
print(f"{(((t-60)//60)%24)*100+(t-60)%60} in Winnipeg")
print(f"{(n)%2400} in Toronto")
print(f"{(((t+60)//60)%24)*100+(t+60)%60} in Halifax")
print(f"{(((t+90)//60)%24)*100+(t+90)%60} in St. John's")