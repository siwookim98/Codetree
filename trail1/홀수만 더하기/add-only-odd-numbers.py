n = int(input())
arr = [int(input()) for _ in range(n)]

sum = 0
for i in arr:
    if i % 2 == 1 and i % 3 == 0:
        sum += i
print(sum)
    