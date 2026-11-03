n = int(input())
cnt = 0

while True:

    if n % 2 == 0:
        cnt += 1
        n /= 2
        # print(cnt)
    
    else:
        if n == 1:
            break
        else:
            cnt += 1
            n = 3*n + 1
            # print(cnt)
        
print(cnt)    
