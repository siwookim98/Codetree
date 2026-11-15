a1, a2 = map(int, input().split())
arr = [a1, a2]

for n in range(2, 10):
    arr.append(arr[n-1] + 2 * arr[n-2])

print(*arr)
