numbers = [int(input()) for _ in range(5)]
cnt = 0
for number in numbers:
    if number % 2 == 0:
        cnt += 1
print(cnt)