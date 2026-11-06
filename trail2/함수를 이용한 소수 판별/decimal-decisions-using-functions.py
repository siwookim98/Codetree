a, b = map(int, input().split())
sum_prime = 0
def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


for j in range(a, b+1):
    if is_prime(j):
        sum_prime += j

print(sum_prime)
