n = int(input())
words = list(map(int,input().split(" ")))
words.sort()
sum = 0
prev = 0
for i in words:
    prev = prev + i
    sum += prev
print(sum)