arr = list(map(int, input().split()))
a = sum(arr[1::2])
b = sum(arr[2::3]) / len(arr[2::3])
print(f'{a} {b:.1f}')
