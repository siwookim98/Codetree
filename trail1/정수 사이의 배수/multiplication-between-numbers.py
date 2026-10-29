a, b = list(map(int, input().split()))
sum = 0
avg_num = 0

for i in range(a, b+1):
    if i % 5 == 0 or i % 7 == 0:
        sum += i
        avg_num += 1
print(f'{sum} {sum / avg_num:.1f}')