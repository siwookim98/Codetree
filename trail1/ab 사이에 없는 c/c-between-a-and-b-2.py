a,b,c = map(int,input().split())

satisfied = 'YES'
for i in range(a, b+1):
    if i % c == 0:
        satisfied = 'NO'

print(satisfied)