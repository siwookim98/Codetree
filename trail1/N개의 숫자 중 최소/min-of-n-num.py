n = int(input())
a = list(map(int, input().split()))
min_val = a[0]
min_cnt = 0

for elem in a:
    if min_val >= elem:
        min_val = elem

for elem in a:
    if min_val == elem:
        min_cnt +=1

print(min_val, min_cnt)