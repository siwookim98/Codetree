arr = list(map(int, input().split()))
new_arr = []

for elem in arr:
    if elem == 0:
        break
    elif elem % 2 == 1:
        new_arr.append(elem + 3)
    elif elem % 2 == 0:
        new_arr.append(elem // 2)

print(*new_arr)
    