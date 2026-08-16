A, B, C = map(int, input().split())
if A > B:
    if A > C:
        if B > C:
            print(B)
        else:
            print(C)
    else:
        if B > C:
            print(C)
        else:
            print(A)

else:
    if B > C:
        if C > A:
            print(C)
        else:
            print(A)
    else:
        if A > C:
            print(C)
        else:
            print(B)