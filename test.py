from math import ceil
count_days = int(input())
first_day_kilometers = float(input())
percentage_increase_daily_norm = int(input())
first_day_increase = (first_day_kilometers / percentage_increase_daily_norm)
kilometers_per_day = 0
counter_kilometers_per_day = 0
total_kilometers = 0
for days in range(1, count_days + 1):
    if days >= count_days:
        break
    kilometers_per_day = first_day_kilometers + first_day_increase
    percentage_increase_daily_norm = int(input())
    continue

total_kilometers = first_day_kilometers + kilometers_per_day
diff = abs(1000 - total_kilometers)
if total_kilometers >= 1000:
    print(f"You've done a great job running {ceil(diff)} more kilometers!")
else:
    print(f"Sorry Mrs. Ivanova, you need to run {ceil(diff)} more kilometers")

# days = days * kilometers_per_day
# if days == count_days:
# break
# total_kilometers += kilometers_per_day
# percentage_increase_daily_norm /= 100