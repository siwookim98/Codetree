arr = list(map(int, input().split()))
arr1 = []
result = 0

for elem in arr:
    if elem == 0:
        break
    arr1.append(elem)
# print(arr1)
for elem in arr1[-1:-4:-1]:
    result += elem

print(result)