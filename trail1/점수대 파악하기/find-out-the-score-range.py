scores = list(map(int, input().split()))
scores_10 = [0] * 11

for score in scores:
    if score == 0:
        break
    scores_10[score // 10] += 1

for i in range(10, 0, -1):
    print(f'{i}0 - {scores_10[i]}')
    
