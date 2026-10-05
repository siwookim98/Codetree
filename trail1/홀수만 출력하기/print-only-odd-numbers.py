N = int(input())
arr = [int(input()) for _ in range(N)]
for num in arr:
    if num % 2 == 1 and num % 3 == 0:
        print(num)
    
