n = int(input())
arr = [int(input()) for _ in range(n)]
sum = 0

for i in arr:
    sum += i

print(f'{sum} {sum/n:.1f}')