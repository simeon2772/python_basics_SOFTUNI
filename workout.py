from math import ceil
count_days = int(input())
first_day_kilometers = float(input())
percentage_increase_daily_norm = int(input())
first_day_increase = first_day_kilometers / percentage_increase_daily_norm
kilometers_percentage_per_day = 0
days_kilometers = 0
for days in range(1, count_days + 1):
    percentage_increase_daily_norm = int(input())
    kilometers_percentage_per_day = first_day_increase / percentage_increase_daily_norm

print(kilometers_percentage_per_day)









# diff = abs(1000 - total_kilometers)
# if total_kilometers >= 1000:
#     print(f"You've done a great job running {ceil(diff)} more kilometers!")
# else:
#     print(f"Sorry Mrs. Ivanova, you need to run {ceil(diff)} more kilometers")

