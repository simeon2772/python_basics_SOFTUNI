first_multi = 0
second_multi = 0
result = 0
for first_multi in range(1, 11):
    for second_multi in range(1, 11):
        result = first_multi * second_multi
        print(f"{first_multi} * {second_multi} = {result}")