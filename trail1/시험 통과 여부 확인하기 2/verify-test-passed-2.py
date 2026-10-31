n = int(input())
cnt = 0

for _ in range(1, n+1):
    scores = list(map(int, input().split()))

    average = sum(scores) // len(scores)
    
    if average >= 60:
        cnt += 1
        print('pass')
        
    else:
        print('fail')
        
print(cnt)
