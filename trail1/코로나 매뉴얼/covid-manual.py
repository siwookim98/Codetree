flu_a, bt_a = input().split()
flu_b, bt_b = input().split()
flu_c, bt_c = input().split()

cnt = 0
if flu_a == 'Y' and int(bt_a) >= 37:
    cnt += 1
if flu_b == 'Y' and int(bt_b) >= 37:
    cnt += 1
if flu_c == 'Y' and int(bt_c) >= 37:
    cnt += 1

if cnt >= 2:
    print('E')
else:
    print('N')
