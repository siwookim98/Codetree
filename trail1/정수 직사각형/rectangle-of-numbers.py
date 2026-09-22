N, M = map(int, input().split())

arr_2d = [
    [0 for _ in range(M)]
    for _ in range(N)
]

num = 1
for r in range(N):
    for c in range(M):
        arr_2d[r][c] = num
        num += 1

for row in arr_2d:
    for elem in row:
        print(elem, end=' ')
    print()