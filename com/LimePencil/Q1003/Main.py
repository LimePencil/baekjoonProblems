import sys

t = int(sys.stdin.readline())
one_called =[0]*41
zero_called =[0]*41
nums = []
maximum = -1
ans = ""
for i in range(t):
    n = int(sys.stdin.readline())
    maximum = max(n,maximum)
    nums.append(n)
for j in range(maximum+1):
    if j== 0:
        zero_called[j] = 1
    elif j == 1:
        one_called[j] = 1
    else:
        zero_called[j] = zero_called[j-1] + zero_called[j-2]
        one_called[j] = one_called[j-1] + one_called[j-2]
for n in nums:
    ans += str(zero_called[n]) + " " + str(one_called[n]) +"\n"
sys.stdout.write(ans)
