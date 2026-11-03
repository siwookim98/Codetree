def is_magic_number(n):
    result = ''
    if n % 2 == 0 and (n // 10 + n % 10) % 5 == 0:
        result = 'Yes'
    else:
        result = 'No'
    
    return result

n = int(input())

print(is_magic_number(n))