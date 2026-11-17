matrix = [list(map(int, input().split())) for _ in range(4)]
# print(matrix)
sum = 0

for i in range(4):
    for j in range(4):
        if j <= i:
            sum += matrix[i][j]

print(sum)