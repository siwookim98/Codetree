arr = list(map(int, input().split()))
n = len(arr)
odd_arr = 0
even_arr = 0

for i in range(n):
    if i % 2 == 0:
        odd_arr += arr[i]
    else:
        even_arr += arr[i]

print(abs(odd_arr - even_arr))