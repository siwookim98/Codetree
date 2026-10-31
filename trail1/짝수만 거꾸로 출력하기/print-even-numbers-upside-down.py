n = int(input())
arr = list(map(int, input().split()))
arr1 = []
for num in arr:
    if num % 2 == 0:
        arr1.append(num)

arr2 = arr1[::-1]
print(*arr2)