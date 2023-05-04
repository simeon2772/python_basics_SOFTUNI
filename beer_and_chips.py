from math import ceil
name_fan = input()
budget = float(input())
count_beers = int(input())
count_chips = int(input())
price_per_beer = 1.20
total_beer_price = count_beers * price_per_beer
chips_price = total_beer_price * 0.45
total_chips_price = ceil(count_chips * chips_price)

total_sum = total_chips_price + total_beer_price

diff = abs(budget - total_sum)
if total_sum <= budget:
    print(f"{name_fan} bought a snack and has {diff:.2f} leva left.")
else:
    print(f"{name_fan} needs {diff:.2f} more leva!")
