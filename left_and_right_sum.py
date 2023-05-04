count_number = int(input())
left_number = 0
right_number = 0
for number in range(count_number * 2):
    current_number = int(input())
    if number < count_number:
        left_number += current_number
    else:
        right_number += current_number
if left_number == right_number:
    print(f"Yes, sum = {left_number}")
else:
    diff = abs(left_number - right_number)
    print(f"No, diff = {diff}")