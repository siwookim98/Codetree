n = int(input())
scores = list(map(float, input().split()))

sum_score = sum(scores) / n
print(f'{sum_score:.1f}')

if sum_score >= 4.0:
    print('Perfect')
elif sum_score >= 3.0:
    print('Good')
else:
    print('Poor')