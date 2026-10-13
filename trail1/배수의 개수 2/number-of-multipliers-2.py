datas = [int(input()) for _ in range(10)]
cnt = 0
for data in datas:
    if data % 2 == 1:
        cnt += 1
print(cnt)