arr = list(map(int, input().split()))
arr1 = []
cnt = 0
sum_val = 0

for i in arr:
    if i == 0:
        break
    arr1.append(i)

for i in arr1:
    if i % 2 == 0:
        cnt += 1
        sum_val += i

print(cnt, sum_val)
