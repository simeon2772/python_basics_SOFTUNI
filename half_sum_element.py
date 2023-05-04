import sys

number = int(input())
total_sum = 0
max_number = -sys.maxsize
for numbers in range(1, number + 1):
    current_number = int(input())
    total_sum += current_number
    if current_number > max_number:
        max_number = current_number

sum = total_sum - max_number
if sum == max_number:
    print("Yes")
    print(f"Sum = {sum}")
else:
    print("No")
    diff = abs(sum - max_number)
    print(f"Diff = {diff}")