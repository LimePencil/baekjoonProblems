import sys

input = sys.stdin.readline
nums=[0]*10
n = input().rstrip()
six_or_nine=0
for i in n:
    if i=="6"or i== "9":
        six_or_nine+=1
    else:
        nums[int(i)]+=1
print(max(max(nums),(six_or_nine+1)//2))