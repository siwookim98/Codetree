n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
dr = [-1,1,0,0]
dc = [0,0,-1,1]

over_point_3 = 0
for r in range(n):
    for c in range(n):
        
        cnt = 0
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if 0 <= nr < n and 0 <= nc < n:
                if grid[nr][nc] == 1:
                    cnt += 1
                    if cnt == 3:
                        over_point_3 += 1
print(over_point_3)