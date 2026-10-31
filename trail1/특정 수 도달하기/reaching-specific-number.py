arr = list(map(int, input().split()))
arr_min250 = []
sum = 0

for elem in arr:
    if elem <= 250:
        arr_min250.append(elem)
    else:
        break

n = len(arr_min250)
for num in arr_min250:
    sum += num

avg = sum / n
print(f'{sum} {avg:.1f}')
