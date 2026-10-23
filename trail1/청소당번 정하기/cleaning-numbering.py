n = int(input())
classroom_cleaning = 0
hallway_cleaning = 0
restroom_cleaning = 0
for i in range(1, n+1):
    if i % 12 == 0:
        restroom_cleaning += 1
    elif i % 3 == 0:
        hallway_cleaning += 1
    elif i % 2 == 0:
        classroom_cleaning += 1
print(classroom_cleaning, hallway_cleaning, restroom_cleaning)