days_stay = int(input())
kind_of_room = input()
impression = input()
price_per_night = 0
night_spend = days_stay - 1
total_sum = 0
if kind_of_room == "room for one person":
    price_per_night = 18
    total_sum = night_spend * price_per_night
elif kind_of_room == "apartment":
    price_per_night = 25
    total_sum = night_spend * price_per_night
    if night_spend < 10:
        total_sum *= 0.70
    elif 10 < night_spend < 15:
        total_sum *= 0.65
    else:
        total_sum *= 0.50
elif kind_of_room == "president apartment":
    price_per_night = 35
    total_sum = night_spend * price_per_night
    if night_spend < 10:
        total_sum *= 0.90
    elif 10 < night_spend < 15:
        total_sum *= 0.85
    else:
        total_sum *= 0.80

sum_positive = total_sum * 0.25
if impression == "positive":
    total_sum += sum_positive
elif impression == "negative":
    total_sum *= 0.90

print(f"{total_sum:.2f}")