clinic = [0] * 4

for i in range(3):
    cold, temp = map(str, input().split())
    temp = int(temp)

    if cold == 'Y' and temp >= 37:
        clinic[0] += 1
    elif cold == 'N' and temp >= 37:
        clinic[1] += 1
    elif cold == 'Y' and temp < 37:
        clinic[2] += 1
    else:
        clinic[3] += 1

    if clinic[0] >= 2:
        clinic.append('E')
    
print(*clinic)
