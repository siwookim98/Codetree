N = int(input())
cnt = 0

for i in range(N):
    scores = list(map(int, input().split()))

    sum_score = 0

    for score in scores:
        sum_score += score
        
    average = sum_score // 4
    
    if average >= 60:
        cnt += 1
        print('pass')
        
    else:
        print('fail')
print(cnt)
