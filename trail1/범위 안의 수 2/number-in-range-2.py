arr = [int(input()) for _ in range(10)]
sum = 0
cnt = 0

for i in arr:
    if 0 <= i <= 200:
        sum += i
        cnt += 1

print(f'{sum} {sum/cnt:.1f}')