A, B, C = map(int, input().split())
if A == min(A, B, C):
    print(1, end= ' ')
else:
    print(0, end= ' ')

if A == B == C:
    print(1, end= ' ')
else:
    print(0)