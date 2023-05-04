begging_number = int(input())
ending_number = int(input())
magical_number = int(input())
counter = 0
combination_found = False
for first_number in range(begging_number, ending_number + 1):
    for second_number in range(begging_number, ending_number + 1):
        counter += 1
        if first_number + second_number == magical_number:
            combination_found = True
            break
    if combination_found:
        break
if combination_found:
    print(f"Combination N:{counter} ({first_number} + {second_number} = {magical_number})")
else:
    print(f"{counter} combinations - neither equals {magical_number}")

