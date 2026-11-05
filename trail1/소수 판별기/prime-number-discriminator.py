n = int(input())
satisfied = True

for i in range(2, n):
    # print(i)
    if n % i == 0:
        satisfied = False

if satisfied == True:
    print("P")
else:
    print("C")