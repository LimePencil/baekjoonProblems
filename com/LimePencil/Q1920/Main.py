import sys

def binary_search(arr, low, high, x):
    if high >= low:
        mid = (high + low) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
        else:
            return binary_search(arr, mid + 1, high, x)
 
    else:
        return -1

n = int(sys.stdin.readline())
numbers = list(map(int,sys.stdin.readline().strip('\n').split(" ")))
numbers.sort()

n = int(sys.stdin.readline())
items_to_find = list(map(int,sys.stdin.readline().strip('\n').split(" ")))
for i in items_to_find:
    sys.stdout.write(str(1 if binary_search(numbers,0, len(numbers)-1,i) !=-1 else 0)  +"\n")