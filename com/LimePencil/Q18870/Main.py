import sys

n = sys.stdin.readline()
nums = list(map(int,sys.stdin.readline().strip('\n').split(" ")))
dt = {}
ans = ""
nums_copy = nums.copy()
nums.sort()
count = 0
for x in nums:
    if x not in dt:
        dt[x] = count
        count+=1
for i in nums_copy:
    ans += str(dt[i])+ " "
sys.stdout.write(ans)