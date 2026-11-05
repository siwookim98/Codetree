nums = [int(input()) for _ in range(5)]
satisfied = True

for num in nums:
    if num % 3 != 0:
        satisfied = False

if satisfied == True:
    print(1)
else:
    print(0)
    