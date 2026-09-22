# 2차원 배열을 구현해 각 줄마다 정수를 입력받습니다.
arr_2d = [
    list(map(int, input().split())) 
    for _ in range(2)
    ]

# 가로 평균을 출력합니다.
for r in range(2):
    sum_val = 0
    for c in range(4):
        sum_val += arr_2d[r][c]
    print(f'{sum_val / 4:.1f}', end=' ')
print()

# 세로 평균을 출력합니다.
for c in range(4):
    sum_val = 0
    for r in range(2):
        sum_val += arr_2d[r][c]
    print(f'{sum_val / 2:.1f}', end=' ')
print()

# 전체 평균을 출력합니다. 
sum_val = 0
for c in range(4):
    for r in range(2):
        sum_val += arr_2d[r][c]
print(f'{sum_val / 8:.1f}')



