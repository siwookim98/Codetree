arr = list(map(int, input().split()))
arr1 = []

for i in arr:
    if i == 0:
        break
    arr1.append(i)

print(f'{sum(arr1)} {sum(arr1) / len(arr1):.1f}')