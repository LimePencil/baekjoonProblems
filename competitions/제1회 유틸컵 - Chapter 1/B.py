import datetime

# format of date is YYYY-MM-DD
current_date = input()
current_date=datetime.datetime.strptime(current_date, "%Y-%m-%d")
n=int(input())
cnt=0
for i in range(n):
    date_to_compare = input()
    date_to_compare=datetime.datetime.strptime(date_to_compare, "%Y-%m-%d")
    if date_to_compare >= current_date:
        cnt+=1
print(cnt)