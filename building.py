floor_count = int(input())
rooms_per_floor = int(input())
letter_of_floor = ""

for floors in range(floor_count, 0, -1):
    print()
    for rooms in range(rooms_per_floor):
        if floors == floor_count:
            letter_of_floor = "L"
        elif floors % 2 == 0:
            letter_of_floor = "O"
        else:
            letter_of_floor = "A"
        print(f"{letter_of_floor}{floors}{rooms}", end=" ")

