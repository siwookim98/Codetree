import sys

# 변수를 선언하고 입력을 받습니다
n = int(input())
A = list(map(int, input().split()))

min_dist = sys.maxsize
# 각 i번째 집으로 모였을 때의 합을 구해준다
for i in range(n):
    sum_dist = 0
    for j in range(n):
        sum_dist += abs(j - i) * A[j]

        #가능한 거리의 합 중 최솟값을 구해준다
    min_dist = min(min_dist, sum_dist)
    
# 결과를 출력한다
print(min_dist)