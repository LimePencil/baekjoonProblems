import sys

def backtracking(order,max_order):
    global minimum, maximum
    global nums
    global addition, substraction, multiplication, division
    global total
    if max_order == order+1:
        minimum = min(minimum,total)
        maximum = max(maximum,total)
        return
    if(addition > 0):
        addition -= 1
        order +=1
        total += nums[order]
        backtracking(order,max_order)
        total -= nums[order]
        addition += 1
        order -=1
    if(substraction > 0):
        substraction -= 1
        order +=1
        total -= nums[order]
        backtracking(order,max_order)
        total += nums[order]
        substraction += 1
        order -=1
    if(multiplication > 0):
        multiplication -= 1
        order +=1
        total *= nums[order]
        backtracking(order,max_order)
        total //= nums[order]
        multiplication += 1
        order -=1
    if(division > 0):
        division -= 1
        order +=1
        prev_total = total
        if total < 0:
            total = -((abs(total)) // nums[order])
        else:
            total //= nums[order]
        backtracking(order,max_order)
        total = prev_total
        division += 1
        order -=1

    

n = int(sys.stdin.readline().rstrip("\n"))

nums = list(map(int,sys.stdin.readline().rstrip("\n").split(" ")))

addition, substraction, multiplication, division = list(map(int,sys.stdin.readline().rstrip("\n").split(" ")))

minimum = float('inf')
maximum = float('-inf')
total = nums[0]
backtracking(0,n)

print(maximum)
print(minimum)