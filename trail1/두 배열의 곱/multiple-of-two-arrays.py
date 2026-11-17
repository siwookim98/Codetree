A_grid = [list(map(int, input().split())) for _ in range(3)]
_ = input()
B_grid = [list(map(int, input().split())) for _ in range(3)]

new_grid = [[0] * 3 for _ in range(3)]
for i in range(3):
    for j in range(3):
        new_grid[i][j] = A_grid[i][j] * B_grid[i][j]

for i in range(3):
    for j in range(3):
        print(new_grid[i][j], end=' ')

    print()

