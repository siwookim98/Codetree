a, b = map(int, input().split())

remain = [0] * b

while True:
    if a <= 1:
        break
    
    remain[a % b] += 1
    a //= b

# print(remain)
result = sum(x ** 2 for x in remain)
print(result)