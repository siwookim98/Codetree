dice = list(map(int, input().split()))
dice_cnt = [0] * 7

for elem in dice:
    dice_cnt[elem] += 1

for i in range(1, 7):
    cnt = dice_cnt[i]
    print(f'{i} - {cnt}')
