arr = list(map(int, input().split()))
new = [0] * 10

for elem in arr:
    if elem == 0:
        break
    new[elem // 10] += 1

for i in range(1, 10):
    print(f'{i} - {new[i]}')
    