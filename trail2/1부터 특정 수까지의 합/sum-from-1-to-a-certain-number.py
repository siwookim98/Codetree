def func(n):
    sum = 0
    for i in range(1, n+1):
        sum += i
    
    result = sum // 10

    return result

n = int(input())

# Please write your code here.

a = func(n)
print(a)