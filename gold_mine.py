locations = int(input())
for i in range(1, locations + 1):
    gold_counter = 0
    expected_average_gold_per_day = float(input())
    day_on_location = int(input())
    for days in range(1, day_on_location + 1):
        gold_per_day = float(input())
        gold_counter += gold_per_day
    average_gold = gold_counter / day_on_location
    if average_gold >= expected_average_gold_per_day:
        print(f"Good job! Average gold per day: {average_gold:.2f}.")
    else:
        diff = abs(expected_average_gold_per_day - average_gold)
        print(f"You need {diff:.2f} gold.")
