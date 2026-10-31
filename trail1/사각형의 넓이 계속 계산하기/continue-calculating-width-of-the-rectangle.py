while True:
    width, height, char = input().split()
    width = int(width)
    height = int(height)
    print(width * height)
    if char == 'C':
        break
